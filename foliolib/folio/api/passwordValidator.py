# -*- coding: utf-8 -*-
# Generated at 2023-04-16

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.passwordValidator")



class PasswordvalidatorAdmin(FolioAdminApi):
    """Password validator module
    Administration

    
    """

    def validatePassword(self, password):
        """Validate password

        ``POST /tenant/password/validate``

        Args:
            password (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not found error
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Passwordvalidator_validatePassword_request.schema
            .. literalinclude:: ../files/Passwordvalidator_validatePassword_request.schema_response.schema
        """
        return self.call("POST", "/tenant/password/validate", password)



class ValidatorregistryAdmin(FolioAdminApi):
    """Validator Registry
    Administration

    
    """

    def getTenantRules(self, **kwargs):
        """Get a list of existing validation rules for a tenant

        ``GET /tenant/rules``

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)
            query (str): A query string to filter rules based on matching criteria in fields.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Validatorregistry_getTenantRules_response.schema
        """
        return self.call("GET", "/tenant/rules", query=kwargs)

		
    def postTenantRules(self, validationRule):
        """Add a rule to a tenant

        ``POST /tenant/rules``

        Args:
            validationRule (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Validatorregistry_postTenantRules_request.schema
        """
        return self.call("POST", "/tenant/rules", validationRule)

		
    def putTenantRule(self, validationRule):
        """Enable/disable/change the rule

        ``PUT /tenant/rules``

        Args:
            validationRule (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Rule not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Validatorregistry_putTenantRule_request.schema
        """
        return self.call("PUT", "/tenant/rules", validationRule)

    def getTenantRuleById(self):
        """

        ``GET /tenant/rules/{ruleId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Rule not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Validatorregistry_getTenantRuleById_response.schema
        """
        return self.call("GET", "/tenant/rules/{ruleId}")
