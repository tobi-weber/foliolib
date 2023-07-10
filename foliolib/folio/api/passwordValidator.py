# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.passwordValidator")



class Passwordvalidator(FolioApi):
    """Password validator module

    
    """

    def validatepassword(self, password):
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

            .. literalinclude:: ../files/Passwordvalidator_validatepassword_request.schema
            .. literalinclude:: ../files/Passwordvalidator_validatepassword_request.schema_response.schema
        """
        return self.call("POST", f"/tenant/password/validate", password)



class Validatorregistry(FolioApi):
    """Validator Registry

    
    """

    def gettenantrules(self, **kwargs):
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

            .. literalinclude:: ../files/Validatorregistry_gettenantrules_response.schema
        """
        return self.call("GET", "/tenant/rules", query=kwargs)

		
    def posttenantrules(self, validationRule):
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

            .. literalinclude:: ../files/Validatorregistry_posttenantrules_request.schema
        """
        return self.call("POST", f"/tenant/rules", validationRule)

		
    def puttenantrule(self, validationRule):
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

            .. literalinclude:: ../files/Validatorregistry_puttenantrule_request.schema
        """
        return self.call("PUT", f"/tenant/rules", validationRule)

    def gettenantrulebyid(self, ruleId):
        """

        ``GET /tenant/rules/{ruleId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Rule not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Validatorregistry_gettenantrulebyid_response.schema
        """
        return self.call("GET", f"/tenant/rules/{ruleId}")
