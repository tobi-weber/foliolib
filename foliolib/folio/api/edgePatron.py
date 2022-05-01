# -*- coding: utf-8 -*-
# Generated at 2022-04-08

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.edgePatron")


class EdgePatron(FolioApi):
    """Patron Services

    This module allows 3rd party discovery services to perform patron
		actions in FOLIO
    """

    def get_account(self, accountId: str, **kwargs):
        """Return account details for the specified FOLIO user id

        ``GET /patron/account/{accountId}``

        Args:
            accountId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            includeLoans (bool): (default=False) Indicates whether or not to include the loans array in
                    the response
                    
            includeCharges (bool): (default=False) Indicates whether or not to include the charges array in
                    the response
                    
            includeHolds (bool): (default=False) Indicates whether or not to include the holds array in
                    the response
                    
            apikey (str):  API Key
            sortBy (str):  Part of CQL query, indicates the order of records within the lists of holds, charges, loans
                    
                    
                    Example:
                    
                     - item.title/sort.ascending
            offset (int):  Skip over a number of elements by specifying an offset value for the query
                    
                    
                    Example:
                    
                     - 1
            limit (int):  Limit the number of elements returned in the response
                    
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiRequestForbidden: Forbidden
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/EdgePatron_get_account_return.schema 
        """
        return self.call("GET", f"/patron/account/{accountId}", query=kwargs)

    def set_renew(self, accountId: str, itemId: str, **kwargs):
        """Renews a loan on the item for the user

        ``POST /patron/account/{accountId}/item/{itemId}/renew``

        Args:
            accountId (str)
            itemId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            apikey (str):  API Key

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiRequestForbidden: Forbidden
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/EdgePatron_set_renew_return.schema 
        """
        return self.call("POST", f"/patron/account/{accountId}/item/{itemId}/renew", query=kwargs)

    def set_hold_for_account(self, accountId: str, itemId: str, hold: dict, **kwargs):
        """Creates a hold request on an existing item for the user

        ``POST /patron/account/{accountId}/item/{itemId}/hold``

        Args:
            accountId (str)
            itemId (str)
            hold (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            apikey (str):  API Key

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiRequestForbidden: Forbidden
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/EdgePatron_set_hold_for_account_request.schema
        """
        return self.call("POST", f"/patron/account/{accountId}/item/{itemId}/hold", data=hold, query=kwargs)

    def set_hold(self, accountId: str, instanceId: str, hold: dict, **kwargs):
        """Creates a hold request on an existing item by instance ID for the user

        ``POST /patron/account/{accountId}/instance/{instanceId}/hold``

        Args:
            accountId (str)
            instanceId (str)
            hold (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            apikey (str):  API Key

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiRequestForbidden: Forbidden
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/EdgePatron_set_hold_request.schema
        """
        return self.call("POST", f"/patron/account/{accountId}/instance/{instanceId}/hold", data=hold, query=kwargs)

    def set_cancel(self, accountId: str, holdId: str, cancel: dict, **kwargs):
        """Removes the specified hold request

        ``POST /patron/account/{accountId}/hold/{holdId}/cancel``

        Args:
            accountId (str)
            holdId (str)
            cancel (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            apikey (str):  API Key

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiRequestForbidden: Forbidden
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/EdgePatron_set_cancel_request.schema
            .. literalinclude:: ../files/EdgePatron_set_cancel_return.schema 
        """
        return self.call("POST", f"/patron/account/{accountId}/hold/{holdId}/cancel", data=cancel, query=kwargs)
