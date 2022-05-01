# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os

from foliolib.folio import FolioService
from foliolib.folio.api.inventory import Inventory
from foliolib.folio.api.inventoryStorage import AlternativeTitleType

log = logging.getLogger("foliolib.folio.inventory")


class Inventory(FolioService):

    def __init__(self, tenant: str) -> None:
        """
        Args:
            tenant (str): Tenant id
        """
        super().__init__(tenant)
        self._inventory = Inventory(tenant)

    def upload_modsFiles(self, filePathes: list):
        statusIds = []
        for path in filePathes:
            self._inventory.upload_mods(path)
            statusIds.append(self._inventory.headers()[
                             "Location"].split("/")[-1])
        return statusIds

    def get_uploadStatus(self, statusId):
        return self._inventory.get_status(statusId)
