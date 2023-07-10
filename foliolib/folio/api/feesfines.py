# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.feesfines")


class TransferCriteria(FolioApi):
    """Transfers criteria API

    This documents the API calls that can be made to query and manage fee/fine of the system
    """

    def get_transferCriterias(self, **kwargs):
        """Return a list of transfer criteria

        ``GET /transfer-criterias``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - active=true
            orderBy (str):  Order by field: field A, field B
                    
            order (str (desc|asc):): (default=desc) Order
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

            .. literalinclude:: ../files/TransferCriteria_get_transferCriterias_return.schema 
        """
        return self.call("GET", "/transfer-criterias", query=kwargs)

    def set_transferCriteria(self, transferCriteria: dict):
        """Create a transfer criteria

        ``POST /transfer-criterias``

        Args:
            transferCriteria (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created transferCriteria item

        Schema:

            .. literalinclude:: ../files/TransferCriteria_set_transferCriteria_request.schema
        """
        return self.call("POST", "/transfer-criterias", data=transferCriteria)

    def get_transferCriteria(self, transferCriteriaId: str):
        """Get a single transfer criteria

        ``GET /transfer-criterias/{transferCriteriaId}``

        Args:
            transferCriteriaId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/TransferCriteria_get_transferCriteria_return.schema 
        """
        return self.call("GET", f"/transfer-criterias/{transferCriteriaId}")

    def delete_transferCriteria(self, transferCriteriaId: str):
        """Delete transferCriteria item with given {transferCriteriaId}

        ``DELETE /transfer-criterias/{transferCriteriaId}``

        Args:
            transferCriteriaId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/transfer-criterias/{transferCriteriaId}")

    def modify_transferCriteria(self, transferCriteriaId: str, transferCriteria: dict):
        """Update transferCriteria item with given {transferCriteriaId}

        ``PUT /transfer-criterias/{transferCriteriaId}``

        Args:
            transferCriteriaId (str)
            transferCriteria (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/TransferCriteria_modify_transferCriteria_request.schema
        """
        return self.call("PUT", f"/transfer-criterias/{transferCriteriaId}", data=transferCriteria)


class Owners(FolioApi):
    """Owners API

    This documents the API calls that can be made to query and manage owner of the system
    """

    def get_owners(self, **kwargs):
        """Return a list of owners

        ``GET /owners``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - active=true
            orderBy (str):  Order by field: field A, field B
                    
            order (str (desc|asc):): (default=desc) Order
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

            .. literalinclude:: ../files/Owners_get_owners_return.schema 
        """
        return self.call("GET", "/owners", query=kwargs)

    def set_owner(self, owner: dict):
        """Create a owner

        ``POST /owners``

        Args:
            owner (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created owner item

        Schema:

            .. literalinclude:: ../files/Owners_set_owner_request.schema
        """
        return self.call("POST", "/owners", data=owner)

    def get_owner(self, ownerId: str):
        """Get a single owner

        ``GET /owners/{ownerId}``

        Args:
            ownerId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Owners_get_owner_return.schema 
        """
        return self.call("GET", f"/owners/{ownerId}")

    def delete_owner(self, ownerId: str):
        """Delete owner item with given {ownerId}

        ``DELETE /owners/{ownerId}``

        Args:
            ownerId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/owners/{ownerId}")

    def modify_owner(self, ownerId: str, owner: dict):
        """Update owner item with given {ownerId}

        ``PUT /owners/{ownerId}``

        Args:
            ownerId (str)
            owner (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Owners_modify_owner_request.schema
        """
        return self.call("PUT", f"/owners/{ownerId}", data=owner)


class Comments(FolioApi):
    """Comments API

    This documents the API calls that can be made to query and manage feefine of the system
    """

    def get_comments(self, **kwargs):
        """Return a list of comments

        ``GET /comments``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - active=true
            orderBy (str):  Order by field: field A, field B
                    
            order (str (desc|asc):): (default=desc) Order
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            facets (list):  facets to return in the collection result set, can be suffixed by a count of facet values to return, for example, patronGroup:10 default to top 5 facet values

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Comments_get_comments_return.schema 
        """
        return self.call("GET", "/comments", query=kwargs)

    def set_comment(self, comment: dict):
        """Create a comment

        ``POST /comments``

        Args:
            comment (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created comment item

        Schema:

            .. literalinclude:: ../files/Comments_set_comment_request.schema
        """
        return self.call("POST", "/comments", data=comment)

    def get_comment(self, commentId: str):
        """Get a single comment

        ``GET /comments/{commentId}``

        Args:
            commentId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Comments_get_comment_return.schema 
        """
        return self.call("GET", f"/comments/{commentId}")

    def delete_comment(self, commentId: str):
        """Delete comment item with given {commentId}

        ``DELETE /comments/{commentId}``

        Args:
            commentId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/comments/{commentId}")

    def modify_comment(self, commentId: str, comment: dict):
        """Update comment item with given {commentId}

        ``PUT /comments/{commentId}``

        Args:
            commentId (str)
            comment (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Comments_modify_comment_request.schema
        """
        return self.call("PUT", f"/comments/{commentId}", data=comment)


class OverdueFinePolicy(FolioApi):
    """Overdue Fine Policies API

    **Overdue Fine Policies**
    """

    def get_overdueFinesPolicies(self, **kwargs):
        """Get Overdue Fine Policy list

        ``GET /overdue-fines-policies``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    searchable using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name="undergrad*"
            orderBy (str):  Order by field: field A, field B
                    
            order (str (desc|asc):): (default=desc) Order
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

            .. literalinclude:: ../files/OverdueFinePolicy_get_overdueFinesPolicies_return.schema 
        """
        return self.call("GET", "/overdue-fines-policies", query=kwargs)

    def set_overdueFinesPolicy(self, overdueFinesPolicy: dict):
        """Create new Overdue Fine Policy

        ``POST /overdue-fines-policies``

        Args:
            overdueFinesPolicy (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created overdueFinesPolicy item

        Schema:

            .. literalinclude:: ../files/OverdueFinePolicy_set_overdueFinesPolicy_request.schema
        """
        return self.call("POST", "/overdue-fines-policies", data=overdueFinesPolicy)

    def get_overdueFinesPolicy(self, overdueFinePolicyId: str):
        """Get Overdue Fine Policy by id

        ``GET /overdue-fines-policies/{overdueFinePolicyId}``

        Args:
            overdueFinePolicyId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/OverdueFinePolicy_get_overdueFinesPolicy_return.schema 
        """
        return self.call("GET", f"/overdue-fines-policies/{overdueFinePolicyId}")

    def delete_overdueFinesPolicy(self, overdueFinePolicyId: str):
        """Delete Overdue Fine Policy by id

        ``DELETE /overdue-fines-policies/{overdueFinePolicyId}``

        Args:
            overdueFinePolicyId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/overdue-fines-policies/{overdueFinePolicyId}")

    def modify_overdueFinesPolicy(self, overdueFinePolicyId: str, overdueFinesPolicy: dict):
        """Update overdueFinesPolicy item with given {overdueFinesPolicyId}

        ``PUT /overdue-fines-policies/{overdueFinePolicyId}``

        Args:
            overdueFinePolicyId (str)
            overdueFinesPolicy (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/OverdueFinePolicy_modify_overdueFinesPolicy_request.schema
        """
        return self.call("PUT", f"/overdue-fines-policies/{overdueFinePolicyId}", data=overdueFinesPolicy)


class FeefineReports(FolioApi):
    """Fee/fine reports API

    This documents the API calls for loading fee/fine reports
    """

    def set_refund(self, refund: dict):
        """Return data for a refund report

        ``POST /feefine-reports/refund``

        Args:
            refund (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/FeefineReports_set_refund_request.schema
            .. literalinclude:: ../files/FeefineReports_set_refund_return.schema 
        """
        return self.call("POST", "/feefine-reports/refund", data=refund)

    def set_cashDrawerReconciliation(self, cashDrawerReconciliation: dict):
        """Return data for a refund cash drawer reconciliation report

        ``POST /feefine-reports/cash-drawer-reconciliation``

        Args:
            cashDrawerReconciliation (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/FeefineReports_set_cashDrawerReconciliation_request.schema
            .. literalinclude:: ../files/FeefineReports_set_cashDrawerReconciliation_return.schema 
        """
        return self.call("POST", "/feefine-reports/cash-drawer-reconciliation", data=cashDrawerReconciliation)

    def set_source(self, source: dict):
        """Return list of sources for a refund cash drawer reconciliation report

        ``POST /feefine-reports/cash-drawer-reconciliation/sources``

        Args:
            source (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/FeefineReports_set_source_request.schema
            .. literalinclude:: ../files/FeefineReports_set_source_return.schema 
        """
        return self.call("POST", "/feefine-reports/cash-drawer-reconciliation/sources", data=source)

    def set_financialTransactionsDetail(self, financialTransactionsDetail: dict):
        """Return data for a financial transactions detail report

        ``POST /feefine-reports/financial-transactions-detail``

        Args:
            financialTransactionsDetail (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/FeefineReports_set_financialTransactionsDetail_request.schema
            .. literalinclude:: ../files/FeefineReports_set_financialTransactionsDetail_return.schema 
        """
        return self.call("POST", "/feefine-reports/financial-transactions-detail", data=financialTransactionsDetail)


class Payments(FolioApi):
    """Payments API

    This documents the API calls that can be made to query and manage feefine of the system
    """

    def get_payments(self, **kwargs):
        """Return a list of payments

        ``GET /payments``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - active=true
            orderBy (str):  Order by field: field A, field B
                    
            order (str (desc|asc):): (default=desc) Order
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            facets (list):  facets to return in the collection result set, can be suffixed by a count of facet values to return, for example, patronGroup:10 default to top 5 facet values

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Payments_get_payments_return.schema 
        """
        return self.call("GET", "/payments", query=kwargs)

    def set_payment(self, payment: dict):
        """Create a payment

        ``POST /payments``

        Args:
            payment (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created payment item

        Schema:

            .. literalinclude:: ../files/Payments_set_payment_request.schema
        """
        return self.call("POST", "/payments", data=payment)

    def get_payment(self, paymentId: str):
        """Get a single payment

        ``GET /payments/{paymentId}``

        Args:
            paymentId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Payments_get_payment_return.schema 
        """
        return self.call("GET", f"/payments/{paymentId}")

    def delete_payment(self, paymentId: str):
        """Delete payment item with given {paymentId}

        ``DELETE /payments/{paymentId}``

        Args:
            paymentId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/payments/{paymentId}")

    def modify_payment(self, paymentId: str, payment: dict):
        """Update payment item with given {paymentId}

        ``PUT /payments/{paymentId}``

        Args:
            paymentId (str)
            payment (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Payments_modify_payment_request.schema
        """
        return self.call("PUT", f"/payments/{paymentId}", data=payment)


class Accounts(FolioApi):
    """Accounts API

    This documents the API calls that can be made to query and manage feefine of the system
    """

    def get_accounts(self, **kwargs):
        """Return a list of accounts

        ``GET /accounts``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - active=true
            orderBy (str):  Order by field: field A, field B
                    
            order (str (desc|asc):): (default=desc) Order
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            facets (list):  facets to return in the collection result set, can be suffixed by a count of facet values to return, for example, patronGroup:10 default to top 5 facet values

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Accounts_get_accounts_return.schema 
        """
        return self.call("GET", "/accounts", query=kwargs)

    def set_account(self, account: dict):
        """Create an account

        ``POST /accounts``

        Args:
            account (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created account item

        Schema:

            .. literalinclude:: ../files/Accounts_set_account_request.schema
        """
        return self.call("POST", "/accounts", data=account)

    def get_account(self, accountId: str):
        """Get a single account

        ``GET /accounts/{accountId}``

        Args:
            accountId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Accounts_get_account_return.schema 
        """
        return self.call("GET", f"/accounts/{accountId}")

    def delete_account(self, accountId: str):
        """Delete account item with given {accountId}

        ``DELETE /accounts/{accountId}``

        Args:
            accountId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/accounts/{accountId}")

    def modify_account(self, accountId: str, account: dict):
        """Update account item with given {accountId}

        ``PUT /accounts/{accountId}``

        Args:
            accountId (str)
            account (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Accounts_modify_account_request.schema
        """
        return self.call("PUT", f"/accounts/{accountId}", data=account)

    def checkPay(self, accountId: str, checkPay: dict):
        """Checks if an action is allowed

        ``POST /accounts/{accountId}/check-pay``

        Args:
            accountId (str)
            checkPay (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Accounts_checkPay_request.schema
            .. literalinclude:: ../files/Accounts_checkPay_return.schema 
        """
        return self.call("POST", f"/accounts/{accountId}/check-pay", data=checkPay)

    def checkWaive(self, accountId: str, checkWaive: dict):
        """Checks if an action is allowed

        ``POST /accounts/{accountId}/check-waive``

        Args:
            accountId (str)
            checkWaive (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Accounts_checkWaive_request.schema
            .. literalinclude:: ../files/Accounts_checkWaive_return.schema 
        """
        return self.call("POST", f"/accounts/{accountId}/check-waive", data=checkWaive)

    def checkTransfer(self, accountId: str, checkTransfer: dict):
        """Checks if an action is allowed

        ``POST /accounts/{accountId}/check-transfer``

        Args:
            accountId (str)
            checkTransfer (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Accounts_checkTransfer_request.schema
            .. literalinclude:: ../files/Accounts_checkTransfer_return.schema 
        """
        return self.call("POST", f"/accounts/{accountId}/check-transfer", data=checkTransfer)

    def checkRefund(self, accountId: str, checkRefund: dict):
        """Checks if an action is allowed

        ``POST /accounts/{accountId}/check-refund``

        Args:
            accountId (str)
            checkRefund (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Accounts_checkRefund_request.schema
            .. literalinclude:: ../files/Accounts_checkRefund_return.schema 
        """
        return self.call("POST", f"/accounts/{accountId}/check-refund", data=checkRefund)

    def pay(self, accountId: str, pay: dict):
        """Perform action

        ``POST /accounts/{accountId}/pay``

        Args:
            accountId (str)
            pay (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Accounts_pay_request.schema
            .. literalinclude:: ../files/Accounts_pay_return.schema 
        """
        return self.call("POST", f"/accounts/{accountId}/pay", data=pay)

    def waive(self, accountId: str, waive: dict):
        """Perform action

        ``POST /accounts/{accountId}/waive``

        Args:
            accountId (str)
            waive (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Accounts_waive_request.schema
            .. literalinclude:: ../files/Accounts_waive_return.schema 
        """
        return self.call("POST", f"/accounts/{accountId}/waive", data=waive)

    def transfer(self, accountId: str, transfer: dict):
        """Perform action

        ``POST /accounts/{accountId}/transfer``

        Args:
            accountId (str)
            transfer (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Accounts_transfer_request.schema
            .. literalinclude:: ../files/Accounts_transfer_return.schema 
        """
        return self.call("POST", f"/accounts/{accountId}/transfer", data=transfer)

    def refund(self, accountId: str, refund: dict):
        """Perform action

        ``POST /accounts/{accountId}/refund``

        Args:
            accountId (str)
            refund (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Accounts_refund_request.schema
            .. literalinclude:: ../files/Accounts_refund_return.schema 
        """
        return self.call("POST", f"/accounts/{accountId}/refund", data=refund)

    def set_cancel(self, accountId: str, cancel: dict):
        """Perform action

        ``POST /accounts/{accountId}/cancel``

        Args:
            accountId (str)
            cancel (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Accounts_set_cancel_request.schema
            .. literalinclude:: ../files/Accounts_set_cancel_return.schema 
        """
        return self.call("POST", f"/accounts/{accountId}/cancel", data=cancel)


class Feefineactions(FolioApi):
    """Fee Fine Actions API

    This documents the API calls that can be made to query and manage feefine of the system
    """

    def get_feefineactions(self, **kwargs):
        """Return a list of feefineactions

        ``GET /feefineactions``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - active=true
            orderBy (str):  Order by field: field A, field B
                    
            order (str (desc|asc):): (default=desc) Order
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

            .. literalinclude:: ../files/Feefineactions_get_feefineactions_return.schema 
        """
        return self.call("GET", "/feefineactions", query=kwargs)

    def set_feefineaction(self, feefineaction: dict):
        """Create a feefineaction

        ``POST /feefineactions``

        Args:
            feefineaction (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created feefineaction item

        Schema:

            .. literalinclude:: ../files/Feefineactions_set_feefineaction_request.schema
        """
        return self.call("POST", "/feefineactions", data=feefineaction)

    def get_feefineaction(self, feefineactionId: str):
        """Get a single feefineaction

        ``GET /feefineactions/{feefineactionId}``

        Args:
            feefineactionId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Feefineactions_get_feefineaction_return.schema 
        """
        return self.call("GET", f"/feefineactions/{feefineactionId}")

    def delete_feefineaction(self, feefineactionId: str):
        """Delete feefineaction item with given {feefineactionId}

        ``DELETE /feefineactions/{feefineactionId}``

        Args:
            feefineactionId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/feefineactions/{feefineactionId}")

    def modify_feefineaction(self, feefineactionId: str, feefineaction: dict):
        """Update feefineaction item with given {feefineactionId}

        ``PUT /feefineactions/{feefineactionId}``

        Args:
            feefineactionId (str)
            feefineaction (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Feefineactions_modify_feefineaction_request.schema
        """
        return self.call("PUT", f"/feefineactions/{feefineactionId}", data=feefineaction)


class Refunds(FolioApi):
    """Refunds API

    This documents the API calls that can be made to query and manage feefine of the system
    """

    def get_refunds(self, **kwargs):
        """Return a list of refunds

        ``GET /refunds``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - active=true
            orderBy (str):  Order by field: field A, field B
                    
            order (str (desc|asc):): (default=desc) Order
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            facets (list):  facets to return in the collection result set, can be suffixed by a count of facet values to return, for example, patronGroup:10 default to top 5 facet values

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Refunds_get_refunds_return.schema 
        """
        return self.call("GET", "/refunds", query=kwargs)

    def set_refund(self, refund: dict):
        """Create a refund

        ``POST /refunds``

        Args:
            refund (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created refund item

        Schema:

            .. literalinclude:: ../files/Refunds_set_refund_request.schema
        """
        return self.call("POST", "/refunds", data=refund)

    def get_refund(self, refundId: str):
        """Get a single refund

        ``GET /refunds/{refundId}``

        Args:
            refundId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Refunds_get_refund_return.schema 
        """
        return self.call("GET", f"/refunds/{refundId}")

    def delete_refund(self, refundId: str):
        """Delete refund item with given {refundId}

        ``DELETE /refunds/{refundId}``

        Args:
            refundId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/refunds/{refundId}")

    def modify_refund(self, refundId: str, refund: dict):
        """Update refund item with given {refundId}

        ``PUT /refunds/{refundId}``

        Args:
            refundId (str)
            refund (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Refunds_modify_refund_request.schema
        """
        return self.call("PUT", f"/refunds/{refundId}", data=refund)


class Transfers(FolioApi):
    """Transfers API

    This documents the API calls that can be made to query and manage feefine of the system
    """

    def get_transfers(self, **kwargs):
        """Return a list of transfers

        ``GET /transfers``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - active=true
            orderBy (str):  Order by field: field A, field B
                    
            order (str (desc|asc):): (default=desc) Order
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            facets (list):  facets to return in the collection result set, can be suffixed by a count of facet values to return, for example, patronGroup:10 default to top 5 facet values

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Transfers_get_transfers_return.schema 
        """
        return self.call("GET", "/transfers", query=kwargs)

    def set_transfer(self, transfer: dict):
        """Create a transfer

        ``POST /transfers``

        Args:
            transfer (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created transfer item

        Schema:

            .. literalinclude:: ../files/Transfers_set_transfer_request.schema
        """
        return self.call("POST", "/transfers", data=transfer)

    def get_transfer(self, transferId: str):
        """Get a single transfer

        ``GET /transfers/{transferId}``

        Args:
            transferId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Transfers_get_transfer_return.schema 
        """
        return self.call("GET", f"/transfers/{transferId}")

    def delete_transfer(self, transferId: str):
        """Delete transfer item with given {transferId}

        ``DELETE /transfers/{transferId}``

        Args:
            transferId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/transfers/{transferId}")

    def modify_transfer(self, transferId: str, transfer: dict):
        """Update transfer item with given {transferId}

        ``PUT /transfers/{transferId}``

        Args:
            transferId (str)
            transfer (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Transfers_modify_transfer_request.schema
        """
        return self.call("PUT", f"/transfers/{transferId}", data=transfer)


class AccountsBulk(FolioApi):
    """Accounts bulk actions API

    This documents the API calls for bulk actions against accounts
    """

    def checkPay(self, checkPay: dict):
        """Checks if an action is allowed

        ``POST /accounts-bulk/check-pay``

        Args:
            checkPay (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AccountsBulk_checkPay_request.schema
            .. literalinclude:: ../files/AccountsBulk_checkPay_return.schema 
        """
        return self.call("POST", "/accounts-bulk/check-pay", data=checkPay)

    def checkTransfer(self, checkTransfer: dict):
        """Checks if an action is allowed

        ``POST /accounts-bulk/check-transfer``

        Args:
            checkTransfer (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AccountsBulk_checkTransfer_request.schema
            .. literalinclude:: ../files/AccountsBulk_checkTransfer_return.schema 
        """
        return self.call("POST", "/accounts-bulk/check-transfer", data=checkTransfer)

    def checkWaive(self, checkWaive: dict):
        """Checks if an action is allowed

        ``POST /accounts-bulk/check-waive``

        Args:
            checkWaive (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AccountsBulk_checkWaive_request.schema
            .. literalinclude:: ../files/AccountsBulk_checkWaive_return.schema 
        """
        return self.call("POST", "/accounts-bulk/check-waive", data=checkWaive)

    def checkRefund(self, checkRefund: dict):
        """Checks if an action is allowed

        ``POST /accounts-bulk/check-refund``

        Args:
            checkRefund (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AccountsBulk_checkRefund_request.schema
            .. literalinclude:: ../files/AccountsBulk_checkRefund_return.schema 
        """
        return self.call("POST", "/accounts-bulk/check-refund", data=checkRefund)

    def pay(self, pay: dict):
        """Perform an action

        ``POST /accounts-bulk/pay``

        Args:
            pay (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AccountsBulk_pay_request.schema
            .. literalinclude:: ../files/AccountsBulk_pay_return.schema 
        """
        return self.call("POST", "/accounts-bulk/pay", data=pay)

    def waive(self, waive: dict):
        """Perform an action

        ``POST /accounts-bulk/waive``

        Args:
            waive (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AccountsBulk_waive_request.schema
            .. literalinclude:: ../files/AccountsBulk_waive_return.schema 
        """
        return self.call("POST", "/accounts-bulk/waive", data=waive)

    def transfer(self, transfer: dict):
        """Perform an action

        ``POST /accounts-bulk/transfer``

        Args:
            transfer (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AccountsBulk_transfer_request.schema
            .. literalinclude:: ../files/AccountsBulk_transfer_return.schema 
        """
        return self.call("POST", "/accounts-bulk/transfer", data=transfer)

    def refund(self, refund: dict):
        """Perform an action

        ``POST /accounts-bulk/refund``

        Args:
            refund (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AccountsBulk_refund_request.schema
            .. literalinclude:: ../files/AccountsBulk_refund_return.schema 
        """
        return self.call("POST", "/accounts-bulk/refund", data=refund)

    def set_cancel(self, cancel: dict):
        """Perform an action

        ``POST /accounts-bulk/cancel``

        Args:
            cancel (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AccountsBulk_set_cancel_request.schema
            .. literalinclude:: ../files/AccountsBulk_set_cancel_return.schema 
        """
        return self.call("POST", "/accounts-bulk/cancel", data=cancel)


class Manualblocks(FolioApi):
    """Manual Patron Blocks API

    This documents the API calls that can be made to query and manage manualblock of the system
    """

    def get_manualblocks(self, **kwargs):
        """Return a list of manualblocks

        ``GET /manualblocks``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - active=true
            orderBy (str):  Order by field: field A, field B
                    
            order (str (desc|asc):): (default=desc) Order
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

            .. literalinclude:: ../files/Manualblocks_get_manualblocks_return.schema 
        """
        return self.call("GET", "/manualblocks", query=kwargs)

    def set_manualblock(self, manualblock: dict):
        """Create a manualblock

        ``POST /manualblocks``

        Args:
            manualblock (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created manualblock item

        Schema:

            .. literalinclude:: ../files/Manualblocks_set_manualblock_request.schema
        """
        return self.call("POST", "/manualblocks", data=manualblock)

    def get_manualblock(self, manualblockId: str):
        """Get a single manualblock

        ``GET /manualblocks/{manualblockId}``

        Args:
            manualblockId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Manualblocks_get_manualblock_return.schema 
        """
        return self.call("GET", f"/manualblocks/{manualblockId}")

    def delete_manualblock(self, manualblockId: str):
        """Delete manualblock item with given {manualblockId}

        ``DELETE /manualblocks/{manualblockId}``

        Args:
            manualblockId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/manualblocks/{manualblockId}")

    def modify_manualblock(self, manualblockId: str, manualblock: dict):
        """Update manualblock item with given {manualblockId}

        ``PUT /manualblocks/{manualblockId}``

        Args:
            manualblockId (str)
            manualblock (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Manualblocks_modify_manualblock_request.schema
        """
        return self.call("PUT", f"/manualblocks/{manualblockId}", data=manualblock)


class ActualCostFeeFine(FolioApi):
    """Actual Cost Fee Fine API

    This documents the Actual Cost Fee Fine API
    """

    def set_cancel(self, cancel: dict):
        """Cancel actual cost record

        ``POST /actual-cost-fee-fine/cancel``

        Args:
            cancel (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/ActualCostFeeFine_set_cancel_request.schema
            .. literalinclude:: ../files/ActualCostFeeFine_set_cancel_return.schema 
        """
        return self.call("POST", "/actual-cost-fee-fine/cancel", data=cancel)

    def set_bill(self, bill: dict):
        """Bill actual cost record

        ``POST /actual-cost-fee-fine/bill``

        Args:
            bill (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/ActualCostFeeFine_set_bill_request.schema
            .. literalinclude:: ../files/ActualCostFeeFine_set_bill_return.schema 
        """
        return self.call("POST", "/actual-cost-fee-fine/bill", data=bill)


class ManualBlockTemplates(FolioApi):
    """Manual Patron Block Templates API

    This documents the API calls that can be made to query and manage templates for manualblocks of the system
    """

    def get_manualBlockTemplates(self, **kwargs):
        """Return a list of manualblock templates

        ``GET /manual-block-templates``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - active=true
            orderBy (str):  Order by field: field A, field B
                    
            order (str (desc|asc):): (default=desc) Order
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

            .. literalinclude:: ../files/ManualBlockTemplates_get_manualBlockTemplates_return.schema 
        """
        return self.call("GET", "/manual-block-templates", query=kwargs)

    def set_manualBlockTemplate(self, manualBlockTemplate: dict):
        """Create a manualblock template

        ``POST /manual-block-templates``

        Args:
            manualBlockTemplate (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created manualBlockTemplate item

        Schema:

            .. literalinclude:: ../files/ManualBlockTemplates_set_manualBlockTemplate_request.schema
        """
        return self.call("POST", "/manual-block-templates", data=manualBlockTemplate)

    def get_manualBlockTemplate(self, manualBlockTemplatesId: str):
        """Get a single manualblock template

        ``GET /manual-block-templates/{manualBlockTemplatesId}``

        Args:
            manualBlockTemplatesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ManualBlockTemplates_get_manualBlockTemplate_return.schema 
        """
        return self.call("GET", f"/manual-block-templates/{manualBlockTemplatesId}")

    def delete_manualBlockTemplate(self, manualBlockTemplatesId: str):
        """Delete a single manualblock template

        ``DELETE /manual-block-templates/{manualBlockTemplatesId}``

        Args:
            manualBlockTemplatesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/manual-block-templates/{manualBlockTemplatesId}")

    def modify_manualBlockTemplate(self, manualBlockTemplatesId: str, manualBlockTemplate: dict):
        """Update a single manualblock template

        ``PUT /manual-block-templates/{manualBlockTemplatesId}``

        Args:
            manualBlockTemplatesId (str)
            manualBlockTemplate (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ManualBlockTemplates_modify_manualBlockTemplate_request.schema
        """
        return self.call("PUT", f"/manual-block-templates/{manualBlockTemplatesId}", data=manualBlockTemplate)


class Waiver(FolioApi):
    """Waives API

    This documents the API calls that can be made to query and manage waive of the system
    """

    def get_waives(self, **kwargs):
        """Return a list of waive

        ``GET /waives``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - active=true
            orderBy (str):  Order by field: field A, field B
                    
            order (str (desc|asc):): (default=desc) Order
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            facets (list):  facets to return in the collection result set, can be suffixed by a count of facet values to return, for example, patronGroup:10 default to top 5 facet values

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Waiver_get_waives_return.schema 
        """
        return self.call("GET", "/waives", query=kwargs)

    def set_waife(self, waife: dict):
        """Create a waive

        ``POST /waives``

        Args:
            waife (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created waife item

        Schema:

            .. literalinclude:: ../files/Waiver_set_waife_request.schema
        """
        return self.call("POST", "/waives", data=waife)

    def get_waife(self, waiveId: str):
        """Get a single waive

        ``GET /waives/{waiveId}``

        Args:
            waiveId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Waiver_get_waife_return.schema 
        """
        return self.call("GET", f"/waives/{waiveId}")

    def delete_waife(self, waiveId: str):
        """Delete waife item with given {waifeId}

        ``DELETE /waives/{waiveId}``

        Args:
            waiveId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/waives/{waiveId}")

    def modify_waife(self, waiveId: str, waife: dict):
        """Update waife item with given {waifeId}

        ``PUT /waives/{waiveId}``

        Args:
            waiveId (str)
            waife (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Waiver_modify_waife_request.schema
        """
        return self.call("PUT", f"/waives/{waiveId}", data=waife)


class Feefines(FolioApi):
    """Feefines API

    This documents the API calls that can be made to query and manage feefine of the system
    """

    def get_feefines(self, **kwargs):
        """Return a list of feefines

        ``GET /feefines``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - active=true
            orderBy (str):  Order by field: field A, field B
                    
            order (str (desc|asc):): (default=desc) Order
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            facets (list):  facets to return in the collection result set, can be suffixed by a count of facet values to return, for example, patronGroup:10 default to top 5 facet values

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Feefines_get_feefines_return.schema 
        """
        return self.call("GET", "/feefines", query=kwargs)

    def set_feefine(self, feefine: dict):
        """Create a feefine

        ``POST /feefines``

        Args:
            feefine (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created feefine item

        Schema:

            .. literalinclude:: ../files/Feefines_set_feefine_request.schema
        """
        return self.call("POST", "/feefines", data=feefine)

    def get_feefine(self, feefineId: str):
        """Get a single feefine

        ``GET /feefines/{feefineId}``

        Args:
            feefineId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Feefines_get_feefine_return.schema 
        """
        return self.call("GET", f"/feefines/{feefineId}")

    def delete_feefine(self, feefineId: str):
        """Delete feefine item with given {feefineId}

        ``DELETE /feefines/{feefineId}``

        Args:
            feefineId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/feefines/{feefineId}")

    def modify_feefine(self, feefineId: str, feefine: dict):
        """Update feefine item with given {feefineId}

        ``PUT /feefines/{feefineId}``

        Args:
            feefineId (str)
            feefine (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Feefines_modify_feefine_request.schema
        """
        return self.call("PUT", f"/feefines/{feefineId}", data=feefine)


class LostItemFeePolicy(FolioApi):
    """Lost Item Fee Policies API

    **Lost Item Fee Policies**
    """

    def get_lostItemFeesPolicies(self, **kwargs):
        """Get Lost Item Fee Policy list

        ``GET /lost-item-fees-policies``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    searchable using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name="undergrad*"
            orderBy (str):  Order by field: field A, field B
                    
            order (str (desc|asc):): (default=desc) Order
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

            .. literalinclude:: ../files/LostItemFeePolicy_get_lostItemFeesPolicies_return.schema 
        """
        return self.call("GET", "/lost-item-fees-policies", query=kwargs)

    def set_lostItemFeesPolicy(self, lostItemFeesPolicy: dict):
        """Create new Lost Item Fee Policy

        ``POST /lost-item-fees-policies``

        Args:
            lostItemFeesPolicy (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created lostItemFeesPolicy item

        Schema:

            .. literalinclude:: ../files/LostItemFeePolicy_set_lostItemFeesPolicy_request.schema
        """
        return self.call("POST", "/lost-item-fees-policies", data=lostItemFeesPolicy)

    def get_lostItemFeesPolicy(self, lostItemFeePolicyId: str):
        """Get Lost Item Fee Policy by id

        ``GET /lost-item-fees-policies/{lostItemFeePolicyId}``

        Args:
            lostItemFeePolicyId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LostItemFeePolicy_get_lostItemFeesPolicy_return.schema 
        """
        return self.call("GET", f"/lost-item-fees-policies/{lostItemFeePolicyId}")

    def delete_lostItemFeesPolicy(self, lostItemFeePolicyId: str):
        """Delete Lost Item Fee Policy by id

        ``DELETE /lost-item-fees-policies/{lostItemFeePolicyId}``

        Args:
            lostItemFeePolicyId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/lost-item-fees-policies/{lostItemFeePolicyId}")

    def modify_lostItemFeesPolicy(self, lostItemFeePolicyId: str, lostItemFeesPolicy: dict):
        """Update lostItemFeesPolicy item with given {lostItemFeesPolicyId}

        ``PUT /lost-item-fees-policies/{lostItemFeePolicyId}``

        Args:
            lostItemFeePolicyId (str)
            lostItemFeesPolicy (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LostItemFeePolicy_modify_lostItemFeesPolicy_request.schema
        """
        return self.call("PUT", f"/lost-item-fees-policies/{lostItemFeePolicyId}", data=lostItemFeesPolicy)
