# -*- coding: utf-8 -*-
# Generated at 2020-11-29

import logging

from foliolib.folio import FolioApi

log = logging.getLogger("foliolib.folio.api.quickMarc")


class RecordsEditor(FolioApi):
    """quickMARC record API

    This documents the API calls that can be made to work with MARC records
    """

    def get_records(self, **kwargs):
        """Get MARC record by instanceId

        ``GET /records-editor/records``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            instanceId (uuid):  UUID of the instance that is related to the MARC record
                    
                    Example:
                    
                     - f6c574b5-b1d5-4e5e-a28b-161b7e03e81a
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/RecordsEditor_get_records_return.schema 
        """
        return self.call("GET", "/records-editor/records", query=kwargs)

    def modify_record(self, recordsId: str, record: dict):
        """Edit MARC record

        ``PUT /records-editor/records/{recordsId}``

        Args:
            recordsId (str)
            record (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/RecordsEditor_modify_record_request.schema
        """
        return self.call("PUT", f"/records-editor/records/{recordsId}", data=record)
