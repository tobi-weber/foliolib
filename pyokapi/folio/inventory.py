# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import logging
import os

from pyokapi.folio import FolioServices
from pyokapi.folio.users import UserServices

log = logging.getLogger("okapi.folio.inventory")


class InventoryServices(FolioServices):

    def get_servicePoints(self):
        return self.call("GET", "service-points")

    def set_service_points(self, username: str, servicePointsIds: str, defaultServicePointId: str):
        user = UserServices(self._tenant).get_user(username)
        log.debug(user)
        log.debug(servicePointsIds)
        sp_user = {
            "userId": user["id"],
            "servicePointsIds": servicePointsIds,
            "defaultServicePointId": defaultServicePointId
        }
        return self.call("POST", "service-points-users", data=sp_user)
