# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>

import logging
import math
from io import StringIO
from typing import Union

from foliolib.config import Config
from foliolib.helper import split_modid
from foliolib.okapi.okapiModule import OkapiModule

from . import GLOBAL_ENV_NAME_KUBERNETES, get_hazelcast_xml

log = logging.getLogger("foliolib.okapi.okapiModuleKuberenetes")


class OkapiModuleKubernetes:
    """Defines an okapi module for Kubernetes.
    """

    def __init__(self, module: Union[dict, str]):
        """
        Args:
            module (Union[dict, str]): Module id or instance of OkapiModule.
        """
        if isinstance(module, OkapiModule):
            self._modId = module.get_id()
        elif isinstance(module, str):
            self._modId = module
            module = OkapiModule(module)
        self._name, self._version = split_modid(self._modId)
        self._docker_image = module.get_docker_image()
        docker_args = module.get_docker_args()
        self._kind = "Deployment"
        self._memory = docker_args["memory"]
        self._port = docker_args["port"]
        self._protocol = docker_args["protocol"]
        self._env = module.get_env()
        self.healthCheck = True
        self.podAntiAffinity = True
        modcfg = Config().modulescfg(self._modId)
        servercfg = Config().servercfg()
        self._namespace = servercfg.get(
            "Kubernetes", "namespace", fallback="folio")
        self.imagePullSecret = servercfg.get(
            "Kubernetes", "imagePullSecret", fallback=None)

        self._replicas = servercfg.getint("Kubernetes", "replicas", fallback=1)

        if self._modId.startswith("mod-authtoken"):
            self._replicas = 1

        if self._modId.startswith("mod-data-import"):
            self._replicas = 1

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
                self.podAntiAffinity = modcfg.getboolean(
                    "Kubernetes", "podAntiAffinity", fallback=True)
                self.imagePullSecret = modcfg.get(
                    "Kubernetes", "imagePullSecret", fallback=self.imagePullSecret)

    def get_kind(self):
        """Get resource kind.

        Returns:
            str: Deployment or StatefulSet
        """
        return self._kind

    def get_namespace(self):
        """Get namespace of the module

        Returns:
            str: Namespace
        """
        return self._namespace

    def get_rfc_name(self):
        """Get module id as rfc name.

        Returns:
            str: rfc name.
        """
        return self._modId.replace(".", "-")

    def get_service(self):
        """Get Kubernetes service definition for the module.

        Returns:
            dict: Kubernetes service definition.
        """
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
        """Get Kubernetes deployment or statefulset definition for the module.

        Returns:
            dict: Kubernetes deployment or statefulset definition.
        """
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
                                            "name": GLOBAL_ENV_NAME_KUBERNETES,
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

        securityContext = self.__securityContext()
        deployment["spec"]["template"]["spec"]["containers"][0]["resources"] = self.__resources()
        if self.healthCheck:
            deployment["spec"]["template"]["spec"]["containers"][0]["startupProbe"] = self.__startupProbe()
            deployment["spec"]["template"]["spec"]["containers"][0]["livenessProbe"] = self.__livenessProbe()
            deployment["spec"]["template"]["spec"]["containers"][0]["readinessProbe"] = self.__readinessProbe()
        if self.has_volume() or self.has_hazelcast():
            deployment["spec"]["template"]["spec"]["containers"][0]["volumeMounts"] = []
            deployment["spec"]["template"]["spec"]["volumes"] = []
        if self.has_volume():
            persistentVolumeClaim = self.get_persistentVolumeClaim()
            deployment["spec"]["template"]["spec"]["containers"][0]["volumeMounts"].append(
                self.__volume_mount())
            deployment["spec"]["template"]["spec"]["volumes"].append(
                self.__volume_claim())
        if self.has_hazelcast():
            hazelcast = self.get_hazelcast_configMap()
            deployment["spec"]["template"]["spec"]["containers"][0]["volumeMounts"].append(
                {"name": "hazelcast-xml",
                 "mountPath": "/etc/hazelcast",
                 "readOnly": True})
            deployment["spec"]["template"]["spec"]["volumes"].append(
                {"name": "hazelcast-xml",
                 "configMap": {"name": self.__hazelcast_configMap_name()}})
            deployment["spec"]["template"]["spec"]["containers"][0]["ports"] = [{"containerPort": 5701},
                                                                                {"containerPort": 5702},
                                                                                {"containerPort": 5703},
                                                                                {"containerPort": 5704},
                                                                                {"containerPort": 54327}]
            env = deployment["spec"]["template"]["spec"]["containers"][0]["env"]
            for e in env:
                if e["name"] == "JAVA_OPTIONS":
                    e["value"] += " -Dhazelcast.config=/etc/hazelcast/hazelcast.xml"
            deployment["spec"]["template"]["spec"]["containers"][0]["env"] = env
        if securityContext:
            deployment["spec"]["template"]["spec"]["securityContext"] = securityContext
        if self._kind == "StatefulSet":
            deployment["spec"]["serviceName"] = self._modId.replace(".", "-")
            deployment["spec"]["selector"] = {"matchLabels":
                                              {"app": self._modId}}
        if self.podAntiAffinity:
            deployment["spec"]["template"]["spec"]["affinity"] = {
                "podAntiAffinity": {
                    "preferredDuringSchedulingIgnoredDuringExecution": [
                        {
                            "weight": 1,
                            "podAffinityTerm": {
                                "labelSelector": {
                                    "matchExpressions": [
                                        {
                                            "key": "app",
                                            "operator": "In",
                                                        "values": [
                                                            self._modId
                                                        ]
                                        }
                                    ]
                                },
                                "topologyKey": "kubernetes.io/hostname"
                            }
                        }
                    ]
                }
            }
        if self.imagePullSecret:
            deployment["spec"]["template"]["spec"]["imagePullSecrets"] = [{
                "name": self.imagePullSecret}]

        return deployment

    def get_persistentVolumeClaim(self):
        """Get Kubernetes PersistentVolumeClaim definition.

        Returns:
            dict: Kubernetes PersistentVolumeClaim definition.
        """
        conf = Config().modulescfg(self._modId)
        name = f"{self._modId}-data"
        name = "%s-data" % self._modId.replace(".", "-")
        persistentVolumeClaim = None
        if self.has_volume():
            mountPath = conf.get("Volume", "mountPath")
            storageClassName = conf.get(
                "Volume", "storageClassName", fallback=None)
            size = conf.get("Volume", "size")
            persistentVolumeClaim = {"apiVersion": "v1",
                                     "kind": "PersistentVolumeClaim",
                                     "metadata": {"name": name,
                                                  "labels":  {"app": self._modId}},
                                     "spec": {"accessModes": ["ReadWriteOnce"],
                                              "resources": {"requests": {"storage": size}},
                                              }
                                     }
            if storageClassName is not None:
                persistentVolumeClaim["spec"]["storageClassName"] = storageClassName

        return persistentVolumeClaim

    def get_hazelcast_configMap(self):
        """Get Kubernetes ConfigMap definition for Hazelcast.

        Returns:
            dict: Kubernetes ConfigMap definition for Hazelcast.
        """
        if self.has_hazelcast():
            return {
                "apiVersion": "v1",
                "kind": "ConfigMap",
                "metadata": {"name": self.__hazelcast_configMap_name()},
                "data": {"hazelcast.xml": get_hazelcast_xml(self.get_rfc_name(), self._namespace)},
            }
        return None

    def has_volume(self):
        """Wether module has a volume defined.

        Returns:
            bool: Wether module has a volume defined.
        """
        conf = Config().modulescfg(self._modId)
        if conf is not None:
            if conf.has_section("Volume"):
                return True

        return False

    def has_hazelcast(self):
        """Wether module has hazelcast enabled.

        Returns:
            bool: Wether module has hazelcast enabled.
        """
        conf = Config().modulescfg(self._modId)
        if conf is not None and conf.getboolean(
                "Kubernetes", "hazelcast", fallback=False):
            return True

        return False

    def __hazelcast_configMap_name(self):
        return f"{self._modId}-hazelcast-xml"

    def __healthProbe(self):
        return {"httpGet": {"path": "admin/health",
                            "port": self._port,
                            "scheme": "HTTP"
                            }
                }

    def __startupProbe(self):
        conf = Config().modulescfg(self._modId)
        failureThreshold = 60
        periodSeconds = 10
        if conf is not None:
            failureThreshold = conf.get(
                "StartupProbe", "failureThreshold", fallback=failureThreshold)
            periodSeconds = conf.get(
                "StartupProbe", "periodSeconds", fallback=periodSeconds)
        data = self.__healthProbe()
        data["failureThreshold"] = failureThreshold
        data["periodSeconds"] = periodSeconds

        return data

    def __livenessProbe(self):
        conf = Config().modulescfg(self._modId)
        failureThreshold = 3
        initialDelaySeconds = 45
        periodSeconds = 60
        successThreshold = 1
        timeoutSeconds = 5
        if conf is not None:
            failureThreshold = conf.get(
                "LivenessProbe", "failureThreshold", fallback=failureThreshold)
            initialDelaySeconds = conf.get(
                "LivenessProbe", "initialDelaySeconds", fallback=initialDelaySeconds)
            periodSeconds = conf.get(
                "LivenessProbe", "periodSeconds", fallback=periodSeconds)
            successThreshold = conf.get(
                "LivenessProbe", "successThreshold", fallback=successThreshold)
            timeoutSeconds = conf.get(
                "LivenessProbe", "timeoutSeconds", fallback=timeoutSeconds)
        data = self.__healthProbe()
        data["failureThreshold"] = failureThreshold
        data["initialDelaySeconds"] = initialDelaySeconds
        data["periodSeconds"] = periodSeconds
        data["successThreshold"] = successThreshold
        data["timeoutSeconds"] = timeoutSeconds

        return data

    def __readinessProbe(self):
        conf = Config().modulescfg(self._modId)
        failureThreshold = 3
        initialDelaySeconds = 45
        periodSeconds = 60
        successThreshold = 1
        timeoutSeconds = 5
        if conf is not None:
            failureThreshold = conf.get(
                "ReadinessProbe", "failureThreshold", fallback=failureThreshold)
            initialDelaySeconds = conf.get(
                "ReadinessProbe", "initialDelaySeconds", fallback=initialDelaySeconds)
            periodSeconds = conf.get(
                "ReadinessProbe", "periodSeconds", fallback=periodSeconds)
            successThreshold = conf.get(
                "ReadinessProbe", "successThreshold", fallback=successThreshold)
            timeoutSeconds = conf.get(
                "ReadinessProbe", "timeoutSeconds", fallback=timeoutSeconds)
        data = self.__healthProbe()
        data["failureThreshold"] = failureThreshold
        data["initialDelaySeconds"] = initialDelaySeconds
        data["periodSeconds"] = periodSeconds
        data["successThreshold"] = successThreshold
        data["timeoutSeconds"] = timeoutSeconds

        return data

    def __volume_name(self):
        name = f"{self._modId}-data"
        name = "%s-data" % self._modId.replace(".", "-")

        return name

    def __volume_claim(self):
        conf = Config().modulescfg(self._modId)
        volume_claim = {"name": self.__volume_name(),
                        "persistentVolumeClaim": {"claimName": self.__volume_name()}}

        return volume_claim

    def __volume_mount(self):
        conf = Config().modulescfg(self._modId)
        volume_mount = {"mountPath": conf.get("Volume", "mountPath"),
                        "name": self.__volume_name()}

        return volume_mount

    def __resources(self):
        conf = Config().modulescfg(self._modId)
        module = OkapiModule(self._modId)
        min_cpu = "10m"
        max_cpu = 0
        memory = module.get_docker_args()["memory"]
        if memory is not None:
            memoryRequestPercentage = Config().servercfg().getint(
                "Kubernetes", "memoryRequestPercentage", fallback=100)
            mk = math.ceil(memory/1024)
            min_mem = "%iKi" % ((mk * memoryRequestPercentage) / 100)
            max_mem = "%iKi" % mk
        else:
            log.warning(
                "ModuleDescriptor for %s has no memory defined", self._modId)
            min_mem = 0
            max_mem = 0
        min_memory = min_mem
        max_memory = max_mem
        if conf is not None:
            if conf.has_section("Resources"):
                min_cpu = conf.get(
                    "Resources", "min-cpu", fallback=min_cpu)
                max_cpu = conf.get(
                    "Resources", "max-cpu", fallback=max_cpu)
                min_memory = conf.get(
                    "Resources", "min-memory", fallback=min_memory)
                max_memory = conf.get(
                    "Resources", "max-memory", fallback=max_memory)

        resources = {}
        if min_cpu or min_memory:
            requests = {}
            if min_cpu:
                requests["cpu"] = min_cpu
            if min_memory:
                requests["memory"] = min_memory
            resources["requests"] = requests
        if max_cpu or max_memory:
            limits = {}
            if max_cpu:
                limits["cpu"] = max_cpu
            if max_memory:
                limits["memory"] = max_memory
            resources["limits"] = limits

        return resources

    def __securityContext(self):
        conf = Config().modulescfg(self._modId)
        sc = {}
        if conf is not None:
            if conf.has_section("SecurityContext"):
                runAsUser = conf.getint(
                    "SecurityContext", "runAsUser", fallback=None)
                runAsNonRoot = conf.getboolean(
                    "SecurityContext", "runAsNonRoot", fallback=None)
                runAsGroup = conf.getint(
                    "SecurityContext", "runAsGroup", fallback=None)
                fsGroup = conf.getint(
                    "SecurityContext", "fsGroup", fallback=None)
                fsGroupChangePolicy = conf.get(
                    "SecurityContext", "fsGroupChangePolicy", fallback=None)

                if runAsUser is not None:
                    sc["runAsUser"] = runAsUser
                if runAsNonRoot is not None:
                    sc["runAsNonRoot"] = runAsNonRoot
                if runAsGroup is not None:
                    sc["runAsGroup"] = runAsGroup
                if fsGroup is not None:
                    sc["fsGroup"] = fsGroup
                if fsGroupChangePolicy is not None:
                    sc["fsGroupChangePolicy"] = fsGroupChangePolicy

        return sc


