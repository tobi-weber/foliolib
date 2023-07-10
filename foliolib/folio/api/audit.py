# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.audit")


class AcquisitionEvents(FolioApi):
    """Acquisition Audit events API

    API for retrieving events for acquisition changes
    """

    def get_order(self, orderId: str, **kwargs):
        """Get list of order events by order_id

        ``GET /audit-data/acquisition/order/{orderId}``

        Args:
            orderId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            sortBy (str): (default=action_date) sorting by field: actionDate
            sortOrder (str): (default=desc) sort order: asc or desc
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AcquisitionEvents_get_order_return.schema 
        """
        return self.call("GET", f"/audit-data/acquisition/order/{orderId}", query=kwargs)

    def get_orderLine(self, orderLineId: str, **kwargs):
        """Get list of order_line events by order_line_id

        ``GET /audit-data/acquisition/order-line/{orderLineId}``

        Args:
            orderLineId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            sortBy (str): (default=action_date) sorting by field: actionDate
            sortOrder (str): (default=desc) sort order: asc or desc
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AcquisitionEvents_get_orderLine_return.schema 
        """
        return self.call("GET", f"/audit-data/acquisition/order-line/{orderLineId}", query=kwargs)


class ModAuditHandlers(FolioApi):
    """Audit event handlers API

    API for event handling
    """

    def set_logRecord(self, logRecord: dict):
        """

        ``POST /audit/handlers/log-record``

        Args:
            logRecord (dict): See Schema below

        Schema:

            .. literalinclude:: ../files/ModAuditHandlers_set_logRecord_request.schema
        """
        return self.call("POST", "/audit/handlers/log-record", data=logRecord)


class CirculationLogs(FolioApi):
    """mod-audit API

    This documents the API calls that can be made to query circulation audit logs records
    """

    def get_logs(self, **kwargs):
        """Retrieve a list of log items.

        ``GET /audit-data/circulation/logs``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields, for example userBarcode
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - userBarcode=1000024158
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

            .. literalinclude:: ../files/CirculationLogs_get_logs_return.schema 
        """
        return self.call("GET", "/audit-data/circulation/logs", query=kwargs)


class AuditData(FolioApi):
    """mod-audit API

    This documents the API calls that can be made to query and manage audit records
    """

    def get_auditData(self, **kwargs):
        """Retrieve a list of auditDatum items.

        ``GET /audit-data``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example link = 1234
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - link=/users/1234
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
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AuditData_get_auditData_return.schema 
        """
        return self.call("GET", "/audit-data", query=kwargs)

    def set_auditDatum(self, auditDatum: dict):
        """Create a new auditDatum item.

        ``POST /audit-data``

        Args:
            auditDatum (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created auditDatum item

        Schema:

            .. literalinclude:: ../files/AuditData_set_auditDatum_request.schema
        """
        return self.call("POST", "/audit-data", data=auditDatum)

    def get_auditDatum(self, auditDataId: str):
        """Retrieve auditDatum item with given {auditDatumId}

        ``GET /audit-data/{auditDataId}``

        Args:
            auditDataId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required

        Schema:

            .. literalinclude:: ../files/AuditData_get_auditDatum_return.schema 
        """
        return self.call("GET", f"/audit-data/{auditDataId}")

    def delete_auditDatum(self, auditDataId: str):
        """Delete auditDatum item with given {auditDatumId}

        ``DELETE /audit-data/{auditDataId}``

        Args:
            auditDataId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnauthorized: Authentication is required
        """
        return self.call("DELETE", f"/audit-data/{auditDataId}")

    def modify_auditDatum(self, auditDataId: str, auditDatum: dict):
        """Update auditDatum item with given {auditDatumId}

        ``PUT /audit-data/{auditDataId}``

        Args:
            auditDataId (str)
            auditDatum (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AuditData_modify_auditDatum_request.schema
        """
        return self.call("PUT", f"/audit-data/{auditDataId}", data=auditDatum)
