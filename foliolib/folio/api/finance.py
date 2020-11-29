# -*- coding: utf-8 -*-
# Generated at 2020-11-29

import logging

from foliolib.folio import FolioApi

log = logging.getLogger("foliolib.folio.api.finance")


class FundTypes(FolioApi):
    """Fund types APIs

    This documents the API calls that can be made to manage fund types
    """

    def get_fundTypes(self, **kwargs):
        """Retrieve a list of fundType items.

        ``GET /finance/fund-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example name
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["name", "MEDGRANT", "="]

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FundTypes_get_fundTypes_return.schema 
        """
        return self.call("GET", "/finance/fund-types", query=kwargs)

    def set_fundType(self, fundType: dict):
        """Create a new fundType item.

        ``POST /finance/fund-types``

        Args:
            fundType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created fundType item

        Schema:

            .. literalinclude:: ../files/FundTypes_set_fundType_request.schema
        """
        return self.call("POST", "/finance/fund-types", data=fundType)

    def get_fundType(self, fundTypesId: str):
        """Retrieve fundType item with given {fundTypeId}

        ``GET /finance/fund-types/{fundTypesId}``

        Args:
            fundTypesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FundTypes_get_fundType_return.schema 
        """
        return self.call("GET", f"/finance/fund-types/{fundTypesId}")

    def delete_fundType(self, fundTypesId: str):
        """Delete fundType item with given {fundTypeId}

        ``DELETE /finance/fund-types/{fundTypesId}``

        Args:
            fundTypesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance/fund-types/{fundTypesId}")

    def modify_fundType(self, fundTypesId: str, fundType: dict):
        """Update fundType item with given {fundTypeId}

        ``PUT /finance/fund-types/{fundTypesId}``

        Args:
            fundTypesId (str)
            fundType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/FundTypes_modify_fundType_request.schema
        """
        return self.call("PUT", f"/finance/fund-types/{fundTypesId}", data=fundType)


class ReleaseEncumbrance(FolioApi):
    """Release encumbrance API

    This documents the API calls that release any remaining money encumbered back to the budget's available pool
    """

    def set_releaseEncumbrance(self, releaseEncumbranceId: str, **kwargs):
        """Release encumbrance

        ``POST /finance/release-encumbrance/{releaseEncumbranceId}``

        Args:
            releaseEncumbranceId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("POST", f"/finance/release-encumbrance/{releaseEncumbranceId}", query=kwargs)


