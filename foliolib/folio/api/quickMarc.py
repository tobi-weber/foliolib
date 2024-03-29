# -*- coding: utf-8 -*-
# Generated at 2024-03-23

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.quickMarc")



class Recordseditor(FolioApi):
    """quickMARC Record Editor

    
    """

    def getrecordbyexternalid(self, **kwargs):
        """Get MARC record by externalId

        ``GET /records-editor/records``

        Keyword Args:
            externalId (str): UUID of the external that is related to the MARC record
            lang (str): Requested language. Optional. [lang=en] (pattern: [a-zA-Z]{2}, default: en)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter. Details of the error (e.g. name of the parameter or line/character number with malformed data) provided in the response.
            OkapiRequestNotFound: MARC record with a given ID not found
            OkapiRequestFatalError: Internal server error, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Recordseditor_getrecordbyexternalid_response.schema
        """
        return self.call("GET", "/records-editor/records", query=kwargs)

		
    def createnewrecord(self, quickMarcCreate):
        """

        ``POST /records-editor/records``

        Args:
            quickMarcCreate (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestFatalError: Internal server error, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Recordseditor_createnewrecord_request.schema
            .. literalinclude:: ../files/Recordseditor_createnewrecord_request.schema_response.schema
        """
        return self.call("POST", f"/records-editor/records", quickMarcCreate)

    def getrecordcreationstatus(self, **kwargs):
        """Get status of MARC bibliographic record creation

        ``GET /records-editor/records/status``

        Keyword Args:
            qmRecordId (str): UUID of ParsedRecord to be created

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter. Details of the error (e.g. name of the parameter or line/character number with malformed data) provided in the response.
            OkapiRequestNotFound: MARC record with a given ID not found
            OkapiRequestFatalError: Internal server error, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Recordseditor_getrecordcreationstatus_response.schema
        """
        return self.call("GET", "/records-editor/records/status", query=kwargs)

    def suggestion(self, quickMarcView, **kwargs):
        """

        ``POST /records-editor/links/suggestion``

        Args:
            quickMarcView (dict): See Schema below.

        Keyword Args:
            authoritySearchParameter (str): Authority field to search by (description: Authority search parameter for link suggestions, enum: ['ID', 'NATURAL_ID'], default: NATURAL_ID)
            ignoreAutoLinkingEnabled (bool): Indicates if we need to ignore autoLinkingEnabled flag when filtering the fields for suggestions (default: False)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestFatalError: Internal server error, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Recordseditor_suggestion_request.schema
        """
        return self.call("POST", f"/records-editor/links/suggestion", quickMarcView, query=kwargs)



class Recordseditorasync(FolioApi):
    """quickMARC Record Editor

    
    """

    def putrecord(self, quickMarcEdit, id_):
        """Edit MARC record

        ``PUT /records-editor/records/{id}``

        Args:
            quickMarcEdit (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter. Details of the error (e.g. name of the parameter or line/character number with malformed data) provided in the response.
            OkapiRequestConflict: Update failed due to optimistic locking
            OkapiRequestFatalError: Internal server error, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Recordseditorasync_putrecord_request.schema
        """
        return self.call("PUT", f"/records-editor/records/{id_}", quickMarcEdit)

		
    def deleterecordbyexternalid(self, id_):
        """Delete MARC record by externalId

        ``DELETE /records-editor/records/{id}``

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter. Details of the error (e.g. name of the parameter or line/character number with malformed data) provided in the response.
            OkapiRequestNotFound: MARC record with a given ID not found
            OkapiRequestFatalError: Internal server error, e.g. due to misconfiguration
        """
        return self.call("DELETE", f"/records-editor/records/{id_}")



class Marcspecifications(FolioApi):
    """quickMARC MARC Specifications

    
    """

    def getmarcspecification(self, recordType, fieldTag):
        """Get MARC specification by recordType and fieldTag

        ``GET /marc-specifications/{recordType}/{fieldTag}``

        Args:
            recordType (str): Record type (enum: ['bibliographic', 'holdings', 'authority'], example: bibliographic)
            fieldTag (str): Field's tag (pattern: ^[0-9]{3}$, example: 008)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter. Details of the error (e.g. name of the parameter or line/character number with malformed data) provided in the response.
            OkapiRequestNotFound: MARC specification with a given recordType and fieldTag not found
            OkapiRequestFatalError: Internal server error, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Marcspecifications_getmarcspecification_response.schema
        """
        return self.call("GET", f"/marc-specifications/{recordType}/{fieldTag}")
