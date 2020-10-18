# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>


import json
import logging
import sys
from distutils.version import LooseVersion
from urllib.parse import urlencode

import requests
from github import Github
from lxml import etree
from pyokapi.config import CONFIG
from pyokapi.okapi.exceptions import (OkapiException, OkapiForbidden,
                                      OkapiInvalid, OkapiNotFound,
                                      OkapiUnauthorized)
from pyokapi.okapi.okapiModule import OkapiModule

log = logging.getLogger("okapi.okapiClient")


class OkapiClient:
    """
    https://s3.amazonaws.com/foliodocs/api/okapi/p/okapi.html
    """

    tenant_access_tokens = {}

    def __init__(self, host: str = None, port: str = None) -> None:
        host = host or CONFIG.okapicfg().get("Okapi", "host")
        port = port or CONFIG.okapicfg().get("Okapi", "port")
        self._host = f"http://{host}:{port}"
        self._client = requests.Session()

        self._access_token = CONFIG.okapicfg().get(
            "Okapi", "token") if CONFIG.okapicfg().has_option("Okapi", "token") else None
        self.headers = None
        self.status_code = 0

    def version(self):
        return self._request("GET", "/_/version")

    def get_env(self):
        return self._request("GET", "/_/env")

    def set_env(self, name, value):
        return self._request("POST", "/_/env", {"name": name, "value": value})

    def health(self, serviceID=None, instanceId=None):
        url = "/_/discovery/health"
        if serviceID is not None:
            url += "/" + serviceID
            if instanceId is not None:
                url += "/" + instanceId
        return self._request("GET", url)

    def get_nodes(self):
        return self._request("GET", "/_/discovery/nodes")

    def get_module(self, modId):
        return self._request("GET", f"/_/proxy/modules/{modId}")

    def get_modules(self, **query):
        """
        Query Parameters
            dot: (boolean - default: false)
            If true, return Graphviz DOT content as plain text

            filter: (string)
            Filter by module ID

            full: (boolean - default: false)
            Whether full or compact MD should be returned

            latest: (integer)
            Limit to latest N releases (most likely 1 if given)

            npmSnapshot: (boolean - default: true)
            Whether to include NPM module snapshots

            order: (one of desc, asc)
            Order

            orderBy: (string)
            Order by field

            preRelease: (boolean - default: true)
            Whether to include modules with pre-release info

            provide: (string)
            Limit to provided interface

            require: (string)
            Limit to required interface

            scope: (string)
            Limit to interface scope (only useful with provide and require)
        """
        return self._request("GET", "/_/proxy/modules", query=query)

    def add_module(self, okapiModule: OkapiModule, **query):
        """
        Query Parameters:
            check: (boolean - default: true)
            Whether to check dependencies

            preRelease: (boolean - default: true)
            Whether to allow pre-release modules in dependency check

            npmSnapshot: (boolean - default: true)
            Whether to allow NPM module snapshots in dependency check
        """
        return self._request("POST", "/_/proxy/modules", okapiModule.get_descriptor(), query)

    def remove_module(self, modId: str):
        return self._request("DELETE", f"/_/proxy/modules/{modId}")

    def get_deployed_module(self, modId, instanceId=None):
        url = f"/_/discovery/modules/{modId}"
        if instanceId is not None:
            url += "/" + instanceId
        return self._request("GET", url)

    def get_deployed_modules(self):
        return self._request("GET", "/_/discovery/modules")

    def deploy_module(self, modId: str, node: str):
        modules = self.get_deployed_modules()
        for module in modules:
            if module["srvcId"] == modId:
                return False
        return self._request("POST", "/_/discovery/modules",
                             {"srvcId": modId, "nodeId": node})

    def undeploy_module(self, modId: str, instanceId=None):
        url = f"/_/discovery/modules/{modId}"
        if instanceId is not None:
            url += "/" + instanceId
        return self._request("DELETE", url)

    def undeploy_modules(self):
        return self._request("DELETE", "/_/discovery/modules")

    def get_tenants(self):
        return self._request("GET", "/_/proxy/tenants")

    def get_tenant_module(self, modId: str, tenantId: str):
        return self._request("GET", f"/_/proxy/tenants/{tenantId}/modules{modId}")

    def get_tenant_modules(self, tenantId: str, **query):
        """
        Query Parameters
            dot: (boolean - default: false)
            If true, return Graphviz DOT content as plain text

            filter: (string)
            Filter by module ID

            full: (boolean - default: false)
            Whether full or compact MD should be returned

            latest: (integer)
            Limit to latest N releases (most likely 1 if given)

            npmSnapshot: (boolean - default: true)
            Whether to include NPM module snapshots

            order: (one of desc, asc)
            Order

            orderBy: (string)
            Order by field

            preRelease: (boolean - default: true)
            Whether to include modules with pre-release info

            provide: (string)
            Limit to provided interface

            require: (string)
            Limit to required interface

            scope: (string)
            Limit to interface scope (only useful with provide and require)
        """
        return self._request("GET", f"/_/proxy/tenants/{tenantId}/modules", query=query)

    def get_tenant_interfaces(self, tenantId: str, **query):
        """
        Query Parameters
            full: (boolean - default: false)
            Whether brief or full interface list

            type: (string)
            Limit by interfaceType
        """
        return self._request("GET", f"/_/proxy/tenants/{tenantId}/interfaces")

    def get_tenant_interface(self,  interfaceId: str, tenantId: str, **query):
        """
        Query Parameters
            type: (string)
            Limit by interfaceType
        """
        return self._request("GET", f"/_/proxy/tenants/{tenantId}/interfaces/{interfaceId}")

    def create_tenant(self, tenantId: str, name: str = "", description: str = ""):
        name = name or tenantId
        description = description or f"{name} library"
        self._request("POST", "/_/proxy/tenants",
                      {"id": tenantId, "name": name, "description": description})
        self._request(
            "POST", f"/_/proxy/tenants/{tenantId}/modules", {"id": "okapi"})

    def modify_tenant(self, tenantId: str, name: str = "", description: str = ""):
        self._request("PUT", "/_/proxy/tenants",
                      {"id": tenantId, "name": name, "description": description})

    def remove_tenant(self, tenantId: str):
        return self._request("DELETE", f"/_/proxy/tenants/{tenantId}")

    def enable_module(self, modId: str, tenantId: str, loadSample: bool = False,
                      loadReference: bool = False, **query):
        # return self._request("POST", f"/_/proxy/tenants/{tenant}/modules", {"id": modId})
        return self.enable_modules([modId], tenantId, loadSample=loadSample, loadReference=loadReference, **query)

    def enable_modules(self, modIds: list, tenantId: str, loadSample: bool = False,
                       loadReference: bool = False, **query):
        """
        Query Parameters
            async: (boolean - default: false)
            Whether to install in the background

            deploy: (boolean - default: false)
            Whether to deploy (or undeploy if disabling)

            ignoreErrors: (boolean - default: false)
            Okapi 4.2.0 and later, it is possible to ignore errors during the install operation. This is done by supplying parameter ignoreErrors=true. In this case, Okapi will try to upgrade all modules in the modules list, regardless if one of them fails. However, for individual modules, if they fail, their upgrade will not be commited. This is an experimental parameter which was added to be able to inspect all problem(s) with module upgrade(s).

            invoke: (boolean - default: true)
            Whether to invoke for tenant init/permissions/purge

            npmSnapshot: (boolean - default: true)
            Whether to include NPM module snapshots (default:true).

            preRelease: (boolean - default: true)
            Whether pre-releases should be considered for installation.

            purge: (boolean - default: false)
            Disabled modules will also be purged.

            simulate: (boolean - default: false)
            Whether the installation is simulated
        """
        tenantParameters = []
        if loadSample:
            tenantParameters.append("loadSample=true")
        if loadReference:
            tenantParameters.append("loadReference=true")
        if tenantParameters:
            query["tenantParameters"] = ",".join(tenantParameters)
        data = [{"id": modId, "action": "enable"} for modId in modIds]
        return self.install_modules(data, tenantId, **query)

    def disable_module(self, modId: str, tenantId: str):
        # return self._request("DELETE", f"/_/proxy/tenants/{tenant}/modules/{modId}")
        return self.disable_modules([modId], tenantId)

    def disable_modules(self, modIds: str, tenantId: str):
        data = [{"id": modId, "action": "disable"} for modId in modIds]
        return self.install_modules(data, tenantId)

    def install_modules(self, tenantModuleDescriptorList: list, tenantId: str, **query):
        return self._request("POST", f"/_/proxy/tenants/{tenantId}/install",
                             tenantModuleDescriptorList, query=query)

    def disable_all_modules(self, tenantId: str, **query):
        """
        Query Parameters
            invoke: (boolean - default: true)
            Whether to invoke for tenant init/permissions/purge

            purge: (boolean - default: false)
            Disabled modules will also be purged.

            tenantParameters: (string)
            Parameters for Tenant init
        """
        return self._request("POST", f"/ _/proxy/tenants/{tenantId}/modules", query=query)

    def upgrade_modules(self, tenantId: str, **query):
        """
        Query Parameters
            async: (boolean - default: false)
            Whether to upgrade in the background

            deploy: (boolean - default: false)
            Whether to deploy (or undeploy if disabling)

            ignoreErrors: (boolean - default: false)
            Okapi 4.2.0 and later, it is possible to ignore errors during the upgrade operation. This is done by supplying parameter ignoreErrors=true. In this case, Okapi will try to upgrade all modules in the modules list, regardless if one of them fails. However, for individual modules, if they fail, their upgrade will not be commited. This is an experimental parameter which was added to be able to inspect all problem(s) with module upgrade(s).

            invoke: (boolean - default: true)
            Whether to invoke for tenant init/permissions/purge

            preRelease: (boolean - default: true)
            Whether pre-releases should be considered for installation.

            purge: (boolean - default: false)
            Disabled modules will also be purged

            simulate: (boolean - default: false)
            Whether the upgrade is simulated

            tenantParameters: (string)
            Parameters for Tenant init
        """
        path = f"/_/proxy/tenants/{tenantId}/upgrade"
        return self._request("POST", path, data="", query=query)

    def get_install_jobs(self, tenantId, install_id=None):
        url = f"/ _/proxy/tenants/{tenantId}/install"
        if install_id is not None:
            url += "/" + install_id
        return self._request("Get", url)

    def is_module_enabled(self, modName: str, tenantId: str):
        return modName in [i["id"] for i in self.get_tenant_interfaces(tenantId)]

    def call_tenant_service(self, method, service: str, tenantId: str, data: dict = None,
                            query: dict = None, headers: dict = None, files: dict = None):
        if not service.startswith(("/")):
            service = "/" + service
        headers = headers or {}
        headers["X-Okapi-Tenant"] = tenantId
        if tenantId in OkapiClient.tenant_access_tokens:
            headers["X-Okapi-Token"] = OkapiClient.tenant_access_tokens[tenantId]
        res = self._request(method.upper(), service,
                            data=data, query=query, headers=headers, files=files)
        if "x-okapi-token" in self.headers:
            log.debug("Token for %s: %s", tenantId,
                      self.headers["X-Okapi-Token"])
            OkapiClient.tenant_access_tokens[tenantId] = self.headers["X-Okapi-Token"]
        if self.status_code >= 200 or self.status_code <= 226:
            return res
        else:
            log.debug("ERROR %i - %s: %s", self.status_code,
                      service, str(res))
            return None

    def _request(self, method: str, path: str, data: dict = None,
                 query: dict = None, headers: dict = None, files: dict = None):
        url = self._host + path
        if query:
            url += "?" + urlencode(query)
        headers = headers or {}
        headers["Accept"] = 'application/json, text/plain'
        if "X-Okapi-Token" not in headers:
            if self._access_token is not None:
                headers["X-Okapi-Token"] = self._access_token

        if method == "GET" or method == "DELETE":
            request = self._client.prepare_request(
                requests.Request(method, url, headers))
        elif files is not None:
            request = self._client.prepare_request(
                requests.Request(
                    method, url, files=files, data=data, headers=headers))
        else:
            headers["content-type"] = "application/json"
            request = self._client.prepare_request(
                requests.Request(
                    method, url, data=json.dumps(data), headers=headers))

        try:
            response = self._client.send(request)
        except requests.exceptions.ConnectionError:
            print(f"Okapi server {self._host} is not reachable!")
            sys.exit(1)

        log.debug("%s %s %i", method, url, response.status_code)
        log.debug(headers)
        self.headers = response.headers
        self.status_code = response.status_code
        if response.status_code == 200 or response.status_code == 201:
            try:
                return response.json()
            except json.decoder.JSONDecodeError:
                return response.text
        elif response.status_code == 202:
            return response.text
        elif response.status_code == 204:
            return True
        elif response.status_code == 400:
            raise OkapiInvalid(response)
        elif response.status_code == 401:
            raise OkapiUnauthorized(
                f"ERROR {response.status_code}: {response.text}")
        elif response.status_code == 403:
            raise OkapiForbidden(
                f"ERROR {response.status_code}: {response.text}")
        elif response.status_code == 404:
            raise OkapiNotFound(
                f"ERROR {response.status_code}: {response.text}")
        elif response.status_code == 422:
            raise OkapiInvalid(response)
        elif response.status_code >= 500:
            raise OkapiException(
                f"ERROR {response.status_code}: {response.text}\n{url}")
        else:
            print(response.text)
            raise OkapiException(
                f"ERROR {response.status_code}: Not implemented")


