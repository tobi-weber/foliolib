# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>


import json
import logging
import sys
from urllib.parse import urlencode

import requests

from okapi import CONFIG, OKAPI_FORWARDING, OKAPI_HOST, OKAPI_PORT
from okapi.exceptions import (OkapiException, OkapiForbidden, OkapiNotFound,
                              TenantNotFound)
from okapi.okapiModule import OkapiModule

log = logging.getLogger("okapi.okapiClient")


class OkapiClient:

    tenant_access_tokens = {}

    def __init__(self) -> None:
        self._host = f"http://{OKAPI_HOST}:{OKAPI_PORT}"
        self._client = requests.Session()

        self._access_token = CONFIG.get(
            "Okapi", "token") if "token" in CONFIG["Okapi"] else None
        self.headers = None
        self.status_code = 0

    def get_env(self):
        return self._request("GET", "/_/env")

    def set_env(self, name, value):
        return self._request("POST", "/_/env", {"name": name, "value": value})

    def get_nodes(self):
        return self._request("GET", "/_/discovery/nodes")

    def get_modules(self):
        return self._request("GET", "/_/proxy/modules")

    def add_module(self, okapiModule: OkapiModule):
        return self._request("POST", "/_/proxy/modules", okapiModule.get_descriptor())

    def remove_module(self, modId: str):
        return self._request("DELETE", f"/_/proxy/modules/{modId}")

    def get_deployed_modules(self):
        return self._request("GET", "/_/discovery/modules")

    def deploy_module(self, modId: str, node: str):
        modules = self.get_deployed_modules()
        for module in modules:
            if module["srvcId"] == modId:
                return False
        return self._request("POST", "/_/discovery/modules",
                             {"srvcId": modId, "nodeId": node})

    def undeploy_module(self, modId: str, node: str, port: str):
        return self._request("DELETE", f"/_/discovery/modules/{modId}/{node}-{port}")

    def get_tenants(self):
        return self._request("GET", "/_/proxy/tenants")

    def get_tenant_modules(self, tenant: str):
        try:
            return self._request("GET", f"/_/proxy/tenants/{tenant}/modules")
        except OkapiNotFound:
            raise TenantNotFound(f"Tenant {tenant} not found")

    def get_tenant_interfaces(self, tenant: str):
        try:
            return self._request("GET", f"/_/proxy/tenants/{tenant}/interfaces")
        except OkapiNotFound:
            raise TenantNotFound(f"Tenant {tenant} not found")

    def get_tenant_interface(self,  interfaceId: str, tenant: str):
        return self._request("GET", f"/_/proxy/tenants/{tenant}/interfaces/{interfaceId}")

    def create_tenant(self, tenant: str, name: str = "", description: str = ""):
        name = name or tenant
        description = description or f"{name} library"
        self._request("POST", "/_/proxy/tenants",
                      {"id": tenant, "name": name, "description": description})
        self._request(
            "POST", f"/_/proxy/tenants/{tenant}/modules", {"id": "okapi"})

    def remove_tenant(self, tenant: str):
        return self._request("DELETE", f"/_/proxy/tenants/{tenant}")

    def enable_module(self, modId: str, tenant: str, preRelease: bool = False,
                      ignoreErrors: bool = False, purge: bool = False, simulate: bool = False,
                      deploy: bool = False, loadSample: bool = False, loadReference: bool = False):
        # return self._request("POST", f"/_/proxy/tenants/{tenant}/modules", {"id": modId})
        return self.enable_modules([modId], tenant, preRelease=preRelease, deploy=deploy,
                                   ignoreErrors=ignoreErrors, purge=purge, simulate=simulate,
                                   loadSample=loadSample, loadReference=loadReference)

    def enable_modules(self, modIds: list, tenant: str, preRelease: bool = False, deploy: bool = False,
                       ignoreErrors: bool = False, purge: bool = False, simulate: bool = False,
                       loadSample: bool = False, loadReference: bool = False):
        query = {}
        if preRelease:
            query["preRelease"] = "true"
        if deploy:
            query["deploy"] = "true"
        if ignoreErrors:
            query["ignoreErrors"] = "true"
        if purge:
            query["purge"] = "true"
        if simulate:
            query["simulate"] = "true"
        tenantParameters = []
        if loadSample:
            tenantParameters.append("loadSample=true")
        if loadReference:
            tenantParameters.append("loadReference=true")
        if tenantParameters:
            query["tenantParameters"] = ",".join(tenantParameters)
        path = f"/_/proxy/tenants/{tenant}/install"
        data = [{"id": modId, "action": "enable"} for modId in modIds]
        return self._request("POST", path, data=data, query=query)

    def upgrade_modules(self, tenant: str, preRelease: bool = False,
                        simulate: bool = False):
        query = {}
        if preRelease:
            query["preRelease"] = "true"
        if simulate:
            query["simulate"] = "true"
        path = f"/_/proxy/tenants/{tenant}/upgrade"
        return self._request("POST", path, data="", query=query)

    def disable_module(self, modId: str, tenant: str):
        # return self._request("DELETE", f"/_/proxy/tenants/{tenant}/modules/{modId}")
        return self.disable_modules([modId], tenant)

    def disable_modules(self, modIds: str, tenant: str):
        data = [{"id": modId, "action": "disable"} for modId in modIds]
        return self._request("POST", f"/_/proxy/tenants/{tenant}/install", data)

    def is_module_enabled(self, modName: str, tenant: str):
        return modName in [i["id"] for i in self.get_tenant_interfaces(tenant)]

    def call_tenant_service(self, method, service: str, tenant: str, data: dict = None,
                            query: dict = None, headers: dict = None):
        if not service.startswith(("/")):
            service = "/" + service
        headers = headers or {}
        headers["X-Okapi-Tenant"] = tenant
        if tenant in OkapiClient.tenant_access_tokens:
            headers["X-Okapi-Token"] = OkapiClient.tenant_access_tokens[tenant]
        res = self._request(method.upper(), service,
                            data=data, query=query, headers=headers)
        if "x-okapi-token" in self.headers:
            OkapiClient.tenant_access_tokens[tenant] = self.headers["X-Okapi-Token"]
        if self.status_code == 200 or self.status_code == 201:
            return res
        else:
            log.debug("ERROR %i - %s: %s", self.status_code,
                      service, str(res))
            return None

    def _request(self, method: str, path: str, data: dict = None,
                 query: dict = None, headers: dict = None):
        url = self._host + path
        if query:
            url += "?" + urlencode(query)
        headers = headers or {}
        headers["Accept"] = 'application/json, text/plain'
        if "X-Okapi-Token" not in headers:
            if self._access_token is not None:
                headers["X-Okapi-Token"] = self._access_token
        # if data is not None:
        #    pp = pprint.PrettyPrinter(indent=2)
        #    pp.pprint(data)

        if method == "GET":
            request = self._client.prepare_request(
                requests.Request(method, url, headers)
            )
        else:
            headers["content-type"] = "application/json"
            request = self._client.prepare_request(
                requests.Request(
                    method, url, data=json.dumps(data), headers=headers)
            )

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
        elif response.status_code == 204:
            return True
        elif response.status_code == 400:
            try:
                return response.json()
            except json.decoder.JSONDecodeError:
                log.error(response.text)
                return response.text
        elif response.status_code == 403:
            raise OkapiForbidden(
                f"ERROR {response.status_code}: {response.text}")
        elif response.status_code == 404:
            raise OkapiNotFound(
                f"ERROR {response.status_code}: {response.text}")
        elif response.status_code == 422:
            try:
                return response.json()
            except:
                raise OkapiException(
                    f"ERROR {response.status_code}: {response.text}")
        elif response.status_code == 500:
            raise OkapiException(
                f"ERROR {response.status_code}: {response.text}")
        else:
            print(response.text)
            raise OkapiException(
                f"ERROR {response.status_code}: Not implemented")
