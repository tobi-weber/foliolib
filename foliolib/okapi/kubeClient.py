# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>

import base64
import json
import logging
import time

from foliolib.config import Config
from foliolib.helper import split_modid
from foliolib.okapi.exceptions import KubeDeployError, OkapiRequestError
from foliolib.okapi.okapiModule import OkapiModule
from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException

log = logging.getLogger("foliolib.okapi.kubeClient")

GLOBAL_ENV_NAME = "okapi-global-env"


class HealthProbe:

    def __init__(self, modId, http_port) -> None:
        self._conf = Config().modulescfg(modId)
        self._healthCheck = True
        self._path = "admin/health"
        self._port = http_port

    def get_path(self):
        return self._path

    def get_port(self):
        return self._port

    def get_probe(self):
        data = {"httpGet": {"path": self.get_path(),
                            "port": self.get_port(),
                            "scheme": "HTTP"
                            }
                }
        return data


class StartupProbe(HealthProbe):

    def __init__(self, modId, http_port) -> None:
        super().__init__(modId, http_port)
        self.failureThreshold = 60
        self.periodSeconds = 10
        if self._conf is not None:
            self.failureThreshold = self._conf.get(
                "StartupProbe", "failureThreshold", fallback=self.failureThreshold)
            self.periodSeconds = self._conf.get(
                "StartupProbe", "periodSeconds", fallback=self.periodSeconds)

    def get_probe(self):
        data = super().get_probe()
        data["failureThreshold"] = self.failureThreshold
        data["periodSeconds"] = self.periodSeconds

        return data


class LivenessProbe(HealthProbe):

    def __init__(self, modId, http_port) -> None:
        super().__init__(modId, http_port)
        self.failureThreshold = 3
        self.initialDelaySeconds = 45
        self.periodSeconds = 60
        self.successThreshold = 1
        self.timeoutSeconds = 5
        if self._conf is not None:
            self.failureThreshold = self._conf.get(
                "LivenessProbe", "failureThreshold", fallback=self.failureThreshold)
            self.initialDelaySeconds = self._conf.get(
                "LivenessProbe", "periodSeconds", fallback=self.initialDelaySeconds)
            self.periodSeconds = self._conf.get(
                "LivenessProbe", "periodSeconds", fallback=self.periodSeconds)
            self.successThreshold = self._conf.get(
                "LivenessProbe", "successThreshold", fallback=self.successThreshold)
            self.timeoutSeconds = self._conf.get(
                "LivenessProbe", "timeoutSeconds", fallback=self.timeoutSeconds)

    def get_probe(self):
        data = super().get_probe()
        data["failureThreshold"] = self.failureThreshold
        data["initialDelaySeconds"] = self.initialDelaySeconds
        data["periodSeconds"] = self.periodSeconds
        data["timeoutSeconds"] = self.timeoutSeconds

        return data


class ReadinessProbe(HealthProbe):

    def __init__(self, modId, http_port) -> None:
        super().__init__(modId, http_port)
        self.failureThreshold = 3
        self.initialDelaySeconds = 45
        self.periodSeconds = 60
        self.successThreshold = 1
        self.timeoutSeconds = 5
        if self._conf is not None:
            self.failureThreshold = self._conf.get(
                "ReadinessProbe", "failureThreshold", fallback=self.failureThreshold)
            self.initialDelaySeconds = self._conf.get(
                "ReadinessProbe", "periodSeconds", fallback=self.initialDelaySeconds)
            self.periodSeconds = self._conf.get(
                "ReadinessProbe", "periodSeconds", fallback=self.periodSeconds)
            self.successThreshold = self._conf.get(
                "ReadinessProbe", "successThreshold", fallback=self.successThreshold)
            self.timeoutSeconds = self._conf.get(
                "ReadinessProbe", "timeoutSeconds", fallback=self.timeoutSeconds)

    def get_probe(self):
        data = super().get_probe()
        data["failureThreshold"] = self.failureThreshold
        data["initialDelaySeconds"] = self.initialDelaySeconds
        data["periodSeconds"] = self.periodSeconds
        data["timeoutSeconds"] = self.timeoutSeconds

        return data


