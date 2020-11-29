# -*- coding: utf-8 -*-
# Generated at 2020-11-29

import logging

from foliolib.folio import FolioApi

log = logging.getLogger("foliolib.folio.api.email")


class Email(FolioApi):
    """mod-email API

    The module should provide possibility of sending email through REST API of module.
    """

    def get_emails(self, **kwargs):
        """Get emails

        ``GET /email``

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
                    
                     - status==FAILURE
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Email_get_emails_return.schema 
        """
        return self.call("GET", "/email", query=kwargs)

    def set_email(self, email: dict):
        """Send email notifications

        ``POST /email``

        Args:
            email (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Email_set_email_request.schema
        """
        return self.call("POST", "/email", data=email)


class DelayedTasks(FolioApi):
    """mod-email API

    The module should provide the ability to delete emails by status and date through the REST API
    """

    def delete_expiredMessages(self, **kwargs):
        """delete expired email messages

        ``DELETE /delayedTask/expiredMessages``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            expirationDate (str):  Expiration Date
                    
                    Example:
                    
                     - 2019-01-31
            emailStatus (str):  Email status
                    
                    Example:
                    
                     - DELIVERED

        Raises:
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", "/delayedTask/expiredMessages", query=kwargs)
