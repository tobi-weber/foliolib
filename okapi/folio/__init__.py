# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>


from okapi.okapiClient import OkapiClient


class FolioServices:

    def __init__(self, tenant, okapi: OkapiClient = None):
        self._tenant = tenant
        self._okapi = okapi or OkapiClient()

    def get_tenant(self):
        return self._tenant

    def get_okapiClient(self):
        return self._okapi
