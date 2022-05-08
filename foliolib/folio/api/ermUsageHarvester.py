# -*- coding: utf-8 -*-
# Generated at 2022-05-05

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.ermUsageHarvester")


class Harvester(FolioApi):
    """mod-erm-usage-harvester API

    This documents the API calls that can be made to mod-erm-usage-harvester
    """

    def get_starts(self):
        """Start harvesting for tenant - process all defined usage data providers

        ``GET /erm-usage-harvester/start``
        """
        return self.call("GET", "/erm-usage-harvester/start")

    def get_start(self, startId: str):
        """Start harvesting for tenant - process a specific usage data provider only

        ``GET /erm-usage-harvester/start/{startId}``

        Args:
            startId (str)
        """
        return self.call("GET", f"/erm-usage-harvester/start/{startId}")

    def get_impls(self, **kwargs):
        """Get available service implementations

        ``GET /erm-usage-harvester/impl``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            aggregator (str):  Filter by 'isAggregator' property (true or false)
        """
        return self.call("GET", "/erm-usage-harvester/impl", query=kwargs)


class Periodic(FolioApi):
    """mod-erm-usage-harvester periodic API

    This documents the API calls that can be made to mod-erm-usage-harvester periodic API
    """

    def get_periodics(self):
        """

        ``GET /erm-usage-harvester/periodic``

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/Periodic_get_periodics_return.schema 
        """
        return self.call("GET", "/erm-usage-harvester/periodic")

    def set_periodic(self, periodic: dict):
        """

        ``POST /erm-usage-harvester/periodic``

        Args:
            periodic (dict): See Schema below

        Schema:

            .. literalinclude:: ../files/Periodic_set_periodic_request.schema
        """
        return self.call("POST", "/erm-usage-harvester/periodic", data=periodic)
