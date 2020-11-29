# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>


import json
import logging
import sys
from distutils.version import LooseVersion
from typing import Union
from urllib.parse import urlencode

import requests
from github import Github
from lxml import etree
from foliolib.config import Config
from foliolib.okapi import okapiModule
from foliolib.okapi.exceptions import (OkapiException, OkapiFatalError,
                                       OkapiMoved, OkapiRequestConflict,
                                       OkapiRequestError, OkapiRequestForbidden,
                                       OkapiRequestNotAcceptable,
                                       OkapiRequestNotFound,
                                       OkapiRequestPayloadToLarge,
                                       OkapiRequestTimeout,
                                       OkapiRequestUnauthorized,
                                       OkapiRequestUnprocessableEntity)

log = logging.getLogger("foliolib.okapi.okapiClient")


class Success:

    def __init__(self, response) -> None:
        self.response = response
        self.status_code = response.status_code
        self.message = response.text or "success"
        self.headers = response.headers

    def __str__(self) -> str:
        return f"{self.status_code}: {self.message}"


class OkapiClient:
    """
    An Okapi client

    https://s3.amazonaws.com/foliodocs/api/okapi/p/okapi.html
    """

    tenant_access_tokens = {}

    def __init__(self, host: str = None, port: str = None) -> None:
        """
        Args:
            host (str, optional): IP or Hostame of the Okapi server. Defaults from foliolib.conf.
            port (str, optional):. Defaults from foliolib.conf.
        """
        host = host or Config().okapicfg().get("Okapi", "host")
        port = port or Config().okapicfg().get("Okapi", "port")
        self._host = f"http://{host}:{port}"
        self._client = requests.Session()

        self._access_token = Config().okapicfg().get(
            "Okapi", "token") if Config().okapicfg().has_option("Okapi", "token") else None
        self.headers = None
        self.status_code = 0

    def version(self):
        """Get the Okapi version.

        Returns:
            str: Okapi version
        """
        return self._request("GET", "/_/version")

    def get_env(self):
        """Get enviroment variables.

        Returns:
            dict: Enviroment variables
        """
        return self._request("GET", "/_/env")

    def set_env(self, name: str, value: str, description: str = ""):
        """Set an enviroment variable.

        Args:
            name (str): Name of the enviroment variable.
            value (str): Value of the enviroment variable.

        Returns:
            dict: Dict of the enviroment variable.

        Headers:
            - **Location** - URI to the environment entry instance


        """
        return self._request("POST", "/_/env", {"name": name, "value": value, "description": description})

    def health(self, serviceID: str = None, instanceId: str = None):
        """Check health of modules

        Args:
            serviceID (str, optional): Get Health for service with serviceID. Defaults to None.
            instanceId (str, optional): Get Health for instance with instanceId. Defaults to None.

        Returns:
            dict: Dict with health status.
        """
        url = "/_/discovery/health"
        if serviceID is not None:
            url += "/" + serviceID
            if instanceId is not None:
                url += "/" + instanceId
        return self._request("GET", url)

    def get_nodes(self):
        """Get list of all nodes

        Returns:
            dict: Dict with node items.
        """
        return self._request("GET", "/_/discovery/nodes")

    def get_module(self, modId: str):
        """Retrieve descriptor for a particular module

        Args:
            modId (str): Module id.

        Returns:
            dict: Module descriptor
        """
        return self._request("GET", f"/_/proxy/modules/{modId}")

    def get_modules(self, **kwargs):
        """List all or subset of modules for proxy

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            dot (boolean): default = false
                        If true, return Graphviz DOT content as plain text
            filter (string): Filter by module ID
            full (boolean): default = false
                        Whether full or compact MD should be returned
            latest (integer): Limit to latest N releases (most likely 1 if given)
            npmSnapshot (boolean): default = true
                            Whether to include NPM module snapshots
            order (one of desc, asc): Order
            orderBy (string): Order by field
            preRelease (boolean): default = true
                            Whether to include modules with pre-release info
            provide (string): Limit to provided interface
            require (string): Limit to required interface
            scope (string): Limit to interface scope (only useful with provide and require)

        Returns:
            dict: Dict with modules
        """
        return self._request("GET", "/_/proxy/modules", query=kwargs)

    def add_module(self, module: Union[str, okapiModule.OkapiModule], **kwargs):
        """Add a module

        Args:
            module (Union[str, OkapiModule]): Module Descriptor or instance of OkapiModule
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            check (boolean): default = true
                        Whether to check dependencies
            preRelease (boolean): default = true
                        Whether to allow pre-release modules in dependency check
            npmSnapshot (boolean): default = true
                        Whether to allow NPM module snapshots in dependency check

        Returns:
            dict: Module descriptor
        """
        if isinstance(module, okapiModule.OkapiModule):
            descriptor = module.get_descriptor()
        else:
            descriptor = module
        return self._request("POST", "/_/proxy/modules",
                             descriptor, query=kwargs)

    def remove_module(self, modId: str):
        """Remove module descriptor for a particular module,
        module will no longer be selectable by tenants.

        Args:
            modId (str): Module id
        """
        return self._request("DELETE", f"/_/proxy/modules/{modId}")

    def get_deployed_module(self, modId, instanceId=None):
        """Get deployed module

        Args:
            modId (str): Module id.
            instanceId (str, optional): Instance id. Defaults to None.

        Returns:
            dict: Deployment descriptor
        """
        url = f"/_/discovery/modules/{modId}"
        if instanceId is not None:
            url += "/" + instanceId
        return self._request("GET", url)

    def get_deployed_modules(self):
        """Get all deployed modules.

        Returns:
            dict: Dict with deployment descriptors.
        """
        return self._request("GET", "/_/discovery/modules")

    def deploy_module(self, modId: str, node: str):
        """Deploy a module.

        Args:
            modId (str): Module id
            node (str):

        Returns:
            dict: Deployment descriptor
        """
        modules = self.get_deployed_modules()
        for module in modules:
            if module["srvcId"] == modId:
                return False
        return self._request("POST", "/_/discovery/modules",
                             {"srvcId": modId, "nodeId": node})

    def undeploy_module(self, modId: str, instanceId=None):
        """Remove registration for a given instance

        Args:
            modId (str): Module id
            instanceId (str, optional): Instance id. Defaults to None.
        """
        url = f"/_/discovery/modules/{modId}"
        if instanceId is not None:
            url += "/" + instanceId
        return self._request("DELETE", url)

    def undeploy_modules(self):
        """Remove registration for all instances
        """
        return self._request("DELETE", "/_/discovery/modules")

    def get_tenants(self):
        """Get a list of all tenants

        Returns:
            dict: Dict with all tenants
        """
        return self._request("GET", "/_/proxy/tenants")

    def get_tenant_module(self, modId: str, tenantId: str):
        """Get a list of all modules of a tenant

        Args:
            modId (str): Module id
            tenantId (str): Tenant id

        Returns:
            dict: Dict with modules
        """
        return self._request("GET", f"/_/proxy/tenants/{tenantId}/modules{modId}")

    def get_tenant_modules(self, tenantId: str, **kwargs):
        """[summary]

        Args:
            tenantId (str): Tenant id.
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            dot (boolean): default: = false
                        If true, return Graphviz DOT content as plain text
            filter (string): Filter by module ID
            full: (boolean): default = false
                        Whether full or compact MD should be returned
            latest (integer): Limit to latest N releases (most likely 1 if given)
            npmSnapshot (boolean): default = true
                        Whether to include NPM module snapshots
            order (one of desc, asc): Order
            orderBy (string): Order by field
            preRelease (boolean): default: true
                        Whether to include modules with pre-release info
            provide (string): Limit to provided interface
            require (string): Limit to required interface
            scope (string): Limit to interface scope (only useful with provide and require)

        Returns:
            dict: Modules registered at this tenant
        """
        return self._request("GET", f"/_/proxy/tenants/{tenantId}/modules", query=kwargs)

    def get_tenant_interfaces(self, tenantId: str, **kwargs):
        """Get all interfaces of a tenant

        Args:
            tenantId (str): Tenant id.
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            full (boolean): default = false
                    Whether brief or full interface list
            type (string): Limit by interfaceType

        Returns:
            dict: Dict with interfaces of a tenant.
        """
        return self._request("GET", f"/_/proxy/tenants/{tenantId}/interfaces", query=kwargs)

    def get_tenant_interface(self,  interfaceId: str, tenantId: str, **kwargs):
        """Get interface for a tenant.

        Args:
            interfaceId (str):
            tenantId (str):
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            type (string): Limit by interfaceType

        Returns:
            dict: Dict with a interface of a tenant.
        """
        return self._request("GET", f"/_/proxy/tenants/{tenantId}/interfaces/{interfaceId}", query=kwargs)

    def create_tenant(self, tenantId: str, name: str = "", description: str = ""):
        """Create a new tenant

        Args:
            tenantId (str): Tenant id
            name (str, optional): Name of the tenant. Defaults to "".
            description (str, optional): Description of the tenant. Defaults to "".
        """
        name = name or tenantId
        description = description or f"{name} library"
        self._request("POST", "/_/proxy/tenants",
                      {"id": tenantId, "name": name, "description": description})
        self._request(
            "POST", f"/_/proxy/tenants/{tenantId}/modules", {"id": "okapi"})

    def modify_tenant(self, tenantId: str, name: str = "", description: str = ""):
        """Modify a tenant

        Args:
            tenantId (str): Tenant id
            name (str, optional): Name of the tenant. Defaults to "".
            description (str, optional): Description of the tenant. Defaults to "".
        """
        self._request("PUT", "/_/proxy/tenants",
                      {"id": tenantId, "name": name, "description": description})

    def remove_tenant(self, tenantId: str):
        """Remove a tenant

        Args:
            tenantId (str): Tenant id

        """
        return self._request("DELETE", f"/_/proxy/tenants/{tenantId}")

    def enable_module(self, modId: str, tenantId: str, loadSample: bool = False,
                      loadReference: bool = False, **kwargs):
        """Enable a module for a tenant

        Args:
            modId (str): Module id
            tenantId (str): Tenant id
            loadSample (bool, optional): If samples should loaded. Defaults to False.
            loadReference (bool, optional): If references should loaded. Defaults to False.
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            async (boolean): default = false
                        Whether to install in the background
            deploy (boolean): default = false
                        Whether to deploy
            ignoreErrors (boolean): default = false
                        Okapi 4.2.0 and later, it is possible to ignore errors during the install operation. This is done by supplying parameter ignoreErrors=true.
                        In this case, Okapi will try to upgrade all modules in the modules list, regardless if one of them fails. However, for individual modules,
                        if they fail, their upgrade will not be commited.
                        This is an experimental parameter which was added to be able to inspect all problem(s) with module upgrade(s).
            invoke (boolean): default = true
                        Whether to invoke for tenant init/permissions/purge
            npmSnapshot (boolean): default = true
                        Whether to include NPM module snapshots (default:true).
            preRelease (boolean): default = true
                        Whether pre-releases should be considered for installation.
            simulate (boolean): default = false
                        Whether the installation is simulated


        Returns:
            dict: Tenant module descriptor
        """
        return self.enable_modules([modId], tenantId, loadSample=loadSample, loadReference=loadReference, **kwargs)

    def enable_modules(self, modIds: list, tenantId: str, loadSample: bool = False,
                       loadReference: bool = False, **kwargs):
        """Enable modules for a tenant

        Args:
            modIds (list): List with Module ids
            tenantId (str): Tenant id
            loadSample (bool, optional): If samples should loaded. Defaults to False.
            loadReference (bool, optional): If references should loaded. Defaults to False.
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            async (boolean): default = false
                        Whether to install in the background
            deploy (boolean): default = false
                        Whether to deploy
            ignoreErrors (boolean): default = false
                        Okapi 4.2.0 and later, it is possible to ignore errors during the install operation. This is done by supplying parameter ignoreErrors=true.
                        In this case, Okapi will try to upgrade all modules in the modules list, regardless if one of them fails. However, for individual modules,
                        if they fail, their upgrade will not be commited.
                        This is an experimental parameter which was added to be able to inspect all problem(s) with module upgrade(s).
            invoke (boolean): default = true
                        Whether to invoke for tenant init/permissions/purge
            npmSnapshot (boolean): default = true
                        Whether to include NPM module snapshots (default:true).
            preRelease (boolean): default = true
                        Whether pre-releases should be considered for installation.
            simulate (boolean): default = false
                        Whether the installation is simulated

        Returns:
            dict: Tenant module descriptors
        """
        tenantParameters = []
        if loadSample:
            tenantParameters.append("loadSample=true")
        if loadReference:
            tenantParameters.append("loadReference=true")
        if tenantParameters:
            kwargs["tenantParameters"] = ",".join(tenantParameters)
        data = [{"id": modId, "action": "enable"} for modId in modIds]
        return self.install_modules(data, tenantId, **kwargs)

    def disable_module(self, modId: str, tenantId: str, **kwargs):
        """Disable a module for a tenant.

        Args:
            modId (str): Module id
            tenantId (str): Tenant id
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            async (boolean): default = false
                        Whether to uninstall in the background
            deploy (boolean): default = false
                        Whether to undeploy
            ignoreErrors (boolean): default = false
                        Okapi 4.2.0 and later, it is possible to ignore errors during the install operation. This is done by supplying parameter ignoreErrors=true.
                        In this case, Okapi will try to upgrade all modules in the modules list, regardless if one of them fails. However, for individual modules,
                        if they fail, their upgrade will not be commited.
                        This is an experimental parameter which was added to be able to inspect all problem(s) with module upgrade(s).
            invoke (boolean): default = true
                        Whether to invoke for tenant init/permissions/purge
            purge (boolean): default = false
                        Disabled modules will also be purged.
            simulate (boolean): default = false
                        Whether the installation is simulated

        Returns:
            dict: Dict with disabled modules
        """
        return self.disable_modules([modId], tenantId, **kwargs)

    def disable_modules(self, modIds: str, tenantId: str, **kwargs):
        """Disable modules for a tenant.

        Args:
            modIds (str):
            tenantId (str):
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            async (boolean): default = false
                        Whether to uninstall in the background
            deploy (boolean): default = false
                        Whether to undeploy
            ignoreErrors (boolean): default = false
                        Okapi 4.2.0 and later, it is possible to ignore errors during the install operation. This is done by supplying parameter ignoreErrors=true.
                        In this case, Okapi will try to upgrade all modules in the modules list, regardless if one of them fails. However, for individual modules,
                        if they fail, their upgrade will not be commited.
                        This is an experimental parameter which was added to be able to inspect all problem(s) with module upgrade(s).
            invoke (boolean): default = true
                        Whether to invoke for tenant init/permissions/purge
            npmSnapshot (boolean): default = true
                        Whether to include NPM module snapshots (default:true).
            purge (boolean): default = false
                        Disabled modules will also be purged.
            simulate (boolean): default = false
                        Whether the installation is simulated

        Returns:
            dict: Dict with disabled modules
        """
        data = [{"id": modId, "action": "disable"} for modId in modIds]
        return self.install_modules(data, tenantId, **kwargs)

    def install_modules(self, tenantModuleDescriptorList: list, tenantId: str, loadSample: bool = False,
                        loadReference: bool = False, **kwargs):
        """Enable, disable or upgrade one or more modules for tenant. The request body and response body is of the same type TenantModuleDescriptorList.
        This list includes one or more modules to be enabled, disabled or upgraded. The request is the initial desired changes and the response is the
        list of changes that must be fulfilled to satisfy dependencies. This service will eventually partially replace /_/proxy/tenants/{tenant}/modules .
        It also allows enabling multiple modules in one transaction. For simulate=true, the response, can be viewed as a recipe for what must
        be deployed (optionally) and enabled/disabled by the existing tenants-modules CRUD service.

        Args:
            tenantModuleDescriptorList (list):
            tenantId (str):
            loadSample (bool, optional): If samples should loaded. Defaults to False.
            loadReference (bool, optional): If references should loaded. Defaults to False.
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            async (boolean): default = false
                        Whether to install in the background
            deploy (boolean): default = false
                        Whether to deploy (or undeploy if disabling)
            ignoreErrors (boolean): default = false
                        Okapi 4.2.0 and later, it is possible to ignore errors during the install operation. This is done by supplying parameter ignoreErrors=true.
                        In this case, Okapi will try to upgrade all modules in the modules list, regardless if one of them fails. However, for individual modules,
                        if they fail, their upgrade will not be commited.
                        This is an experimental parameter which was added to be able to inspect all problem(s) with module upgrade(s).
            invoke (boolean): default = true
                        Whether to invoke for tenant init/permissions/purge
            npmSnapshot (boolean): default = true
                        Whether to include NPM module snapshots (default:true).
            preRelease (boolean): default = true
                        Whether pre-releases should be considered for installation.
            purge (boolean): default = false
                        Disabled modules will also be purged.
            simulate (boolean): default = false
                        Whether the installation is simulated

        Returns:
            dict: Tenant module descriptors
        """
        tenantParameters = []
        if loadSample:
            tenantParameters.append("loadSample=true")
        if loadReference:
            tenantParameters.append("loadReference=true")
        if tenantParameters:
            kwargs["tenantParameters"] = ",".join(tenantParameters)
        return self._request("POST", f"/_/proxy/tenants/{tenantId}/install",
                             tenantModuleDescriptorList, query=kwargs)

    def disable_all_modules(self, tenantId: str, **query):
        """Disable all modules of a tenant

        Args:
            tenantId (str):
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            invoke (boolean): default = true
                            Whether to invoke for tenant init/permissions/purge
            purge (boolean): default = false
                            Disabled modules will also be purged.
            tenantParameters (string): Parameters for Tenant init
        """
        return self._request("POST", f"/ _/proxy/tenants/{tenantId}/modules", query=query)

    def upgrade_modules(self, tenantId: str, **kwargs):
        """[summary]

        Args:
            tenantId (str):
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            async (boolean): default = false
                        Whether to upgrade in the background
            deploy (boolean): default = false
                        Whether to deploy (or undeploy if disabling)
            ignoreErrors (boolean): default = false
                        Okapi 4.2.0 and later, it is possible to ignore errors during the upgrade operation.
                        This is done by supplying parameter ignoreErrors=true.
                        In this case, Okapi will try to upgrade all modules in the modules list, regardless if one of them fails.
                        However, for individual modules, if they fail, their upgrade will not be commited. This is an experimental
                        parameter which was added to be able to inspect all problem(s) with module upgrade(s).
            invoke (boolean): default = true
                        Whether to invoke for tenant init/permissions/purge
            preRelease (boolean): default = true
                        Whether pre-releases should be considered for installation.
            purge (boolean): default = false
                        Disabled modules will also be purged
            simulate (boolean): default = false
                        Whether the upgrade is simulated
            tenantParameters (string): Parameters for Tenant init

        Returns:
            dict: Tenant module descriptors
        """
        path = f"/_/proxy/tenants/{tenantId}/upgrade"
        return self._request("POST", path, data="", query=kwargs)

    def get_install_jobs(self, tenantId: str, install_id: str = None):
        """Get install jobs for a tenant

        Args:
            tenantId (str): Tenant id
            install_id (str, optional): Install id. Defaults to None.

        Returns:
            dict: Dict with install jobs
        """
        url = f"/ _/proxy/tenants/{tenantId}/install"
        if install_id is not None:
            url += "/" + install_id
        return self._request("Get", url)

    def is_module_enabled(self, modName: str, tenantId: str):
        """Check if a module is enabled

        Args:
            modName (str): Modulename
            tenantId (str): Tenant id

        Returns:
            bool: True if enabled else False
        """
        return modName in [i["id"] for i in self.get_tenant_interfaces(tenantId)]

    def call_tenant_service(self, method: str, service: str, tenantId: str, data: dict = None,
                            query: dict = None, headers: dict = None, files: dict = None):
        """Call a tenant service

        Args:
            method (str): HTML method (GET, POST, PUT, DELETE ...)
            service (str): Path of the service
            tenantId (str): Tenant id
            data (dict, optional): Post data to call the service. Defaults to None.
            query (dict, optional): Query data to call the service. Defaults to None.
            headers (dict, optional): Headers to call the service. Defaults to None.
            files (dict, optional): Files to upload. Defaults to None.

        Returns:
            any: Return data of the service
        """
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
        if self.status_code >= 200 or self.status_code < 300:
            return res
        else:
            log.error("%i - %s: %s", self.status_code,
                      service, str(res))
            return None

    def _request(self, method: str, path: str, data: dict = None,
                 query: dict = None, headers: dict = None, files: dict = None):
        """Make a request

        Args:
            method (str): HTML method (GET, POST, PUT, DELETE ...)
            path (str): Path of the service
            data (dict, optional): Post data for the request. Defaults to None.
            query (dict, optional): Query data for the request. Defaults to None.
            headers (dict, optional): Headers for the request. Defaults to None.
            files (dict, optional): Files to upload. Defaults to None.

        Raises:
            OkapiRequestError:
            OkapiRequestUnauthorized:
            OkapiRequestForbidden:
            OkapiRequestNotFound:
            OkapiRequestNotAcceptable:
            OkapiRequestTimeout:
            OkapiRequestConflict:
            OkapiRequestPayloadToLarge:
            OkapiRequestUnprocessableEntity:
            OkapiFatalError:
            OkapiException:

        Returns:
            any: return the response of the request
        """
        url = self._host + path
        if query:
            url += "?" + urlencode(query)
        headers = headers or {}
        headers = requests.structures.CaseInsensitiveDict(data=headers)
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
        elif "Content-Type" in headers and "octet-stream" in headers["Content-Type"]:
            request = self._client.prepare_request(
                requests.Request(
                    method, url, data=data, headers=headers))
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
            return Success(response)
        elif response.status_code == 204:
            return Success(response)
        elif response.status_code == 302:
            return OkapiMoved(response)
        elif response.status_code == 400:
            raise OkapiRequestError(response)
        elif response.status_code == 401:
            raise OkapiRequestUnauthorized(response)
        elif response.status_code == 403:
            raise OkapiRequestForbidden(response)
        elif response.status_code == 404:
            raise OkapiRequestNotFound(response)
        elif response.status_code == 406:
            raise OkapiRequestNotAcceptable(response)
        elif response.status_code == 408:
            raise OkapiRequestTimeout(response)
        elif response.status_code == 409:
            raise OkapiRequestConflict(response)
        elif response.status_code == 413:
            raise OkapiRequestPayloadToLarge(response)
        elif response.status_code == 422:
            raise OkapiRequestUnprocessableEntity(response)
        elif response.status_code >= 500:
            raise OkapiFatalError(response)
        else:
            print(response.text)
            raise OkapiException(
                f"ERROR {response.status_code}: Not implemented")


