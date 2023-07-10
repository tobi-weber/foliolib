# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.invoice")


class BatchGroup(FolioApi):
    """Batch group API

    This documents the API calls that can be made to manage batch groups
    """

    def get_batchGroups(self, **kwargs):
        """Retrieve a list of batchGroup items.

        ``GET /batch-groups``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
                    
                    using CQL (indexes for batch group)
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=="FOLIO"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/BatchGroup_get_batchGroups_return.schema 
        """
        return self.call("GET", "/batch-groups", query=kwargs)

    def set_batchGroup(self, batchGroup: dict):
        """Post a batch group.

        ``POST /batch-groups``

        Args:
            batchGroup (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created batchGroup item

        Schema:

            .. literalinclude:: ../files/BatchGroup_set_batchGroup_request.schema
        """
        return self.call("POST", "/batch-groups", data=batchGroup)

    def get_batchGroup(self, batchGroupsId: str):
        """Return a batch-group with given {id}

        ``GET /batch-groups/{batchGroupsId}``

        Args:
            batchGroupsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/BatchGroup_get_batchGroup_return.schema 
        """
        return self.call("GET", f"/batch-groups/{batchGroupsId}")

    def delete_batchGroup(self, batchGroupsId: str):
        """Delete a batch-group with given {id}

        ``DELETE /batch-groups/{batchGroupsId}``

        Args:
            batchGroupsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/batch-groups/{batchGroupsId}")

    def modify_batchGroup(self, batchGroupsId: str, batchGroup: dict):
        """Update batch-group.

        ``PUT /batch-groups/{batchGroupsId}``

        Args:
            batchGroupsId (str)
            batchGroup (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/BatchGroup_modify_batchGroup_request.schema
        """
        return self.call("PUT", f"/batch-groups/{batchGroupsId}", data=batchGroup)


class Invoice(FolioApi):
    """Invoice API

    This documents the API calls that can be made to manage invoices
    """

    def get_invoices(self, **kwargs):
        """Retrieve a list of invoice items.

        ``GET /invoice/invoices``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
                    
                    using CQL (indexes for invoice)
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - invoiceLineStatus=="Open"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Invoice_get_invoices_return.schema 
        """
        return self.call("GET", "/invoice/invoices", query=kwargs)

    def set_invoice(self, invoice: dict):
        """Post invoice. Only in case an acquisition unit has to be assigned to the invoice, it is required that user should have extra permission invoices.acquisitions-units-assignments.assign to create an Invoice.

        ``POST /invoice/invoices``

        Args:
            invoice (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created invoice item

        Schema:

            .. literalinclude:: ../files/Invoice_set_invoice_request.schema
        """
        return self.call("POST", "/invoice/invoices", data=invoice)

    def get_invoice(self, invoicesId: str):
        """Return an invoice with given {id}

        ``GET /invoice/invoices/{invoicesId}``

        Args:
            invoicesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Invoice_get_invoice_return.schema 
        """
        return self.call("GET", f"/invoice/invoices/{invoicesId}")

    def delete_invoice(self, invoicesId: str):
        """Delete an invoice with given {id}

        ``DELETE /invoice/invoices/{invoicesId}``

        Args:
            invoicesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/invoice/invoices/{invoicesId}")

    def modify_invoice(self, invoicesId: str, invoice: dict):
        """Update invoice. Only in case an acquisition units list has to be changed, it is required that user should have extra permission invoices.acquisitions-units-assignments.manage to update an Invoice.

        ``PUT /invoice/invoices/{invoicesId}``

        Args:
            invoicesId (str)
            invoice (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Invoice_modify_invoice_request.schema
        """
        return self.call("PUT", f"/invoice/invoices/{invoicesId}", data=invoice)

    def get_documents(self, invoicesId: str, **kwargs):
        """Get list of documents

        ``GET /invoice/invoices/{invoicesId}/documents``

        Args:
            invoicesId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
                    
                    with valid searchable fields: for example metadata.createdDate
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - metadata.createdDate > '2018-07-19T00:00:00.000+0000'

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Invoice_get_documents_return.schema 
        """
        return self.call("GET", f"/invoice/invoices/{invoicesId}/documents", query=kwargs)

    def set_document(self, invoicesId: str):
        """

        ``POST /invoice/invoices/{invoicesId}/documents``

        Args:
            invoicesId (str)
        """
        return self.call("POST", f"/invoice/invoices/{invoicesId}/documents")

    def get_document(self, invoicesId: str, documentId: str):
        """Retrieve document item with given {documentId}

        ``GET /invoice/invoices/{invoicesId}/documents/{documentId}``

        Args:
            invoicesId (str)
            documentId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Invoice_get_document_return.schema 
        """
        return self.call("GET", f"/invoice/invoices/{invoicesId}/documents/{documentId}")

    def delete_document(self, invoicesId: str, documentId: str):
        """Delete document item with given {documentId}

        ``DELETE /invoice/invoices/{invoicesId}/documents/{documentId}``

        Args:
            invoicesId (str)
            documentId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/invoice/invoices/{invoicesId}/documents/{documentId}")

    def get_fiscalYears(self, invoicesId: str, **kwargs):
        """Get a list of fiscal years to approve or pay the invoice

        ``GET /invoice/invoices/{invoicesId}/fiscal-years``

        Args:
            invoicesId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
                    
                    with valid searchable fields: for example metadata.createdDate
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - metadata.createdDate > '2018-07-19T00:00:00.000+0000'

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Invoice_get_fiscalYears_return.schema 
        """
        return self.call("GET", f"/invoice/invoices/{invoicesId}/fiscal-years", query=kwargs)

    def set_fiscalYear(self, invoicesId: str):
        """

        ``POST /invoice/invoices/{invoicesId}/fiscal-years``

        Args:
            invoicesId (str)
        """
        return self.call("POST", f"/invoice/invoices/{invoicesId}/fiscal-years")

    def get_invoiceLines(self, **kwargs):
        """Retrieve a list of invoiceLine items.

        ``GET /invoice/invoice-lines``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
                    
                    using CQL (indexes for invoice lines)
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - status=="Open"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Invoice_get_invoiceLines_return.schema 
        """
        return self.call("GET", "/invoice/invoice-lines", query=kwargs)

    def set_invoiceLine(self, invoiceLine: dict):
        """Post an invoice lines to corresponding invoice

        ``POST /invoice/invoice-lines``

        Args:
            invoiceLine (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created invoiceLine item

        Schema:

            .. literalinclude:: ../files/Invoice_set_invoiceLine_request.schema
        """
        return self.call("POST", "/invoice/invoice-lines", data=invoiceLine)

    def get_invoiceLine(self, invoiceLinesId: str):
        """Return an invoice line with given {id}

        ``GET /invoice/invoice-lines/{invoiceLinesId}``

        Args:
            invoiceLinesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Invoice_get_invoiceLine_return.schema 
        """
        return self.call("GET", f"/invoice/invoice-lines/{invoiceLinesId}")

    def delete_invoiceLine(self, invoiceLinesId: str):
        """Delete an invoice line with given {id}

        ``DELETE /invoice/invoice-lines/{invoiceLinesId}``

        Args:
            invoiceLinesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/invoice/invoice-lines/{invoiceLinesId}")

    def modify_invoiceLine(self, invoiceLinesId: str, invoiceLine: dict):
        """Update an invoice line with given {id}

        ``PUT /invoice/invoice-lines/{invoiceLinesId}``

        Args:
            invoiceLinesId (str)
            invoiceLine (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Invoice_modify_invoiceLine_request.schema
        """
        return self.call("PUT", f"/invoice/invoice-lines/{invoiceLinesId}", data=invoiceLine)

    def modify_validate(self, validate: dict):
        """Validate is total amount equals to sum of all fund distributions

        ``PUT /invoice/invoice-lines/fund-distributions/validate``

        Args:
            validate (dict): See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Invoice_modify_validate_request.schema
        """
        return self.call("PUT", "/invoice/invoice-lines/fund-distributions/validate", data=validate)

    def get_invoiceNumbers(self):
        """Get system generated Invoice Number

        ``GET /invoice/invoice-number``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Invoice_get_invoiceNumbers_return.schema 
        """
        return self.call("GET", "/invoice/invoice-number")

    def set_invoiceNumber(self):
        """

        ``POST /invoice/invoice-number``
        """
        return self.call("POST", "/invoice/invoice-number")


class BatchVoucherExportConfiguration(FolioApi):
    """Batch voucher export configurations CRUD API

    This documents the API calls that can be made to manage batch voucher export configurations
    """

    def get_exportConfigurations(self, **kwargs):
        """Get list of batch voucher export configurations

        ``GET /batch-voucher/export-configurations``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
                    
                    with valid searchable fields: for example format
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - format=="Application/xml"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/BatchVoucherExportConfiguration_get_exportConfigurations_return.schema 
        """
        return self.call("GET", "/batch-voucher/export-configurations", query=kwargs)

    def set_exportConfiguration(self, exportConfiguration: dict):
        """Create a new exportConfiguration item.

        ``POST /batch-voucher/export-configurations``

        Args:
            exportConfiguration (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created exportConfiguration item

        Schema:

            .. literalinclude:: ../files/BatchVoucherExportConfiguration_set_exportConfiguration_request.schema
        """
        return self.call("POST", "/batch-voucher/export-configurations", data=exportConfiguration)

    def get_exportConfiguration(self, exportConfigurationsId: str):
        """Retrieve exportConfiguration item with given {exportConfigurationId}

        ``GET /batch-voucher/export-configurations/{exportConfigurationsId}``

        Args:
            exportConfigurationsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/BatchVoucherExportConfiguration_get_exportConfiguration_return.schema 
        """
        return self.call("GET", f"/batch-voucher/export-configurations/{exportConfigurationsId}")

    def delete_exportConfiguration(self, exportConfigurationsId: str):
        """Delete exportConfiguration item with given {exportConfigurationId}

        ``DELETE /batch-voucher/export-configurations/{exportConfigurationsId}``

        Args:
            exportConfigurationsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/batch-voucher/export-configurations/{exportConfigurationsId}")

    def modify_exportConfiguration(self, exportConfigurationsId: str, exportConfiguration: dict):
        """Update exportConfiguration item with given {exportConfigurationId}

        ``PUT /batch-voucher/export-configurations/{exportConfigurationsId}``

        Args:
            exportConfigurationsId (str)
            exportConfiguration (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/BatchVoucherExportConfiguration_modify_exportConfiguration_request.schema
        """
        return self.call("PUT", f"/batch-voucher/export-configurations/{exportConfigurationsId}", data=exportConfiguration)

    def set_credential(self, exportConfigurationsId: str, credential: dict):
        """Create a credentials record

        ``POST /batch-voucher/export-configurations/{exportConfigurationsId}/credentials``

        Args:
            exportConfigurationsId (str)
            credential (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created credentials

        Schema:

            .. literalinclude:: ../files/BatchVoucherExportConfiguration_set_credential_request.schema
        """
        return self.call("POST", f"/batch-voucher/export-configurations/{exportConfigurationsId}/credentials", data=credential)

    def get_credentials_by_exportConfiguration(self, exportConfigurationsId: str):
        """Get the credentials for the specified export_configuration

        ``GET /batch-voucher/export-configurations/{exportConfigurationsId}/credentials``

        Args:
            exportConfigurationsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/BatchVoucherExportConfiguration_get_credentials_by_exportConfiguration_return.schema 
        """
        return self.call("GET", f"/batch-voucher/export-configurations/{exportConfigurationsId}/credentials")

    def modify_credential(self, exportConfigurationsId: str, credential: dict):
        """Edit a credentials record

        ``PUT /batch-voucher/export-configurations/{exportConfigurationsId}/credentials``

        Args:
            exportConfigurationsId (str)
            credential (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/BatchVoucherExportConfiguration_modify_credential_request.schema
        """
        return self.call("PUT", f"/batch-voucher/export-configurations/{exportConfigurationsId}/credentials", data=credential)

    def set_test(self, exportConfigurationsId: str):
        """Test that you can connect to and log into the uploadURI with the configured credentials

        ``POST /batch-voucher/export-configurations/{exportConfigurationsId}/credentials/test``

        Args:
            exportConfigurationsId (str)

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/BatchVoucherExportConfiguration_set_test_return.schema 
        """
        return self.call("POST", f"/batch-voucher/export-configurations/{exportConfigurationsId}/credentials/test")


class BatchVoucherExports(FolioApi):
    """Batch voucher exports CRUD API

    This documents the API calls that can be made to manage batch voucher exports
    """

    def get_batchVoucherExports(self, **kwargs):
        """Get list of batch voucher exports

        ``GET /batch-voucher/batch-voucher-exports``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
                    
                    with valid searchable fields: for example status
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - status==Pending

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/BatchVoucherExports_get_batchVoucherExports_return.schema 
        """
        return self.call("GET", "/batch-voucher/batch-voucher-exports", query=kwargs)

    def set_batchVoucherExport(self, batchVoucherExport: dict):
        """Create a new batchVoucherExport item.

        ``POST /batch-voucher/batch-voucher-exports``

        Args:
            batchVoucherExport (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created batchVoucherExport item

        Schema:

            .. literalinclude:: ../files/BatchVoucherExports_set_batchVoucherExport_request.schema
        """
        return self.call("POST", "/batch-voucher/batch-voucher-exports", data=batchVoucherExport)

    def get_batchVoucherExport(self, batchVoucherExportsId: str):
        """Return a batch-voucher-export with given {id}

        ``GET /batch-voucher/batch-voucher-exports/{batchVoucherExportsId}``

        Args:
            batchVoucherExportsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/BatchVoucherExports_get_batchVoucherExport_return.schema 
        """
        return self.call("GET", f"/batch-voucher/batch-voucher-exports/{batchVoucherExportsId}")

    def delete_batchVoucherExport(self, batchVoucherExportsId: str):
        """Delete a batch-voucher-export with given {id}

        ``DELETE /batch-voucher/batch-voucher-exports/{batchVoucherExportsId}``

        Args:
            batchVoucherExportsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("DELETE", f"/batch-voucher/batch-voucher-exports/{batchVoucherExportsId}")

    def modify_batchVoucherExport(self, batchVoucherExportsId: str, batchVoucherExport: dict):
        """Update a batch-voucher-export with given {id}

        ``PUT /batch-voucher/batch-voucher-exports/{batchVoucherExportsId}``

        Args:
            batchVoucherExportsId (str)
            batchVoucherExport (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/BatchVoucherExports_modify_batchVoucherExport_request.schema
        """
        return self.call("PUT", f"/batch-voucher/batch-voucher-exports/{batchVoucherExportsId}", data=batchVoucherExport)

    def set_upload(self, batchVoucherExportsId: str):
        """(Re)upload the batch voucher associated with this voucher export to the configured URI, using the configured credentials

        ``POST /batch-voucher/batch-voucher-exports/{batchVoucherExportsId}/upload``

        Args:
            batchVoucherExportsId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
        """
        return self.call("POST", f"/batch-voucher/batch-voucher-exports/{batchVoucherExportsId}/upload")

    def set_scheduled(self):
        """Conditionally creates a batch voucher export

        ``POST /batch-voucher/batch-voucher-exports/scheduled``

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
        """
        return self.call("POST", "/batch-voucher/batch-voucher-exports/scheduled")


class BatchVoucher(FolioApi):
    """Batch Vouchers API

    **API used to manage batch vouchers.**
    """

    def get_batchVouchers(self, batchVouchersId: str):
        """Retrieve batchVoucher item with given {batchVoucherId}

        ``GET /batch-voucher/batch-vouchers/{batchVouchersId}``

        Args:
            batchVouchersId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/BatchVoucher_get_batchVouchers_return.schema 
        """
        return self.call("GET", f"/batch-voucher/batch-vouchers/{batchVouchersId}")


class Voucher(FolioApi):
    """Voucher API

    This documents the API calls that can be made to manage vouchers
    """

    def get_vouchers(self, **kwargs):
        """Retrieve a list of voucher items.

        ``GET /voucher/vouchers``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
                    
                    using CQL (indexes for voucher)
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - voucherNumber=="1000"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Voucher_get_vouchers_return.schema 
        """
        return self.call("GET", "/voucher/vouchers", query=kwargs)

    def get_voucher(self, vouchersId: str):
        """Return a voucher with given {id}

        ``GET /voucher/vouchers/{vouchersId}``

        Args:
            vouchersId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Voucher_get_voucher_return.schema 
        """
        return self.call("GET", f"/voucher/vouchers/{vouchersId}")

    def modify_voucher(self, vouchersId: str):
        """

        ``PUT /voucher/vouchers/{vouchersId}``

        Args:
            vouchersId (str)
        """
        return self.call("PUT", f"/voucher/vouchers/{vouchersId}")

    def get_voucherLines(self):
        """Retrieve a list of voucher lines.

        ``GET /voucher/voucher-lines``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Voucher_get_voucherLines_return.schema 
        """
        return self.call("GET", "/voucher/voucher-lines")

    def get_voucherLine(self, voucherLinesId: str, **kwargs):
        """Return an voucher line with given {id}

        ``GET /voucher/voucher-lines/{voucherLinesId}``

        Args:
            voucherLinesId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
                    
                    using CQL (indexes for voucher)
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - voucherNumber=="1000"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Voucher_get_voucherLine_return.schema 
        """
        return self.call("GET", f"/voucher/voucher-lines/{voucherLinesId}", query=kwargs)

    def modify_voucherLine(self, voucherLinesId: str):
        """

        ``PUT /voucher/voucher-lines/{voucherLinesId}``

        Args:
            voucherLinesId (str)
        """
        return self.call("PUT", f"/voucher/voucher-lines/{voucherLinesId}")

    def set_start(self, value: str):
        """(Re)set the start value of the voucher number sequence

        ``POST /voucher/voucher-number/start/{value}``

        Args:
            value (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("POST", f"/voucher/voucher-number/start/{value}")

    def get_starts(self):
        """Get the current start value of the voucher number sequence

        ``GET /voucher/voucher-number/start``

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Voucher_get_starts_return.schema 
        """
        return self.call("GET", "/voucher/voucher-number/start")
