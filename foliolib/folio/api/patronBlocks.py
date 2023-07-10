# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.patronBlocks")


class PatronBlockLimits(FolioApi):
    """mod-users Patron Block Limits API

    This documents the API calls that can be made to query and manage patron block limits
    """

    def get_patronBlockLimits(self, **kwargs):
        """Return a list of patron block limits

        ``GET /patron-block-limits``

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
                    
                    searchable using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name="undergrad*"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PatronBlockLimits_get_patronBlockLimits_return.schema 
        """
        return self.call("GET", "/patron-block-limits", query=kwargs)

    def set_patronBlockLimit(self, patronBlockLimit: dict):
        """Create a patron block limit

        ``POST /patron-block-limits``

        Args:
            patronBlockLimit (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created patronBlockLimit item

        Schema:

            .. literalinclude:: ../files/PatronBlockLimits_set_patronBlockLimit_request.schema
        """
        return self.call("POST", "/patron-block-limits", data=patronBlockLimit)

    def get_patronBlockLimit(self, patronBlockLimitId: str):
        """Retrieve patronBlockLimit item with given {patronBlockLimitId}

        ``GET /patron-block-limits/{patronBlockLimitId}``

        Args:
            patronBlockLimitId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PatronBlockLimits_get_patronBlockLimit_return.schema 
        """
        return self.call("GET", f"/patron-block-limits/{patronBlockLimitId}")

    def delete_patronBlockLimit(self, patronBlockLimitId: str):
        """Delete patronBlockLimit item with given {patronBlockLimitId}

        ``DELETE /patron-block-limits/{patronBlockLimitId}``

        Args:
            patronBlockLimitId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/patron-block-limits/{patronBlockLimitId}")

    def modify_patronBlockLimit(self, patronBlockLimitId: str, patronBlockLimit: dict):
        """Update a patron block limit

        ``PUT /patron-block-limits/{patronBlockLimitId}``

        Args:
            patronBlockLimitId (str)
            patronBlockLimit (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/PatronBlockLimits_modify_patronBlockLimit_request.schema
        """
        return self.call("PUT", f"/patron-block-limits/{patronBlockLimitId}", data=patronBlockLimit)


class AutomatedPatronBlocks(FolioApi):
    """API for checking if any automated patron blocks exist for patron

    **Automated patron blocks API**
    """

    def get_automatedPatronBlock(self, userId: str):
        """

        ``GET /automated-patron-blocks/{userId}``

        Args:
            userId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AutomatedPatronBlocks_get_automatedPatronBlock_return.schema 
        """
        return self.call("GET", f"/automated-patron-blocks/{userId}")

    def set_job(self, job: dict):
        """

        ``POST /automated-patron-blocks/synchronization/job``

        Args:
            job (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AutomatedPatronBlocks_set_job_request.schema
        """
        return self.call("POST", "/automated-patron-blocks/synchronization/job", data=job)

    def get_job(self, syncJobId: str):
        """Checks synchronization status of job

        ``GET /automated-patron-blocks/synchronization/job/{syncJobId}``

        Args:
            syncJobId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AutomatedPatronBlocks_get_job_return.schema 
        """
        return self.call("GET", f"/automated-patron-blocks/synchronization/job/{syncJobId}")

    def set_start(self):
        """

        ``POST /automated-patron-blocks/synchronization/start``

        Raises:
            OkapiFatalError: Server Error
        """
        return self.call("POST", "/automated-patron-blocks/synchronization/start")


class UserSummary(FolioApi):
    """Diagnostic API for retreiving internal UserSummary objects

    **User summary API**
    """

    def get_userSummary(self, userId: str):
        """

        ``GET /user-summary/{userId}``

        Args:
            userId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/UserSummary_get_userSummary_return.schema 
        """
        return self.call("GET", f"/user-summary/{userId}")


class PatronBlockConditions(FolioApi):
    """mod-users Patron Block Conditions API

    Query and manage each condition that can trigger a patron block and the messages that should be displayed when triggered.
    """

    def get_patronBlockConditions(self, **kwargs):
        """Return a list of patron block conditions

        ``GET /patron-block-conditions``

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
                    
                    searchable using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name="undergrad*"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PatronBlockConditions_get_patronBlockConditions_return.schema 
        """
        return self.call("GET", "/patron-block-conditions", query=kwargs)

    def get_patronBlockCondition(self, patronBlockConditionId: str):
        """Retrieve patronBlockCondition item with given {patronBlockConditionId}

        ``GET /patron-block-conditions/{patronBlockConditionId}``

        Args:
            patronBlockConditionId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PatronBlockConditions_get_patronBlockCondition_return.schema 
        """
        return self.call("GET", f"/patron-block-conditions/{patronBlockConditionId}")

    def modify_patronBlockCondition(self, patronBlockConditionId: str):
        """

        ``PUT /patron-block-conditions/{patronBlockConditionId}``

        Args:
            patronBlockConditionId (str)
        """
        return self.call("PUT", f"/patron-block-conditions/{patronBlockConditionId}")


class EventHandlers(FolioApi):
    """Event handlers API

    **API for consuming events**
    """

    def set_feeFineBalanceChanged(self, feeFineBalanceChanged: dict):
        """

        ``POST /automated-patron-blocks/handlers/fee-fine-balance-changed``

        Args:
            feeFineBalanceChanged (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/EventHandlers_set_feeFineBalanceChanged_request.schema
        """
        return self.call("POST", "/automated-patron-blocks/handlers/fee-fine-balance-changed", data=feeFineBalanceChanged)

    def set_itemCheckedOut(self, itemCheckedOut: dict):
        """

        ``POST /automated-patron-blocks/handlers/item-checked-out``

        Args:
            itemCheckedOut (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/EventHandlers_set_itemCheckedOut_request.schema
        """
        return self.call("POST", "/automated-patron-blocks/handlers/item-checked-out", data=itemCheckedOut)

    def set_itemCheckedIn(self, itemCheckedIn: dict):
        """

        ``POST /automated-patron-blocks/handlers/item-checked-in``

        Args:
            itemCheckedIn (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/EventHandlers_set_itemCheckedIn_request.schema
        """
        return self.call("POST", "/automated-patron-blocks/handlers/item-checked-in", data=itemCheckedIn)

    def set_itemDeclaredLost(self, itemDeclaredLost: dict):
        """

        ``POST /automated-patron-blocks/handlers/item-declared-lost``

        Args:
            itemDeclaredLost (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/EventHandlers_set_itemDeclaredLost_request.schema
        """
        return self.call("POST", "/automated-patron-blocks/handlers/item-declared-lost", data=itemDeclaredLost)

    def set_itemAgedToLost(self, itemAgedToLost: dict):
        """

        ``POST /automated-patron-blocks/handlers/item-aged-to-lost``

        Args:
            itemAgedToLost (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/EventHandlers_set_itemAgedToLost_request.schema
        """
        return self.call("POST", "/automated-patron-blocks/handlers/item-aged-to-lost", data=itemAgedToLost)

    def set_itemClaimedReturned(self, itemClaimedReturned: dict):
        """

        ``POST /automated-patron-blocks/handlers/item-claimed-returned``

        Args:
            itemClaimedReturned (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/EventHandlers_set_itemClaimedReturned_request.schema
        """
        return self.call("POST", "/automated-patron-blocks/handlers/item-claimed-returned", data=itemClaimedReturned)

    def set_loanDueDateChanged(self, loanDueDateChanged: dict):
        """

        ``POST /automated-patron-blocks/handlers/loan-due-date-changed``

        Args:
            loanDueDateChanged (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/EventHandlers_set_loanDueDateChanged_request.schema
        """
        return self.call("POST", "/automated-patron-blocks/handlers/loan-due-date-changed", data=loanDueDateChanged)

    def set_loanClosed(self, loanClosed: dict):
        """

        ``POST /automated-patron-blocks/handlers/loan-closed``

        Args:
            loanClosed (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/EventHandlers_set_loanClosed_request.schema
        """
        return self.call("POST", "/automated-patron-blocks/handlers/loan-closed", data=loanClosed)
