# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.circulation")


class PickSlips(FolioApi):
    """API for fetching current pick slips

    **API for pick slips generation**
    """

    def get_pickSlips(self, servicePointId: str):
        """Retrieve pickSlip item with given {pickSlipId}

        ``GET /circulation/pick-slips/{servicePointId}``

        Args:
            servicePointId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PickSlips_get_pickSlips_return.schema 
        """
        return self.call("GET", f"/circulation/pick-slips/{servicePointId}")


class RequestsReports(FolioApi):
    """Circulation Business Logic API

    **API for report generation**
    """

    def get_holdShelfClearances(self, servicePointId: str):
        """Retrieve holdShelfClearance item with given {holdShelfClearanceId}

        ``GET /circulation/requests-reports/hold-shelf-clearance/{servicePointId}``

        Args:
            servicePointId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/RequestsReports_get_holdShelfClearances_return.schema 
        """
        return self.call("GET", f"/circulation/requests-reports/hold-shelf-clearance/{servicePointId}")


class EndPatronActionSession(FolioApi):
    """End Patron Action Session API

    **End patron action session**
    """

    def set_endPatronActionSession(self, endPatronActionSession: dict):
        """

        ``POST /circulation/end-patron-action-session``

        Args:
            endPatronActionSession (dict): See Schema below

        Raises:
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/EndPatronActionSession_set_endPatronActionSession_request.schema
        """
        return self.call("POST", "/circulation/end-patron-action-session", data=endPatronActionSession)


class LoanAnonymization(FolioApi):
    """Loan Anonymization API

    **Loan Anonymization API**
    """

    def set_byUser(self, userId: str):
        """Note that a 422 error with haveAssociatedFeesAndFines message and key loanIds has a value that is not a JSON array but a JSON string that contains a serialized JSON array of the loan ids.

        ``POST /loan-anonymization/by-user/{userId}``

        Args:
            userId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/LoanAnonymization_set_byUser_return.schema 
        """
        return self.call("POST", f"/loan-anonymization/by-user/{userId}")


class AgeToLostBackgroundProcesses(FolioApi):
    """Background processes for ageing borrowed items to lost

    **Background processes for ageing borrowed items to lost**
    """

    def set_scheduledAgeToLost(self):
        """

        ``POST /circulation/scheduled-age-to-lost``

        Raises:
            OkapiFatalError: Server Error
        """
        return self.call("POST", "/circulation/scheduled-age-to-lost")

    def set_scheduledAgeToLostFeeCharging(self):
        """

        ``POST /circulation/scheduled-age-to-lost-fee-charging``

        Raises:
            OkapiFatalError: Server Error
        """
        return self.call("POST", "/circulation/scheduled-age-to-lost-fee-charging")


class AddInfo(FolioApi):
    """API for adding patron or staff info

    **Add info API**
    """

    def set_addInfo(self, loansId: str, addInfo: dict):
        """

        ``POST /circulation/loans/{loansId}/add-info``

        Args:
            loansId (str)
            addInfo (dict): See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AddInfo_set_addInfo_request.schema
        """
        return self.call("POST", f"/circulation/loans/{loansId}/add-info", data=addInfo)


class DeclareItemLost(FolioApi):
    """API for declaring loaned item lost

    **Declare item lost API**
    """

    def set_declareItemLost(self, loansId: str, declareItemLost: dict):
        """

        ``POST /circulation/loans/{loansId}/declare-item-lost``

        Args:
            loansId (str)
            declareItemLost (dict): See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DeclareItemLost_set_declareItemLost_request.schema
        """
        return self.call("POST", f"/circulation/loans/{loansId}/declare-item-lost", data=declareItemLost)


