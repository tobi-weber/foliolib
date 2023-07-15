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
        self._namespace = Config().servercfg().get(
            "Kubernetes", "namespace", fallback="default")
        self._deploy_timeout = Config().servercfg().getint(
            "Kubernetes", "deployTimeout", fallback=3600)

    def deploy(self, modId: str):
        """Deploy a Folio module

        Args:
            modId (str): Module id, e.g. mod-users-1.8.0
        """
        from foliolib.okapi.okapiClient import OkapiClient
        if OkapiClient().is_module_deployed(modId):
            log.error("Module %s is already deployed" % modId)
            return
        module = OkapiModuleKubernetes(modId)
        name = module.get_rfc_name()
        service = module.get_service()
        volume = module.volume()
        hazelcast = module.hazelcast()
        if volume:
            persistentVolumeClaim = volume["persistentVolumeClaim"]
            log.debug("Create PersistentVolumeClaim:\n%s" %
                      json.dumps(persistentVolumeClaim, indent=2))
            self.create_persistenVolumeClaim(persistentVolumeClaim)
        if hazelcast:
            if self.is_configMap(hazelcast["name"]):
                self.remove_configMap(hazelcast["name"])
            self.create_configMap(
                hazelcast["name"], hazelcast["data"])
        log.debug("Create Service:\n%s" % json.dumps(service, indent=2))
        if self.is_service(name):
            self.remove_service(name)
        self.create_service(service)
        deployment = module.get_deployment()
        log.debug("Create Deployment:\n%s" % json.dumps(deployment, indent=2))
        if module.get_kind() == "Deployment":
            if self.is_deployment(name):
                self.remove_deployment(name)
            self.create_deployment(deployment)
        elif module.get_kind() == "StatefulSet":
            if self.is_stateful_set(name):
                self.remove_stateful_set(name)
            self.create_stateful_set(deployment)
        else:
            raise Exception("Unknown kind %s" % self._kind)
        isDeployed = False
        maxSecs = self._deploy_timeout
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

    def patch(self, modId: str):
        from foliolib.okapi.okapiClient import OkapiClient
        module = OkapiModuleKubernetes(modId)
        deployment = module.get_deployment()
        log.debug("Create Deployment:\n%s" % json.dumps(deployment, indent=2))
        if module.get_kind() == "Deployment":
            self.patch_deployment(module.get_rfc_name(),
                                  deployment)
        elif module.get_kind() == "StatefulSet":
            self.patch_stateful_set(
                module.get_rfc_name(), deployment)
        else:
            raise Exception("Unknown kind %s" % self._kind)

    def undeploy(self, modId: str):
        """Undeploy a Folio module

        Args:
            modId (str): Module id, e.g. mod-users-1.8.0
        """
        module = OkapiModuleKubernetes(modId)
        log.debug(self.remove_service(
            module.get_rfc_name()))
        if module.get_kind() == "Deployment":
            log.debug(self.remove_deployment(
                module.get_rfc_name()))
        elif module.get_kind() == "StatefulSet":
            self.remove_stateful_set(
                module.get_rfc_name())
        else:
            raise Exception("Unknown kind %s" % self._kind)
        volume = module.volume()
        hazelcast = module.hazelcast()
        if volume:
            log.debug(self.remove_persistenVolumeClaim(
                volume["claim"]["name"]))
        if module.hazelcast():
            self.remove_configMap(hazelcast["name"])

    def get_env(self):
        """Get enviroment variables.

        Returns:
            list: List with enviroment variables.
        """
        env = self.get_secret(GLOBAL_ENV_NAME_KUBERNETES)
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
        env = self.get_secret(GLOBAL_ENV_NAME_KUBERNETES) or {}
        v = base64.b64encode(value.encode("utf-8"))
        env[name] = v.decode("utf-8")
        if self.exists_secret(GLOBAL_ENV_NAME_KUBERNETES):
            self.remove_secret(GLOBAL_ENV_NAME_KUBERNETES)
        self.create_secret(GLOBAL_ENV_NAME_KUBERNETES)

    def delete_env(self, name: str):
        """Delete an enviroment variable.

        Args:
            name (str): Name of the variable.
        """
        env = self.get_secret(GLOBAL_ENV_NAME_KUBERNETES)
        if name in env:
            del env[name]
        if self.exists_secret(GLOBAL_ENV_NAME_KUBERNETES):
            self.remove_secret(GLOBAL_ENV_NAME_KUBERNETES)
        if env:
            self.create_secret(GLOBAL_ENV_NAME_KUBERNETES, env)

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

    def get_service(self, name: str):
        """Get a service.

        Args:
            name (str): Name of the service
            namespace (str, optional): Namespace of the service. Defaults to "default".

        Returns:
            dict: Dictonary of the service.
        """
        core_v1 = client.CoreV1Api()
        return core_v1.read_namespaced_service(name, self._namespace)

    def get_services(self):
        """Get services.

        Returns:
            list: List of services.
        """
        core_v1 = client.CoreV1Api()
        return core_v1.list_namespaced_service(self._namespace)

    def create_service(self, data: dict):
        """Create a service.

        Args:
            data (dict): Dict of the service.
            namespace (str, optional): Namespace. Defaults to "default".

        Returns:
            dict: Created service.
        """
        core_v1 = client.CoreV1Api()
        return core_v1.create_namespaced_service(self._namespace, data)

    def remove_service(self, name: str):
        """Remove a service.

        Args:
            name (str): Name of the service.
            namespace (str, optional): Namespace. Defaults to "default".

        Returns:
            _type_: _description_
        """
        core_v1 = client.CoreV1Api()
        return core_v1.delete_namespaced_service(name, self._namespace)

    def is_service(self, name: str):
        services = self.get_services()
        for service in services.items:
            if name == service.metadata.name:
                return True
        return False

    def get_deployment(self, name: str):
        apps_v1 = client.AppsV1Api()

    def get_deployments(self):
        apps_v1 = client.AppsV1Api()
        return apps_v1.list_namespaced_deployment(self._namespace)

    def create_deployment(self, data: dict):
        log.debug("Create Deployment in namespace %s with %s",
                  self._namespace, str(data))
        apps_v1 = client.AppsV1Api()
        return apps_v1.create_namespaced_deployment(self._namespace, data)

    def patch_deployment(self, name, data: dict):
        log.debug("Patch Deployment %s in namespace %s with %s",
                  name, self._namespace, str(data))
        apps_v1 = client.AppsV1Api()
        return apps_v1.patch_namespaced_deployment(name, self._namespace, data)

    def remove_deployment(self, name: str):
        log.debug("Remove Deployment %s in namespace %s",
                  name, self._namespace)
        apps_v1 = client.AppsV1Api()
        return apps_v1.delete_namespaced_deployment(name, self._namespace)

    def is_deployment(self, name: str):
        deployments = self.get_deployments()
        for deployment in deployments.items:
            if name == deployment.metadata.name:
                return True
        return False

    def exists_secret(self, name: str):
        core_v1 = client.CoreV1Api()
        secrets = core_v1.list_namespaced_secret(self._namespace)
        for k in secrets.items:
            if k.metadata.name == name:
                return True
        return False

    def get_secret(self, name: str):
        core_v1 = client.CoreV1Api()
        secrets = core_v1.list_namespaced_secret(self._namespace)
        for k in secrets.items:
            if k.metadata.name == name:
                return k.data
        return None

    def create_secret(self, name: str, data: dict):
        log.debug("Create secret %s in namespace %s with %s",
                  name, self._namespace, str(data))
        core_v1 = client.CoreV1Api()
        body = client.V1Secret()
        body.api_version = 'v1'
        body.data = data
        body.kind = 'Secret'
        body.metadata = {'name': name}
        body.type = 'Opaque'
        return core_v1.create_namespaced_secret(self._namespace, body)

    def remove_secret(self, name: str):
        core_v1 = client.CoreV1Api()
        return core_v1.delete_namespaced_secret(name, self._namespace)

    def get_stateful_sets(self):
        apps_v1 = client.AppsV1Api()
        return apps_v1.list_namespaced_stateful_set(self._namespace)

    def create_stateful_set(self, data: dict):
        log.debug("Create StatefulSet in namespace %s with %s",
                  self._namespace, str(data))
        apps_v1 = client.AppsV1Api()
        apps_v1.create_namespaced_stateful_set(self._namespace, data)

    def patch_stateful_set(self, name: str, data: dict):
        log.debug("Patch StatefulSet %s in namespace %s with %s",
                  name, self._namespace, str(data))
        apps_v1 = client.AppsV1Api()
        apps_v1.patch_namespaced_stateful_set(name, self._namespace, data)

    def remove_stateful_set(self, name: str):
        log.debug("Remove StatefulSet %s in namespace %s",
                  name, self._namespace)
        apps_v1 = client.AppsV1Api()
        apps_v1.delete_namespaced_stateful_set(name, self._namespace)

    def is_stateful_set(self, name: str):
        stateful_sets = self.get_stateful_sets()
        for stateful_set in stateful_sets.items:
            if name == stateful_set.metadata.name:
                return True
        return False

    def create_persistenVolumeClaim(self, data: dict):
        log.debug("Create PersistentVolumeClaim in namespace %s with %s",
                  self._namespace, str(data))
        core_v1 = client.CoreV1Api()
        core_v1.create_namespaced_persistent_volume_claim(
            self._namespace, data)

    def remove_persistenVolumeClaim(self, name: str):
        log.debug("Remove PersistentVolumeClaim %s in namespace %s",
                  name, self._namespace)
        core_v1 = client.CoreV1Api()
        core_v1.delete_namespaced_persistent_volume_claim(
            name, self._namespace)

    def create_configMap(self, name: str, data: dict):
        log.debug("Create ConfigMap %s in namespace %s",
                  name, self._namespace)
        core_v1 = client.CoreV1Api()
        metadata = client.V1ObjectMeta(
            name=name,
            namespace=self._namespace,
        )
        configmap = client.V1ConfigMap(
            api_version="v1",
            kind="ConfigMap",
            data=data,
            metadata=metadata
        )
        core_v1.create_namespaced_config_map(self._namespace, configmap)

    def remove_configMap(self, name: str):
        log.debug("Remove ConfigMap %s in namespace %s",
                  name, self._namespace)
        core_v1 = client.CoreV1Api()
        core_v1.delete_namespaced_config_map(name, self._namespace)

    def get_configMaps(self):
        core_v1 = client.CoreV1Api()
        return core_v1.list_namespaced_config_map(self._namespace)

    def is_configMap(self, name: str):
        configMaps = self.get_configMaps()
        for configMap in configMaps.items:
            if name == configMap.metadata.name:
                return True
        return False


