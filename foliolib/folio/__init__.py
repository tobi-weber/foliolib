# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import uuid

from foliolib.okapi.okapiClient import OkapiClient


class FolioApi:

    def __init__(self, tenant: str, okapi: OkapiClient = None):
        """
        Args:
            tenant (str): Tenant id
            okapi (OkapiClient, optional): Instance of OkapiClient. Defaults to None.
        """
        self._tenant = tenant
        self._okapi = okapi or OkapiClient()

    def get_tenant(self):
        return self._tenant

    def get_okapiClient(self):
        return self._okapi

    def headers(self):
        return self._okapi.headers

    def call(self, method: str, path: str, data: dict = None,
             query: dict = None, headers: dict = None, files: dict = None):
        return self._okapi.call_tenant_service(self._tenant, method, path, data=data,
                                               query=query, headers=headers, files=files)


class FolioAdminApi:

    def __init__(self, okapi: OkapiClient = None):
        """
        Args:
            okapi (OkapiClient, optional): Instance of OkapiClient. Defaults to None.
        """
        self._okapi = okapi or OkapiClient()

    def get_okapiClient(self):
        return self._okapi

    def headers(self):
        return self._okapi.headers

    def call(self, method: str, path: str, data: dict = None,
             query: dict = None, headers: dict = None, files: dict = None):
        return self._okapi.request()(method, path, data=data,
                                     query=query, headers=headers, files=files)


class FolioService:

    def __init__(self, tenant: str):
        """
        Args:
            tenant (str): Tenant id
        """
        self._tenant = tenant

    def make_uuid(self):
        return str(uuid.uuid4())

    def get_tenant(self):
        return self._tenant
