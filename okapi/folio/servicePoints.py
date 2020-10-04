# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import logging

from okapi.folio import FolioServices

log = logging.getLogger("okapi.folio.permissions")


class ServicePointServices(FolioServices):

    def get_servicePoints(self):
        return self._okapi.call_tenant_service("GET", "service-points", self._tenant)