class Resources:

    def __init__(self, modId) -> None:
        self._conf = Config().modulescfg(modId)
        self._min_cpu = 0
        self._max_cpu = 0
        self._min_memory = 0
        self._max_memory = 0
        if self._conf is not None:
            if self._conf.has_section("Resources"):
                self._min_cpu = self._conf.get(
                    "Resources", "min-cpu", fallback=self._min_cpu)
                self._max_cpu = self._conf.get(
                    "Resources", "max-cpu", fallback=self._max_cpu)
                self._min_memory = self._conf.get(
                    "Resources", "min-memory", fallback=self._min_memory)
                self._max_memory = self._conf.get(
                    "Resources", "max-memory", fallback=self._max_memory)

    def get_resources(self):
        resources = {}
        if self._min_cpu or self._min_memory:
            requests = {}
            if self._min_cpu:
                requests["cpu"] = self._min_cpu
            if self._min_memory:
                requests["memory"] = self._min_memory
            resources["requests"] = requests
        if self._max_cpu or self._max_memory:
            limits = {}
            if self._max_cpu:
                limits["cpu"] = self._max_cpu
            if self._max_memory:
                limits["memory"] = self._max_memory
            resources["limits"] = limits

        return resources


class Volume:

    def __init__(self, modId) -> None:
        self._conf = Config().modulescfg(modId)
        self.name = f"{modId}-data"
        self.name = "%s-data" % modId.replace(".", "-")
        self.mountPath = None
        self.size = None
        if self._conf is not None:
            if self._conf.has_section("Volume"):
                # self.name = self._conf.get("Volume", "name")
                self.mountPath = self._conf.get("Volume", "mountPath")
                self.size = self._conf.get("Volume", "size")

    def get_volumeMount(self):
        return {"mountPath": self.mountPath,
                "name": self.name

                }

    def get_volumeClaim(self):
        return {"name": self.name,
                "persistentVolumeClaim": {"claimName": self.name}
                }