class FiscalYears(FolioApi):
    """Fiscal year API

    This documents the API calls that can be made to manage fiscal-years
    """

    def get_fiscalYears(self, **kwargs):
        """Retrieve a list of fiscalYear items.

        ``GET /finance/fiscal-years``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FiscalYears_get_fiscalYears_return.schema 
        """
        return self.call("GET", "/finance/fiscal-years", query=kwargs)

    def set_fiscalYear(self, fiscalYear: dict):
        """Create a new fiscalYear item.

        ``POST /finance/fiscal-years``

        Args:
            fiscalYear (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created fiscalYear item

        Schema:

            .. literalinclude:: ../files/FiscalYears_set_fiscalYear_request.schema
        """
        return self.call("POST", "/finance/fiscal-years", data=fiscalYear)

    def get_fiscalYear(self, fiscalYearsId: str):
        """Retrieve fiscalYear item with given {fiscalYearId}

        ``GET /finance/fiscal-years/{fiscalYearsId}``

        Args:
            fiscalYearsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FiscalYears_get_fiscalYear_return.schema 
        """
        return self.call("GET", f"/finance/fiscal-years/{fiscalYearsId}")

    def delete_fiscalYear(self, fiscalYearsId: str):
        """Delete fiscalYear item with given {fiscalYearId}

        ``DELETE /finance/fiscal-years/{fiscalYearsId}``

        Args:
            fiscalYearsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance/fiscal-years/{fiscalYearsId}")

    def modify_fiscalYear(self, fiscalYearsId: str, fiscalYear: dict):
        """Update fiscalYear item with given {fiscalYearId}

        ``PUT /finance/fiscal-years/{fiscalYearsId}``

        Args:
            fiscalYearsId (str)
            fiscalYear (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/FiscalYears_modify_fiscalYear_request.schema
        """
        return self.call("PUT", f"/finance/fiscal-years/{fiscalYearsId}", data=fiscalYear)


class GroupFundFiscalYear(FolioApi):
    """Group Fund Fiscal Year API

    This documents the API calls that can be made to manage group-fund-fiscal-years
    """

    def get_groupFundFiscalYears(self, **kwargs):
        """Retrieve a list of groupFundFiscalYear items.

        ``GET /finance/group-fund-fiscal-years``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example fundId
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["fundId", "6e2fbba3-d557-4480-bca3-b6f5c645de04", "="]

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/GroupFundFiscalYear_get_groupFundFiscalYears_return.schema 
        """
        return self.call("GET", "/finance/group-fund-fiscal-years", query=kwargs)

    def set_groupFundFiscalYear(self, groupFundFiscalYear: dict):
        """Create a new groupFundFiscalYear item.

        ``POST /finance/group-fund-fiscal-years``

        Args:
            groupFundFiscalYear (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created groupFundFiscalYear item

        Schema:

            .. literalinclude:: ../files/GroupFundFiscalYear_set_groupFundFiscalYear_request.schema
        """
        return self.call("POST", "/finance/group-fund-fiscal-years", data=groupFundFiscalYear)

    def delete_groupFundFiscalYear(self, groupFundFiscalYearsId: str, **kwargs):
        """Delete a group fund fiscal year

        ``DELETE /finance/group-fund-fiscal-years/{groupFundFiscalYearsId}``

        Args:
            groupFundFiscalYearsId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("DELETE", f"/finance/group-fund-fiscal-years/{groupFundFiscalYearsId}", query=kwargs)


class Transaction(FolioApi):
    """mod-finance (Transactions)

    **CRUD APIs used to manage transactions.**
    """

    def set_allocation(self, allocation: dict):
        """Create an allocation by transaction

        ``POST /finance/allocations``

        Args:
            allocation (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Transaction_set_allocation_request.schema
        """
        return self.call("POST", "/finance/allocations", data=allocation)

    def set_transfer(self, transfer: dict):
        """Create a transfer by transaction

        ``POST /finance/transfers``

        Args:
            transfer (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Transaction_set_transfer_request.schema
        """
        return self.call("POST", "/finance/transfers", data=transfer)

    def set_encumbrance(self, encumbrance: dict):
        """Create an encumbrance by transaction

        ``POST /finance/encumbrances``

        Args:
            encumbrance (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Transaction_set_encumbrance_request.schema
        """
        return self.call("POST", "/finance/encumbrances", data=encumbrance)

    def modify_encumbrance(self, encumbrancesId: str, encumbrance: dict, **kwargs):
        """Update a Transaction instance

        ``PUT /finance/encumbrances/{encumbrancesId}``

        Args:
            encumbrancesId (str)
            encumbrance (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Schema:

            .. literalinclude:: ../files/Transaction_modify_encumbrance_request.schema
        """
        return self.call("PUT", f"/finance/encumbrances/{encumbrancesId}", data=encumbrance, query=kwargs)

    def set_payment(self, payment: dict):
        """Create a payment by transaction

        ``POST /finance/payments``

        Args:
            payment (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Transaction_set_payment_request.schema
        """
        return self.call("POST", "/finance/payments", data=payment)

    def set_pendingPayment(self, pendingPayment: dict):
        """Create a pending payment by transaction

        ``POST /finance/pending-payments``

        Args:
            pendingPayment (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Transaction_set_pendingPayment_request.schema
        """
        return self.call("POST", "/finance/pending-payments", data=pendingPayment)

    def modify_pendingPayment(self, pendingPaymentsId: str, pendingPayment: dict):
        """Update a pending payment by transaction

        ``PUT /finance/pending-payments/{pendingPaymentsId}``

        Args:
            pendingPaymentsId (str)
            pendingPayment (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Transaction_modify_pendingPayment_request.schema
        """
        return self.call("PUT", f"/finance/pending-payments/{pendingPaymentsId}", data=pendingPayment)

    def set_credit(self, credit: dict):
        """Create a credit by transaction

        ``POST /finance/credits``

        Args:
            credit (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Transaction_set_credit_request.schema
        """
        return self.call("POST", "/finance/credits", data=credit)

    def get_transactions(self, **kwargs):
        """Retrieve a list of transaction items.

        ``GET /finance/transactions``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example currency = USD
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - currency=USD
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
            OkapiRequestUnauthorized: Authentication is required

        Schema:

            .. literalinclude:: ../files/Transaction_get_transactions_return.schema 
        """
        return self.call("GET", "/finance/transactions", query=kwargs)

    def get_transaction(self, transactionsId: str):
        """Retrieve transaction item with given {transactionId}

        ``GET /finance/transactions/{transactionsId}``

        Args:
            transactionsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Transaction_get_transaction_return.schema 
        """
        return self.call("GET", f"/finance/transactions/{transactionsId}")


class TransactionSummary(FolioApi):
    """Transaction Summaries API

    This documents the API calls that can be made to create Transaction summaries for Orders and Invoices
    """

    def set_orderTransactionSummary(self, orderTransactionSummary: dict):
        """Create a new order transaction summary, for an order with number of transactions(encumbrances)

        ``POST /finance/order-transaction-summaries``

        Args:
            orderTransactionSummary (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/TransactionSummary_set_orderTransactionSummary_request.schema
        """
        return self.call("POST", "/finance/order-transaction-summaries", data=orderTransactionSummary)

    def modify_orderTransactionSummary(self, orderTransactionSummariesId: str, orderTransactionSummary: dict):
        """Updated order transaction summary, for an order with number of transactions(encumbrances)

        ``PUT /finance/order-transaction-summaries/{orderTransactionSummariesId}``

        Args:
            orderTransactionSummariesId (str)
            orderTransactionSummary (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/TransactionSummary_modify_orderTransactionSummary_request.schema
        """
        return self.call("PUT", f"/finance/order-transaction-summaries/{orderTransactionSummariesId}", data=orderTransactionSummary)

    def set_invoiceTransactionSummary(self, invoiceTransactionSummary: dict):
        """Create a new invoice transaction summary, for an order with number of transactions(encumbrances) and number of payment credits

        ``POST /finance/invoice-transaction-summaries``

        Args:
            invoiceTransactionSummary (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/TransactionSummary_set_invoiceTransactionSummary_request.schema
        """
        return self.call("POST", "/finance/invoice-transaction-summaries", data=invoiceTransactionSummary)

    def modify_invoiceTransactionSummary(self, invoiceTransactionSummariesId: str, invoiceTransactionSummary: dict):
        """Updated invoice transaction summary, for an invoice with number of pending payments and number of payment/credits

        ``PUT /finance/invoice-transaction-summaries/{invoiceTransactionSummariesId}``

        Args:
            invoiceTransactionSummariesId (str)
            invoiceTransactionSummary (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/TransactionSummary_modify_invoiceTransactionSummary_request.schema
        """
        return self.call("PUT", f"/finance/invoice-transaction-summaries/{invoiceTransactionSummariesId}", data=invoiceTransactionSummary)


class GroupFiscalYearSummaries(FolioApi):
    """Group Fiscal Year Summary API

    This documents the API calls that can be made to manage group-fiscal-year-summaries
    """

    def get_groupFiscalYearSummaries(self, **kwargs):
        """Retrieve groupFiscalYearSummary item with given {groupFiscalYearSummaryId}

        ``GET /finance/group-fiscal-year-summaries``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example fund.ledgerId
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["fund.ledgerId", "6e2fbba3-d557-4480-bca3-b6f5c645de04", "="]

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/GroupFiscalYearSummaries_get_groupFiscalYearSummaries_return.schema 
        """
        return self.call("GET", "/finance/group-fiscal-year-summaries", query=kwargs)


class Groups(FolioApi):
    """Group API

    This documents the API calls that can be made to manage groups
    """

    def get_groups(self, **kwargs):
        """Retrieve a list of group items.

        ``GET /finance/groups``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Groups_get_groups_return.schema 
        """
        return self.call("GET", "/finance/groups", query=kwargs)

    def set_group(self, group: dict):
        """Create a new group item.

        ``POST /finance/groups``

        Args:
            group (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created group item

        Schema:

            .. literalinclude:: ../files/Groups_set_group_request.schema
        """
        return self.call("POST", "/finance/groups", data=group)

    def get_group(self, groupsId: str):
        """Retrieve group item with given {groupId}

        ``GET /finance/groups/{groupsId}``

        Args:
            groupsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Groups_get_group_return.schema 
        """
        return self.call("GET", f"/finance/groups/{groupsId}")

    def delete_group(self, groupsId: str):
        """Delete group item with given {groupId}

        ``DELETE /finance/groups/{groupsId}``

        Args:
            groupsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance/groups/{groupsId}")

    def modify_group(self, groupsId: str, group: dict):
        """Update group item with given {groupId}

        ``PUT /finance/groups/{groupsId}``

        Args:
            groupsId (str)
            group (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Groups_modify_group_request.schema
        """
        return self.call("PUT", f"/finance/groups/{groupsId}", data=group)

    def get_expenseClassesTotals(self, groupsId: str, **kwargs):
        """Retrieve expenseClassesTotal item with given {expenseClassesTotalId}

        ``GET /finance/groups/{groupsId}/expense-classes-totals``

        Args:
            groupsId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            fiscalYearId (uuid):  The UUID of a fiscal year

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Groups_get_expenseClassesTotals_return.schema 
        """
        return self.call("GET", f"/finance/groups/{groupsId}/expense-classes-totals", query=kwargs)


class Budgets(FolioApi):
    """Budget API

    This documents the API calls that can be made to manage budgets
    """

    def get_budgets(self, **kwargs):
        """Retrieve a list of budget items.

        ``GET /finance/budgets``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["name", "HIST-FY19", "="]

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Budgets_get_budgets_return.schema 
        """
        return self.call("GET", "/finance/budgets", query=kwargs)

    def set_budget(self, budget: dict):
        """Create a new budget item.

        ``POST /finance/budgets``

        Args:
            budget (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created budget item

        Schema:

            .. literalinclude:: ../files/Budgets_set_budget_request.schema
        """
        return self.call("POST", "/finance/budgets", data=budget)

    def get_budget(self, budgetsId: str):
        """Retrieve budget item with given {budgetId}

        ``GET /finance/budgets/{budgetsId}``

        Args:
            budgetsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Budgets_get_budget_return.schema 
        """
        return self.call("GET", f"/finance/budgets/{budgetsId}")

    def delete_budget(self, budgetsId: str):
        """Delete budget item with given {budgetId}

        ``DELETE /finance/budgets/{budgetsId}``

        Args:
            budgetsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance/budgets/{budgetsId}")

    def modify_budget(self, budgetsId: str, budget: dict):
        """Update budget item with given {budgetId}

        ``PUT /finance/budgets/{budgetsId}``

        Args:
            budgetsId (str)
            budget (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Budgets_modify_budget_request.schema
        """
        return self.call("PUT", f"/finance/budgets/{budgetsId}", data=budget)

    def get_expenseClassesTotals(self, budgetsId: str):
        """Retrieve expenseClassesTotal item with given {expenseClassesTotalId}

        ``GET /finance/budgets/{budgetsId}/expense-classes-totals``

        Args:
            budgetsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Budgets_get_expenseClassesTotals_return.schema 
        """
        return self.call("GET", f"/finance/budgets/{budgetsId}/expense-classes-totals")


class ExchangeRate(FolioApi):
    """Exchange rate API

    This documents the API calls that can be made to get exchange rates
    """

    def get_exchangeRates(self, **kwargs):
        """Get exchange rate

        ``GET /finance/exchange-rate``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            from (currency_code):  From currency code
                    
                    Example:
                    
                     - USD
            to (currency_code):  To currency code
                    
                    Example:
                    
                     - EUR
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ExchangeRate_get_exchangeRates_return.schema 
        """
        return self.call("GET", "/finance/exchange-rate", query=kwargs)


class Funds(FolioApi):
    """Fund API

    This documents the API calls that can be made to manage funds
    """

    def get_funds(self, **kwargs):
        """Retrieve a list of fund items.

        ``GET /finance/funds``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Funds_get_funds_return.schema 
        """
        return self.call("GET", "/finance/funds", query=kwargs)

    def set_fund(self, fund: dict):
        """Create a new fund item.

        ``POST /finance/funds``

        Args:
            fund (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created fund item

        Schema:

            .. literalinclude:: ../files/Funds_set_fund_request.schema
        """
        return self.call("POST", "/finance/funds", data=fund)

    def get_fund(self, fundsId: str):
        """Retrieve fund item with given {fundId}

        ``GET /finance/funds/{fundsId}``

        Args:
            fundsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Funds_get_fund_return.schema 
        """
        return self.call("GET", f"/finance/funds/{fundsId}")

    def delete_fund(self, fundsId: str):
        """Delete fund item with given {fundId}

        ``DELETE /finance/funds/{fundsId}``

        Args:
            fundsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance/funds/{fundsId}")

    def modify_fund(self, fundsId: str, fund: dict):
        """Update fund item with given {fundId}

        ``PUT /finance/funds/{fundsId}``

        Args:
            fundsId (str)
            fund (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Funds_modify_fund_request.schema
        """
        return self.call("PUT", f"/finance/funds/{fundsId}", data=fund)

    def get_expenseClasses(self, fundsId: str, **kwargs):
        """Retrieve expenseClass item with given {expenseClassId}

        ``GET /finance/funds/{fundsId}/expense-classes``

        Args:
            fundsId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            status (str):  Status of the expense classes
                    
                    Example:
                    
                     - Active

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Funds_get_expenseClasses_return.schema 
        """
        return self.call("GET", f"/finance/funds/{fundsId}/expense-classes", query=kwargs)

    def get_budget_by_fund(self, fundsId: str, **kwargs):
        """Retrieve budget item with given {budgetId}

        ``GET /finance/funds/{fundsId}/budget``

        Args:
            fundsId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            status (str):  Status of the budget
                    
                    Example:
                    
                     - Active

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Funds_get_budget_by_fund_return.schema 
        """
        return self.call("GET", f"/finance/funds/{fundsId}/budget", query=kwargs)


class Ledgers(FolioApi):
    """Ledger API

    This documents the API calls that can be made to manage ledgers
    """

    def get_ledgers(self, **kwargs):
        """Retrieve a list of ledger items.

        ``GET /finance/ledgers``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            fiscalYear (uuid):  Fiscal Year Id
                    
                    Example:
                    
                     - 3defdcde-3002-41d3-a31c-1fb88288f872
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Ledgers_get_ledgers_return.schema 
        """
        return self.call("GET", "/finance/ledgers", query=kwargs)

    def set_ledger(self, ledger: dict):
        """Create a new ledger item.

        ``POST /finance/ledgers``

        Args:
            ledger (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created ledger item

        Schema:

            .. literalinclude:: ../files/Ledgers_set_ledger_request.schema
        """
        return self.call("POST", "/finance/ledgers", data=ledger)

    def get_ledger(self, ledgersId: str, **kwargs):
        """Retrieve ledger item with given {ledgerId}

        ``GET /finance/ledgers/{ledgersId}``

        Args:
            ledgersId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            fiscalYear (uuid):  The UUID of a fiscal year

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Ledgers_get_ledger_return.schema 
        """
        return self.call("GET", f"/finance/ledgers/{ledgersId}", query=kwargs)

    def delete_ledger(self, ledgersId: str):
        """Delete ledger item with given {ledgerId}

        ``DELETE /finance/ledgers/{ledgersId}``

        Args:
            ledgersId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance/ledgers/{ledgersId}")

    def modify_ledger(self, ledgersId: str, ledger: dict):
        """Update ledger item with given {ledgerId}

        ``PUT /finance/ledgers/{ledgersId}``

        Args:
            ledgersId (str)
            ledger (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Ledgers_modify_ledger_request.schema
        """
        return self.call("PUT", f"/finance/ledgers/{ledgersId}", data=ledger)

    def get_currentFiscalYear_by_ledger(self, ledgersId: str):
        """Retrieve currentFiscalYear item with given {currentFiscalYearId}

        ``GET /finance/ledgers/{ledgersId}/current-fiscal-year``

        Args:
            ledgersId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Ledgers_get_currentFiscalYear_by_ledger_return.schema 
        """
        return self.call("GET", f"/finance/ledgers/{ledgersId}/current-fiscal-year")


class ExpenseClasses(FolioApi):
    """Group API

    This documents the API calls that can be made to manage groups
    """

    def get_expenseClasses(self, **kwargs):
        """Retrieve a list of expenseClass items.

        ``GET /finance/expense-classes``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ExpenseClasses_get_expenseClasses_return.schema 
        """
        return self.call("GET", "/finance/expense-classes", query=kwargs)

    def set_expenseClass(self, expenseClass: dict):
        """Create a new expenseClass item.

        ``POST /finance/expense-classes``

        Args:
            expenseClass (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created expenseClass item

        Schema:

            .. literalinclude:: ../files/ExpenseClasses_set_expenseClass_request.schema
        """
        return self.call("POST", "/finance/expense-classes", data=expenseClass)

    def get_expenseClass(self, expenseClassesId: str):
        """Retrieve expenseClass item with given {expenseClassId}

        ``GET /finance/expense-classes/{expenseClassesId}``

        Args:
            expenseClassesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ExpenseClasses_get_expenseClass_return.schema 
        """
        return self.call("GET", f"/finance/expense-classes/{expenseClassesId}")

    def delete_expenseClass(self, expenseClassesId: str):
        """Delete expenseClass item with given {expenseClassId}

        ``DELETE /finance/expense-classes/{expenseClassesId}``

        Args:
            expenseClassesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance/expense-classes/{expenseClassesId}")

    def modify_expenseClass(self, expenseClassesId: str, expenseClass: dict):
        """Update expenseClass item with given {expenseClassId}

        ``PUT /finance/expense-classes/{expenseClassesId}``

        Args:
            expenseClassesId (str)
            expenseClass (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/ExpenseClasses_modify_expenseClass_request.schema
        """
        return self.call("PUT", f"/finance/expense-classes/{expenseClassesId}", data=expenseClass)