def request_release(name: str, version: str = None):
    """Get release data of a folio module from github

    Args:
        name (str): Module name
        version (str, optional): Version of the release. Defaults to None.

    Raises:
        OkapiNotFound:

    Returns:
        dict: Dict with release data.
    """
    access_token = Config().foliolibcfg().get("GitHub", "access-token")
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
        raise OkapiRequestNotFound(f"There is no release for {name} {version}")
    tarball_url = release.tarball_url

    return {"name": name,
            "version": version,
            "url": tarball_url}


def request_docker_tag(name: str, version: str = None, repository: str = "folioorg"):
    """Get the docker tag of a folio module.

    Args:
        name (str): Module name
        version (str, optional): Version of the module. Defaults to None.
        repository (str, optional):Docker repository. Defaults to "folioorg".

    Raises:
        OkapiException:

    Returns:
        str: Docker tag
    """
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


def request_snapshot_version(name: str):
    """Get the latest snapshot version from github.

    Args:
        name (str): Module name

    Returns:
        str: Snapshot version
    """
    url = f"https://raw.githubusercontent.com/folio-org/{name}/master/pom.xml"
    response = requests.get(url)
    root = etree.fromstring(response.text.encode("utf-8"))
    version = root.find('version', root.nsmap).text
    tag = request_docker_tag(name, version, repository="folioci")
    log.info("Latest snapshot version is %s", tag)

    return tag
