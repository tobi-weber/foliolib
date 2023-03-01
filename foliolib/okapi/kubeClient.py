# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>

import base64
import json
import logging
import time

from foliolib.config import Config
from foliolib.okapi.exceptions import (KubeDeployError, OkapiFatalError,
                                       OkapiRequestError)
from foliolib.okapi.okapiModuleKubernetes import OkapiModuleKubernetes
from kubernetes import client, config
from kubernetes.client.exceptions import ApiException
from kubernetes.config.config_exception import ConfigException

from . import GLOBAL_ENV_NAME_KUBERNETES

log = logging.getLogger("foliolib.okapi.kubeClient")


class KubeClient:

    def __init__(self, kube_config: str = None):
        """Client for kubernetes to manage Folio modules

        Args:
            kube_config (str)): Path to kube config. Defaults to None.
        """
        kube_config = kube_config or Config().get_kube_config()
        try:
            config.load_kube_config(config_file=kube_config)
        except ConfigException as e:
            log.error("Failed to load kube config %s", kube_config)
        self._namespace = Config().okapicfg().get(
            "Kubernetes", "namespace", fallback="default")

    def deploy(self, modId: str):
        """Deploy a Folio module

        Args:
            modId (str): Module id, e.g. mod-users-1.8.0
        """
        from foliolib.okapi.okapiClient import OkapiClient
        module = OkapiModuleKubernetes(modId)
        service = module.get_service()
        volume = module.volume()
        hazelcast = module.hazelcast()
        if volume:
            persistentVolumeClaim = volume["persistentVolumeClaim"]
            log.debug("Create PersistentVolumeClaim:\n%s" %
                      json.dumps(persistentVolumeClaim, indent=2))
            self.create_persistenVolumeClaim(
                persistentVolumeClaim, self._namespace)
        if hazelcast:
            self.create_configMap(
                hazelcast["name"], hazelcast["data"], namespace=self._namespace)
        log.debug("Create Service:\n%s" % json.dumps(service, indent=2))
        self.create_service(service, namespace=self._namespace)
        deployment = module.get_deployment()
        log.debug("Create Deployment:\n%s" % json.dumps(deployment, indent=2))
        if module.get_kind() == "Deployment":
            self.create_deployment(deployment, namespace=self._namespace)
        elif module.get_kind() == "StatefulSet":
            self.create_stateful_set(deployment, namespace=self._namespace)
        else:
            raise Exception("Unknown kind %s" % self._kind)
        isDeployed = False
        maxSecs = 600
        secs = 0
        while not isDeployed:
            time.sleep(5)
            secs += 5
            log.debug("Wait for %s is deployed" % modId)
            try:
                isDeployed = OkapiClient().is_module_deployed(modId)
            except OkapiFatalError:
                pass
            except OkapiRequestError:
                pass
            except ApiException:
                pass

            if not isDeployed and secs >= maxSecs:
                log.error("Deployment for %s in namespace %s failed",
                          modId, self._namespace)
                self.undeploy(modId)
                raise KubeDeployError(modId, self._namespace)

    def undeploy(self, modId: str):
        """Undeploy a Folio module

        Args:
            modId (str): Module id, e.g. mod-users-1.8.0
        """
        module = OkapiModuleKubernetes(modId)
        log.debug(self.remove_service(
            module.get_rfc_name(), namespace=self._namespace))
        if module.get_kind() == "Deployment":
            log.debug(self.remove_deployment(
                module.get_rfc_name(), namespace=self._namespace))
        elif module.get_kind() == "StatefulSet":
            self.remove_stateful_set(
                module.get_rfc_name(), namespace=self._namespace)
        else:
            raise Exception("Unknown kind %s" % self._kind)
        volume = module.volume()
        hazelcast = module.hazelcast()
        if volume:
            log.debug(self.remove_persistenVolumeClaim(
                volume["claim"]["name"], namespace=self._namespace))
        if module.hazelcast():
            self.remove_configMap(hazelcast["name"], namespace=self._namespace)

    def get_env(self):
        """Get enviroment variables.

        Returns:
            list: List with enviroment variables.
        """
        env = self.get_secret(GLOBAL_ENV_NAME_KUBERNETES,
                              namespace=self._namespace)
        if env is not None:
            return [{"name": k, "value": base64.b64decode(v).decode("utf-8")}
                    for k, v in env.items()]

        return {}

    def set_env(self, name: str, value: str):
        """Set an enviroment variable.

        Args:
            name (str): Name of the variable.
            value (str): Value of the variable.
        """
        env = self.get_secret(GLOBAL_ENV_NAME_KUBERNETES,
                              namespace=self._namespace) or {}
        v = base64.b64encode(value.encode("utf-8"))
        env[name] = v.decode("utf-8")
        if self.exists_secret(GLOBAL_ENV_NAME_KUBERNETES, namespace=self._namespace):
            self.remove_secret(GLOBAL_ENV_NAME_KUBERNETES,
                               namespace=self._namespace)
        self.create_secret(GLOBAL_ENV_NAME_KUBERNETES,
                           env, namespace=self._namespace)

    def delete_env(self, name: str):
        """Delete an enviroment variable.

        Args:
            name (str): Name of the variable.
        """
        env = self.get_secret(GLOBAL_ENV_NAME_KUBERNETES,
                              namespace=self._namespace)
        if name in env:
            del env[name]
        if self.exists_secret(GLOBAL_ENV_NAME_KUBERNETES, namespace=self._namespace):
            self.remove_secret(GLOBAL_ENV_NAME_KUBERNETES,
                               namespace=self._namespace)
        if env:
            self.create_secret(GLOBAL_ENV_NAME_KUBERNETES,
                               env, namespace=self._namespace)

    def get_api_versions(self):
        versions = []
        for api in client.ApisApi().get_api_versions().groups:
            for v in api.versions:
                name = ""
                if v.version == api.preferred_version.version and len(
                        api.versions) > 1:
                    name += "*"
                name += v.version
                versions.append(name)

        return versions

    def get_service(self, name: str, namespace: str = "default"):
        """Get a service.

        Args:
            name (str): Name of the service
            namespace (str, optional): Namespace of the service. Defaults to "default".

        Returns:
            dict: Dictonary of the service.
        """
        core_v1 = client.CoreV1Api()
        return core_v1.read_namespaced_service(name, namespace)

    def get_services(self, namespace: str = None):
        """Get services of one or all namespaces.

        Args:
            namespace (str, optional): Namespace. Defaults to None.

        Returns:
            list: List of services.
        """
        core_v1 = client.CoreV1Api()
        if namespace is None:
            return core_v1.list_service_for_all_namespaces()
        else:
            return core_v1.list_namespaced_service(namespace)

    def create_service(self, data: dict, namespace: str = "default"):
        """Create a service.

        Args:
            data (dict): Dict of the service.
            namespace (str, optional): Namespace. Defaults to "default".

        Returns:
            dict: Created service.
        """
        core_v1 = client.CoreV1Api()
        return core_v1.create_namespaced_service(namespace, data)

    def remove_service(self, name: str, namespace: str = "default"):
        """Remove a service.

        Args:
            name (str): Name of the service.
            namespace (str, optional): Namespace. Defaults to "default".

        Returns:
            _type_: _description_
        """
        core_v1 = client.CoreV1Api()
        return core_v1.delete_namespaced_service(name, namespace)

    def get_deployment(self, name: str):
        apps_v1 = client.AppsV1Api()

    def get_deployments(self, namespace: str = None):
        apps_v1 = client.AppsV1Api()

    def create_deployment(self, data: dict, namespace: str = "default"):
        log.debug("Create Deployment in namespace %s with %s",
                  namespace, str(data))
        apps_v1 = client.AppsV1Api()
        return apps_v1.create_namespaced_deployment(namespace, data)

    def remove_deployment(self, name: str, namespace: str = "default"):
        log.debug("Remove Deployment %s in namespace %s", name, namespace)
        apps_v1 = client.AppsV1Api()
        return apps_v1.delete_namespaced_deployment(name, namespace)

    def exists_secret(self, name: str, namespace: str = "default"):
        core_v1 = client.CoreV1Api()
        secrets = core_v1.list_namespaced_secret(namespace)
        for k in secrets.items:
            if k.metadata.name == name:
                return True
        return False

    def get_secret(self, name: str, namespace: str = "default"):
        core_v1 = client.CoreV1Api()
        secrets = core_v1.list_namespaced_secret(namespace)
        for k in secrets.items:
            if k.metadata.name == name:
                return k.data
        return None

    def create_secret(self, name: str, data: dict, namespace: str = "default"):
        log.debug("Create secret %s in namespace %s with %s",
                  name, namespace, str(data))
        core_v1 = client.CoreV1Api()
        body = client.V1Secret()
        body.api_version = 'v1'
        body.data = data
        body.kind = 'Secret'
        body.metadata = {'name': name}
        body.type = 'Opaque'
        return core_v1.create_namespaced_secret(namespace, body)

    def remove_secret(self, name: str, namespace: str = "default"):
        core_v1 = client.CoreV1Api()
        return core_v1.delete_namespaced_secret(name, namespace)

    def create_stateful_set(self, data: dict, namespace: str = "default"):
        log.debug("Create StatefulSet in namespace %s with %s",
                  namespace, str(data))
        apps_v1 = client.AppsV1Api()
        apps_v1.create_namespaced_stateful_set(namespace, data)

    def remove_stateful_set(self, name: str, namespace: str = "default"):
        log.debug("Remove StatefulSet %s in namespace %s", name, namespace)
        apps_v1 = client.AppsV1Api()
        apps_v1.delete_namespaced_stateful_set(name, namespace)

    def create_persistenVolumeClaim(self, data: dict, namespace: str = "default"):
        log.debug("Create PersistentVolumeClaim in namespace %s with %s",
                  namespace, str(data))
        core_v1 = client.CoreV1Api()
        core_v1.create_namespaced_persistent_volume_claim(namespace, data)

    def remove_persistenVolumeClaim(self, name: str, namespace: str = "default"):
        log.debug("Remove PersistentVolumeClaim %s in namespace %s",
                  name, namespace)
        core_v1 = client.CoreV1Api()
        core_v1.delete_namespaced_persistent_volume_claim(name, namespace)

    def create_configMap(self, name: str, data: dict, namespace: str = "default"):
        log.debug("Create ConfigMap %s in namespace %s",
                  name, namespace)
        core_v1 = client.CoreV1Api()
        metadata = client.V1ObjectMeta(
            name=name,
            namespace=namespace,
        )
        configmap = client.V1ConfigMap(
            api_version="v1",
            kind="ConfigMap",
            data=data,
            metadata=metadata
        )
        core_v1.create_namespaced_config_map(namespace, configmap)

    def remove_configMap(self, name: str, namespace: str = "default"):
        log.debug("Remove ConfigMap %s in namespace %s",
                  name, namespace)
        core_v1 = client.CoreV1Api()
        core_v1.delete_namespaced_config_map(name, namespace)


