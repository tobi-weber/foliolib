# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.organizationsStorage")


class Organization(FolioApi):
    """Organizations

    **CRUD APIs used to manage organizations.**
    """

    def get_organizations(self, **kwargs):
        """Get list of organizations

        ``GET /organizations-storage/organizations``

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

            .. literalinclude:: ../files/Organization_get_organizations_return.schema 
        """
        return self.call("GET", "/organizations-storage/organizations", query=kwargs)

    def set_organization(self, organization: dict):
        """Create a new organization item.

        ``POST /organizations-storage/organizations``

        Args:
            organization (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created organization item

        Schema:

            .. literalinclude:: ../files/Organization_set_organization_request.schema
        """
        return self.call("POST", "/organizations-storage/organizations", data=organization)

    def get_organization(self, organizationsId: str):
        """Retrieve organization item with given {organizationId}

        ``GET /organizations-storage/organizations/{organizationsId}``

        Args:
            organizationsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Organization_get_organization_return.schema 
        """
        return self.call("GET", f"/organizations-storage/organizations/{organizationsId}")

    def delete_organization(self, organizationsId: str):
        """Delete organization item with given {organizationId}

        ``DELETE /organizations-storage/organizations/{organizationsId}``

        Args:
            organizationsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/organizations-storage/organizations/{organizationsId}")

    def modify_organization(self, organizationsId: str, organization: dict):
        """Update organization with 'organization_id'

        ``PUT /organizations-storage/organizations/{organizationsId}``

        Args:
            organizationsId (str)
            organization (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Organization_modify_organization_request.schema
        """
        return self.call("PUT", f"/organizations-storage/organizations/{organizationsId}", data=organization)


class Category(FolioApi):
    """Categories

    **CRUD APIs used to manage cateogries.**
    """

    def get_categories(self, **kwargs):
        """Get list of categories

        ``GET /organizations-storage/categories``

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

            .. literalinclude:: ../files/Category_get_categories_return.schema 
        """
        return self.call("GET", "/organizations-storage/categories", query=kwargs)

    def set_category(self, category: dict):
        """Create a new category item.

        ``POST /organizations-storage/categories``

        Args:
            category (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created category item

        Schema:

            .. literalinclude:: ../files/Category_set_category_request.schema
        """
        return self.call("POST", "/organizations-storage/categories", data=category)

    def get_category(self, categoriesId: str):
        """Retrieve category item with given {categoryId}

        ``GET /organizations-storage/categories/{categoriesId}``

        Args:
            categoriesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Category_get_category_return.schema 
        """
        return self.call("GET", f"/organizations-storage/categories/{categoriesId}")

    def delete_category(self, categoriesId: str):
        """Delete category item with given {categoryId}

        ``DELETE /organizations-storage/categories/{categoriesId}``

        Args:
            categoriesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/organizations-storage/categories/{categoriesId}")

    def modify_category(self, categoriesId: str, category: dict):
        """Update category item with given {categoryId}

        ``PUT /organizations-storage/categories/{categoriesId}``

        Args:
            categoriesId (str)
            category (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Category_modify_category_request.schema
        """
        return self.call("PUT", f"/organizations-storage/categories/{categoriesId}", data=category)


class Interface(FolioApi):
    """Interfaces

    **CRUD APIs used to manage interfaces.**
    """

    def get_interfaces(self, **kwargs):
        """Get list of interfaces

        ``GET /organizations-storage/interfaces``

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

            .. literalinclude:: ../files/Interface_get_interfaces_return.schema 
        """
        return self.call("GET", "/organizations-storage/interfaces", query=kwargs)

    def set_interface(self, interface: dict):
        """Create a new interface item.

        ``POST /organizations-storage/interfaces``

        Args:
            interface (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created interface item

        Schema:

            .. literalinclude:: ../files/Interface_set_interface_request.schema
        """
        return self.call("POST", "/organizations-storage/interfaces", data=interface)

    def get_interface(self, interfacesId: str):
        """Retrieve interface item with given {interfaceId}

        ``GET /organizations-storage/interfaces/{interfacesId}``

        Args:
            interfacesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Interface_get_interface_return.schema 
        """
        return self.call("GET", f"/organizations-storage/interfaces/{interfacesId}")

    def delete_interface(self, interfacesId: str):
        """Delete interface item with given {interfaceId}

        ``DELETE /organizations-storage/interfaces/{interfacesId}``

        Args:
            interfacesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/organizations-storage/interfaces/{interfacesId}")

    def modify_interface(self, interfacesId: str, interface: dict):
        """Update interface item with given {interfaceId}

        ``PUT /organizations-storage/interfaces/{interfacesId}``

        Args:
            interfacesId (str)
            interface (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Interface_modify_interface_request.schema
        """
        return self.call("PUT", f"/organizations-storage/interfaces/{interfacesId}", data=interface)

    def set_interface_by_interfacesId(self, interfacesId: str):
        """

        ``POST /organizations-storage/interfaces/{interfacesId}``

        Args:
            interfacesId (str)
        """
        return self.call("POST", f"/organizations-storage/interfaces/{interfacesId}")

    def get_credential(self, interfacesId: str):
        """Retrieve credential item with given {credentialId}

        ``GET /organizations-storage/interfaces/{interfacesId}/credentials``

        Args:
            interfacesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Interface_get_credential_return.schema 
        """
        return self.call("GET", f"/organizations-storage/interfaces/{interfacesId}/credentials")

    def delete_credential(self, interfacesId: str):
        """Delete credential item with given {credentialId}

        ``DELETE /organizations-storage/interfaces/{interfacesId}/credentials``

        Args:
            interfacesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/organizations-storage/interfaces/{interfacesId}/credentials")

    def modify_credential(self, interfacesId: str, credential: dict):
        """Update credential item with given {credentialId}

        ``PUT /organizations-storage/interfaces/{interfacesId}/credentials``

        Args:
            interfacesId (str)
            credential (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Interface_modify_credential_request.schema
        """
        return self.call("PUT", f"/organizations-storage/interfaces/{interfacesId}/credentials", data=credential)

    def set_credential(self, interfacesId: str):
        """

        ``POST /organizations-storage/interfaces/{interfacesId}/credentials``

        Args:
            interfacesId (str)
        """
        return self.call("POST", f"/organizations-storage/interfaces/{interfacesId}/credentials")


class Contact(FolioApi):
    """Contacts

    **CRUD APIs used to manage contacts.**
    """

    def get_contacts(self, **kwargs):
        """Get list of contact persons

        ``GET /organizations-storage/contacts``

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

            .. literalinclude:: ../files/Contact_get_contacts_return.schema 
        """
        return self.call("GET", "/organizations-storage/contacts", query=kwargs)

    def set_contact(self, contact: dict):
        """Create a new contact item.

        ``POST /organizations-storage/contacts``

        Args:
            contact (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created contact item

        Schema:

            .. literalinclude:: ../files/Contact_set_contact_request.schema
        """
        return self.call("POST", "/organizations-storage/contacts", data=contact)

    def get_contact(self, contactsId: str):
        """Retrieve contact item with given {contactId}

        ``GET /organizations-storage/contacts/{contactsId}``

        Args:
            contactsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Contact_get_contact_return.schema 
        """
        return self.call("GET", f"/organizations-storage/contacts/{contactsId}")

    def delete_contact(self, contactsId: str):
        """Delete contact item with given {contactId}

        ``DELETE /organizations-storage/contacts/{contactsId}``

        Args:
            contactsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/organizations-storage/contacts/{contactsId}")

    def modify_contact(self, contactsId: str, contact: dict):
        """Update contact item with given {contactId}

        ``PUT /organizations-storage/contacts/{contactsId}``

        Args:
            contactsId (str)
            contact (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Contact_modify_contact_request.schema
        """
        return self.call("PUT", f"/organizations-storage/contacts/{contactsId}", data=contact)


class Email(FolioApi):
    """**Deprecated.** Emails

    CRUD APIs used to manage emails.
		**These APIs are not currently in use and may at some point be removed or resurrected**
    """

    def get_emails(self, **kwargs):
        """Get list of emails

        ``GET /organizations-storage/emails``

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

            .. literalinclude:: ../files/Email_get_emails_return.schema 
        """
        return self.call("GET", "/organizations-storage/emails", query=kwargs)

    def set_email(self, email: dict):
        """Create a new email item.

        ``POST /organizations-storage/emails``

        Args:
            email (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created email item

        Schema:

            .. literalinclude:: ../files/Email_set_email_request.schema
        """
        return self.call("POST", "/organizations-storage/emails", data=email)

    def get_email(self, emailsId: str):
        """Retrieve email item with given {emailId}

        ``GET /organizations-storage/emails/{emailsId}``

        Args:
            emailsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Email_get_email_return.schema 
        """
        return self.call("GET", f"/organizations-storage/emails/{emailsId}")

    def delete_email(self, emailsId: str):
        """Delete email item with given {emailId}

        ``DELETE /organizations-storage/emails/{emailsId}``

        Args:
            emailsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/organizations-storage/emails/{emailsId}")

    def modify_email(self, emailsId: str, email: dict):
        """Update email item with given {emailId}

        ``PUT /organizations-storage/emails/{emailsId}``

        Args:
            emailsId (str)
            email (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Email_modify_email_request.schema
        """
        return self.call("PUT", f"/organizations-storage/emails/{emailsId}", data=email)


class Url(FolioApi):
    """**Deprecated.** URLs

    CRUD APIs used to manage URLs.
		**These APIs are not currently in use and may at some point be removed or resurrected**
    """

    def get_urls(self, **kwargs):
        """Get list of URLs

        ``GET /organizations-storage/urls``

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

            .. literalinclude:: ../files/Url_get_urls_return.schema 
        """
        return self.call("GET", "/organizations-storage/urls", query=kwargs)

    def set_url(self, url: dict):
        """Create a new url item.

        ``POST /organizations-storage/urls``

        Args:
            url (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created url item

        Schema:

            .. literalinclude:: ../files/Url_set_url_request.schema
        """
        return self.call("POST", "/organizations-storage/urls", data=url)

    def get_url(self, urlsId: str):
        """Retrieve url item with given {urlId}

        ``GET /organizations-storage/urls/{urlsId}``

        Args:
            urlsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Url_get_url_return.schema 
        """
        return self.call("GET", f"/organizations-storage/urls/{urlsId}")

    def delete_url(self, urlsId: str):
        """Delete url item with given {urlId}

        ``DELETE /organizations-storage/urls/{urlsId}``

        Args:
            urlsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/organizations-storage/urls/{urlsId}")

    def modify_url(self, urlsId: str, url: dict):
        """Update url item with given {urlId}

        ``PUT /organizations-storage/urls/{urlsId}``

        Args:
            urlsId (str)
            url (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Url_modify_url_request.schema
        """
        return self.call("PUT", f"/organizations-storage/urls/{urlsId}", data=url)


class Address(FolioApi):
    """**Deprecated.** Addresses

    CRUD APIs used to manage addresses.
		**These APIs are not currently in use and may at some point be removed or resurrected**
    """

    def get_addresses(self, **kwargs):
        """Get list of addresses

        ``GET /organizations-storage/addresses``

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

            .. literalinclude:: ../files/Address_get_addresses_return.schema 
        """
        return self.call("GET", "/organizations-storage/addresses", query=kwargs)

    def set_address(self, address: dict):
        """Create a new address item.

        ``POST /organizations-storage/addresses``

        Args:
            address (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created address item

        Schema:

            .. literalinclude:: ../files/Address_set_address_request.schema
        """
        return self.call("POST", "/organizations-storage/addresses", data=address)

    def get_address(self, addressesId: str):
        """Retrieve address item with given {addressId}

        ``GET /organizations-storage/addresses/{addressesId}``

        Args:
            addressesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Address_get_address_return.schema 
        """
        return self.call("GET", f"/organizations-storage/addresses/{addressesId}")

    def delete_address(self, addressesId: str):
        """Delete address item with given {addressId}

        ``DELETE /organizations-storage/addresses/{addressesId}``

        Args:
            addressesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/organizations-storage/addresses/{addressesId}")

    def modify_address(self, addressesId: str, address: dict):
        """Update address item with given {addressId}

        ``PUT /organizations-storage/addresses/{addressesId}``

        Args:
            addressesId (str)
            address (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Address_modify_address_request.schema
        """
        return self.call("PUT", f"/organizations-storage/addresses/{addressesId}", data=address)


class OrganizationType(FolioApi):
    """Organization types

    **CRUD APIs used to manage organization types.**
    """

    def get_organizationTypes(self, **kwargs):
        """Get a list of organization types

        ``GET /organizations-storage/organization-types``

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
                    
                     - status=Active
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

            .. literalinclude:: ../files/OrganizationType_get_organizationTypes_return.schema 
        """
        return self.call("GET", "/organizations-storage/organization-types", query=kwargs)

    def set_organizationType(self, organizationType: dict):
        """Create an organization type

        ``POST /organizations-storage/organization-types``

        Args:
            organizationType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created organizationType item

        Schema:

            .. literalinclude:: ../files/OrganizationType_set_organizationType_request.schema
        """
        return self.call("POST", "/organizations-storage/organization-types", data=organizationType)

    def get_organizationType(self, organizationTypesId: str):
        """Retrieve organizationType item with given {organizationTypeId}

        ``GET /organizations-storage/organization-types/{organizationTypesId}``

        Args:
            organizationTypesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/OrganizationType_get_organizationType_return.schema 
        """
        return self.call("GET", f"/organizations-storage/organization-types/{organizationTypesId}")

    def delete_organizationType(self, organizationTypesId: str):
        """Delete an organization type by id

        ``DELETE /organizations-storage/organization-types/{organizationTypesId}``

        Args:
            organizationTypesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("DELETE", f"/organizations-storage/organization-types/{organizationTypesId}")

    def modify_organizationType(self, organizationTypesId: str, organizationType: dict):
        """Update an organization type by id

        ``PUT /organizations-storage/organization-types/{organizationTypesId}``

        Args:
            organizationTypesId (str)
            organizationType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/OrganizationType_modify_organizationType_request.schema
        """
        return self.call("PUT", f"/organizations-storage/organization-types/{organizationTypesId}", data=organizationType)


class PhoneNumber(FolioApi):
    """**Deprecated.** Phone Numbers

    CRUD APIs used to manage phone numbers.
		**These APIs are not currently in use and may at some point be removed or resurrected**
    """

    def get_phoneNumbers(self, **kwargs):
        """Get list of phone_numbers

        ``GET /organizations-storage/phone-numbers``

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

            .. literalinclude:: ../files/PhoneNumber_get_phoneNumbers_return.schema 
        """
        return self.call("GET", "/organizations-storage/phone-numbers", query=kwargs)

    def set_phoneNumber(self, phoneNumber: dict):
        """Create a new phoneNumber item.

        ``POST /organizations-storage/phone-numbers``

        Args:
            phoneNumber (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created phoneNumber item

        Schema:

            .. literalinclude:: ../files/PhoneNumber_set_phoneNumber_request.schema
        """
        return self.call("POST", "/organizations-storage/phone-numbers", data=phoneNumber)

    def get_phoneNumber(self, phoneNumbersId: str):
        """Retrieve phoneNumber item with given {phoneNumberId}

        ``GET /organizations-storage/phone-numbers/{phoneNumbersId}``

        Args:
            phoneNumbersId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PhoneNumber_get_phoneNumber_return.schema 
        """
        return self.call("GET", f"/organizations-storage/phone-numbers/{phoneNumbersId}")

    def delete_phoneNumber(self, phoneNumbersId: str):
        """Delete phoneNumber item with given {phoneNumberId}

        ``DELETE /organizations-storage/phone-numbers/{phoneNumbersId}``

        Args:
            phoneNumbersId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/organizations-storage/phone-numbers/{phoneNumbersId}")

    def modify_phoneNumber(self, phoneNumbersId: str, phoneNumber: dict):
        """Update phoneNumber item with given {phoneNumberId}

        ``PUT /organizations-storage/phone-numbers/{phoneNumbersId}``

        Args:
            phoneNumbersId (str)
            phoneNumber (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PhoneNumber_modify_phoneNumber_request.schema
        """
        return self.call("PUT", f"/organizations-storage/phone-numbers/{phoneNumbersId}", data=phoneNumber)
