# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.fincConfig")


class FincConfigFilters(FolioApi):
    """mod-finc-config API

    This documents the API calls that can be made to query filters of metadata collections for all tenants/isils
    """

    def get_filters(self, **kwargs):
        """Get all filters

        ``GET /finc-config/filters``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ((label="test*") and type="Blacklist") sortby label
            orderBy (str):  Order by field: label, type
                    
            order (str (desc|asc):): (default=desc) Order
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

            .. literalinclude:: ../files/FincConfigFilters_get_filters_return.schema 
        """
        return self.call("GET", "/finc-config/filters", query=kwargs)

    def set_filter(self, filter: dict):
        """Post new filter

        ``POST /finc-config/filters``

        Args:
            filter (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created filter item

        Schema:

            .. literalinclude:: ../files/FincConfigFilters_set_filter_request.schema
        """
        return self.call("POST", "/finc-config/filters", data=filter)

    def get_filter(self, filtersId: str):
        """Get one finc config filter identified by id

        ``GET /finc-config/filters/{filtersId}``

        Args:
            filtersId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincConfigFilters_get_filter_return.schema 
        """
        return self.call("GET", f"/finc-config/filters/{filtersId}")

    def delete_filter(self, filtersId: str):
        """Delete a filter identified by id

        ``DELETE /finc-config/filters/{filtersId}``

        Args:
            filtersId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finc-config/filters/{filtersId}")

    def modify_filter(self, filtersId: str, filter: dict):
        """Put a filter identified by id

        ``PUT /finc-config/filters/{filtersId}``

        Args:
            filtersId (str)
            filter (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincConfigFilters_modify_filter_request.schema
        """
        return self.call("PUT", f"/finc-config/filters/{filtersId}", data=filter)

    def get_collections_by_filter(self, filtersId: str):
        """Get all metadata collections the current filter is assigned to

        ``GET /finc-config/filters/{filtersId}/collections``

        Args:
            filtersId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincConfigFilters_get_collections_by_filter_return.schema 
        """
        return self.call("GET", f"/finc-config/filters/{filtersId}/collections")

    def modify_collection(self, filtersId: str, collection: dict):
        """Add collections to this filter

        ``PUT /finc-config/filters/{filtersId}/collections``

        Args:
            filtersId (str)
            collection (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincConfigFilters_modify_collection_request.schema
        """
        return self.call("PUT", f"/finc-config/filters/{filtersId}/collections", data=collection)


class FincSelectEZBCredentials(FolioApi):
    """mod-finc-config EZB Credentials API

    This documents the API calls that can be made to query and manage EZB credentials for the current tenant/isil
    """

    def get_ezbCredentials(self):
        """Get the ezb credential of current tenant

        ``GET /finc-select/ezb-credentials``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincSelectEZBCredentials_get_ezbCredentials_return.schema 
        """
        return self.call("GET", "/finc-select/ezb-credentials")

    def modify_ezbCredential(self, ezbCredential: dict):
        """Add or edit an ezb credential entry

        ``PUT /finc-select/ezb-credentials``

        Args:
            ezbCredential (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincSelectEZBCredentials_modify_ezbCredential_request.schema
        """
        return self.call("PUT", "/finc-select/ezb-credentials", data=ezbCredential)

    def delete_ezbCredentials(self):
        """Delete ezb credential

        ``DELETE /finc-select/ezb-credentials``

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", "/finc-select/ezb-credentials")


class Isils(FolioApi):
    """mod-finc-config Isils API

    This documents the API calls that can be made to query and manage isils of the system
    """

    def get_isils(self, **kwargs):
        """Return a list of isisls

        ``GET /finc-config/isils``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
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

            .. literalinclude:: ../files/Isils_get_isils_return.schema 
        """
        return self.call("GET", "/finc-config/isils", query=kwargs)

    def set_isil(self, isil: dict):
        """Create an isil

        ``POST /finc-config/isils``

        Args:
            isil (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created isil item

        Schema:

            .. literalinclude:: ../files/Isils_set_isil_request.schema
        """
        return self.call("POST", "/finc-config/isils", data=isil)

    def get_isil(self, isilsId: str):
        """Retrieve isil item with given {isilId}

        ``GET /finc-config/isils/{isilsId}``

        Args:
            isilsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Isils_get_isil_return.schema 
        """
        return self.call("GET", f"/finc-config/isils/{isilsId}")

    def delete_isil(self, isilsId: str):
        """Delete isil item with given {isilId}

        ``DELETE /finc-config/isils/{isilsId}``

        Args:
            isilsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finc-config/isils/{isilsId}")

    def modify_isil(self, isilsId: str, isil: dict):
        """Update isil item with given {isilId}

        ``PUT /finc-config/isils/{isilsId}``

        Args:
            isilsId (str)
            isil (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Isils_modify_isil_request.schema
        """
        return self.call("PUT", f"/finc-config/isils/{isilsId}", data=isil)


class FincSelectMetadataCollections(FolioApi):
    """mod-finc-config API

    This documents the API calls that can be made to query and manage metadata collections for the current tenant/isil
    """

    def get_metadataCollections(self, **kwargs):
        """Get all metadata collections

        ``GET /finc-select/metadata-collections``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ((label="Science*") and permitted="yes" and selected="no") sortby label
            orderBy (str):  Order by field: label, mdSource, permitted, filters, freeContent
                    
            order (str (desc|asc):): (default=desc) Order
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
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincSelectMetadataCollections_get_metadataCollections_return.schema 
        """
        return self.call("GET", "/finc-select/metadata-collections", query=kwargs)

    def get_metadataCollection(self, metadataCollectionsId: str):
        """Get one metadata collection identified by id

        ``GET /finc-select/metadata-collections/{metadataCollectionsId}``

        Args:
            metadataCollectionsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincSelectMetadataCollections_get_metadataCollection_return.schema 
        """
        return self.call("GET", f"/finc-select/metadata-collections/{metadataCollectionsId}")

    def get_select(self, metadataCollectionsId: str):
        """Retrieve select item with given {selectId}

        ``GET /finc-select/metadata-collections/{metadataCollectionsId}/select``

        Args:
            metadataCollectionsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincSelectMetadataCollections_get_select_return.schema 
        """
        return self.call("GET", f"/finc-select/metadata-collections/{metadataCollectionsId}/select")

    def delete_select(self, metadataCollectionsId: str):
        """Delete select item with given {selectId}

        ``DELETE /finc-select/metadata-collections/{metadataCollectionsId}/select``

        Args:
            metadataCollectionsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finc-select/metadata-collections/{metadataCollectionsId}/select")

    def modify_select(self, metadataCollectionsId: str, select: dict):
        """Put, if this metadata collection is selected resp. deselected

        ``PUT /finc-select/metadata-collections/{metadataCollectionsId}/select``

        Args:
            metadataCollectionsId (str)
            select (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincSelectMetadataCollections_modify_select_request.schema
        """
        return self.call("PUT", f"/finc-select/metadata-collections/{metadataCollectionsId}/select", data=select)


class FincConfigFiles(FolioApi):
    """mod-finc-config API

    This documents the API calls that can be made to query files for all tenants/isils
    """

    def upload_file(self, filePath: str, **kwargs):
        """Upload/update a finc select file.

        ``POST /finc-config/files``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            isil (str):  The isil this file is assigned to.

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        import os
        headers = {}
        headers["Content-Type"] = "application/octet-stream"
        headers["Content-length"] = str(os.path.getsize(filePath))
        headers["Content-Disposition"] = "attachment; filename=%s" % os.path.basename(
            filePath)
        with open(filePath, 'rb') as f:
            data = f.read()
        
        return self.call("POST", "/finc-config/files", headers=headers, data=data, query=kwargs)

    def get_file(self, filesId: str):
        """Get file by id

        ``GET /finc-config/files/{filesId}``

        Args:
            filesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("GET", f"/finc-config/files/{filesId}")

    def delete_file(self, filesId: str):
        """Delete a file identified by id

        ``DELETE /finc-config/files/{filesId}``

        Args:
            filesId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finc-config/files/{filesId}")


class FincSelectFilters(FolioApi):
    """mod-finc-config API

    This documents the API calls that can be made to query and manage filters of metadata collections for the current tenant/isil
    """

    def get_filters(self, **kwargs):
        """Get all filters of current tenant

        ``GET /finc-select/filters``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ((label="test*") and type="Blacklist") sortby label
            orderBy (str):  Order by field: label, type
                    
            order (str (desc|asc):): (default=desc) Order
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

            .. literalinclude:: ../files/FincSelectFilters_get_filters_return.schema 
        """
        return self.call("GET", "/finc-select/filters", query=kwargs)

    def set_filter(self, filter: dict):
        """Post new finc select filter for the current tenant

        ``POST /finc-select/filters``

        Args:
            filter (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created filter item

        Schema:

            .. literalinclude:: ../files/FincSelectFilters_set_filter_request.schema
        """
        return self.call("POST", "/finc-select/filters", data=filter)

    def get_filter(self, filtersId: str):
        """Get one finc select filter identified by id

        ``GET /finc-select/filters/{filtersId}``

        Args:
            filtersId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincSelectFilters_get_filter_return.schema 
        """
        return self.call("GET", f"/finc-select/filters/{filtersId}")

    def delete_filter(self, filtersId: str):
        """Delete a filter identified by id

        ``DELETE /finc-select/filters/{filtersId}``

        Args:
            filtersId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finc-select/filters/{filtersId}")

    def modify_filter(self, filtersId: str, filter: dict):
        """Put a filter identified by id

        ``PUT /finc-select/filters/{filtersId}``

        Args:
            filtersId (str)
            filter (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincSelectFilters_modify_filter_request.schema
        """
        return self.call("PUT", f"/finc-select/filters/{filtersId}", data=filter)

    def get_collections_by_filter(self, filtersId: str):
        """Get collections the current filter is assigned to

        ``GET /finc-select/filters/{filtersId}/collections``

        Args:
            filtersId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincSelectFilters_get_collections_by_filter_return.schema 
        """
        return self.call("GET", f"/finc-select/filters/{filtersId}/collections")

    def modify_collection(self, filtersId: str, collection: dict):
        """Add collections to this filter

        ``PUT /finc-select/filters/{filtersId}/collections``

        Args:
            filtersId (str)
            collection (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincSelectFilters_modify_collection_request.schema
        """
        return self.call("PUT", f"/finc-select/filters/{filtersId}/collections", data=collection)


class FincConfigEZBCredentials(FolioApi):
    """mod-finc-config EZB Credentials API

    This documents the API calls that can be made to query and manage EZB credentials for all tenants/isils
    """

    def get_ezbCredentials(self, **kwargs):
        """Return a list of ezb credentials (credentials of all tenants)

        ``GET /finc-config/ezb-credentials``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
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

            .. literalinclude:: ../files/FincConfigEZBCredentials_get_ezbCredentials_return.schema 
        """
        return self.call("GET", "/finc-config/ezb-credentials", query=kwargs)

    def set_ezbCredential(self, ezbCredential: dict):
        """Create an ezb credential

        ``POST /finc-config/ezb-credentials``

        Args:
            ezbCredential (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created ezbCredential item

        Schema:

            .. literalinclude:: ../files/FincConfigEZBCredentials_set_ezbCredential_request.schema
        """
        return self.call("POST", "/finc-config/ezb-credentials", data=ezbCredential)

    def get_ezbCredential(self, isil: str):
        """Get one ezb credentials entry by isil

        ``GET /finc-config/ezb-credentials/{isil}``

        Args:
            isil (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincConfigEZBCredentials_get_ezbCredential_return.schema 
        """
        return self.call("GET", f"/finc-config/ezb-credentials/{isil}")

    def delete_ezbCredential(self, isil: str):
        """Delete an ezb credentials entry identified by isil

        ``DELETE /finc-config/ezb-credentials/{isil}``

        Args:
            isil (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finc-config/ezb-credentials/{isil}")

    def modify_ezbCredential(self, isil: str, ezbCredential: dict):
        """Put an ezb credentials entry identified by isil

        ``PUT /finc-config/ezb-credentials/{isil}``

        Args:
            isil (str)
            ezbCredential (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincConfigEZBCredentials_modify_ezbCredential_request.schema
        """
        return self.call("PUT", f"/finc-config/ezb-credentials/{isil}", data=ezbCredential)


class FincSelectFiles(FolioApi):
    """mod-finc-config API

    This documents the API calls that can be made to query and manage files for the current tenant/isil
    """

    def upload_file(self, filePath: str):
        """Upload/update a finc select file.

        ``POST /finc-select/files``

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        import os
        headers = {}
        headers["Content-Type"] = "application/octet-stream"
        headers["Content-length"] = str(os.path.getsize(filePath))
        headers["Content-Disposition"] = "attachment; filename=%s" % os.path.basename(
            filePath)
        with open(filePath, 'rb') as f:
            data = f.read()
        
        return self.call("POST", "/finc-select/files", headers=headers, data=data)

    def get_file(self, filesId: str):
        """Get file by id

        ``GET /finc-select/files/{filesId}``

        Args:
            filesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("GET", f"/finc-select/files/{filesId}")

    def delete_file(self, filesId: str):
        """Delete a file identified by id

        ``DELETE /finc-select/files/{filesId}``

        Args:
            filesId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finc-select/files/{filesId}")


class FincConfigMetadataCollections(FolioApi):
    """mod-finc-config API

    This documents the API calls that can be made to query and manage metadata collections for all tenants/isils
    """

    def get_metadataCollections(self, **kwargs):
        """Get all metadata collections

        ``GET /finc-config/metadata-collections``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ((label="Science*") and metadataAvailable=("yes" or "no")) sortby label
            orderBy (str):  Order by field: label, mdSource, metadataAvailable, usageRestricted, permittedFor, freeContent
                    
            order (str (desc|asc):): (default=desc) Order
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

            .. literalinclude:: ../files/FincConfigMetadataCollections_get_metadataCollections_return.schema 
        """
        return self.call("GET", "/finc-config/metadata-collections", query=kwargs)

    def set_metadataCollection(self, metadataCollection: dict):
        """Post new metadata collection

        ``POST /finc-config/metadata-collections``

        Args:
            metadataCollection (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created metadataCollection item

        Schema:

            .. literalinclude:: ../files/FincConfigMetadataCollections_set_metadataCollection_request.schema
        """
        return self.call("POST", "/finc-config/metadata-collections", data=metadataCollection)

    def get_metadataCollection(self, metadataCollectionsId: str):
        """Get one metadata collection identified by id

        ``GET /finc-config/metadata-collections/{metadataCollectionsId}``

        Args:
            metadataCollectionsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincConfigMetadataCollections_get_metadataCollection_return.schema 
        """
        return self.call("GET", f"/finc-config/metadata-collections/{metadataCollectionsId}")

    def delete_metadataCollection(self, metadataCollectionsId: str):
        """Delete an metadata collection identified by id

        ``DELETE /finc-config/metadata-collections/{metadataCollectionsId}``

        Args:
            metadataCollectionsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finc-config/metadata-collections/{metadataCollectionsId}")

    def modify_metadataCollection(self, metadataCollectionsId: str, metadataCollection: dict):
        """Put an metadata collection identified by id

        ``PUT /finc-config/metadata-collections/{metadataCollectionsId}``

        Args:
            metadataCollectionsId (str)
            metadataCollection (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincConfigMetadataCollections_modify_metadataCollection_request.schema
        """
        return self.call("PUT", f"/finc-config/metadata-collections/{metadataCollectionsId}", data=metadataCollection)


class FincSelectMetadataSources(FolioApi):
    """mod-finc-config API

    This documents the API calls that can be made to query and manage metadata sources for the current tenant/isil
    """

    def get_metadataSources(self, **kwargs):
        """Get all metadata sources

        ``GET /finc-select/metadata-sources``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ((label="Journals*") and status=("active" or "technical implementation") and selected="none") sortby label
            orderBy (str):  Order by field: label, sourceId, status, lastProcessed
                    
            order (str (desc|asc):): (default=desc) Order
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

            .. literalinclude:: ../files/FincSelectMetadataSources_get_metadataSources_return.schema 
        """
        return self.call("GET", "/finc-select/metadata-sources", query=kwargs)

    def set_metadataSource(self, metadataSource: dict):
        """Create a new metadataSource item.

        ``POST /finc-select/metadata-sources``

        Args:
            metadataSource (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created metadataSource item

        Schema:

            .. literalinclude:: ../files/FincSelectMetadataSources_set_metadataSource_request.schema
        """
        return self.call("POST", "/finc-select/metadata-sources", data=metadataSource)

    def get_metadataSource(self, metadataSourcesId: str):
        """Get one metadata source identified by id

        ``GET /finc-select/metadata-sources/{metadataSourcesId}``

        Args:
            metadataSourcesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincSelectMetadataSources_get_metadataSource_return.schema 
        """
        return self.call("GET", f"/finc-select/metadata-sources/{metadataSourcesId}")

    def delete_metadataSource(self, metadataSourcesId: str):
        """Delete metadataSource item with given {metadataSourceId}

        ``DELETE /finc-select/metadata-sources/{metadataSourcesId}``

        Args:
            metadataSourcesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finc-select/metadata-sources/{metadataSourcesId}")

    def modify_metadataSource(self, metadataSourcesId: str, metadataSource: dict):
        """Put, if all metadata collections of this source are selected resp. deselected

        ``PUT /finc-select/metadata-sources/{metadataSourcesId}``

        Args:
            metadataSourcesId (str)
            metadataSource (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincSelectMetadataSources_modify_metadataSource_request.schema
        """
        return self.call("PUT", f"/finc-select/metadata-sources/{metadataSourcesId}", data=metadataSource)

    def get_collections_by_metadataSource(self, metadataSourcesId: str):
        """Get metadata collections assigned to this metadata source

        ``GET /finc-select/metadata-sources/{metadataSourcesId}/collections``

        Args:
            metadataSourcesId (str)
        """
        return self.call("GET", f"/finc-select/metadata-sources/{metadataSourcesId}/collections")

    def get_selectAll(self, metadataSourcesId: str):
        """Retrieve selectAll item with given {selectAllId}

        ``GET /finc-select/metadata-sources/{metadataSourcesId}/collections/select-all``

        Args:
            metadataSourcesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincSelectMetadataSources_get_selectAll_return.schema 
        """
        return self.call("GET", f"/finc-select/metadata-sources/{metadataSourcesId}/collections/select-all")

    def delete_selectAll(self, metadataSourcesId: str):
        """Delete selectAll item with given {selectAllId}

        ``DELETE /finc-select/metadata-sources/{metadataSourcesId}/collections/select-all``

        Args:
            metadataSourcesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finc-select/metadata-sources/{metadataSourcesId}/collections/select-all")

    def modify_selectAll(self, metadataSourcesId: str, selectAll: dict):
        """Put, if all metadata collections of this source are selected resp. deselected

        ``PUT /finc-select/metadata-sources/{metadataSourcesId}/collections/select-all``

        Args:
            metadataSourcesId (str)
            selectAll (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincSelectMetadataSources_modify_selectAll_request.schema
        """
        return self.call("PUT", f"/finc-select/metadata-sources/{metadataSourcesId}/collections/select-all", data=selectAll)


class FincConfigMetadataSources(FolioApi):
    """mod-finc-config API

    This documents the API calls that can be made to query and manage metadata sources for all tenants/isils
    """

    def get_metadataSources(self, **kwargs):
        """Get all metadata sources

        ``GET /finc-config/metadata-sources``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ((label="Journals*" or sourceId="Journals*") and status=("active" or "technical implementation")) sortby label
            orderBy (str):  Order by field: label, sourceId, status, solrShard, lastProcessed
                    
            order (str (desc|asc):): (default=desc) Order
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

            .. literalinclude:: ../files/FincConfigMetadataSources_get_metadataSources_return.schema 
        """
        return self.call("GET", "/finc-config/metadata-sources", query=kwargs)

    def set_metadataSource(self, metadataSource: dict):
        """Post new metadata source

        ``POST /finc-config/metadata-sources``

        Args:
            metadataSource (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created metadataSource item

        Schema:

            .. literalinclude:: ../files/FincConfigMetadataSources_set_metadataSource_request.schema
        """
        return self.call("POST", "/finc-config/metadata-sources", data=metadataSource)

    def get_metadataSource(self, metadataSourcesId: str):
        """Get one metadata source identified by id

        ``GET /finc-config/metadata-sources/{metadataSourcesId}``

        Args:
            metadataSourcesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincConfigMetadataSources_get_metadataSource_return.schema 
        """
        return self.call("GET", f"/finc-config/metadata-sources/{metadataSourcesId}")

    def delete_metadataSource(self, metadataSourcesId: str):
        """Delete an metadata source identified by id

        ``DELETE /finc-config/metadata-sources/{metadataSourcesId}``

        Args:
            metadataSourcesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/finc-config/metadata-sources/{metadataSourcesId}")

    def modify_metadataSource(self, metadataSourcesId: str, metadataSource: dict):
        """Put an metadata source identified by id

        ``PUT /finc-config/metadata-sources/{metadataSourcesId}``

        Args:
            metadataSourcesId (str)
            metadataSource (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FincConfigMetadataSources_modify_metadataSource_request.schema
        """
        return self.call("PUT", f"/finc-config/metadata-sources/{metadataSourcesId}", data=metadataSource)

    def get_tinyMetadataSources(self, **kwargs):
        """Get all tiny metadata sources

        ``GET /finc-config/tiny-metadata-sources``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ((label="Journals*" or sourceId="Journals*") and status=("active" or "technical implementation")) sortby label
            orderBy (str):  Order by field: label, sourceId, status, solrShard, lastProcessed
                    
            order (str (desc|asc):): (default=desc) Order
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

            .. literalinclude:: ../files/FincConfigMetadataSources_get_tinyMetadataSources_return.schema 
        """
        return self.call("GET", "/finc-config/tiny-metadata-sources", query=kwargs)

    def set_tinyMetadataSource(self, tinyMetadataSource: dict):
        """Post new metadata source

        ``POST /finc-config/tiny-metadata-sources``

        Args:
            tinyMetadataSource (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created tinyMetadataSource item

        Schema:

            .. literalinclude:: ../files/FincConfigMetadataSources_set_tinyMetadataSource_request.schema
        """
        return self.call("POST", "/finc-config/tiny-metadata-sources", data=tinyMetadataSource)

    def get_contacts(self, **kwargs):
        """Get all contacts defined in metadata sources

        ``GET /finc-config/contacts``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ((label="Journals*" or sourceId="Journals*") and status=("active" or "technical implementation")) sortby label
            orderBy (str):  Order by field: label, sourceId, status, solrShard, lastProcessed
                    
            order (str (desc|asc):): (default=desc) Order
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

            .. literalinclude:: ../files/FincConfigMetadataSources_get_contacts_return.schema 
        """
        return self.call("GET", "/finc-config/contacts", query=kwargs)

    def set_contact(self, contact: dict):
        """Post new metadata source

        ``POST /finc-config/contacts``

        Args:
            contact (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created contact item

        Schema:

            .. literalinclude:: ../files/FincConfigMetadataSources_set_contact_request.schema
        """
        return self.call("POST", "/finc-config/contacts", data=contact)