class KubeAdmin(KubeClient):

    def __init__(self, kube_config: str = None):
        """Manage folio in kubernetes.

        Args:
            kube_config (str, optional): Path to kube config. Defaults to None.
        """
        super().__init__(kube_config)
        self.__apps_v1 = client.AppsV1Api()
        self.__core_v1 = client.CoreV1Api()
        self.__dnames = {}
        self.__snames = {}

    def stop_folio(self):
        deps = self.__apps_v1.list_namespaced_deployment(self._namespace)
        stfs = self.__apps_v1.list_namespaced_stateful_set(self._namespace)
        self.__dnames = {d.metadata.name: d.spec.replicas for d in deps.items}
        self.__snames = {s.metadata.name: s.spec.replicas for s in stfs.items}
        for name in self.__dnames.keys():
            log.info("Stop Pods for Deployment %s", name)
            self.__apps_v1.patch_namespaced_deployment_scale(
                name, self._namespace, [{'op': 'replace', 'path': '/spec/replicas', 'value': 0}])
        for name in self.__snames.keys():
            log.info("Stop Pods for StatefulSet %s", name)
            self.__apps_v1.patch_namespaced_stateful_set_scale(
                name, self._namespace, [{'op': 'replace', 'path': '/spec/replicas', 'value': 0}])
        log.info("Wait for all Pods terminated ...")
        while True:
            pods = self.__core_v1.list_namespaced_pod(self._namespace)
            if pods.items:
                time.sleep(1)
            else:
                break

    def start_folio(self):
        for name, replicas in self.__dnames.items():
            if replicas == 0:
                replicas = 1
            log.info("Start %i Pods for Deployment %s",
                     replicas, name)
            self.__apps_v1.patch_namespaced_deployment_scale(
                name, self._namespace, [{'op': 'replace', 'path': '/spec/replicas', 'value': replicas}])
        for name, replicas in self.__snames.items():
            if replicas == 0:
                replicas = 1
            log.info("Start %i Pods for StatefulSet %s",
                     replicas, name)
            self.__apps_v1.patch_namespaced_stateful_set_scale(
                name, self._namespace, [{'op': 'replace', 'path': '/spec/replicas', 'value': replicas}])

    def restart_folio(self):
        self.stop_folio()
        self.start_folio()
