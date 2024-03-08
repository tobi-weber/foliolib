# -*- coding: utf-8 -*-
# Generated at 2024-03-23

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.dcb")



class DcbTransaction(FolioApi):
    """mod DCB FOLIO API

    mod DCB FOLIO API
    """

    def createcirculationrequest(self, dcbTransactionId, dcbTransaction):
        """Create circulation request

        ``POST /transactions/{dcbTransactionId}``

        Args:
            dcbTransactionId (str): 
            dcbTransaction (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestConflict: Validation errors
            OkapiRequestFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/DcbTransaction_createcirculationrequest_request.schema
            .. literalinclude:: ../files/DcbTransaction_createcirculationrequest_request.schema_response.schema
        """
        return self.call("POST", f"/transactions/{dcbTransactionId}", dcbTransaction)

    def gettransactionstatusbyid(self, dcbTransactionId):
        """Get transaction status across circulation institutions

        ``GET /transactions/{dcbTransactionId}/status``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Resource not found
            OkapiRequestError: Bad request
            OkapiRequestFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/DcbTransaction_gettransactionstatusbyid_response.schema
        """
        return self.call("GET", f"/transactions/{dcbTransactionId}/status")

		
    def updatetransactionstatus(self, transactionStatus, dcbTransactionId):
        """Update transaction status across circulation institutions

        ``PUT /transactions/{dcbTransactionId}/status``

        Args:
            transactionStatus (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Resource not found
            OkapiRequestFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/DcbTransaction_updatetransactionstatus_request.schema
            .. literalinclude:: ../files/DcbTransaction_updatetransactionstatus_request.schema_response.schema
        """
        return self.call("PUT", f"/transactions/{dcbTransactionId}/status", transactionStatus)