def get_yaml(modId):
    """Get complete kubernetes yaml for a folio module.


    Example:

    .. code-block:: python

        >>> from foliolib import server
        >>> from foliolib.okapi.okapiModuleKubernetes import get_yaml
        >>> server(SERVER_NAME)
        >>> print(get_yaml("mod-users-18.0.1"))

    Args:
        modId (str): Module id

    Returns:
        str: Kubernetes yaml
    """
    import yaml
    m = OkapiModuleKubernetes(modId)
    service = m.get_service()
    deployment = m.get_deployment()
    namespace = m.get_namespace()
    persistentVolumeClaim = m.get_persistentVolumeClaim()
    hazelcast_configMap = m.get_hazelcast_configMap()
    with StringIO() as f:
        if hazelcast_configMap:
            hazelcast_configMap["metadata"]["namespace"] = namespace
            yaml.dump(hazelcast_configMap, f)
            f.write("\n\n---\n\n")
        if persistentVolumeClaim:
            persistentVolumeClaim["metadata"]["namespace"] = namespace
            yaml.dump(persistentVolumeClaim, f)
            f.write("\n\n---\n\n")
        service["metadata"]["namespace"] = namespace
        yaml.dump(service, f)
        f.write("\n\n---\n\n")
        deployment["metadata"]["namespace"] = namespace
        yaml.dump(deployment, f)
        f.seek(0)
        return f.read()
