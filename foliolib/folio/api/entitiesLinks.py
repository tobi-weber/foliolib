# -*- coding: utf-8 -*-
# Generated at 2023-04-16

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.entitiesLinks")



class EntitieslinksAdmin(FolioAdminApi):
    """Entities Links API
    Administration

    Entity Links API
    """

    def updateInstanceLinks(self, instanceId, instanceLinkDtoCollection):
        """Update links collection related to Instance

        ``PUT /links/instances/{instanceId}``

        Args:
            instanceId (str): UUID of the Instance that is related to the MARC record (format: uuid)
            instanceLinkDtoCollection (dict): See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestUnprocessableEntity: Validation error for the request.
            OkapiFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_updateInstanceLinks_request.schema
        """
        return self.call("PUT", "/links/instances/{instanceId}", instanceId, instanceLinkDtoCollection)

		
    def getInstanceLinks(self, instanceId):
        """Get links collection related to Instance

        ``GET /links/instances/{instanceId}``

        Args:
            instanceId (str): UUID of the Instance that is related to the MARC record (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_getInstanceLinks_response.schema
        """
        return self.call("GET", "/links/instances/{instanceId}", instanceId)

    def countLinksByAuthorityIds(self, uuidCollection):
        """Retrieve number of links by authority IDs

        ``POST /links/authorities/bulk/count``

        Args:
            uuidCollection (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_countLinksByAuthorityIds_request.schema
            .. literalinclude:: ../files/Entitieslinks_countLinksByAuthorityIds_request.schema_response.schema
        """
        return self.call("POST", "/links/authorities/bulk/count", uuidCollection)

    def getInstanceAuthorityLinkingRules(self):
        """Retrieve instance-authority linking rules

        ``GET /linking-rules/instance-authority``

        Raises:
            OkapiRequestError: Validation errors.
            OkapiFatalError: Internal server error.
        """
        return self.call("GET", "/linking-rules/instance-authority")

    def getAuthorityLinksStats(self, **kwargs):
        """Retrieve authority updates (related to links) statistics

        ``GET /links/stats/authority``

        Keyword Args:
            fromDate (str): Start date to seek from (format: date-time)
            toDate (str): End date to seek from (format: date-time)
            action (str): Action to filter by
            limit (int): Max number of items in collection (minimum: 1, default: 100)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_getAuthorityLinksStats_response.schema
        """
        return self.call("GET", "/links/stats/authority", query=kwargs)

    def getLinkedBibUpdateStats(self, **kwargs):
        """Retrieve linked bib update statistics

        ``GET /links/stats/instance``

        Keyword Args:
            fromDate (str): Start date to seek from (format: date-time)
            toDate (str): End date to seek to (format: date-time)
            status (str): Status to filter by
            limit (int): Max number of items in collection (minimum: 1, default: 100)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_getLinkedBibUpdateStats_response.schema
        """
        return self.call("GET", "/links/stats/instance", query=kwargs)
