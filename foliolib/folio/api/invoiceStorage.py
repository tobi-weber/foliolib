# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.invoiceStorage")


class VoucherNumber(FolioApi):
    """Voucher Number

    **API used to manage voucher number.**
    """

    def get_voucherNumbers(self):
        """Get generated voucher number

        ``GET /voucher-storage/voucher-number``

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/VoucherNumber_get_voucherNumbers_return.schema 
        """
        return self.call("GET", "/voucher-storage/voucher-number")

    def get_starts(self):
        """Get voucher number start

        ``GET /voucher-storage/voucher-number/start``

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/VoucherNumber_get_starts_return.schema 
        """
        return self.call("GET", "/voucher-storage/voucher-number/start")

    def set_start(self, value: str):
        """(Re)set the start value of the voucher number sequence

        ``POST /voucher-storage/voucher-number/start/{value}``

        Args:
            value (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("POST", f"/voucher-storage/voucher-number/start/{value}")


class BatchGroup(FolioApi):
    """Batch group CRUD API

    This documents the API calls that can be made to manage batch groups; This API is intended for internal use only
    """

    def get_batchGroups(self, **kwargs):
        """Get list of batch groups

        ``GET /batch-group-storage/batch-groups``

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
                    
                    with valid searchable fields: for example name
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=="FOLIO"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/BatchGroup_get_batchGroups_return.schema 
        """
        return self.call("GET", "/batch-group-storage/batch-groups", query=kwargs)

    def set_batchGroup(self, batchGroup: dict):
        """Create a new batchGroup item.

        ``POST /batch-group-storage/batch-groups``

        Args:
            batchGroup (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created batchGroup item

        Schema:

            .. literalinclude:: ../files/BatchGroup_set_batchGroup_request.schema
        """
        return self.call("POST", "/batch-group-storage/batch-groups", data=batchGroup)

    def get_batchGroup(self, batchGroupsId: str):
        """Retrieve batchGroup item with given {batchGroupId}

        ``GET /batch-group-storage/batch-groups/{batchGroupsId}``

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
        return self.call("GET", f"/batch-group-storage/batch-groups/{batchGroupsId}")

    def delete_batchGroup(self, batchGroupsId: str):
        """Delete batchGroup item with given {batchGroupId}

        ``DELETE /batch-group-storage/batch-groups/{batchGroupsId}``

        Args:
            batchGroupsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/batch-group-storage/batch-groups/{batchGroupsId}")

    def modify_batchGroup(self, batchGroupsId: str, batchGroup: dict):
        """Update batchGroup item with given {batchGroupId}

        ``PUT /batch-group-storage/batch-groups/{batchGroupsId}``

        Args:
            batchGroupsId (str)
            batchGroup (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/BatchGroup_modify_batchGroup_request.schema
        """
        return self.call("PUT", f"/batch-group-storage/batch-groups/{batchGroupsId}", data=batchGroup)


class Invoice(FolioApi):
    """Invoice CRUD API

    This documents the API calls that can be made to manage invoices
    """

    def get_invoices(self, **kwargs):
        """Get list of invoices

        ``GET /invoice-storage/invoices``

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
                    
                    with valid searchable fields: for example folioInvoiceNo
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - folioInvoiceNo=="123invoicenumber45"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Invoice_get_invoices_return.schema 
        """
        return self.call("GET", "/invoice-storage/invoices", query=kwargs)

    def set_invoice(self, invoice: dict):
        """Create a new invoice item.

        ``POST /invoice-storage/invoices``

        Args:
            invoice (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created invoice item

        Schema:

            .. literalinclude:: ../files/Invoice_set_invoice_request.schema
        """
        return self.call("POST", "/invoice-storage/invoices", data=invoice)

    def get_invoice(self, invoicesId: str):
        """Retrieve invoice item with given {invoiceId}

        ``GET /invoice-storage/invoices/{invoicesId}``

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
        return self.call("GET", f"/invoice-storage/invoices/{invoicesId}")

    def delete_invoice(self, invoicesId: str):
        """Delete invoice item with given {invoiceId}

        ``DELETE /invoice-storage/invoices/{invoicesId}``

        Args:
            invoicesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/invoice-storage/invoices/{invoicesId}")

    def modify_invoice(self, invoicesId: str, invoice: dict):
        """Update invoice item with given {invoiceId}

        ``PUT /invoice-storage/invoices/{invoicesId}``

        Args:
            invoicesId (str)
            invoice (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Invoice_modify_invoice_request.schema
        """
        return self.call("PUT", f"/invoice-storage/invoices/{invoicesId}", data=invoice)

    def get_documents(self, invoicesId: str, **kwargs):
        """Get list of documents

        ``GET /invoice-storage/invoices/{invoicesId}/documents``

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
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Invoice_get_documents_return.schema 
        """
        return self.call("GET", f"/invoice-storage/invoices/{invoicesId}/documents", query=kwargs)

    def set_document(self, invoicesId: str, document: dict):
        """Create a new document item.

        ``POST /invoice-storage/invoices/{invoicesId}/documents``

        Args:
            invoicesId (str)
            document (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created document item

        Schema:

            .. literalinclude:: ../files/Invoice_set_document_request.schema
        """
        return self.call("POST", f"/invoice-storage/invoices/{invoicesId}/documents", data=document)

    def get_document(self, invoicesId: str, documentId: str):
        """Retrieve document item with given {documentId}

        ``GET /invoice-storage/invoices/{invoicesId}/documents/{documentId}``

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
        return self.call("GET", f"/invoice-storage/invoices/{invoicesId}/documents/{documentId}")

    def delete_document(self, invoicesId: str, documentId: str):
        """Delete document item with given {documentId}

        ``DELETE /invoice-storage/invoices/{invoicesId}/documents/{documentId}``

        Args:
            invoicesId (str)
            documentId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/invoice-storage/invoices/{invoicesId}/documents/{documentId}")

    def get_invoiceLines(self, **kwargs):
        """Get list of invoice lines

        ``GET /invoice-storage/invoice-lines``

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
                    
                    with valid searchable fields: for example poLineId
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - poLineId=="c0d08448-347b-418a-8c2f-5fb50248d67e"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Invoice_get_invoiceLines_return.schema 
        """
        return self.call("GET", "/invoice-storage/invoice-lines", query=kwargs)

    def set_invoiceLine(self, invoiceLine: dict):
        """Create a new invoiceLine item.

        ``POST /invoice-storage/invoice-lines``

        Args:
            invoiceLine (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created invoiceLine item

        Schema:

            .. literalinclude:: ../files/Invoice_set_invoiceLine_request.schema
        """
        return self.call("POST", "/invoice-storage/invoice-lines", data=invoiceLine)

    def get_invoiceLine(self, invoiceLinesId: str):
        """Retrieve invoiceLine item with given {invoiceLineId}

        ``GET /invoice-storage/invoice-lines/{invoiceLinesId}``

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
        return self.call("GET", f"/invoice-storage/invoice-lines/{invoiceLinesId}")

    def delete_invoiceLine(self, invoiceLinesId: str):
        """Delete invoiceLine item with given {invoiceLineId}

        ``DELETE /invoice-storage/invoice-lines/{invoiceLinesId}``

        Args:
            invoiceLinesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/invoice-storage/invoice-lines/{invoiceLinesId}")

    def modify_invoiceLine(self, invoiceLinesId: str, invoiceLine: dict):
        """Update invoiceLine item with given {invoiceLineId}

        ``PUT /invoice-storage/invoice-lines/{invoiceLinesId}``

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
        return self.call("PUT", f"/invoice-storage/invoice-lines/{invoiceLinesId}", data=invoiceLine)


class InvoiceNumber(FolioApi):
    """Invoice Number

    **API used to manage invoice number.**
    """

    def get_invoiceNumbers(self):
        """Get generated invoice number

        ``GET /invoice-storage/invoice-number``

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InvoiceNumber_get_invoiceNumbers_return.schema 
        """
        return self.call("GET", "/invoice-storage/invoice-number")


class BatchVoucherExportConfiguration(FolioApi):
    """Batch voucher export configurations CRUD API

    This documents the API calls that can be made to manage batch voucher export configurations; This API is intended for internal use only
    """

    def get_exportConfigurations(self, **kwargs):
        """Get list of batch voucher export configurations

        ``GET /batch-voucher-storage/export-configurations``

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
        return self.call("GET", "/batch-voucher-storage/export-configurations", query=kwargs)

    def set_exportConfiguration(self, exportConfiguration: dict):
        """Create a new exportConfiguration item.

        ``POST /batch-voucher-storage/export-configurations``

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
        return self.call("POST", "/batch-voucher-storage/export-configurations", data=exportConfiguration)

    def get_exportConfiguration(self, exportConfigurationsId: str):
        """Retrieve exportConfiguration item with given {exportConfigurationId}

        ``GET /batch-voucher-storage/export-configurations/{exportConfigurationsId}``

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
        return self.call("GET", f"/batch-voucher-storage/export-configurations/{exportConfigurationsId}")

    def delete_exportConfiguration(self, exportConfigurationsId: str):
        """Delete exportConfiguration item with given {exportConfigurationId}

        ``DELETE /batch-voucher-storage/export-configurations/{exportConfigurationsId}``

        Args:
            exportConfigurationsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/batch-voucher-storage/export-configurations/{exportConfigurationsId}")

    def modify_exportConfiguration(self, exportConfigurationsId: str, exportConfiguration: dict):
        """Update exportConfiguration item with given {exportConfigurationId}

        ``PUT /batch-voucher-storage/export-configurations/{exportConfigurationsId}``

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
        return self.call("PUT", f"/batch-voucher-storage/export-configurations/{exportConfigurationsId}", data=exportConfiguration)

    def set_exportConfiguration_by_exportConfigurationsId(self, exportConfigurationsId: str):
        """

        ``POST /batch-voucher-storage/export-configurations/{exportConfigurationsId}``

        Args:
            exportConfigurationsId (str)
        """
        return self.call("POST", f"/batch-voucher-storage/export-configurations/{exportConfigurationsId}")

    def get_credential(self, exportConfigurationsId: str):
        """Retrieve credential item with given {credentialId}

        ``GET /batch-voucher-storage/export-configurations/{exportConfigurationsId}/credentials``

        Args:
            exportConfigurationsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/BatchVoucherExportConfiguration_get_credential_return.schema 
        """
        return self.call("GET", f"/batch-voucher-storage/export-configurations/{exportConfigurationsId}/credentials")

    def delete_credential(self, exportConfigurationsId: str):
        """Delete credential item with given {credentialId}

        ``DELETE /batch-voucher-storage/export-configurations/{exportConfigurationsId}/credentials``

        Args:
            exportConfigurationsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/batch-voucher-storage/export-configurations/{exportConfigurationsId}/credentials")

    def modify_credential(self, exportConfigurationsId: str, credential: dict):
        """Update credential item with given {credentialId}

        ``PUT /batch-voucher-storage/export-configurations/{exportConfigurationsId}/credentials``

        Args:
            exportConfigurationsId (str)
            credential (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/BatchVoucherExportConfiguration_modify_credential_request.schema
        """
        return self.call("PUT", f"/batch-voucher-storage/export-configurations/{exportConfigurationsId}/credentials", data=credential)

    def set_credential(self, exportConfigurationsId: str):
        """

        ``POST /batch-voucher-storage/export-configurations/{exportConfigurationsId}/credentials``

        Args:
            exportConfigurationsId (str)
        """
        return self.call("POST", f"/batch-voucher-storage/export-configurations/{exportConfigurationsId}/credentials")


class BatchVoucherExports(FolioApi):
    """Batch voucher exports CRUD API

    This documents the API calls that can be made to manage batch voucher exports
    """

    def get_batchVoucherExports(self, **kwargs):
        """Get list of batch voucher exports

        ``GET /batch-voucher-storage/batch-voucher-exports``

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
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/BatchVoucherExports_get_batchVoucherExports_return.schema 
        """
        return self.call("GET", "/batch-voucher-storage/batch-voucher-exports", query=kwargs)

    def set_batchVoucherExport(self, batchVoucherExport: dict):
        """Create a new batchVoucherExport item.

        ``POST /batch-voucher-storage/batch-voucher-exports``

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
        return self.call("POST", "/batch-voucher-storage/batch-voucher-exports", data=batchVoucherExport)

    def get_batchVoucherExport(self, batchVoucherExportsId: str):
        """Retrieve batchVoucherExport item with given {batchVoucherExportId}

        ``GET /batch-voucher-storage/batch-voucher-exports/{batchVoucherExportsId}``

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
        return self.call("GET", f"/batch-voucher-storage/batch-voucher-exports/{batchVoucherExportsId}")

    def delete_batchVoucherExport(self, batchVoucherExportsId: str):
        """Delete batchVoucherExport item with given {batchVoucherExportId}

        ``DELETE /batch-voucher-storage/batch-voucher-exports/{batchVoucherExportsId}``

        Args:
            batchVoucherExportsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("DELETE", f"/batch-voucher-storage/batch-voucher-exports/{batchVoucherExportsId}")

    def modify_batchVoucherExport(self, batchVoucherExportsId: str, batchVoucherExport: dict):
        """Update batchVoucherExport item with given {batchVoucherExportId}

        ``PUT /batch-voucher-storage/batch-voucher-exports/{batchVoucherExportsId}``

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
        return self.call("PUT", f"/batch-voucher-storage/batch-voucher-exports/{batchVoucherExportsId}", data=batchVoucherExport)


class BatchVoucher(FolioApi):
    """Batch Vouchers CRUD API

    **API used to manage batch vouchers.**
    """

    def set_batchVoucher(self, batchVoucher: dict):
        """Process batchVouchers.

        ``POST /batch-voucher-storage/batch-vouchers``

        Args:
            batchVoucher (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created batchVoucher item

        Schema:

            .. literalinclude:: ../files/BatchVoucher_set_batchVoucher_request.schema
        """
        return self.call("POST", "/batch-voucher-storage/batch-vouchers", data=batchVoucher)

    def get_batchVouchers(self, batchVouchersId: str):
        """Retrieve batchVoucher item with given {batchVoucherId}

        ``GET /batch-voucher-storage/batch-vouchers/{batchVouchersId}``

        Args:
            batchVouchersId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/BatchVoucher_get_batchVouchers_return.schema 
        """
        return self.call("GET", f"/batch-voucher-storage/batch-vouchers/{batchVouchersId}")

    def delete_batchVoucher(self, batchVouchersId: str):
        """Delete batchVoucher item with given {batchVoucherId}

        ``DELETE /batch-voucher-storage/batch-vouchers/{batchVouchersId}``

        Args:
            batchVouchersId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("DELETE", f"/batch-voucher-storage/batch-vouchers/{batchVouchersId}")


class Voucher(FolioApi):
    """Vouchers CRUD API

    This documents the API calls that can be made to manage vouchers;This API is intended for internal use only
    """

    def get_vouchers(self, **kwargs):
        """Get list of vouchers

        ``GET /voucher-storage/vouchers``

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
                    
                    with valid searchable fields: for example voucherStatus
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - voucherStatus=="Paid"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Voucher_get_vouchers_return.schema 
        """
        return self.call("GET", "/voucher-storage/vouchers", query=kwargs)

    def set_voucher(self, voucher: dict):
        """Create a new voucher item.

        ``POST /voucher-storage/vouchers``

        Args:
            voucher (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created voucher item

        Schema:

            .. literalinclude:: ../files/Voucher_set_voucher_request.schema
        """
        return self.call("POST", "/voucher-storage/vouchers", data=voucher)

    def get_voucher(self, vouchersId: str):
        """Retrieve voucher item with given {voucherId}

        ``GET /voucher-storage/vouchers/{vouchersId}``

        Args:
            vouchersId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Voucher_get_voucher_return.schema 
        """
        return self.call("GET", f"/voucher-storage/vouchers/{vouchersId}")

    def delete_voucher(self, vouchersId: str):
        """Delete voucher item with given {voucherId}

        ``DELETE /voucher-storage/vouchers/{vouchersId}``

        Args:
            vouchersId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/voucher-storage/vouchers/{vouchersId}")

    def modify_voucher(self, vouchersId: str, voucher: dict):
        """Update voucher item with given {voucherId}

        ``PUT /voucher-storage/vouchers/{vouchersId}``

        Args:
            vouchersId (str)
            voucher (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Voucher_modify_voucher_request.schema
        """
        return self.call("PUT", f"/voucher-storage/vouchers/{vouchersId}", data=voucher)

    def get_voucherLines(self, **kwargs):
        """Get list of voucher lines

        ``GET /voucher-storage/voucher-lines``

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
                    
                    with valid searchable fields: for example externalAccountNumber
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - externalAccountNumber=="567891045"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Voucher_get_voucherLines_return.schema 
        """
        return self.call("GET", "/voucher-storage/voucher-lines", query=kwargs)

    def set_voucherLine(self, voucherLine: dict):
        """Create a new voucherLine item.

        ``POST /voucher-storage/voucher-lines``

        Args:
            voucherLine (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created voucherLine item

        Schema:

            .. literalinclude:: ../files/Voucher_set_voucherLine_request.schema
        """
        return self.call("POST", "/voucher-storage/voucher-lines", data=voucherLine)

    def get_voucherLine(self, voucherLinesId: str):
        """Retrieve voucherLine item with given {voucherLineId}

        ``GET /voucher-storage/voucher-lines/{voucherLinesId}``

        Args:
            voucherLinesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Voucher_get_voucherLine_return.schema 
        """
        return self.call("GET", f"/voucher-storage/voucher-lines/{voucherLinesId}")

    def delete_voucherLine(self, voucherLinesId: str):
        """Delete voucherLine item with given {voucherLineId}

        ``DELETE /voucher-storage/voucher-lines/{voucherLinesId}``

        Args:
            voucherLinesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/voucher-storage/voucher-lines/{voucherLinesId}")

    def modify_voucherLine(self, voucherLinesId: str, voucherLine: dict):
        """Update voucherLine item with given {voucherLineId}

        ``PUT /voucher-storage/voucher-lines/{voucherLinesId}``

        Args:
            voucherLinesId (str)
            voucherLine (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Voucher_modify_voucherLine_request.schema
        """
        return self.call("PUT", f"/voucher-storage/voucher-lines/{voucherLinesId}", data=voucherLine)


class InvoiceLineNumber(FolioApi):
    """Invoice Line Number

    **API used to manage Invoice Line number.  This API is intended for internal use only**
    """

    def get_invoiceLineNumbers(self, **kwargs):
        """Get invoice line number

        ``GET /invoice-storage/invoice-line-number``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            invoiceId (uuid):  The UUID of a invoice
                    
                    Example:
                    
                     - 8ad4b87b-9b47-4199-b0c3-5480745c6b41

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InvoiceLineNumber_get_invoiceLineNumbers_return.schema 
        """
        return self.call("GET", "/invoice-storage/invoice-line-number", query=kwargs)
