# -*- coding: utf-8 -*-
# Copyright (C) 2023 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os
from typing import Union
from urllib.parse import urlencode, urljoin

import requests
import urllib3
from foliolib.config import Config
from foliolib.helper import get_node
from foliolib.okapi import misc, okapiModule
from foliolib.okapi.exceptions import (OkapiException, OkapiFatalError,
                                       OkapiMoved, OkapiNotReachable,
                                       OkapiRequestConflict, OkapiRequestError,
                                       OkapiRequestForbidden,
                                       OkapiRequestNotAcceptable,
                                       OkapiRequestNotFound,
                                       OkapiRequestPayloadToLarge,
                                       OkapiRequestTimeout,
                                       OkapiRequestUnauthorized,
                                       OkapiRequestUnprocessableEntity)
from foliolib.okapi.kubeClient import KubeClient

urllib3.disable_warnings()
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

    def __init__(self, host: str = None, port: str = None, path: str = None, ssl: bool = False) -> None:
        """
        Args:
            host (str, optional): IP or Hostame of the Okapi server. Defaults from foliolib.conf.
            port (str, optional):. Defaults from foliolib.conf.
        """
        host = host or Config().servercfg().get("Okapi", "host")
        port = port or Config().servercfg().get("Okapi", "port")
        self._okapi_path = path or Config().servercfg().get("Okapi", "path", fallback=None)
        ssl = ssl or Config().servercfg().getboolean("Okapi", "ssl", fallback=False)
        self._verify_ssl = Config().servercfg().getboolean(
            "Okapi", "verify_ssl", fallback=True)

        if ssl:
            self._host = f"https://{host}:{port}"
        else:
            self._host = f"http://{host}:{port}"

        self._client = requests.Session()
        self._access_token = Config().get_token("supertenant")
        self.headers = None
        self.status_code = 0

    def version(self):
        """Get the Okapi version.

        Returns:
            str: Okapi version
        """
        return self.request("GET", "/_/version")

    def get_env(self):
        """Get enviroment variables.

        Returns:
            dict: Enviroment variables
        """
        if Config().is_foliolib_env():
            return Config().get_env()
        else:
            if Config().is_kubernetes():
                return KubeClient().get_env()
            else:
                return self.request("GET", "/_/env")

    def set_env(self, name: str, value: str, description: str = ""):
        """Set an enviroment variable.

        Args:
            name (str): Name of the enviroment variable.
            value (str): Value of the enviroment variable.
            description (str): Optional description for the enviroment variable.

        Returns:
            dict: Dict of the enviroment variable.

        Headers:
            - **Location** - URI to the environment entry instance
        """
        if Config().is_foliolib_env():
            log.debug("Set global env in foliolib")
            Config().set_env(name, value)
            return Config().get_env()
        else:
            if Config().is_kubernetes():
                log.debug("Set global env in kubernetes")
                return KubeClient().set_env(name, value)
            else:
                log.debug("Set global env in okapi")
                return self.request("POST", "/_/env", {"name": name, "value": value, "description": description})

    def delete_env(self, name: str):
        """Delete an enviroment variable.

        Args:
            name (str): Name of the enviroment variable.
        """
        if Config().is_foliolib_env():
            Config().delete_env(name)
        else:
            if Config().is_kubernetes():
                return KubeClient().delete_env(name)
            else:
                return self.request("DELETE", "/_/env", {"name": name})

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
        return self.request("GET", url)

    def get_nodes(self):
        """Get list of all nodes

        Returns:
            dict: Dict with node items.
        """
        return self.request("GET", "/_/discovery/nodes")

    def get_module(self, modId: str):
        """Retrieve descriptor for a particular module

        Args:
            modId (str): Module id.

        Returns:
            dict: Module descriptor
        """
        return self.request("GET", f"/_/proxy/modules/{modId}")

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
        return self.request("GET", "/_/proxy/modules", query=kwargs)

    def add_module(self, module: Union[str, okapiModule.OkapiModule], **kwargs):
        """Add a module

        Args:
            module (Union[str, OkapiModule]): Module id, Module Descriptor or instance of OkapiModule
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
        if not isinstance(module, okapiModule.OkapiModule):
            module = okapiModule.OkapiModule(module)
        descriptor = module.get_descriptor()
        return self.request("POST", "/_/proxy/modules",
                            descriptor, query=kwargs)

    def remove_module(self, module: Union[str, okapiModule.OkapiModule]):
        """Remove module descriptor for a particular module,
        module will no longer be selectable by tenants.

        Args:
            module (Union[str, OkapiModule]): Module id, Module Descriptor or instance of OkapiModule
        """
        if not isinstance(module, okapiModule.OkapiModule):
            module = okapiModule.OkapiModule(module)
        modId = module.get_id()
        return self.request("DELETE", f"/_/proxy/modules/{modId}")

    def is_module_added(self, module: Union[str, okapiModule.OkapiModule]):
        """Is module added?

        Args:
            module (Union[str, OkapiModule]): Module id, Module Descriptor or instance of OkapiModule

        Returns:
            bool: wether module is added.
        """
        if not isinstance(module, okapiModule.OkapiModule):
            module = okapiModule.OkapiModule(module)
        modId = module.get_id()
        for m in self.get_modules(filter=modId):
            if m["id"] == modId:
                return True

        return False

    def get_deployed_module(self, modId: Union[str, okapiModule.OkapiModule], instanceId: str = None):
        """Get deployed module

        Args:
            modId (Union[str, OkapiModule]): Module id or instance of OkapiModule.
            instanceId (str, optional): Instance id. Defaults to None.

        Returns:
            dict: Deployment descriptor
        """
        if isinstance(modId, okapiModule.OkapiModule):
            modId = modId.get_id()
        url = f"/_/discovery/modules/{modId}"
        if instanceId is not None:
            url += "/" + instanceId
        return self.request("GET", url)

    def get_deployed_modules(self):
        """Get all deployed modules.

        Returns:
            dict: Dict with deployment descriptors.
        """
        return self.request("GET", "/_/discovery/modules")

    def deploy_module(self, modId: Union[str, okapiModule.OkapiModule], node: str = None):
        """Deploy a module.

        Args:
            modId (Union[str, OkapiModule]): Module id or instance of OkapiModule.
            node (str): The node id on which module should be deployed. Default first node from nodes list.

        Returns:
            dict: Deployment descriptor.
        """
        if isinstance(modId, okapiModule.OkapiModule):
            modId = modId.get_id()
        descriptor = self.get_module(modId)
        if "launchDescriptor" in descriptor:
            modules = self.get_deployed_modules()
            for module in modules:
                if module["srvcId"] == modId:
                    return False
            if Config().is_kubernetes():
                return KubeClient().deploy(modId)
            else:
                node = node or get_node()
                return self.request("POST", "/_/discovery/modules",
                                    {"srvcId": modId, "nodeId": node})
        else:
            log.error("%s has no launchDescriptor", modId)

    def undeploy_module(self, modId: Union[str, okapiModule.OkapiModule], instanceId=None):
        """Remove registration for a given instance.

        Args:
            modId (Union[str, OkapiModule]): Module id or instance of OkapiModule.
            instanceId (str, optional): Instance id. Defaults to None.
        """
        if isinstance(modId, okapiModule.OkapiModule):
            modId = modId.get_id()
        if Config().is_kubernetes():
            return KubeClient().undeploy(modId)
        else:
            url = f"/_/discovery/modules/{modId}"
            if instanceId is not None:
                url += "/" + instanceId
            return self.request("DELETE", url)

    def undeploy_modules(self):
        """Remove registration for all instances
        """
        return self.request("DELETE", "/_/discovery/modules")

    def is_module_deployed(self, modId: Union[str, okapiModule.OkapiModule]):
        """Is module deployed.

        Args:
            modId (Union[str, OkapiModule]): Module id or instance of OkapiModule.

        Returns:
            bool: wether module is deployed.
        """
        if isinstance(modId, okapiModule.OkapiModule):
            modId = modId.get_id()
        try:
            mods = self.get_deployed_modules()
            for mod in mods:
                if mod["srvcId"] == modId:
                    return True
        except:
            pass
        return False

    def get_tenants(self):
        """Get a list of all tenants

        Returns:
            dict: Dict with all tenants
        """
        return self.request("GET", "/_/proxy/tenants")

    def get_tenant_module(tenantId: str, self, modId: str):
        """Get a module of a tenant

        Args:
            tenantId (str): Tenant id.
            modId (str): Module id.

        Returns:
            dict: Dict with module data.
        """
        return self.request("GET", f"/_/proxy/tenants/{tenantId}/modules{modId}")

    def get_tenant_modules(self, tenantId: str, **kwargs):
        """Get a list of all modules of a tenant.

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
            dict: Modules registered at a tenant
        """
        return self.request("GET", f"/_/proxy/tenants/{tenantId}/modules", query=kwargs)

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
        return self.request("GET", f"/_/proxy/tenants/{tenantId}/interfaces", query=kwargs)

    def get_tenant_interface(self, tenantId: str, interfaceId: str, **kwargs):
        """Get interface for a tenant.

        Args:
            tenantId (str): Tenant id
            interfaceId (str): Interface id
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            type (string): Limit by interfaceType

        Returns:
            dict: Dict with a interface of a tenant.
        """
        kwargs["provide"] = interfaceId
        return self.request("GET", f"/_/proxy/tenants/{tenantId}/modules", query=kwargs)
        # return self._request("GET", f"/_/proxy/tenants/{tenantId}/interfaces/{interfaceId}", query=kwargs)

    def create_tenant(self, tenantId: str, name: str = "", description: str = ""):
        """Create a new tenant

        Args:
            tenantId (str): Tenant id
            name (str, optional): Name of the tenant. Defaults to "".
            description (str, optional): Description of the tenant. Defaults to "".
        """
        name = name or tenantId
        description = description or f"{name} library"
        self.request("POST", "/_/proxy/tenants",
                     {"id": tenantId, "name": name, "description": description})
        # Enable okapi module for the tenant.
        self.request(
            "POST", f"/_/proxy/tenants/{tenantId}/modules", {"id": "okapi"})

    def modify_tenant(self, tenantId: str, name: str = "", description: str = ""):
        """Modify a tenant

        Args:
            tenantId (str): Tenant id
            name (str, optional): Name of the tenant. Defaults to "".
            description (str, optional): Description of the tenant. Defaults to "".
        """
        self.request("PUT", f"/_/proxy/tenants/{tenantId}",
                     {"id": tenantId, "name": name, "description": description})

    def remove_tenant(self, tenantId: str):
        """Remove a tenant

        Args:
            tenantId (str): Tenant id

        """
        return self.request("DELETE", f"/_/proxy/tenants/{tenantId}")

    def enable_module(self, tenantId: str, modId: str, loadSample: bool = False,
                      loadReference: bool = False, upgrade=False, **kwargs):
        """Enable a module for a tenant

        Args:
            tenantId (str): Tenant id
            modId (str): Module id
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
        return self.enable_modules(tenantId, [modId], loadSample=loadSample, loadReference=loadReference,
                                   upgrade=upgrade, **kwargs)

    def enable_modules(self, tenantId: str, modIds: list, loadSample: bool = False,
                       loadReference: bool = False, deploy=False, **kwargs):
        """Enable modules for a tenant

        Args:
            tenantId (str): Tenant id
            modIds (list): List with Module ids
            loadSample (bool, optional): If samples should loaded. Defaults to False.
            loadReference (bool, optional): If references should loaded. Defaults to False.
            deploy (boolean), optional: Whether to deploy. Defaults to False
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            async (boolean): default = false
                        Whether to install in the background
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
        if deploy:
            for modId in modIds:
                if not self.is_module_added(modId):
                    self.add_module(modId)
                if not self.is_module_deployed(modId):
                    self.deploy_module(modId, get_node())
        data = [{"id": modId, "action": "enable"} for modId in modIds]
        return self.install_modules(data, tenantId, **kwargs)

    def disable_module(self, modId: str, tenantId: str, **kwargs):
        """Disable a module for a tenant.

        Args:
            modId (str): Module id
            tenantId (str): Tenant id
            **kwargs (properties): Keyword Arguments

        Keyword Args:
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
            reinstall: (boolean - default: false)
                        Whether to install modules even if up-to-update.
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
        return self.request("POST", f"/_/proxy/tenants/{tenantId}/install",
                            tenantModuleDescriptorList, query=kwargs)

    def disable_all_modules(self, tenantId: str, **kwargs):
        """Disable all modules of a tenant

        Args:
            tenantId (str): Tenant id
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            invoke (boolean): default = true
                            Whether to invoke for tenant init/permissions/purge
            purge (boolean): default = false
                            Disabled modules will also be purged.
            tenantParameters (string): Parameters for Tenant init
        """
        return self.request("POST", f"/ _/proxy/tenants/{tenantId}/modules", query=kwargs)

    def upgrade_modules(self, tenantId: str, modules: list = None, loadSample: bool = False,
                        loadReference: bool = False,  **kwargs):
        """[summary]

        Args:
            tenantId (str): Tenant id
            loadSample (bool, optional): If samples should loaded. Defaults to False.
            loadReference (bool, optional): If references should loaded. Defaults to False.
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
            simulate (boolean): default = false
                        Whether the upgrade is simulated
            tenantParameters (string): Parameters for Tenant init

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
        if modules is None:
            return self.request("POST", f"/_/proxy/tenants/{tenantId}/upgrade", query=kwargs)
        else:
            from foliolib.helper import split_modid
            installed_modules = [m["id"]
                                 for m in self.get_tenant_modules(tenantId)]
            upgrade_modules = []
            for modid in modules:
                modname, version = split_modid(modid)
                for from_modid in installed_modules:
                    if from_modid.startswith(modname):
                        upgrade_modules.append({"id": modid,
                                                "from": from_modid,
                                                "action": "enable"})
                        break
                else:
                    log.error("No previous version of %s installed in tenant %s",
                              modid, tenantId)
                    return
            return self.install_modules(upgrade_modules, tenantId, **kwargs)

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
        return self.request("Get", url)

    def is_module_enabled(self, modId: str, tenantId: str):
        """Check if a module is enabled.

        Args:
            modId (str): Modulename
            tenantId (str): Tenant id

        Returns:
            bool: Wether module is enabled.
        """
        modules = self.get_tenant_modules(tenantId, filter=modId)
        for mod in modules:
            if modId == mod["id"]:
                return True
        return False

    def call_tenant_service(self, tenantId: str, method: str, path: str, data: dict = None,
                            query: dict = None, headers: dict = None, files: dict = None):
        """Call a tenant service

        Args:
            tenantId (str): Tenant id
            method (str): HTML method (GET, POST, PUT, DELETE ...)
            path (str): Path of the service
            data (dict, optional): Post data to call the service. Defaults to None.
            query (dict, optional): Query data to call the service. Defaults to None.
            headers (dict, optional): Headers to call the service. Defaults to None.
            files (dict, optional): Files to upload. Defaults to None.

        Returns:
            any: Return data of the service
        """
        if not path.startswith(("/")):
            path = "/" + path
        headers = headers or {}
        headers["X-Okapi-Tenant"] = tenantId
        if not path.endswith("login") and Config().has_token(tenantId):
            headers["X-Okapi-Token"] = Config().get_token(tenantId)
        else:
            headers["X-Okapi-Token"] = ""
        res = self.request(method.upper(), path,
                           data=data, query=query, headers=headers, files=files)
        if "x-okapi-token" in self.headers:
            log.debug("Token for %s: %s", tenantId,
                      self.headers["X-Okapi-Token"])
            Config().set_token(tenantId, self.headers["X-Okapi-Token"])
        if self.status_code >= 200 or self.status_code < 300:
            return res
        else:
            log.error("%i - %s: %s", self.status_code,
                      path, str(res))
            return None

    def request(self, method: str, path: str, data: dict = None,
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
        if self._okapi_path is not None:
            if self._okapi_path.endswith("/"):
                self._okapi_path.pop()
            if not path.startswith("/"):
                path += "/" + path
            path = self._okapi_path + path
        url = urljoin(self._host, path)

        if query:
            query = urlencode(query)
            query = query.replace("True", "true").replace("False", "false")
            url += "?" + query

        headers = headers or {}
        headers = requests.structures.CaseInsensitiveDict(data=headers)
        headers["Accept"] = 'application/json, text/plain'
        if "X-Okapi-Token" not in headers:
            if self._access_token is not None:
                # log.debug("Token for supertenant: %s", self._access_token)
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
            if data is not None:
                data = json.dumps(data)
            request = self._client.prepare_request(
                requests.Request(
                    method, url, data=data, headers=headers))
        log.debug("%s %s", method, url)
        if data is not None:
            log.debug("Data:\n%s", json.dumps(data, indent=2))
        log.debug("Headers:\n%s", str(headers))

        try:
            response = self._client.send(request, verify=self._verify_ssl)
        except requests.exceptions.ConnectionError as err:
            log.error("Okapi server %s is not reachable!", self._host)
            log.error(err)
            raise OkapiNotReachable(
                f"Okapi server {self._host} is not reachable!") from err

        log.debug(response.status_code)
        if "FOLIOLIB_CURL" in os.environ:
            misc.print_curl(url, method, headers, data=data)
        self.headers = response.headers
        self.status_code = response.status_code
        if response.status_code == 200 or response.status_code == 201:
            try:
                return response.json()
            # except json.decoder.JSONDecodeError:
            except:
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