class KubeAdmin(KubeClient):

    def restart_folio(self, namespace: str = "folio"):
        apps_v1 = client.AppsV1Api()
        core_v1 = client.CoreV1Api()
        deps = apps_v1.list_namespaced_deployment(namespace)
        stfs = apps_v1.list_namespaced_stateful_set(namespace)
        dnames = {d.metadata.name: d.spec.replicas for d in deps.items}
        snames = {s.metadata.name: s.spec.replicas for s in stfs.items}
        for name in dnames.keys():
            log.info("Stop Pods for Deployment %s", name)
            apps_v1.patch_namespaced_deployment_scale(
                name, namespace, [{'op': 'replace', 'path': '/spec/replicas', 'value': 0}])
        for name in snames.keys():
            log.info("Stop Pods for StatefulSet %s", name)
            apps_v1.patch_namespaced_stateful_set_scale(
                name, namespace, [{'op': 'replace', 'path': '/spec/replicas', 'value': 0}])
        log.info("Wait for all Pods terminated ...")
        while True:
            pods = core_v1.list_namespaced_pod(namespace)
            if pods.items:
                time.sleep(1)
            else:
                break
        for name, replicas in dnames.items():
            log.info("Start %i Pods for Deployment %s",
                     replicas, name)
            apps_v1.patch_namespaced_deployment_scale(
                name, namespace, [{'op': 'replace', 'path': '/spec/replicas', 'value': replicas}])
        for name, replicas in snames.items():
            log.info("Start %i Pods for StatefulSet %s",
                     replicas, name)
            apps_v1.patch_namespaced_stateful_set_scale(
                name, namespace, [{'op': 'replace', 'path': '/spec/replicas', 'value': replicas}])