def request_release(name: str, version: str = None):
    access_token = CONFIG.pyokapicfg().get("GitHub", "access-token")
    g = Github(access_token)
    repo = g.get_repo(f"folio-org/{name}")
    if version is None:
        release = repo.get_latest_release()
        version = release.tag_name.replace("v", "")
        log.info("No version given. Latest version is %s", version)

    releases = repo.get_releases()
    release = None
    for r in releases:
        if version in r.tag_name:
            release = r
            break
    if not release:
        raise OkapiNotFound(f"There is no release for {name} {version}")
    tarball_url = release.tarball_url

    return {"name": name,
            "version": version,
            "url": tarball_url}


def request_docker_tag(name: str, version: str = None, repository: str = "folioorg"):
    url = f"https://registry.hub.docker.com/v1/repositories/{repository}/{name}/tags"
    response = requests.get(url)
    tags = response.json()
    if not tags:
        raise OkapiException(f"Docker Image for {name} not found")
    if version is not None:
        tags = [tag["name"]
                for tag in tags if version in tag["name"]]
    if version is None or len(tags) == 0:
        tags = response.json()
        tags = [tag["name"].replace("v", "")
                for tag in tags if not "latest" in tag["name"]]
    try:
        tags = sorted(tags, key=LooseVersion)
    except:
        tags = sorted(tags)

    tag = tags.pop()

    return tag


def request_snapshot_version(name):
    url = f"https://raw.githubusercontent.com/folio-org/{name}/master/pom.xml"
    response = requests.get(url)
    root = etree.fromstring(response.text.encode("utf-8"))
    version = root.find('version', root.nsmap).text
    tag = request_docker_tag(name, version, repository="folioci")
    log.info("Latest snapshot version is %s", tag)

    return tag
