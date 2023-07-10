# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.financeStorage")


class LedgerRolloverProgress(FolioApi):
    """mod-finance-storage (Ledger Rollover Progress)

    **CRUD APIs used to manage ledger rollover progress.**
    """

    def get_ledgerRolloversProgresses(self, **kwargs):
        """Get list of rollovers progresses

        ``GET /finance-storage/ledger-rollovers-progress``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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

            .. literalinclude:: ../files/LedgerRolloverProgress_get_ledgerRolloversProgresses_return.schema 
        """
        return self.call("GET", "/finance-storage/ledger-rollovers-progress", query=kwargs)

    def set_ledgerRolloversProgress(self, ledgerRolloversProgress: dict):
        """Create a new ledgerRolloversProgress item.

        ``POST /finance-storage/ledger-rollovers-progress``

        Args:
            ledgerRolloversProgress (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created ledgerRolloversProgress item

        Schema:

            .. literalinclude:: ../files/LedgerRolloverProgress_set_ledgerRolloversProgress_request.schema
        """
        return self.call("POST", "/finance-storage/ledger-rollovers-progress", data=ledgerRolloversProgress)

    def get_ledgerRolloversProgress(self, ledgerRolloversProgressId: str):
        """Retrieve ledgerRolloversProgress item with given {ledgerRolloversProgressId}

        ``GET /finance-storage/ledger-rollovers-progress/{ledgerRolloversProgressId}``

        Args:
            ledgerRolloversProgressId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LedgerRolloverProgress_get_ledgerRolloversProgress_return.schema 
        """
        return self.call("GET", f"/finance-storage/ledger-rollovers-progress/{ledgerRolloversProgressId}")

    def delete_ledgerRolloversProgress(self, ledgerRolloversProgressId: str):
        """Delete ledgerRolloversProgress item with given {ledgerRolloversProgressId}

        ``DELETE /finance-storage/ledger-rollovers-progress/{ledgerRolloversProgressId}``

        Args:
            ledgerRolloversProgressId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance-storage/ledger-rollovers-progress/{ledgerRolloversProgressId}")

    def modify_ledgerRolloversProgress(self, ledgerRolloversProgressId: str, ledgerRolloversProgress: dict):
        """Update ledgerRolloversProgress item with given {ledgerRolloversProgressId}

        ``PUT /finance-storage/ledger-rollovers-progress/{ledgerRolloversProgressId}``

        Args:
            ledgerRolloversProgressId (str)
            ledgerRolloversProgress (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LedgerRolloverProgress_modify_ledgerRolloversProgress_request.schema
        """
        return self.call("PUT", f"/finance-storage/ledger-rollovers-progress/{ledgerRolloversProgressId}", data=ledgerRolloversProgress)


class LedgerRolloverLogs(FolioApi):
    """mod-finance-storage (Ledger Rollover Logs)

    **CRUD APIs used to manage ledger rollover logs.**
    """

    def get_ledgerRolloversLogs(self, **kwargs):
        """Get list of rollovers logs

        ``GET /finance-storage/ledger-rollovers-logs``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example 'ledgerRolloverType'
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["ledgerRolloverType", "Commit", "="]
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LedgerRolloverLogs_get_ledgerRolloversLogs_return.schema 
        """
        return self.call("GET", "/finance-storage/ledger-rollovers-logs", query=kwargs)

    def get_ledgerRolloversLog(self, ledgerRolloversLogsId: str):
        """Retrieve ledgerRolloversLog item with given {ledgerRolloversLogId}

        ``GET /finance-storage/ledger-rollovers-logs/{ledgerRolloversLogsId}``

        Args:
            ledgerRolloversLogsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LedgerRolloverLogs_get_ledgerRolloversLog_return.schema 
        """
        return self.call("GET", f"/finance-storage/ledger-rollovers-logs/{ledgerRolloversLogsId}")


class LedgerRolloverErrors(FolioApi):
    """mod-finance-storage (Ledger Rollover Error Report)

    **CRUD APIs used to manage ledger rollover errors.**
    """

    def get_ledgerRolloversErrors(self, **kwargs):
        """Get list of rollovers errors

        ``GET /finance-storage/ledger-rollovers-errors``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example 'errorType'
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["errorType", "Orders", "="]
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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

            .. literalinclude:: ../files/LedgerRolloverErrors_get_ledgerRolloversErrors_return.schema 
        """
        return self.call("GET", "/finance-storage/ledger-rollovers-errors", query=kwargs)

    def set_ledgerRolloversError(self, ledgerRolloversError: dict):
        """Create a new ledgerRolloversError item.

        ``POST /finance-storage/ledger-rollovers-errors``

        Args:
            ledgerRolloversError (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created ledgerRolloversError item

        Schema:

            .. literalinclude:: ../files/LedgerRolloverErrors_set_ledgerRolloversError_request.schema
        """
        return self.call("POST", "/finance-storage/ledger-rollovers-errors", data=ledgerRolloversError)

    def get_ledgerRolloversError(self, ledgerRolloversErrorsId: str):
        """Retrieve ledgerRolloversError item with given {ledgerRolloversErrorId}

        ``GET /finance-storage/ledger-rollovers-errors/{ledgerRolloversErrorsId}``

        Args:
            ledgerRolloversErrorsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LedgerRolloverErrors_get_ledgerRolloversError_return.schema 
        """
        return self.call("GET", f"/finance-storage/ledger-rollovers-errors/{ledgerRolloversErrorsId}")

    def delete_ledgerRolloversError(self, ledgerRolloversErrorsId: str):
        """Delete ledgerRolloversError item with given {ledgerRolloversErrorId}

        ``DELETE /finance-storage/ledger-rollovers-errors/{ledgerRolloversErrorsId}``

        Args:
            ledgerRolloversErrorsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance-storage/ledger-rollovers-errors/{ledgerRolloversErrorsId}")

    def modify_ledgerRolloversError(self, ledgerRolloversErrorsId: str, ledgerRolloversError: dict):
        """Update ledgerRolloversError item with given {ledgerRolloversErrorId}

        ``PUT /finance-storage/ledger-rollovers-errors/{ledgerRolloversErrorsId}``

        Args:
            ledgerRolloversErrorsId (str)
            ledgerRolloversError (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LedgerRolloverErrors_modify_ledgerRolloversError_request.schema
        """
        return self.call("PUT", f"/finance-storage/ledger-rollovers-errors/{ledgerRolloversErrorsId}", data=ledgerRolloversError)


class FundType(FolioApi):
    """mod-finance-storage (Funds)

    **CRUD APIs used to manage fund types.**
    """

    def get_fundTypes(self, **kwargs):
        """Get list of fund types

        ``GET /finance-storage/fund-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example name
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["name", "MEDGRANT", "="]
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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

            .. literalinclude:: ../files/FundType_get_fundTypes_return.schema 
        """
        return self.call("GET", "/finance-storage/fund-types", query=kwargs)

    def set_fundType(self, fundType: dict):
        """Create a new fundType item.

        ``POST /finance-storage/fund-types``

        Args:
            fundType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created fundType item

        Schema:

            .. literalinclude:: ../files/FundType_set_fundType_request.schema
        """
        return self.call("POST", "/finance-storage/fund-types", data=fundType)

    def get_fundType(self, fundTypesId: str):
        """Retrieve fundType item with given {fundTypeId}

        ``GET /finance-storage/fund-types/{fundTypesId}``

        Args:
            fundTypesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FundType_get_fundType_return.schema 
        """
        return self.call("GET", f"/finance-storage/fund-types/{fundTypesId}")

    def delete_fundType(self, fundTypesId: str):
        """Delete fundType item with given {fundTypeId}

        ``DELETE /finance-storage/fund-types/{fundTypesId}``

        Args:
            fundTypesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance-storage/fund-types/{fundTypesId}")

    def modify_fundType(self, fundTypesId: str, fundType: dict):
        """Update fundType item with given {fundTypeId}

        ``PUT /finance-storage/fund-types/{fundTypesId}``

        Args:
            fundTypesId (str)
            fundType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FundType_modify_fundType_request.schema
        """
        return self.call("PUT", f"/finance-storage/fund-types/{fundTypesId}", data=fundType)


class Ledger(FolioApi):
    """mod-finance-storage (Ledgers)

    **CRUD APIs used to manage ledgers.**
    """

    def get_ledgers(self, **kwargs):
        """Get list of ledgers

        ``GET /finance-storage/ledgers``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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

            .. literalinclude:: ../files/Ledger_get_ledgers_return.schema 
        """
        return self.call("GET", "/finance-storage/ledgers", query=kwargs)

    def set_ledger(self, ledger: dict):
        """Create a new ledger item.

        ``POST /finance-storage/ledgers``

        Args:
            ledger (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created ledger item

        Schema:

            .. literalinclude:: ../files/Ledger_set_ledger_request.schema
        """
        return self.call("POST", "/finance-storage/ledgers", data=ledger)

    def get_ledger(self, ledgersId: str):
        """Retrieve ledger item with given {ledgerId}

        ``GET /finance-storage/ledgers/{ledgersId}``

        Args:
            ledgersId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Ledger_get_ledger_return.schema 
        """
        return self.call("GET", f"/finance-storage/ledgers/{ledgersId}")

    def delete_ledger(self, ledgersId: str):
        """Delete ledger item with given {ledgerId}

        ``DELETE /finance-storage/ledgers/{ledgersId}``

        Args:
            ledgersId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance-storage/ledgers/{ledgersId}")

    def modify_ledger(self, ledgersId: str, ledger: dict):
        """Update ledger item with given {ledgerId}

        ``PUT /finance-storage/ledgers/{ledgersId}``

        Args:
            ledgersId (str)
            ledger (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Ledger_modify_ledger_request.schema
        """
        return self.call("PUT", f"/finance-storage/ledgers/{ledgersId}", data=ledger)


class FiscalYear(FolioApi):
    """mod-finance-storage (Fiscal Year)

    **CRUD APIs used to manage fiscal years.**
    """

    def get_fiscalYears(self, **kwargs):
        """Get list of fiscal years

        ``GET /finance-storage/fiscal-years``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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

            .. literalinclude:: ../files/FiscalYear_get_fiscalYears_return.schema 
        """
        return self.call("GET", "/finance-storage/fiscal-years", query=kwargs)

    def set_fiscalYear(self, fiscalYear: dict):
        """Create a new fiscalYear item.

        ``POST /finance-storage/fiscal-years``

        Args:
            fiscalYear (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created fiscalYear item

        Schema:

            .. literalinclude:: ../files/FiscalYear_set_fiscalYear_request.schema
        """
        return self.call("POST", "/finance-storage/fiscal-years", data=fiscalYear)

    def get_fiscalYear(self, fiscalYearsId: str):
        """Retrieve fiscalYear item with given {fiscalYearId}

        ``GET /finance-storage/fiscal-years/{fiscalYearsId}``

        Args:
            fiscalYearsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FiscalYear_get_fiscalYear_return.schema 
        """
        return self.call("GET", f"/finance-storage/fiscal-years/{fiscalYearsId}")

    def delete_fiscalYear(self, fiscalYearsId: str):
        """Delete fiscalYear item with given {fiscalYearId}

        ``DELETE /finance-storage/fiscal-years/{fiscalYearsId}``

        Args:
            fiscalYearsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance-storage/fiscal-years/{fiscalYearsId}")

    def modify_fiscalYear(self, fiscalYearsId: str, fiscalYear: dict):
        """Update fiscalYear item with given {fiscalYearId}

        ``PUT /finance-storage/fiscal-years/{fiscalYearsId}``

        Args:
            fiscalYearsId (str)
            fiscalYear (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FiscalYear_modify_fiscalYear_request.schema
        """
        return self.call("PUT", f"/finance-storage/fiscal-years/{fiscalYearsId}", data=fiscalYear)


class LedgerRollover(FolioApi):
    """mod-finance-storage (Ledger Rollover)

    **CRUD APIs used to manage ledger rollover.**
    """

    def get_ledgerRollovers(self, **kwargs):
        """Get list of rollovers

        ``GET /finance-storage/ledger-rollovers``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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

            .. literalinclude:: ../files/LedgerRollover_get_ledgerRollovers_return.schema 
        """
        return self.call("GET", "/finance-storage/ledger-rollovers", query=kwargs)

    def set_ledgerRollover(self, ledgerRollover: dict):
        """Create a new ledgerRollover item.

        ``POST /finance-storage/ledger-rollovers``

        Args:
            ledgerRollover (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created ledgerRollover item

        Schema:

            .. literalinclude:: ../files/LedgerRollover_set_ledgerRollover_request.schema
        """
        return self.call("POST", "/finance-storage/ledger-rollovers", data=ledgerRollover)

    def get_ledgerRollover(self, ledgerRolloversId: str):
        """Retrieve ledgerRollover item with given {ledgerRolloverId}

        ``GET /finance-storage/ledger-rollovers/{ledgerRolloversId}``

        Args:
            ledgerRolloversId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LedgerRollover_get_ledgerRollover_return.schema 
        """
        return self.call("GET", f"/finance-storage/ledger-rollovers/{ledgerRolloversId}")

    def delete_ledgerRollover(self, ledgerRolloversId: str):
        """Delete ledgerRollover item with given {ledgerRolloverId}

        ``DELETE /finance-storage/ledger-rollovers/{ledgerRolloversId}``

        Args:
            ledgerRolloversId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance-storage/ledger-rollovers/{ledgerRolloversId}")

    def modify_ledgerRollover(self, ledgerRolloversId: str, ledgerRollover: dict):
        """Update ledgerRollover item with given {ledgerRolloverId}

        ``PUT /finance-storage/ledger-rollovers/{ledgerRolloversId}``

        Args:
            ledgerRolloversId (str)
            ledgerRollover (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LedgerRollover_modify_ledgerRollover_request.schema
        """
        return self.call("PUT", f"/finance-storage/ledger-rollovers/{ledgerRolloversId}", data=ledgerRollover)


class Transaction(FolioApi):
    """mod-finance-storage (Transactions)

    **CRUD APIs used to manage transactions.**
    """

    def get_transactions(self, **kwargs):
        """Get list of transactions

        ``GET /finance-storage/transactions``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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

            .. literalinclude:: ../files/Transaction_get_transactions_return.schema 
        """
        return self.call("GET", "/finance-storage/transactions", query=kwargs)

    def set_transaction(self, transaction: dict):
        """Create a new transaction item.

        ``POST /finance-storage/transactions``

        Args:
            transaction (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created transaction item

        Schema:

            .. literalinclude:: ../files/Transaction_set_transaction_request.schema
        """
        return self.call("POST", "/finance-storage/transactions", data=transaction)

    def get_transaction(self, transactionsId: str):
        """Retrieve transaction item with given {transactionId}

        ``GET /finance-storage/transactions/{transactionsId}``

        Args:
            transactionsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Transaction_get_transaction_return.schema 
        """
        return self.call("GET", f"/finance-storage/transactions/{transactionsId}")

    def delete_transaction(self, transactionsId: str):
        """Delete transaction item with given {transactionId}

        ``DELETE /finance-storage/transactions/{transactionsId}``

        Args:
            transactionsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance-storage/transactions/{transactionsId}")

    def modify_transaction(self, transactionsId: str, transaction: dict):
        """Update transaction item with given {transactionId}

        ``PUT /finance-storage/transactions/{transactionsId}``

        Args:
            transactionsId (str)
            transaction (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Transaction_modify_transaction_request.schema
        """
        return self.call("PUT", f"/finance-storage/transactions/{transactionsId}", data=transaction)


class TransactionSummary(FolioApi):
    """mod-finance-storage (Transaction summaries)

    **CRUD APIs used to manage transaction summaries.**
    """

    def set_orderTransactionSummary(self, orderTransactionSummary: dict):
        """Create a new order transaction summary item.

        ``POST /finance-storage/order-transaction-summaries``

        Args:
            orderTransactionSummary (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created order transaction summary item

        Schema:

            .. literalinclude:: ../files/TransactionSummary_set_orderTransactionSummary_request.schema
        """
        return self.call("POST", "/finance-storage/order-transaction-summaries", data=orderTransactionSummary)

    def get_orderTransactionSummary(self, orderTransactionSummariesId: str):
        """Retrieve orderTransactionSummary item with given {orderTransactionSummaryId}

        ``GET /finance-storage/order-transaction-summaries/{orderTransactionSummariesId}``

        Args:
            orderTransactionSummariesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/TransactionSummary_get_orderTransactionSummary_return.schema 
        """
        return self.call("GET", f"/finance-storage/order-transaction-summaries/{orderTransactionSummariesId}")

    def delete_orderTransactionSummary(self, orderTransactionSummariesId: str):
        """Delete orderTransactionSummary item with given {orderTransactionSummaryId}

        ``DELETE /finance-storage/order-transaction-summaries/{orderTransactionSummariesId}``

        Args:
            orderTransactionSummariesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance-storage/order-transaction-summaries/{orderTransactionSummariesId}")

    def modify_orderTransactionSummary(self, orderTransactionSummariesId: str, orderTransactionSummary: dict):
        """Update orderTransactionSummary item with given {orderTransactionSummaryId}

        ``PUT /finance-storage/order-transaction-summaries/{orderTransactionSummariesId}``

        Args:
            orderTransactionSummariesId (str)
            orderTransactionSummary (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/TransactionSummary_modify_orderTransactionSummary_request.schema
        """
        return self.call("PUT", f"/finance-storage/order-transaction-summaries/{orderTransactionSummariesId}", data=orderTransactionSummary)

    def set_invoiceTransactionSummary(self, invoiceTransactionSummary: dict):
        """Create a new invoice transaction summary item.

        ``POST /finance-storage/invoice-transaction-summaries``

        Args:
            invoiceTransactionSummary (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created invoice transaction summary item

        Schema:

            .. literalinclude:: ../files/TransactionSummary_set_invoiceTransactionSummary_request.schema
        """
        return self.call("POST", "/finance-storage/invoice-transaction-summaries", data=invoiceTransactionSummary)

    def get_invoiceTransactionSummary(self, invoiceTransactionSummariesId: str):
        """Retrieve invoiceTransactionSummary item with given {invoiceTransactionSummaryId}

        ``GET /finance-storage/invoice-transaction-summaries/{invoiceTransactionSummariesId}``

        Args:
            invoiceTransactionSummariesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/TransactionSummary_get_invoiceTransactionSummary_return.schema 
        """
        return self.call("GET", f"/finance-storage/invoice-transaction-summaries/{invoiceTransactionSummariesId}")

    def delete_invoiceTransactionSummary(self, invoiceTransactionSummariesId: str):
        """Delete invoiceTransactionSummary item with given {invoiceTransactionSummaryId}

        ``DELETE /finance-storage/invoice-transaction-summaries/{invoiceTransactionSummariesId}``

        Args:
            invoiceTransactionSummariesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance-storage/invoice-transaction-summaries/{invoiceTransactionSummariesId}")

    def modify_invoiceTransactionSummary(self, invoiceTransactionSummariesId: str, invoiceTransactionSummary: dict):
        """Update invoiceTransactionSummary item with given {invoiceTransactionSummaryId}

        ``PUT /finance-storage/invoice-transaction-summaries/{invoiceTransactionSummariesId}``

        Args:
            invoiceTransactionSummariesId (str)
            invoiceTransactionSummary (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/TransactionSummary_modify_invoiceTransactionSummary_request.schema
        """
        return self.call("PUT", f"/finance-storage/invoice-transaction-summaries/{invoiceTransactionSummariesId}", data=invoiceTransactionSummary)


class Fund(FolioApi):
    """mod-finance-storage (Funds)

    **CRUD APIs used to manage funds.**
    """

    def get_funds(self, **kwargs):
        """Get list of funds

        ``GET /finance-storage/funds``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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

            .. literalinclude:: ../files/Fund_get_funds_return.schema 
        """
        return self.call("GET", "/finance-storage/funds", query=kwargs)

    def set_fund(self, fund: dict):
        """Create a new fund item.

        ``POST /finance-storage/funds``

        Args:
            fund (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created fund item

        Schema:

            .. literalinclude:: ../files/Fund_set_fund_request.schema
        """
        return self.call("POST", "/finance-storage/funds", data=fund)

    def get_fund(self, fundsId: str):
        """Retrieve fund item with given {fundId}

        ``GET /finance-storage/funds/{fundsId}``

        Args:
            fundsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Fund_get_fund_return.schema 
        """
        return self.call("GET", f"/finance-storage/funds/{fundsId}")

    def delete_fund(self, fundsId: str):
        """Delete fund item with given {fundId}

        ``DELETE /finance-storage/funds/{fundsId}``

        Args:
            fundsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance-storage/funds/{fundsId}")

    def modify_fund(self, fundsId: str, fund: dict):
        """Update fund item with given {fundId}

        ``PUT /finance-storage/funds/{fundsId}``

        Args:
            fundsId (str)
            fund (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Fund_modify_fund_request.schema
        """
        return self.call("PUT", f"/finance-storage/funds/{fundsId}", data=fund)


class BudgetExpenseClass(FolioApi):
    """mod-finance-storage (Budget expense classes)

    **CRUD APIs used to manage budget-expense-class records.**
    """

    def get_budgetExpenseClasses(self, **kwargs):
        """Get list of budget-expense-classes

        ``GET /finance-storage/budget-expense-classes``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: e.g.
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["name", "Electronic", "="]
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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

            .. literalinclude:: ../files/BudgetExpenseClass_get_budgetExpenseClasses_return.schema 
        """
        return self.call("GET", "/finance-storage/budget-expense-classes", query=kwargs)

    def set_budgetExpenseClass(self, budgetExpenseClass: dict):
        """Create a new budgetExpenseClass item.

        ``POST /finance-storage/budget-expense-classes``

        Args:
            budgetExpenseClass (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created budgetExpenseClass item

        Schema:

            .. literalinclude:: ../files/BudgetExpenseClass_set_budgetExpenseClass_request.schema
        """
        return self.call("POST", "/finance-storage/budget-expense-classes", data=budgetExpenseClass)

    def get_budgetExpenseClass(self, budgetExpenseClassesId: str):
        """Retrieve budgetExpenseClass item with given {budgetExpenseClassId}

        ``GET /finance-storage/budget-expense-classes/{budgetExpenseClassesId}``

        Args:
            budgetExpenseClassesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/BudgetExpenseClass_get_budgetExpenseClass_return.schema 
        """
        return self.call("GET", f"/finance-storage/budget-expense-classes/{budgetExpenseClassesId}")

    def delete_budgetExpenseClass(self, budgetExpenseClassesId: str):
        """Delete budgetExpenseClass item with given {budgetExpenseClassId}

        ``DELETE /finance-storage/budget-expense-classes/{budgetExpenseClassesId}``

        Args:
            budgetExpenseClassesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance-storage/budget-expense-classes/{budgetExpenseClassesId}")

    def modify_budgetExpenseClass(self, budgetExpenseClassesId: str, budgetExpenseClass: dict):
        """Update budgetExpenseClass item with given {budgetExpenseClassId}

        ``PUT /finance-storage/budget-expense-classes/{budgetExpenseClassesId}``

        Args:
            budgetExpenseClassesId (str)
            budgetExpenseClass (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/BudgetExpenseClass_modify_budgetExpenseClass_request.schema
        """
        return self.call("PUT", f"/finance-storage/budget-expense-classes/{budgetExpenseClassesId}", data=budgetExpenseClass)


class ExpenseClass(FolioApi):
    """mod-finance-storage (Expense classes)

    **CRUD APIs used to manage expense classes.**
    """

    def get_expenseClasses(self, **kwargs):
        """Get list of expense-classes

        ``GET /finance-storage/expense-classes``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: e.g.
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["name", "Electronic", "="]
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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

            .. literalinclude:: ../files/ExpenseClass_get_expenseClasses_return.schema 
        """
        return self.call("GET", "/finance-storage/expense-classes", query=kwargs)

    def set_expenseClass(self, expenseClass: dict):
        """Create a new expenseClass item.

        ``POST /finance-storage/expense-classes``

        Args:
            expenseClass (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created expenseClass item

        Schema:

            .. literalinclude:: ../files/ExpenseClass_set_expenseClass_request.schema
        """
        return self.call("POST", "/finance-storage/expense-classes", data=expenseClass)

    def get_expenseClass(self, expenseClassesId: str):
        """Retrieve expenseClass item with given {expenseClassId}

        ``GET /finance-storage/expense-classes/{expenseClassesId}``

        Args:
            expenseClassesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ExpenseClass_get_expenseClass_return.schema 
        """
        return self.call("GET", f"/finance-storage/expense-classes/{expenseClassesId}")

    def delete_expenseClass(self, expenseClassesId: str):
        """Delete expenseClass item with given {expenseClassId}

        ``DELETE /finance-storage/expense-classes/{expenseClassesId}``

        Args:
            expenseClassesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance-storage/expense-classes/{expenseClassesId}")

    def modify_expenseClass(self, expenseClassesId: str, expenseClass: dict):
        """Update expenseClass item with given {expenseClassId}

        ``PUT /finance-storage/expense-classes/{expenseClassesId}``

        Args:
            expenseClassesId (str)
            expenseClass (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ExpenseClass_modify_expenseClass_request.schema
        """
        return self.call("PUT", f"/finance-storage/expense-classes/{expenseClassesId}", data=expenseClass)


class LedgerRolloverBudgets(FolioApi):
    """mod-finance-storage (Ledger Rollover generated Budgets)

    **CRUD APIs used to manage ledger rollover budgets.**
    """

    def get_ledgerRolloversBudgets(self, **kwargs):
        """Get list of rollovers budgets

        ``GET /finance-storage/ledger-rollovers-budgets``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example 'budgetStatus'
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["budgetStatus", "Active", "="]
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LedgerRolloverBudgets_get_ledgerRolloversBudgets_return.schema 
        """
        return self.call("GET", "/finance-storage/ledger-rollovers-budgets", query=kwargs)

    def get_ledgerRolloversBudget(self, ledgerRolloversBudgetsId: str):
        """Retrieve ledgerRolloversBudget item with given {ledgerRolloversBudgetId}

        ``GET /finance-storage/ledger-rollovers-budgets/{ledgerRolloversBudgetsId}``

        Args:
            ledgerRolloversBudgetsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LedgerRolloverBudgets_get_ledgerRolloversBudget_return.schema 
        """
        return self.call("GET", f"/finance-storage/ledger-rollovers-budgets/{ledgerRolloversBudgetsId}")


class Budget(FolioApi):
    """mod-finance-storage (Budgets)

    **CRUD APIs used to manage budgets.**
    """

    def get_budgets(self, **kwargs):
        """Get list of budgets

        ``GET /finance-storage/budgets``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: e.g.
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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

            .. literalinclude:: ../files/Budget_get_budgets_return.schema 
        """
        return self.call("GET", "/finance-storage/budgets", query=kwargs)

    def set_budget(self, budget: dict):
        """Create a new budget item.

        ``POST /finance-storage/budgets``

        Args:
            budget (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created budget item

        Schema:

            .. literalinclude:: ../files/Budget_set_budget_request.schema
        """
        return self.call("POST", "/finance-storage/budgets", data=budget)

    def get_budget(self, budgetsId: str):
        """Retrieve budget item with given {budgetId}

        ``GET /finance-storage/budgets/{budgetsId}``

        Args:
            budgetsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Budget_get_budget_return.schema 
        """
        return self.call("GET", f"/finance-storage/budgets/{budgetsId}")

    def delete_budget(self, budgetsId: str):
        """Delete budget item with given {budgetId}

        ``DELETE /finance-storage/budgets/{budgetsId}``

        Args:
            budgetsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance-storage/budgets/{budgetsId}")

    def modify_budget(self, budgetsId: str, budget: dict):
        """Update budget item with given {budgetId}

        ``PUT /finance-storage/budgets/{budgetsId}``

        Args:
            budgetsId (str)
            budget (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Budget_modify_budget_request.schema
        """
        return self.call("PUT", f"/finance-storage/budgets/{budgetsId}", data=budget)


class GroupFundFy(FolioApi):
    """Group/fund/fiscal year records relations CRUD APIs

    **CRUD APIs used to manage group/fund/fiscal year records relations**
    """

    def get_groupFundFiscalYears(self, **kwargs):
        """Get list of group/fund/fiscal year records relations

        ``GET /finance-storage/group-fund-fiscal-years``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: e.g.
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - group.name == History and and fund.fundStatus == Active and fiscalYear.periodEnd < 2020-01-01 and fundType.name == Monographs and ledger.name == One-time
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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

            .. literalinclude:: ../files/GroupFundFy_get_groupFundFiscalYears_return.schema 
        """
        return self.call("GET", "/finance-storage/group-fund-fiscal-years", query=kwargs)

    def set_groupFundFiscalYear(self, groupFundFiscalYear: dict):
        """Create a new groupFundFiscalYear item.

        ``POST /finance-storage/group-fund-fiscal-years``

        Args:
            groupFundFiscalYear (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created groupFundFiscalYear item

        Schema:

            .. literalinclude:: ../files/GroupFundFy_set_groupFundFiscalYear_request.schema
        """
        return self.call("POST", "/finance-storage/group-fund-fiscal-years", data=groupFundFiscalYear)

    def get_groupFundFiscalYear(self, groupFundFiscalYearsId: str):
        """Retrieve groupFundFiscalYear item with given {groupFundFiscalYearId}

        ``GET /finance-storage/group-fund-fiscal-years/{groupFundFiscalYearsId}``

        Args:
            groupFundFiscalYearsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/GroupFundFy_get_groupFundFiscalYear_return.schema 
        """
        return self.call("GET", f"/finance-storage/group-fund-fiscal-years/{groupFundFiscalYearsId}")

    def delete_groupFundFiscalYear(self, groupFundFiscalYearsId: str):
        """Delete groupFundFiscalYear item with given {groupFundFiscalYearId}

        ``DELETE /finance-storage/group-fund-fiscal-years/{groupFundFiscalYearsId}``

        Args:
            groupFundFiscalYearsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance-storage/group-fund-fiscal-years/{groupFundFiscalYearsId}")

    def modify_groupFundFiscalYear(self, groupFundFiscalYearsId: str, groupFundFiscalYear: dict):
        """Update groupFundFiscalYear item with given {groupFundFiscalYearId}

        ``PUT /finance-storage/group-fund-fiscal-years/{groupFundFiscalYearsId}``

        Args:
            groupFundFiscalYearsId (str)
            groupFundFiscalYear (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/GroupFundFy_modify_groupFundFiscalYear_request.schema
        """
        return self.call("PUT", f"/finance-storage/group-fund-fiscal-years/{groupFundFiscalYearsId}", data=groupFundFiscalYear)


class GroupBudgets(FolioApi):
    """Budgets

    **Get list of Budgets API.**
    """

    def get_groupBudgets(self, **kwargs):
        """Get list of budgets

        ``GET /finance-storage/group-budgets``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example code
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ["code", "MEDGRANT", "="]
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/GroupBudgets_get_groupBudgets_return.schema 
        """
        return self.call("GET", "/finance-storage/group-budgets", query=kwargs)


class Group(FolioApi):
    """Group CRUD APIs

    **CRUD APIs used to manage groups**
    """

    def get_groups(self, **kwargs):
        """Get list of groups

        ``GET /finance-storage/groups``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: e.g.
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - status==Active sortBy name
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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

            .. literalinclude:: ../files/Group_get_groups_return.schema 
        """
        return self.call("GET", "/finance-storage/groups", query=kwargs)

    def set_group(self, group: dict):
        """Create a new group item.

        ``POST /finance-storage/groups``

        Args:
            group (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created group item

        Schema:

            .. literalinclude:: ../files/Group_set_group_request.schema
        """
        return self.call("POST", "/finance-storage/groups", data=group)

    def get_group(self, groupsId: str):
        """Retrieve group item with given {groupId}

        ``GET /finance-storage/groups/{groupsId}``

        Args:
            groupsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Group_get_group_return.schema 
        """
        return self.call("GET", f"/finance-storage/groups/{groupsId}")

    def delete_group(self, groupsId: str):
        """Delete group item with given {groupId}

        ``DELETE /finance-storage/groups/{groupsId}``

        Args:
            groupsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finance-storage/groups/{groupsId}")

    def modify_group(self, groupsId: str, group: dict):
        """Update group item with given {groupId}

        ``PUT /finance-storage/groups/{groupsId}``

        Args:
            groupsId (str)
            group (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Group_modify_group_request.schema
        """
        return self.call("PUT", f"/finance-storage/groups/{groupsId}", data=group)
