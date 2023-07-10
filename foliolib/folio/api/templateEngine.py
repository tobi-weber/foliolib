# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.templateEngine")


class TemplateEngine(FolioApi):
    """mod-template-engine API

    This module dedicated for storing templates and generating text, html, xml, doc, docx etc from the template.
    """

    def set_template(self, template: dict):
        """Add a new template

        ``POST /templates``

        Args:
            template (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/TemplateEngine_set_template_request.schema
        """
        return self.call("POST", "/templates", data=template)

    def get_templates(self, **kwargs):
        """Get a list of templates

        ``GET /templates``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query string to filter templates based on matching criteria in fields.

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/TemplateEngine_get_templates_return.schema 
        """
        return self.call("GET", "/templates", query=kwargs)

    def get_template(self, templateId: str):
        """Get template by id

        ``GET /templates/{templateId}``

        Args:
            templateId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/TemplateEngine_get_template_return.schema 
        """
        return self.call("GET", f"/templates/{templateId}")

    def modify_template(self, templateId: str, template: dict):
        """Modify a template

        ``PUT /templates/{templateId}``

        Args:
            templateId (str)
            template (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/TemplateEngine_modify_template_request.schema
        """
        return self.call("PUT", f"/templates/{templateId}", data=template)

    def delete_template(self, templateId: str):
        """Delete template by id

        ``DELETE /templates/{templateId}``

        Args:
            templateId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/templates/{templateId}")

    def set_templateRequest(self, templateRequest: dict):
        """process specified template using given context

        ``POST /template-request``

        Args:
            templateRequest (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/TemplateEngine_set_templateRequest_request.schema
            .. literalinclude:: ../files/TemplateEngine_set_templateRequest_return.schema 
        """
        return self.call("POST", "/template-request", data=templateRequest)
