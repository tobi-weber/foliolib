# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.ermUsageHarvester")


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


class Harvester(FolioApi):
    """mod-erm-usage-harvester API

    This documents the API calls that can be made to mod-erm-usage-harvester
    """

    def get_starts(self):
        """Start harvesting for tenant - process all defined usage data providers

        ``GET /erm-usage-harvester/start``

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("GET", "/erm-usage-harvester/start")

    def get_start(self, startId: str):
        """Start harvesting for tenant - process a specific usage data provider only

        ``GET /erm-usage-harvester/start/{startId}``

        Args:
            startId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("GET", f"/erm-usage-harvester/start/{startId}")

    def get_impls(self, **kwargs):
        """Get available service implementations

        ``GET /erm-usage-harvester/impl``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            aggregator (str):  Filter by 'isAggregator' property (true or false)

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("GET", "/erm-usage-harvester/impl", query=kwargs)

    def get_jobs(self, **kwargs):
        """Get harvesting jobs

        ``GET /erm-usage-harvester/jobs``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            timestamp (long):  Only return jobs created at or before this timestamp
                    
                    Example:
                    
                     - 1641020400000
            providerId (str):  Only return jobs with this providerId
                    
                    Example:
                    
                     - 6697f576-78d4-4712-ae18-2612ccdcd66d
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    CQL string
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - type==provider
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Harvester_get_jobs_return.schema 
        """
        return self.call("GET", "/erm-usage-harvester/jobs", query=kwargs)

    def set_purgefinished(self, **kwargs):
        """Purge finished harvesting jobs

        ``POST /erm-usage-harvester/jobs/purgefinished``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            timestamp (long):  Only purge jobs having a timestamp less than or equal to this value
                    
                    Example:
                    
                     - 1641020400000

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("POST", "/erm-usage-harvester/jobs/purgefinished", query=kwargs)

    def set_purgestale(self):
        """Purge stale jobs

        ``POST /erm-usage-harvester/jobs/purgestale``

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("POST", "/erm-usage-harvester/jobs/purgestale")

    def set_cleanup(self):
        """Perform cleanup tasks on harvesting jobs

        ``POST /erm-usage-harvester/jobs/cleanup``

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("POST", "/erm-usage-harvester/jobs/cleanup")
