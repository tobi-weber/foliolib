# -*- coding: utf-8 -*-
# Generated at 2020-11-29

import logging

from foliolib.folio import FolioApi

log = logging.getLogger("foliolib.folio.api.passwordValidator")


class ValidatorRegistry(FolioApi):
    """Validator Registry API

    This component manages password validation rules.
    """

    def get_rules(self, **kwargs):
        """Get a list of existing validation rules for a tenant

        ``GET /tenant/rules``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query string to filter rules based on matching criteria in fields.

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ValidatorRegistry_get_rules_return.schema 
        """
        return self.call("GET", "/tenant/rules", query=kwargs)

    def set_rule(self, rule: dict):
        """Add a rule to a tenant

        ``POST /tenant/rules``

        Args:
            rule (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/ValidatorRegistry_set_rule_request.schema
        """
        return self.call("POST", "/tenant/rules", data=rule)

    def modify_rule(self, rule: dict):
        """Enable/disable/change the rule

        ``PUT /tenant/rules``

        Args:
            rule (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ValidatorRegistry_modify_rule_request.schema
        """
        return self.call("PUT", "/tenant/rules", data=rule)

    def get_rule(self, ruleId: str):
        """

        ``GET /tenant/rules/{ruleId}``

        Args:
            ruleId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ValidatorRegistry_get_rule_return.schema 
        """
        return self.call("GET", f"/tenant/rules/{ruleId}")


class PasswordValidator(FolioApi):
    """mod-password-validator API

    This module is performing validation of the password and storing rules for the specified tenant.
    """

    def set_validate(self, validate: dict):
        """Validate password

        ``POST /password/validate``

        Args:
            validate (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/PasswordValidator_set_validate_request.schema
            .. literalinclude:: ../files/PasswordValidator_set_validate_return.schema 
        """
        return self.call("POST", "/password/validate", data=validate)
