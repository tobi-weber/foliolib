# -*- coding: utf-8 -*-
# Generated at 2024-03-01

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
            OkapiRequestFatalError: Internal server error.

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
            OkapiRequestFatalError: Internal server error.

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
            OkapiRequestFatalError: Internal server error.

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
            OkapiRequestFatalError: Internal server error.
        """
        return self.call("GET", "/linking-rules/instance-authority")

    def getinstanceauthoritylinkingrulebyid(self, ruleId):
        """Retrieve instance-authority linking rule by ID

        ``GET /linking-rules/instance-authority/{ruleId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestNotFound: Record was not found.
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_getinstanceauthoritylinkingrulebyid_response.schema
        """
        return self.call("GET", f"/linking-rules/instance-authority/{ruleId}")

    def suggestlinksformarcrecord(self, parsedRecordContentCollection, **kwargs):
        """Retrieve links suggestions for marc records

        ``POST /links-suggestions/marc``

        Args:
            parsedRecordContentCollection (dict): See Schema below.

        Keyword Args:
            authoritySearchParameter (str): Authority field to search by (description: Authority search parameter for link suggestions, enum: ['ID', 'NATURAL_ID'], default: NATURAL_ID)
            ignoreAutoLinkingEnabled (bool): Indicates if we need to ignore autoLinkingEnabled flag when filtering the fields for suggestions (default: False)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_suggestlinksformarcrecord_request.schema
        """
        return self.call("POST", f"/links-suggestions/marc", parsedRecordContentCollection, query=kwargs)

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
            OkapiRequestFatalError: Internal server error.

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
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_getlinkedbibupdatestats_response.schema
        """
        return self.call("GET", "/links/stats/instance", query=kwargs)

    def retrieveauthorities(self, **kwargs):
        """

        ``GET /authority-storage/authorities``

        Keyword Args:
            deleted (bool): Indicates if only deleted authority records should be retrieved (default: False)
            idOnly (bool): Indicates if only IDs of authority records should be retrieved (default: False)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, maximum: 2147483647, default: 0)
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 2000, default: 100)
            query (str): A query expressed as a CQL string (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql)) using valid searchable fields. Authorities can be queried using the following fields: headingType, authoritySourceFile.id, authoritySourceFile.name, createdDate, updatedDate. Example: headingType=personalName & authoritySourceFile.name=LC Genre/Form Terms & createdDate>2021-10-25T12:00:00.0 (default: cql.allRecords=1)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_retrieveauthorities_response.schema
        """
        return self.call("GET", "/authority-storage/authorities", query=kwargs)

		
    def createauthority(self, authorityDto):
        """

        ``POST /authority-storage/authorities``

        Args:
            authorityDto (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestUnprocessableEntity: Validation error for the request.
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_createauthority_request.schema
        """
        return self.call("POST", f"/authority-storage/authorities", authorityDto)

    def createauthoritybulk(self, authorityBulkRequest):
        """

        ``POST /authority-storage/authorities/bulk``

        Args:
            authorityBulkRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestUnprocessableEntity: Validation error for the request.
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_createauthoritybulk_request.schema
            .. literalinclude:: ../files/Entitieslinks_createauthoritybulk_request.schema_response.schema
        """
        return self.call("POST", f"/authority-storage/authorities/bulk", authorityBulkRequest)

    def getauthority(self, id_):
        """

        ``GET /authority-storage/authorities/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestNotFound: Record was not found.
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_getauthority_response.schema
        """
        return self.call("GET", f"/authority-storage/authorities/{id_}")

		
    def updateauthority(self, authorityDto, id_):
        """

        ``PUT /authority-storage/authorities/{id}``

        Args:
            authorityDto (dict): See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestNotFound: Record was not found.
            OkapiRequestUnprocessableEntity: Validation error for the request.
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_updateauthority_request.schema
        """
        return self.call("PUT", f"/authority-storage/authorities/{id_}", authorityDto)

		
    def deleteauthority(self, id_):
        """

        ``DELETE /authority-storage/authorities/{id}``

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestNotFound: Record was not found.
            OkapiRequestFatalError: Internal server error.
        """
        return self.call("DELETE", f"/authority-storage/authorities/{id_}")

    def getreindexjobs(self, **kwargs):
        """

        ``GET /authority-storage/reindex``

        Keyword Args:
            query (str): A query expressed as a CQL string (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql)) using valid searchable fields. The first example below shows the general form of a full CQL query, but those fields might not be relevant in this context. (default: cql.allRecords=1)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, maximum: 2147483647, default: 0)
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 2000, default: 100)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_getreindexjobs_response.schema
        """
        return self.call("GET", "/authority-storage/reindex", query=kwargs)

		
    def submitreindexjob(self):
        """

        ``POST /authority-storage/reindex``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_submitreindexjob_response.schema
        """
        return self.call("POST", "/authority-storage/reindex")

    def getreindexjob(self, id_):
        """

        ``GET /authority-storage/reindex/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestNotFound: Record was not found.
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_getreindexjob_response.schema
        """
        return self.call("GET", f"/authority-storage/reindex/{id_}")

		
    def deletereindexjob(self, id_):
        """

        ``DELETE /authority-storage/reindex/{id}``

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestNotFound: Record was not found.
            OkapiRequestFatalError: Internal server error.
        """
        return self.call("DELETE", f"/authority-storage/reindex/{id_}")

    def retrieveauthoritynotetypes(self, **kwargs):
        """

        ``GET /authority-note-types``

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, maximum: 2147483647, default: 0)
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 2000, default: 100)
            query (str): A query expressed as a CQL string (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql)) using valid searchable fields. The first example below shows the general form of a full CQL query, but those fields might not be relevant in this context. (default: cql.allRecords=1)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_retrieveauthoritynotetypes_response.schema
        """
        return self.call("GET", "/authority-note-types", query=kwargs)

		
    def createauthoritynotetype(self, authorityNoteTypeDto):
        """

        ``POST /authority-note-types``

        Args:
            authorityNoteTypeDto (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestUnprocessableEntity: Validation error for the request.
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_createauthoritynotetype_request.schema
        """
        return self.call("POST", f"/authority-note-types", authorityNoteTypeDto)

    def getauthoritynotetype(self, id_):
        """

        ``GET /authority-note-types/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestNotFound: Record was not found.
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_getauthoritynotetype_response.schema
        """
        return self.call("GET", f"/authority-note-types/{id_}")

		
    def updateauthoritynotetype(self, authorityNoteTypeDto, id_):
        """

        ``PUT /authority-note-types/{id}``

        Args:
            authorityNoteTypeDto (dict): See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestNotFound: Record was not found.
            OkapiRequestUnprocessableEntity: Validation error for the request.
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_updateauthoritynotetype_request.schema
        """
        return self.call("PUT", f"/authority-note-types/{id_}", authorityNoteTypeDto)

		
    def deleteauthoritynotetype(self, id_):
        """

        ``DELETE /authority-note-types/{id}``

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestNotFound: Record was not found.
            OkapiRequestFatalError: Internal server error.
        """
        return self.call("DELETE", f"/authority-note-types/{id_}")

    def retrieveauthoritysourcefiles(self, **kwargs):
        """

        ``GET /authority-source-files``

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, maximum: 2147483647, default: 0)
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 2000, default: 100)
            query (str): A query expressed as a CQL string (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql)) using valid searchable fields. The first example below shows the general form of a full CQL query, but those fields might not be relevant in this context. (default: cql.allRecords=1)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_retrieveauthoritysourcefiles_response.schema
        """
        return self.call("GET", "/authority-source-files", query=kwargs)

		
    def createauthoritysourcefile(self, authoritySourceFilePostDto):
        """

        ``POST /authority-source-files``

        Args:
            authoritySourceFilePostDto (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestUnprocessableEntity: Validation error for the request.
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_createauthoritysourcefile_request.schema
            .. literalinclude:: ../files/Entitieslinks_createauthoritysourcefile_request.schema_response.schema
        """
        return self.call("POST", f"/authority-source-files", authoritySourceFilePostDto)

    def getauthoritysourcefile(self, id_):
        """

        ``GET /authority-source-files/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestNotFound: Record was not found.
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_getauthoritysourcefile_response.schema
        """
        return self.call("GET", f"/authority-source-files/{id_}")

		
    def deleteauthoritysourcefile(self, id_):
        """

        ``DELETE /authority-source-files/{id}``

        Raises:
            OkapiRequestError: Validation errors.
            OkapiRequestNotFound: Record was not found.
            OkapiRequestFatalError: Internal server error.
        """
        return self.call("DELETE", f"/authority-source-files/{id_}")

    def newauthoritysourcefilenexthrid(self, id_):
        """

        ``POST /authority-source-files/{id}/hrid``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Record was not found.
            OkapiRequestUnprocessableEntity: Validation error for the request.
            OkapiRequestFatalError: Internal server error.

        Schema:

            .. literalinclude:: ../files/Entitieslinks_newauthoritysourcefilenexthrid_response.schema
        """
        return self.call("POST", f"/authority-source-files/{id_}/hrid")
