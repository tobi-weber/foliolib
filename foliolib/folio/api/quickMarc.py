# -*- coding: utf-8 -*-
# Generated at 2023-04-16

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.quickMarc")



class RecordseditorAdmin(FolioAdminApi):
    """quickMARC Record Editor
    Administration

    
    """

    def getRecordByExternalId(self, **kwargs):
        """Get MARC record by externalId

        ``GET /records-editor/records``

        Keyword Args:
            externalId (str): UUID of the external that is related to the MARC record (format: uuid)
            lang (str): Requested language. Optional. [lang=en] (pattern: [a-zA-Z]{2}, default: en)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter. Details of the error (e.g. name of the parameter or line/character number with malformed data) provided in the response.
            OkapiRequestNotFound: MARC record with a given ID not found
            OkapiFatalError: Internal server error, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Recordseditor_getRecordByExternalId_response.schema
        """
        return self.call("GET", "/records-editor/records", query=kwargs)

		
    def records(self, quickMarc):
        """

        ``POST /records-editor/records``

        Args:
            quickMarc (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Internal server error, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Recordseditor_records_request.schema
            .. literalinclude:: ../files/Recordseditor_records_request.schema_response.schema
        """
        return self.call("POST", "/records-editor/records", quickMarc)

    def getRecordCreationStatus(self, **kwargs):
        """Get status of MARC bibliographic record creation

        ``GET /records-editor/records/status``

        Keyword Args:
            qmRecordId (str): UUID of ParsedRecord to be created (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter. Details of the error (e.g. name of the parameter or line/character number with malformed data) provided in the response.
            OkapiRequestNotFound: MARC record with a given ID not found
            OkapiFatalError: Internal server error, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Recordseditor_getRecordCreationStatus_response.schema
        """
        return self.call("GET", "/records-editor/records/status", query=kwargs)



class RecordseditorasyncAdmin(FolioAdminApi):
    """quickMARC Record Editor
    Administration

    
    """

    def putRecord(self, id_, quickMarc):
        """Edit MARC record

        ``PUT /records-editor/records/{id}``

        Args:
            id_ (str): The UUID of a record (format: uuid)
            quickMarc (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter. Details of the error (e.g. name of the parameter or line/character number with malformed data) provided in the response.
            OkapiRequestConflict: Update failed due to optimistic locking
            OkapiFatalError: Internal server error, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Recordseditorasync_putRecord_request.schema
        """
        return self.call("PUT", "/records-editor/records/{id}", id_, quickMarc)

		
    def deleteRecordByExternalId(self, id_):
        """Delete MARC record by externalId

        ``DELETE /records-editor/records/{id}``

        Args:
            id_ (str): UUID of the external that is related to the MARC record (format: uuid)

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter. Details of the error (e.g. name of the parameter or line/character number with malformed data) provided in the response.
            OkapiRequestNotFound: MARC record with a given ID not found
            OkapiFatalError: Internal server error, e.g. due to misconfiguration
        """
        return self.call("DELETE", "/records-editor/records/{id}", id_)
