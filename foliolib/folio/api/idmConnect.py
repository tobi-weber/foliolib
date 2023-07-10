# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.idmConnect")


class IdmConnect(FolioApi):
    """

    
    """

    def get_contracts(self, **kwargs):
        """Retrieve a list of contract items.

        ``GET /idm-connect/contract``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
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

        Schema:

            .. literalinclude:: ../files/IdmConnect_get_contracts_return.schema 
        """
        return self.call("GET", "/idm-connect/contract", query=kwargs)

    def set_contract(self, contract: dict):
        """Create a new contract item.

        ``POST /idm-connect/contract``

        Args:
            contract (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created contract item

        Schema:

            .. literalinclude:: ../files/IdmConnect_set_contract_request.schema
        """
        return self.call("POST", "/idm-connect/contract", data=contract)

    def get_contract(self, contractId: str):
        """Retrieve contract item with given {contractId}

        ``GET /idm-connect/contract/{contractId}``

        Args:
            contractId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/IdmConnect_get_contract_return.schema 
        """
        return self.call("GET", f"/idm-connect/contract/{contractId}")

    def delete_contract(self, contractId: str):
        """Delete contract item with given {contractId}

        ``DELETE /idm-connect/contract/{contractId}``

        Args:
            contractId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/idm-connect/contract/{contractId}")

    def modify_contract(self, contractId: str, contract: dict):
        """Update contract item with given {contractId}

        ``PUT /idm-connect/contract/{contractId}``

        Args:
            contractId (str)
            contract (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/IdmConnect_modify_contract_request.schema
        """
        return self.call("PUT", f"/idm-connect/contract/{contractId}", data=contract)

    def get_transmit_by_contract(self, contractId: str):
        """Transmit the walk-in contract with id to external IDM system and update its status

        ``GET /idm-connect/contract/{contractId}/transmit``

        Args:
            contractId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
        """
        return self.call("GET", f"/idm-connect/contract/{contractId}/transmit")

    def set_bulkDelete(self, bulkDelete: dict):
        """Delete multiple walk-in contracts

        ``POST /idm-connect/contract/bulk-delete``

        Args:
            bulkDelete (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/IdmConnect_set_bulkDelete_request.schema
            .. literalinclude:: ../files/IdmConnect_set_bulkDelete_return.schema 
        """
        return self.call("POST", "/idm-connect/contract/bulk-delete", data=bulkDelete)

    def get_searchidms(self, **kwargs):
        """Get existing users

        ``GET /idm-connect/searchidm``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            firstname ():  Users first name
                    
                    Example:
                    
                     - John
            lastname ():  Users last name
                    
                    Example:
                    
                     - Doe
            dateOfBirth ():  Users date of birth
                    
                    Example:
                    
                     - 2015-12-24

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
        """
        return self.call("GET", "/idm-connect/searchidm", query=kwargs)

    def set_ubreadernumber(self, **kwargs):
        """Set a UBReaderNumber

        ``POST /idm-connect/ubreadernumber``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            unilogin ():  unilogin
                    
                    Example:
                    
                     - 123abc78
            UBReaderNumber ():  UBReaderNumber
                    
                    Example:
                    
                     - 1234567890

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
        """
        return self.call("POST", "/idm-connect/ubreadernumber", query=kwargs)

    def delete_ubreadernumbers(self, **kwargs):
        """Delete a UBReaderNumber

        ``DELETE /idm-connect/ubreadernumber``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            unilogin ():  unilogin
                    
                    Example:
                    
                     - 123abc78

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", "/idm-connect/ubreadernumber", query=kwargs)