class ChangeDueDate(FolioApi):
    """API for changing due date for loans

    **Change loan due date API**
    """

    def set_changeDueDate(self, loansId: str, changeDueDate: dict):
        """

        ``POST /circulation/loans/{loansId}/change-due-date``

        Args:
            loansId (str)
            changeDueDate (dict): See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/ChangeDueDate_set_changeDueDate_request.schema
        """
        return self.call("POST", f"/circulation/loans/{loansId}/change-due-date", data=changeDueDate)


class Circulation(FolioApi):
    """Circulation Business Logic API

    **API for loans and requests**
    """

    def set_checkOutByBarcode(self, checkOutByBarcode: dict, **kwargs):
        """Creates a loan by checking out an item to a loanee

        ``POST /circulation/check-out-by-barcode``

        Args:
            checkOutByBarcode (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Circulation_set_checkOutByBarcode_request.schema
            .. literalinclude:: ../files/Circulation_set_checkOutByBarcode_return.schema 
        """
        return self.call("POST", "/circulation/check-out-by-barcode", data=checkOutByBarcode, query=kwargs)

    def set_renewByBarcode(self, renewByBarcode: dict, **kwargs):
        """Updates the due date of an existing loan

        ``POST /circulation/renew-by-barcode``

        Args:
            renewByBarcode (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Circulation_set_renewByBarcode_request.schema
            .. literalinclude:: ../files/Circulation_set_renewByBarcode_return.schema 
        """
        return self.call("POST", "/circulation/renew-by-barcode", data=renewByBarcode, query=kwargs)

    def set_renewById(self, renewById: dict, **kwargs):
        """Updates the due date of an existing loan

        ``POST /circulation/renew-by-id``

        Args:
            renewById (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Circulation_set_renewById_request.schema
            .. literalinclude:: ../files/Circulation_set_renewById_return.schema 
        """
        return self.call("POST", "/circulation/renew-by-id", data=renewById, query=kwargs)

    def set_checkInByBarcode(self, checkInByBarcode: dict, **kwargs):
        """Updates the status of an existing loan

        ``POST /circulation/check-in-by-barcode``

        Args:
            checkInByBarcode (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Circulation_set_checkInByBarcode_request.schema
            .. literalinclude:: ../files/Circulation_set_checkInByBarcode_return.schema 
        """
        return self.call("POST", "/circulation/check-in-by-barcode", data=checkInByBarcode, query=kwargs)

    def get_loans(self, **kwargs):
        """Retrieve a list of loan items.

        ``GET /circulation/loans``

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
                    
                    by title (using CQL)
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - userId="cf23adf0-61ba-4887-bf82-956c4aae2260"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Circulation_get_loans_return.schema 
        """
        return self.call("GET", "/circulation/loans", query=kwargs)

    def set_loan(self, loan: dict):
        """Create a new loan item.

        ``POST /circulation/loans``

        Args:
            loan (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created loan item

        Schema:

            .. literalinclude:: ../files/Circulation_set_loan_request.schema
        """
        return self.call("POST", "/circulation/loans", data=loan)

    def delete_loans(self):
        """

        ``DELETE /circulation/loans``
        """
        return self.call("DELETE", "/circulation/loans")

    def get_loan(self, loanId: str):
        """Retrieve loan item with given {loanId}

        ``GET /circulation/loans/{loanId}``

        Args:
            loanId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Circulation_get_loan_return.schema 
        """
        return self.call("GET", f"/circulation/loans/{loanId}")

    def delete_loan(self, loanId: str):
        """Delete loan item with given {loanId}

        ``DELETE /circulation/loans/{loanId}``

        Args:
            loanId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/circulation/loans/{loanId}")

    def modify_loan(self, loanId: str, loan: dict):
        """Update loan item with given {loanId}

        ``PUT /circulation/loans/{loanId}``

        Args:
            loanId (str)
            loan (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Circulation_modify_loan_request.schema
        """
        return self.call("PUT", f"/circulation/loans/{loanId}", data=loan)

    def get_requests(self, **kwargs):
        """Retrieve a list of request items.

        ``GET /circulation/requests``

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
                    
                    by using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - requesterId="cf23adf0-61ba-4887-bf82-956c4aae2260"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Circulation_get_requests_return.schema 
        """
        return self.call("GET", "/circulation/requests", query=kwargs)

    def set_request(self, request: dict):
        """Create a new request item.

        ``POST /circulation/requests``

        Args:
            request (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created request item

        Schema:

            .. literalinclude:: ../files/Circulation_set_request_request.schema
        """
        return self.call("POST", "/circulation/requests", data=request)

    def delete_requests(self):
        """

        ``DELETE /circulation/requests``
        """
        return self.call("DELETE", "/circulation/requests")

    def get_request(self, requestId: str):
        """Retrieve request item with given {requestId}

        ``GET /circulation/requests/{requestId}``

        Args:
            requestId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Circulation_get_request_return.schema 
        """
        return self.call("GET", f"/circulation/requests/{requestId}")

    def delete_request(self, requestId: str):
        """Delete request item with given {requestId}

        ``DELETE /circulation/requests/{requestId}``

        Args:
            requestId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/circulation/requests/{requestId}")

    def modify_request(self, requestId: str, request: dict):
        """Update request item with given {requestId}

        ``PUT /circulation/requests/{requestId}``

        Args:
            requestId (str)
            request (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Circulation_modify_request_request.schema
        """
        return self.call("PUT", f"/circulation/requests/{requestId}", data=request)

    def get_instances(self, instanceId: str):
        """Retrieve instance item with given {instanceId}

        ``GET /circulation/requests/queue/instance/{instanceId}``

        Args:
            instanceId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Circulation_get_instances_return.schema 
        """
        return self.call("GET", f"/circulation/requests/queue/instance/{instanceId}")

    def get_items(self, itemId: str):
        """Retrieve item item with given {itemId}

        ``GET /circulation/requests/queue/item/{itemId}``

        Args:
            itemId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Circulation_get_items_return.schema 
        """
        return self.call("GET", f"/circulation/requests/queue/item/{itemId}")

    def set_reorder_for_instance(self, instanceId: str, reorder: dict):
        """Reorder requests in the instance queue

        ``POST /circulation/requests/queue/instance/{instanceId}/reorder``

        Args:
            instanceId (str)
            reorder (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Circulation_set_reorder_for_instance_request.schema
            .. literalinclude:: ../files/Circulation_set_reorder_for_instance_return.schema 
        """
        return self.call("POST", f"/circulation/requests/queue/instance/{instanceId}/reorder", data=reorder)

    def set_reorder(self, itemId: str, reorder: dict):
        """Reorder requests in the item queue

        ``POST /circulation/requests/queue/item/{itemId}/reorder``

        Args:
            itemId (str)
            reorder (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Circulation_set_reorder_request.schema
            .. literalinclude:: ../files/Circulation_set_reorder_return.schema 
        """
        return self.call("POST", f"/circulation/requests/queue/item/{itemId}/reorder", data=reorder)

    def set_instance(self, instance: dict, **kwargs):
        """Creates a request for any item from the given instance ID

        ``POST /circulation/requests/instances``

        Args:
            instance (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Circulation_set_instance_request.schema
            .. literalinclude:: ../files/Circulation_set_instance_return.schema 
        """
        return self.call("POST", "/circulation/requests/instances", data=instance, query=kwargs)


class InventoryReports(FolioApi):
    """Circulation Business Logic API

    **API for report generation**
    """

    def get_itemsInTransits(self):
        """Retrieve itemsInTransit item with given {itemsInTransitId}

        ``GET /inventory-reports/items-in-transit``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InventoryReports_get_itemsInTransits_return.schema 
        """
        return self.call("GET", "/inventory-reports/items-in-transit")


class CirculationRules(FolioApi):
    """Circulation Rules API

    **API for circulation Rules**
    """

    def get_rules(self):
        """Get the circulation rules

        ``GET /circulation/rules``

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CirculationRules_get_rules_return.schema 
        """
        return self.call("GET", "/circulation/rules")

    def modify_rule(self, rule: dict):
        """Set the circulation rules using a text file

        ``PUT /circulation/rules``

        Args:
            rule (dict): See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CirculationRules_modify_rule_request.schema
        """
        return self.call("PUT", "/circulation/rules", data=rule)

    def get_loanPolicies(self, **kwargs):
        """Execute circulation rules and return the loan policy that will be applied, either the matching loan policy with the highest priority or the fallback loan policy

        ``GET /circulation/rules/loan-policy``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            item_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Item type id
            loan_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Loan type id
            patron_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Patron type id
            location_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Location id

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CirculationRules_get_loanPolicies_return.schema 
        """
        return self.call("GET", "/circulation/rules/loan-policy", query=kwargs)

    def get_loanPolicyAlls(self, **kwargs):
        """Execute circulation rules and return all matching loan policies in decreasing priority and the fallback loan policy

        ``GET /circulation/rules/loan-policy-all``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            item_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Item type id
            loan_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Loan type id
            patron_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Patron type id
            location_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Location id
            rules ():  Circulation rules if provided, otherwise use stored circulation rules

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CirculationRules_get_loanPolicyAlls_return.schema 
        """
        return self.call("GET", "/circulation/rules/loan-policy-all", query=kwargs)

    def get_overdueFinePolicies(self, **kwargs):
        """Execute circulation rules and return the overdue fine policy that will be applied, either the matching overdue fine policy with the highest priority or the fallback overdue fine policy policy

        ``GET /circulation/rules/overdue-fine-policy``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            item_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Item type id
            loan_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Loan type id
            patron_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Patron type id
            location_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Location id

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CirculationRules_get_overdueFinePolicies_return.schema 
        """
        return self.call("GET", "/circulation/rules/overdue-fine-policy", query=kwargs)

    def get_overdueFinePolicyAlls(self, **kwargs):
        """Execute circulation rules and return all matching overdue fine policies in decreasing priority and the fallback overdue fine policy

        ``GET /circulation/rules/overdue-fine-policy-all``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            item_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Item type id
            loan_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Loan type id
            patron_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Patron type id
            location_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Location id
            rules ():  Circulation rules if provided, otherwise use stored circulation rules

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CirculationRules_get_overdueFinePolicyAlls_return.schema 
        """
        return self.call("GET", "/circulation/rules/overdue-fine-policy-all", query=kwargs)

    def get_lostItemPolicies(self, **kwargs):
        """Execute circulation rules and return the lost item policy that will be applied, either the matching lost item policy with the highest priority or the fallback lost item policy policy

        ``GET /circulation/rules/lost-item-policy``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            item_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Item type id
            loan_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Loan type id
            patron_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Patron type id
            location_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Location id

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CirculationRules_get_lostItemPolicies_return.schema 
        """
        return self.call("GET", "/circulation/rules/lost-item-policy", query=kwargs)

    def get_lostItemPolicyAlls(self, **kwargs):
        """Execute circulation rules and return all matching lost item policies in decreasing priority and the fallback lost item policy

        ``GET /circulation/rules/lost-item-policy-all``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            item_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Item type id
            loan_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Loan type id
            patron_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Patron type id
            location_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Location id
            rules ():  Circulation rules if provided, otherwise use stored circulation rules

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CirculationRules_get_lostItemPolicyAlls_return.schema 
        """
        return self.call("GET", "/circulation/rules/lost-item-policy-all", query=kwargs)

    def get_requestPolicies(self, **kwargs):
        """Execute circulation rules and return the request policy that will be applied, either the matching request policy with the highest priority or the fallback request policy

        ``GET /circulation/rules/request-policy``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            item_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Item type id
            loan_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Loan type id
            patron_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Patron type id
            location_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Location id

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CirculationRules_get_requestPolicies_return.schema 
        """
        return self.call("GET", "/circulation/rules/request-policy", query=kwargs)

    def get_requestPolicyAlls(self, **kwargs):
        """Execute circulation rules and return all matching request policies policies in decreasing priority and the fallback request policy

        ``GET /circulation/rules/request-policy-all``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            item_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Item type id
            loan_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Loan type id
            patron_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Patron type id
            location_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Location id
            rules ():  Circulation rules if provided, otherwise use stored circulation rules

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CirculationRules_get_requestPolicyAlls_return.schema 
        """
        return self.call("GET", "/circulation/rules/request-policy-all", query=kwargs)

    def get_noticePolicies(self, **kwargs):
        """Get the notice policy when applying circulation rules

        ``GET /circulation/rules/notice-policy``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            item_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Item type id
            loan_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Loan type id
            patron_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Patron type id
            location_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Location id

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CirculationRules_get_noticePolicies_return.schema 
        """
        return self.call("GET", "/circulation/rules/notice-policy", query=kwargs)

    def get_noticePolicyAlls(self, **kwargs):
        """Get notice policy for each match when applying circulation rules

        ``GET /circulation/rules/notice-policy-all``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            item_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Item type id
            loan_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Loan type id
            patron_type_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Patron type id
            location_id (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  Location id
            rules ():  Circulation rules if provided, otherwise use stored circulation rules

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CirculationRules_get_noticePolicyAlls_return.schema 
        """
        return self.call("GET", "/circulation/rules/notice-policy-all", query=kwargs)


class RequestMove(FolioApi):
    """Circulation Business Logic API

    **API for moving request from one Item to another**
    """

    def set_move(self, requestId: str, move: dict):
        """Move Request to specified Item

        ``POST /circulation/requests/{requestId}/move``

        Args:
            requestId (str)
            move (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/RequestMove_set_move_request.schema
            .. literalinclude:: ../files/RequestMove_set_move_return.schema 
        """
        return self.call("POST", f"/circulation/requests/{requestId}/move", data=move)


class ClaimItemReturned(FolioApi):
    """API for declaring loaned item as claimed returned

    **Claim item returned API**
    """

    def set_claimItemReturned(self, loansId: str, claimItemReturned: dict):
        """

        ``POST /circulation/loans/{loansId}/claim-item-returned``

        Args:
            loansId (str)
            claimItemReturned (dict): See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/ClaimItemReturned_set_claimItemReturned_request.schema
        """
        return self.call("POST", f"/circulation/loans/{loansId}/claim-item-returned", data=claimItemReturned)

    def set_declareClaimedReturnedItemAsMissing(self, loansId: str, declareClaimedReturnedItemAsMissing: dict):
        """

        ``POST /circulation/loans/{loansId}/declare-claimed-returned-item-as-missing``

        Args:
            loansId (str)
            declareClaimedReturnedItemAsMissing (dict): See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/ClaimItemReturned_set_declareClaimedReturnedItemAsMissing_request.schema
        """
        return self.call("POST", f"/circulation/loans/{loansId}/declare-claimed-returned-item-as-missing", data=declareClaimedReturnedItemAsMissing)


class CirculationEventHandlers(FolioApi):
    """Circulation Event Handlers Endpoints

    **API to handle events**
    """

    def set_loanRelatedFeeFineClosed(self, loanRelatedFeeFineClosed: dict):
        """Handle fee/fine record with loan closed event

        ``POST /circulation/handlers/loan-related-fee-fine-closed``

        Args:
            loanRelatedFeeFineClosed (dict): See Schema below

        Schema:

            .. literalinclude:: ../files/CirculationEventHandlers_set_loanRelatedFeeFineClosed_request.schema
        """
        return self.call("POST", "/circulation/handlers/loan-related-fee-fine-closed", data=loanRelatedFeeFineClosed)
