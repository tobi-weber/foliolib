# -*- coding: utf-8 -*-
# Copyright (C) 2023 Tobias Weber <tobi-weber@gmx.de>

import uuid

from foliolib.okapi.okapiClient import OkapiClient


class FolioApi:

    def __init__(self, tenant: str):
        """Base class of the Folio API

        Args:
            tenant (str): Tenant id
        """
        self._tenant = tenant
        self._okapi = OkapiClient()

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

    def __init__(self):
        """Base class of not tenant related Folio API.
        """
        self._okapi = OkapiClient()

    def get_okapiClient(self):
        return self._okapi

    def headers(self):
        return self._okapi.headers

    def call(self, method: str, path: str, data: dict = None,
             query: dict = None, headers: dict = None, files: dict = None):
        return self._okapi.request()(method, path, data=data,
                                     query=query, headers=headers, files=files)


class FolioAPIImpl:
    """Base class for concrete implementations of the Folio API.
    """

    def __init__(self, tenant: str):
        """
        Args:
            tenant (str): Tenant id
        """
        self._tenant = tenant

    def get_tenant(self):
        return self._tenant
