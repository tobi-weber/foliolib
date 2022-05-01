# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>

import os

from kubernetes import client, config


class KubeClient:

    def __init__(self):
        os.environ["KUBECONFIG"] = "/etc/folio/oakpi/kube_config"
        config.load_kube_config()

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

    def get_service(self, serviceId):
        pass

    def get_services(self, namespace=None):
        core_v1 = client.CoreV1Api()
        if namespace is None:
            return core_v1.list_service_for_all_namespaces()
        else:
            return core_v1.list_namespaced_service(namespace)

    def create_service(self, data):
        pass

    def get_deployment(self, deploymentId):
        pass

    def get_deployments(self):
        pass

    def create_deployment(self, data, namespace="default"):
        apps_v1 = client.AppsV1Api()
        return apps_v1.create_namespaced_deployment(
            body=data, namespace=namespace)
