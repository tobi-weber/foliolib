# -*- coding: utf-8 -*-
# Generated at 2024-03-23

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.organizations")


class Organizations(FolioApi):
    """Organizations Business Logic API

    **API for managing organizations**
    """

    def get_organizations(self, **kwargs):
        """Get list of organizations

        ``GET /organizations/organizations``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    using CQL (indexes for organization)
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - status=="Active"
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
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Organizations_get_organizations_return.schema 
        """
        return self.call("GET", "/organizations/organizations", query=kwargs)

    def set_organization(self, organization: dict):
        """Post an organization

        ``POST /organizations/organizations``

        Args:
            organization (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestFatalError: Server Error

        Headers:
            - **Location** - URI to the created organization item

        Schema:

            .. literalinclude:: ../files/Organizations_set_organization_request.schema
        """
        return self.call("POST", "/organizations/organizations", data=organization)

    def get_organization(self, organizationsId: str):
        """Retrieve organization item with given {organizationId}

        ``GET /organizations/organizations/{organizationsId}``

        Args:
            organizationsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Organizations_get_organization_return.schema 
        """
        return self.call("GET", f"/organizations/organizations/{organizationsId}")

    def delete_organization(self, organizationsId: str):
        """Delete organization item with given {organizationId}

        ``DELETE /organizations/organizations/{organizationsId}``

        Args:
            organizationsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestFatalError: Server Error
        """
        return self.call("DELETE", f"/organizations/organizations/{organizationsId}")

    def modify_organization(self, organizationsId: str, organization: dict):
        """Update an organization with id

        ``PUT /organizations/organizations/{organizationsId}``

        Args:
            organizationsId (str)
            organization (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Organizations_modify_organization_request.schema
        """
        return self.call("PUT", f"/organizations/organizations/{organizationsId}", data=organization)


class BankingInformation(FolioApi):
    """Banking information Logic API

    **API for banking information**
    """

    def get_bankingInformations(self, **kwargs):
        """Get a list of banking information

        ``GET /organizations/banking-information``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    CQL query
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - bankName=TRC
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
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/BankingInformation_get_bankingInformations_return.schema 
        """
        return self.call("GET", "/organizations/banking-information", query=kwargs)

    def set_bankingInformation(self, bankingInformation: dict):
        """Create a banking information

        ``POST /organizations/banking-information``

        Args:
            bankingInformation (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created bankingInformation item

        Schema:

            .. literalinclude:: ../files/BankingInformation_set_bankingInformation_request.schema
        """
        return self.call("POST", "/organizations/banking-information", data=bankingInformation)

    def get_bankingInformation(self, bankingInformationId: str):
        """Retrieve bankingInformation item with given {bankingInformationId}

        ``GET /organizations/banking-information/{bankingInformationId}``

        Args:
            bankingInformationId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/BankingInformation_get_bankingInformation_return.schema 
        """
        return self.call("GET", f"/organizations/banking-information/{bankingInformationId}")

    def delete_bankingInformation(self, bankingInformationId: str):
        """Delete a banking information by id

        ``DELETE /organizations/banking-information/{bankingInformationId}``

        Args:
            bankingInformationId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("DELETE", f"/organizations/banking-information/{bankingInformationId}")

    def modify_bankingInformation(self, bankingInformationId: str, bankingInformation: dict):
        """Update a banking information by id

        ``PUT /organizations/banking-information/{bankingInformationId}``

        Args:
            bankingInformationId (str)
            bankingInformation (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiRequestFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/BankingInformation_modify_bankingInformation_request.schema
        """
        return self.call("PUT", f"/organizations/banking-information/{bankingInformationId}", data=bankingInformation)
