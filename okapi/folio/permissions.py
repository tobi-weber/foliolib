# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import logging

from okapi.folio import FolioServices

log = logging.getLogger("okapi.folio.permissions")


class PermissionServices(FolioServices):

    def get_permissions(self, query: dict = None):
        return self._okapi.call_tenant_service("GET", "perms/permissions", self._tenant, query=query)