class OkapiModuleKubernetes:

    def __init__(self, modId):
        module = OkapiModule(modId)
        self._modId = modId
        self._name, self._version = split_modid(modId)
        self._docker_image = module.get_docker_image()
        docker_args = module.get_docker_args()
        self._kind = "Deployment"
        self._memory = docker_args["memory"]
        self._port = docker_args["port"]
        self._protocol = docker_args["protocol"]
        self._env = module.get_env()
        self.healthCheck = True
        self.hasVolume = False
        self.hasResources = False
        modcfg = Config().modulescfg(modId)
        okapicfg = Config().okapicfg()

        self._replicas = okapicfg.getint("Kubernetes", "replicas", fallback=1)

        if modcfg is not None:
            if modcfg.has_section("Kubernetes"):
                if modcfg.has_option("Kubernetes", "replicas"):
                    self._replicas = modcfg.getint("Kubernetes", "replicas")
                if modcfg.has_option("Kubernetes", "kind"):
                    kind = modcfg.get("Kubernetes", "kind")
                    if kind in ["Deployment", "StatefulSet"]:
                        self._kind = kind
                self.healthCheck = modcfg.getboolean(
                    "Kubernetes", "healthCheck", fallback=True)
            if modcfg.has_section("Volume"):
                self.hasVolume = True
            if modcfg.has_section("Resources"):
                self.hasResources = True

    def get_kind(self):
        return self._kind

    def get_rfc_name(self):
        return self._modId.replace(".", "-")

    def get_persistentVolumeClaim_name(self):
        if self.hasVolume:
            return Volume(self._modId).name

    def get_service(self):
        service = {
            "apiVersion": "v1",
            "kind": "Service",
            "metadata": {
                "name": self.get_rfc_name(),
                "labels": {
                    "run": self._modId,
                    "app.kubernetes.io/name": self._name,
                    "app.kubernetes.io/version": self._version,
                    "app": self._name
                }
            },
            "spec": {
                "ports": [
                    {
                        "name": "http",
                        "port": self._port,
                        "protocol": self._protocol.upper()
                    }
                ],
                "selector": {
                    "app": self._modId
                }
            }
        }
        if self._kind == "StatefulSet":
            service["spec"]["clusterIP"] = "None"
            # service["spec"]["ports"][0]["targetPort"] = self._port

        return service

    def get_deployment(self):
        deployment = {
            "apiVersion": "apps/v1",
            "kind": self._kind,
            "metadata": {
                "name": self.get_rfc_name()
            },
            "spec": {
                "selector": {
                    "matchLabels": {
                        "app": self._modId
                    }
                },
                "replicas": self._replicas,
                "template": {
                    "metadata": {
                        "labels": {
                            "app": self._modId
                        }
                    },
                    "spec": {
                        "containers": [
                            {
                                "name": self._modId.replace(".", "-"),
                                "image": self._docker_image,
                                "imagePullPolicy": "IfNotPresent",
                                "ports": [
                                    {
                                        "containerPort": self._port
                                    }
                                ],
                                "env": self._env,
                                "envFrom": [
                                    {
                                        "secretRef": {
                                            "name": GLOBAL_ENV_NAME,
                                            "optional": True
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
        }

        resources = Resources(self._modId).get_resources()
        if resources:
            deployment["spec"]["template"]["spec"]["containers"][0]["resources"] = resources
        if self.healthCheck:
            deployment["spec"]["template"]["spec"]["containers"][0]["startupProbe"] = StartupProbe(
                self._modId, self._port).get_probe()
            deployment["spec"]["template"]["spec"]["containers"][0]["livenessProbe"] = LivenessProbe(
                self._modId, self._port).get_probe()
            deployment["spec"]["template"]["spec"]["containers"][0]["readinessProbe"] = ReadinessProbe(
                self._modId, self._port).get_probe()
        if self.hasVolume:
            deployment["spec"]["template"]["spec"]["containers"][0]["volumeMounts"] = [
                Volume(self._modId).get_volumeMount()]
            deployment["spec"]["template"]["spec"]["volumes"] = [
                Volume(self._modId).get_volumeClaim()]
        if self._kind == "StatefulSet":
            deployment["spec"]["serviceName"] = self._modId.replace(".", "-")
            deployment["spec"]["selector"] = {"matchLabels":
                                              {"app": self._modId}}

        return deployment

    def get_persistentVolumeClaim(self):
        vol = Volume(self._modId)
        if self.hasVolume:
            return {"apiVersion": "v1",
                    "kind": "PersistentVolumeClaim",
                    # "metadata": {"name": vol.name},
                    "metadata": {"name": vol.name,
                                  "labels":  {"app": self._modId}},
                    "spec": {"accessModes": ["ReadWriteOnce"],
                             "resources": {"requests": {"storage": vol.size}},
                             }
                    }
        return None


class KubeClient:

    def __init__(self):
        kube_config = Config().get_kube_config()
        try:
            config.load_kube_config(config_file=kube_config)
        except ConfigException as e:
            log.error("Failed to load kube config %s", kube_config)
        self._namespace = Config().okapicfg().get(
            "Kubernetes", "namespace", fallback="default")

    def deploy(self, modId):
        from foliolib.okapi.okapiClient import OkapiClient
        module = OkapiModuleKubernetes(modId)
        service = module.get_service()
        if module.hasVolume:
            persistentVolumeClaim = module.get_persistentVolumeClaim()
            log.debug("Create PersistentVolumeClaim:\n%s" %
                      json.dumps(persistentVolumeClaim, indent=2))
            self.create_persistenVolumeClaim(
                persistentVolumeClaim, self._namespace)
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
        maxSecs = 300
        secs = 0
        while not isDeployed:
            time.sleep(5)
            secs += 5
            log.debug("Wait for %s is deployed" % modId)
            try:
                isDeployed = OkapiClient().is_module_deployed(modId)
            except OkapiRequestError:
                pass
            if not isDeployed and secs >= maxSecs:
                log.error("Deployment for %s in namespace %s failed",
                          modId, self._namespace)
                self.undeploy(modId)
                raise KubeDeployError(modId, self._namespace)

    def undeploy(self, modId):
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
        if module.hasVolume:
            log.debug(self.remove_persistenVolumeClaim(
                module.get_persistentVolumeClaim_name(), namespace=self._namespace))

    def get_env(self):
        env = self.get_secret(GLOBAL_ENV_NAME, namespace=self._namespace)
        if env is not None:
            return [{"name": k, "value": base64.b64decode(v).decode("utf-8")}
                    for k, v in env.items()]

        return {}

    def set_env(self, name, value):
        env = self.get_secret(GLOBAL_ENV_NAME, namespace=self._namespace) or {}
        v = base64.b64encode(value.encode("utf-8"))
        env[name] = v.decode("utf-8")
        if self.exists_secret(GLOBAL_ENV_NAME, namespace=self._namespace):
            self.remove_secret(GLOBAL_ENV_NAME, namespace=self._namespace)
        self.create_secret(GLOBAL_ENV_NAME, env, namespace=self._namespace)

    def delete_env(self, name):
        env = self.get_secret(GLOBAL_ENV_NAME, namespace=self._namespace)
        if name in env:
            del env[name]
        if self.exists_secret(GLOBAL_ENV_NAME, namespace=self._namespace):
            self.remove_secret(GLOBAL_ENV_NAME, namespace=self._namespace)
        if env:
            self.create_secret(GLOBAL_ENV_NAME, env, namespace=self._namespace)

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

    def get_service(self, name, namespace="default"):
        core_v1 = client.CoreV1Api()
        return core_v1.read_namespaced_service(name, namespace)

    def get_services(self, namespace=None):
        core_v1 = client.CoreV1Api()
        if namespace is None:
            return core_v1.list_service_for_all_namespaces()
        else:
            return core_v1.list_namespaced_service(namespace)

    def create_service(self, data, namespace="default"):
        core_v1 = client.CoreV1Api()
        return core_v1.create_namespaced_service(namespace, data)

    def remove_service(self, name, namespace="default"):
        core_v1 = client.CoreV1Api()
        return core_v1.delete_namespaced_service(name, namespace)

    def get_deployment(self, name):
        apps_v1 = client.AppsV1Api()

    def get_deployments(self, namespace=None):
        apps_v1 = client.AppsV1Api()

    def create_deployment(self, data, namespace="default"):
        log.debug("Create Deployment in namespace %s with %s",
                  namespace, str(data))
        apps_v1 = client.AppsV1Api()
        return apps_v1.create_namespaced_deployment(namespace, data)

    def remove_deployment(self, name, namespace="default"):
        log.debug("Remove Deployment %s in namespace %s", name, namespace)
        apps_v1 = client.AppsV1Api()
        return apps_v1.delete_namespaced_deployment(name, namespace)

    def exists_secret(self, name, namespace="default"):
        core_v1 = client.CoreV1Api()
        secrets = core_v1.list_namespaced_secret(namespace)
        for k in secrets.items:
            if k.metadata.name == name:
                return True
        return False

    def get_secret(self, name, namespace="default"):
        core_v1 = client.CoreV1Api()
        secrets = core_v1.list_namespaced_secret(namespace)
        for k in secrets.items:
            if k.metadata.name == name:
                return k.data
        return None

    def create_secret(self, name, data, namespace="default"):
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

    def remove_secret(self, name, namespace="default"):
        core_v1 = client.CoreV1Api()
        return core_v1.delete_namespaced_secret(name, namespace)

    def create_stateful_set(self, data, namespace="default"):
        log.debug("Create StatefulSet in namespace %s with %s",
                  namespace, str(data))
        apps_v1 = client.AppsV1Api()
        apps_v1.create_namespaced_stateful_set(namespace, data)

    def remove_stateful_set(self, name, namespace="default"):
        log.debug("Remove StatefulSet %s in namespace %s", name, namespace)
        apps_v1 = client.AppsV1Api()
        apps_v1.delete_namespaced_stateful_set(name, namespace)

    def create_persistenVolumeClaim(self, data, namespace="default"):
        log.debug("Create PersistentVolumeClaim in namespace %s with %s",
                  namespace, str(data))
        core_v1 = client.CoreV1Api()
        core_v1.create_namespaced_persistent_volume_claim(namespace, data)

    def remove_persistenVolumeClaim(self, name, namespace="default"):
        log.debug("Remove PersistentVolumeClaim %s in namespace %s",
                  name, namespace)
        core_v1 = client.CoreV1Api()
        core_v1.delete_namespaced_persistent_volume_claim(name, namespace)
