# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.email")


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

    def set_retryFailedEmail(self):
        """Retry failed emails

        ``POST /delayedTask/retryFailedEmails``
        """
        return self.call("POST", "/delayedTask/retryFailedEmails")


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

    def set_email(self):
        """

        ``POST /email``
        """
        return self.call("POST", "/email")


class SmtpConfiguration(FolioApi):
    """SMTP server configuration API

    **API for managing SMTP server configuration**
    """

    def get_smtpConfigurations(self, **kwargs):
        """Retrieve a list of smtpConfiguration items.

        ``GET /smtp-configuration``

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
                    
                     - ssl=true

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/SmtpConfiguration_get_smtpConfigurations_return.schema 
        """
        return self.call("GET", "/smtp-configuration", query=kwargs)

    def set_smtpConfiguration(self, smtpConfiguration: dict):
        """Create a new smtpConfiguration item.

        ``POST /smtp-configuration``

        Args:
            smtpConfiguration (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created smtpConfiguration item

        Schema:

            .. literalinclude:: ../files/SmtpConfiguration_set_smtpConfiguration_request.schema
        """
        return self.call("POST", "/smtp-configuration", data=smtpConfiguration)

    def get_smtpConfiguration(self, smtpConfigurationId: str):
        """Get SMTP configuration

        ``GET /smtp-configuration/{smtpConfigurationId}``

        Args:
            smtpConfigurationId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/SmtpConfiguration_get_smtpConfiguration_return.schema 
        """
        return self.call("GET", f"/smtp-configuration/{smtpConfigurationId}")

    def delete_smtpConfiguration(self, smtpConfigurationId: str, **kwargs):
        """Delete SMTP configuration

        ``DELETE /smtp-configuration/{smtpConfigurationId}``

        Args:
            smtpConfigurationId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/smtp-configuration/{smtpConfigurationId}", query=kwargs)

    def modify_smtpConfiguration(self, smtpConfigurationId: str, smtpConfiguration: dict):
        """Update SMTP configuration

        ``PUT /smtp-configuration/{smtpConfigurationId}``

        Args:
            smtpConfigurationId (str)
            smtpConfiguration (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/SmtpConfiguration_modify_smtpConfiguration_request.schema
        """
        return self.call("PUT", f"/smtp-configuration/{smtpConfigurationId}", data=smtpConfiguration)
