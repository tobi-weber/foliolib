# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import uuid

from pyokapi.folio.exceptions import FolioTenantMissing
from pyokapi.okapi.okapiClient import OkapiClient


class FolioServices:
    tenant = None

    def __init__(self, tenant, okapi: OkapiClient = None):
        self._tenant = tenant or FolioServices.tenant
        if tenant is None:
            raise FolioTenantMissing("Tenant id must be given.")
        else:
            FolioServices.tenant = tenant
        self._okapi = okapi or OkapiClient()

    def get_tenant(self):
        return self._tenant

    def get_okapiClient(self):
        return self._okapi

    def generate_uuid(self):
        return str(uuid.uuid4())

    def headers(self):
        return self._okapi.headers

    def call(self, method, service, data: dict = None,
             query: dict = None, headers: dict = None, files: dict = None):
        return self._okapi.call_tenant_service(method, service, self._tenant, data=data,
                                               query=query, headers=headers, files=files)
