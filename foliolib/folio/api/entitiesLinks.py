# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.entitiesLinks")



class Entitieslinks(FolioApi):
    """Entities Links API

    Entity Links API
    """

    def updateinstancelinks(self, instanceId, instanceLinkDtoCollection):
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

            .. literalinclude:: ../files/Entitieslinks_updateinstancelinks_request.schema
        """
        return self.call("PUT", f"/links/instances/{instanceId}", instanceLinkDtoCollection)

		
    def getinstancelinks(self, instanceId):
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

            .. literalinclude:: ../files/Entitieslinks_getinstancelinks_response.schema
        """
        return self.call("GET", f"/links/instances/{instanceId}")

    def countlinksbyauthorityids(self, uuidCollection):
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

            .. literalinclude:: ../files/Entitieslinks_countlinksbyauthorityids_request.schema
            .. literalinclude:: ../files/Entitieslinks_countlinksbyauthorityids_request.schema_response.schema
        """
        return self.call("POST", f"/links/authorities/bulk/count", uuidCollection)

    def getinstanceauthoritylinkingrules(self):
        """Retrieve instance-authority linking rules

        ``GET /linking-rules/instance-authority``

        Raises:
            OkapiRequestError: Validation errors.
            OkapiFatalError: Internal server error.
        """
        return self.call("GET", "/linking-rules/instance-authority")

    def getinstanceauthoritylinkingrulebyid(self, ruleId):
        """Retrieve instance-authority linking rule by ID

        ``GET /linking-rules/instance-authority/{ruleId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestNotFound: Validation error for the request.
            OkapiFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_getinstanceauthoritylinkingrulebyid_response.schema
        """
        return self.call("GET", f"/linking-rules/instance-authority/{ruleId}")

    def suggestlinksformarcrecord(self, parsedRecordContentCollection):
        """Retrieve links suggestions for marc records

        ``POST /links-suggestions/marc``

        Args:
            parsedRecordContentCollection (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_suggestlinksformarcrecord_request.schema
        """
        return self.call("POST", f"/links-suggestions/marc", parsedRecordContentCollection)

    def getauthoritylinksstats(self, **kwargs):
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

            .. literalinclude:: ../files/Entitieslinks_getauthoritylinksstats_response.schema
        """
        return self.call("GET", "/links/stats/authority", query=kwargs)

    def getlinkedbibupdatestats(self, **kwargs):
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

            .. literalinclude:: ../files/Entitieslinks_getlinkedbibupdatestats_response.schema
        """
        return self.call("GET", "/links/stats/instance", query=kwargs)
