# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.inventoryStorage")


class ItemDamagedStatuses(FolioApi):
    """Item dameged statuses API

    This documents the API calls that can be made to query and manage item dameged statuses of the system
    """

    def get_itemDamagedStatuses(self, **kwargs):
        """Return a list of item damaged status

        ``GET /item-damaged-statuses``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/ItemDamagedStatuses_get_itemDamagedStatuses_return.schema 
        """
        return self.call("GET", "/item-damaged-statuses", query=kwargs)

    def set_itemDamagedStatus(self, itemDamagedStatus: dict):
        """Create a new item damaged status

        ``POST /item-damaged-statuses``

        Args:
            itemDamagedStatus (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created itemDamagedStatus item

        Schema:

            .. literalinclude:: ../files/ItemDamagedStatuses_set_itemDamagedStatus_request.schema
        """
        return self.call("POST", "/item-damaged-statuses", data=itemDamagedStatus)

    def get_itemDamagedStatus(self, itemDamagedStatusesId: str):
        """Retrieve itemDamagedStatus item with given {itemDamagedStatusId}

        ``GET /item-damaged-statuses/{itemDamagedStatusesId}``

        Args:
            itemDamagedStatusesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ItemDamagedStatuses_get_itemDamagedStatus_return.schema 
        """
        return self.call("GET", f"/item-damaged-statuses/{itemDamagedStatusesId}")

    def delete_itemDamagedStatus(self, itemDamagedStatusesId: str):
        """Delete itemDamagedStatus item with given {itemDamagedStatusId}

        ``DELETE /item-damaged-statuses/{itemDamagedStatusesId}``

        Args:
            itemDamagedStatusesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/item-damaged-statuses/{itemDamagedStatusesId}")

    def modify_itemDamagedStatus(self, itemDamagedStatusesId: str, itemDamagedStatus: dict):
        """Update itemDamagedStatus item with given {itemDamagedStatusId}

        ``PUT /item-damaged-statuses/{itemDamagedStatusesId}``

        Args:
            itemDamagedStatusesId (str)
            itemDamagedStatus (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ItemDamagedStatuses_modify_itemDamagedStatus_request.schema
        """
        return self.call("PUT", f"/item-damaged-statuses/{itemDamagedStatusesId}", data=itemDamagedStatus)


class HoldingsSyncUnsafe(FolioApi):
    """Inventory Storage Holdings Batch Sync Unsafe API

    **Batch API for synchronously uploading holdings records into the inventory with optimistic locking disabled**
    """

    def set_synchronousUnsafe(self, synchronousUnsafe: dict):
        """Create or update a collection of holdings in a single synchronous request; if any holding fails the complete batch will be rejected (all or nothing). Environment variable DB_ALLOW_SUPPRESS_OPTIMISTIC_LOCKING is required, see https://github.com/folio-org/raml-module-builder#environment-variables for details. The _version property is ignored, optimistic locking is disabled - this is known to lead to data loss in some cases, don't use in production, you have been warned!

        ``POST /holdings-storage/batch/synchronous-unsafe``

        Args:
            synchronousUnsafe (dict): See Schema below

        Raises:
            OkapiRequestPayloadToLarge: Payload Too Large
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/HoldingsSyncUnsafe_set_synchronousUnsafe_request.schema
        """
        return self.call("POST", "/holdings-storage/batch/synchronous-unsafe", data=synchronousUnsafe)


class ItemSync(FolioApi):
    """Inventory Storage Item Batch Sync API

    **Batch API for synchronously uploading items into the inventory**
    """

    def set_synchronou(self, synchronou: dict, **kwargs):
        """Create or update a collection of items in a single synchronous request; if any item fails the complete batch will be rejected (all or nothing)

        ``POST /item-storage/batch/synchronous``

        Args:
            synchronou (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            upsert (bool): (default=False) When a record with the same id already exists upsert=true will update it, upsert=false will fail the complete batch. The _version property of each item to be updated must match the stored _version property (optimistic locking).

        Raises:
            OkapiRequestConflict: Conflict
            OkapiRequestPayloadToLarge: Payload Too Large
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ItemSync_set_synchronou_request.schema
        """
        return self.call("POST", "/item-storage/batch/synchronous", data=synchronou, query=kwargs)


class InstanceFormat(FolioApi):
    """Instance Formats API

    This documents the API calls that can be made to query and manage instance formats
    """

    def get_instanceFormats(self, **kwargs):
        """Return a list of instance formats

        ``GET /instance-formats``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/InstanceFormat_get_instanceFormats_return.schema 
        """
        return self.call("GET", "/instance-formats", query=kwargs)

    def set_instanceFormat(self, instanceFormat: dict):
        """Create a new instance format

        ``POST /instance-formats``

        Args:
            instanceFormat (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created instanceFormat item

        Schema:

            .. literalinclude:: ../files/InstanceFormat_set_instanceFormat_request.schema
        """
        return self.call("POST", "/instance-formats", data=instanceFormat)

    def get_instanceFormat(self, instanceFormatId: str):
        """Retrieve instanceFormat item with given {instanceFormatId}

        ``GET /instance-formats/{instanceFormatId}``

        Args:
            instanceFormatId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceFormat_get_instanceFormat_return.schema 
        """
        return self.call("GET", f"/instance-formats/{instanceFormatId}")

    def delete_instanceFormat(self, instanceFormatId: str):
        """Delete instanceFormat item with given {instanceFormatId}

        ``DELETE /instance-formats/{instanceFormatId}``

        Args:
            instanceFormatId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/instance-formats/{instanceFormatId}")

    def modify_instanceFormat(self, instanceFormatId: str, instanceFormat: dict):
        """Update instanceFormat item with given {instanceFormatId}

        ``PUT /instance-formats/{instanceFormatId}``

        Args:
            instanceFormatId (str)
            instanceFormat (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceFormat_modify_instanceFormat_request.schema
        """
        return self.call("PUT", f"/instance-formats/{instanceFormatId}", data=instanceFormat)


class InstancePrecedingSucceedingTitles(FolioApi):
    """Preceding/succeeding Titles API

    **Storage for preceding/succeeding titles in the inventory**
    """

    def get_precedingSucceedingTitles(self, **kwargs):
        """Return a list of preceding succeeding titles

        ``GET /preceding-succeeding-titles``

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
                    
                    by preceding instance ID or by succeeding instance ID (using CQL))
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - precedingInstanceId==83a50dc6-b887-43d9-93ee-28b2c4cd11f8 succeedingInstanceId==30fcc8e7-a019-43f4-b642-2edc389f4501

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/InstancePrecedingSucceedingTitles_get_precedingSucceedingTitles_return.schema 
        """
        return self.call("GET", "/preceding-succeeding-titles", query=kwargs)

    def set_precedingSucceedingTitle(self, precedingSucceedingTitle: dict):
        """Create a new preceding/succeeding title

        ``POST /preceding-succeeding-titles``

        Args:
            precedingSucceedingTitle (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created precedingSucceedingTitle item

        Schema:

            .. literalinclude:: ../files/InstancePrecedingSucceedingTitles_set_precedingSucceedingTitle_request.schema
        """
        return self.call("POST", "/preceding-succeeding-titles", data=precedingSucceedingTitle)

    def get_precedingSucceedingTitle(self, precedingSucceedingTitleId: str):
        """Get a preceding/succeeding title by id

        ``GET /preceding-succeeding-titles/{precedingSucceedingTitleId}``

        Args:
            precedingSucceedingTitleId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/InstancePrecedingSucceedingTitles_get_precedingSucceedingTitle_return.schema 
        """
        return self.call("GET", f"/preceding-succeeding-titles/{precedingSucceedingTitleId}")

    def delete_precedingSucceedingTitle(self, precedingSucceedingTitleId: str, **kwargs):
        """Delete a preceding/succeeding title by id

        ``DELETE /preceding-succeeding-titles/{precedingSucceedingTitleId}``

        Args:
            precedingSucceedingTitleId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/preceding-succeeding-titles/{precedingSucceedingTitleId}", query=kwargs)

    def modify_precedingSucceedingTitle(self, precedingSucceedingTitleId: str, precedingSucceedingTitle: dict):
        """Update a preceding/succeeding title by id

        ``PUT /preceding-succeeding-titles/{precedingSucceedingTitleId}``

        Args:
            precedingSucceedingTitleId (str)
            precedingSucceedingTitle (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/InstancePrecedingSucceedingTitles_modify_precedingSucceedingTitle_request.schema
        """
        return self.call("PUT", f"/preceding-succeeding-titles/{precedingSucceedingTitleId}", data=precedingSucceedingTitle)

    def modify_instance(self, instanceId: str, instance: dict):
        """Update preceding/succeeding titles related to the instance

        ``PUT /preceding-succeeding-titles/instances/{instanceId}``

        Args:
            instanceId (str)
            instance (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/InstancePrecedingSucceedingTitles_modify_instance_request.schema
        """
        return self.call("PUT", f"/preceding-succeeding-titles/instances/{instanceId}", data=instance)


class InstanceSyncUnsafe(FolioApi):
    """Inventory Storage Instance Batch Sync Unsafe API

    **Batch API for synchronously uploading instances into the inventory with optimistic locking disabled**
    """

    def set_synchronousUnsafe(self, synchronousUnsafe: dict):
        """Create or update a collection of instances in a single synchronous request; if any instance fails the complete batch will be rejected (all or nothing). Environment variable DB_ALLOW_SUPPRESS_OPTIMISTIC_LOCKING is required, see https://github.com/folio-org/raml-module-builder#environment-variables for details. The _version property is ignored, optimistic locking is disabled - this is known to lead to data loss in some cases, don't use in production, you have been warned!

        ``POST /instance-storage/batch/synchronous-unsafe``

        Args:
            synchronousUnsafe (dict): See Schema below

        Raises:
            OkapiRequestPayloadToLarge: Payload Too Large
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceSyncUnsafe_set_synchronousUnsafe_request.schema
        """
        return self.call("POST", "/instance-storage/batch/synchronous-unsafe", data=synchronousUnsafe)


class ModeOfIssuance(FolioApi):
    """Statistical code reference API

    This documents the API calls that can be made to query and manage issuance modes of the system
    """

    def get_modesOfIssuance(self, **kwargs):
        """Return a list of issuance modes

        ``GET /modes-of-issuance``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/ModeOfIssuance_get_modesOfIssuance_return.schema 
        """
        return self.call("GET", "/modes-of-issuance", query=kwargs)

    def set_modeOfIssuance(self, modeOfIssuance: dict):
        """Create a new mode of issuance

        ``POST /modes-of-issuance``

        Args:
            modeOfIssuance (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created modeOfIssuance item

        Schema:

            .. literalinclude:: ../files/ModeOfIssuance_set_modeOfIssuance_request.schema
        """
        return self.call("POST", "/modes-of-issuance", data=modeOfIssuance)

    def delete_modesOfIssuance(self):
        """

        ``DELETE /modes-of-issuance``
        """
        return self.call("DELETE", "/modes-of-issuance")

    def get_modeOfIssuance(self, modeOfIssuanceId: str):
        """Retrieve modeOfIssuance item with given {modeOfIssuanceId}

        ``GET /modes-of-issuance/{modeOfIssuanceId}``

        Args:
            modeOfIssuanceId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ModeOfIssuance_get_modeOfIssuance_return.schema 
        """
        return self.call("GET", f"/modes-of-issuance/{modeOfIssuanceId}")

    def delete_modeOfIssuance(self, modeOfIssuanceId: str):
        """Delete modeOfIssuance item with given {modeOfIssuanceId}

        ``DELETE /modes-of-issuance/{modeOfIssuanceId}``

        Args:
            modeOfIssuanceId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/modes-of-issuance/{modeOfIssuanceId}")

    def modify_modeOfIssuance(self, modeOfIssuanceId: str, modeOfIssuance: dict):
        """Update modeOfIssuance item with given {modeOfIssuanceId}

        ``PUT /modes-of-issuance/{modeOfIssuanceId}``

        Args:
            modeOfIssuanceId (str)
            modeOfIssuance (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ModeOfIssuance_modify_modeOfIssuance_request.schema
        """
        return self.call("PUT", f"/modes-of-issuance/{modeOfIssuanceId}", data=modeOfIssuance)


class InventoryView(FolioApi):
    """Inventory view

    Inventory view endpoints
    """

    def get_instances(self, **kwargs):
        """Get instances by id with their holdings and items

        ``GET /inventory-view/instances``

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
                    
                    using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - title="*uproot*"

        Returns:
            binary: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InventoryView_get_instances_return.schema 
        """
        return self.call("GET", "/inventory-view/instances", query=kwargs)


class InventoryHierarchy(FolioApi):
    """Inventory Hierarchy API

    This documents the streaming API for the data needed for Inventory Storage, RTAC and other modules
    """

    def get_updatedInstanceIds(self):
        """Stream updated instances ids for Inventory

        ``GET /inventory-hierarchy/updated-instance-ids``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/InventoryHierarchy_get_updatedInstanceIds_return.schema 
        """
        return self.call("GET", "/inventory-hierarchy/updated-instance-ids")

    def set_itemsAndHolding(self, itemsAndHolding: dict):
        """Stream instances view data for Inventory

        ``POST /inventory-hierarchy/items-and-holdings``

        Args:
            itemsAndHolding (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/InventoryHierarchy_set_itemsAndHolding_request.schema
            .. literalinclude:: ../files/InventoryHierarchy_set_itemsAndHolding_return.schema 
        """
        return self.call("POST", "/inventory-hierarchy/items-and-holdings", data=itemsAndHolding)


class OaiPmhView(FolioApi):
    """OAI-PMH view API

    This documents the streaming API for the data needed for OAI-PMH
    """

    def get_instances(self):
        """Stream data for oai-pmh

        ``GET /oai-pmh-view/instances``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/OaiPmhView_get_instances_return.schema 
        """
        return self.call("GET", "/oai-pmh-view/instances")

    def get_updatedInstanceIds(self):
        """Stream updated instances ids for oai-pmh

        ``GET /oai-pmh-view/updatedInstanceIds``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/OaiPmhView_get_updatedInstanceIds_return.schema 
        """
        return self.call("GET", "/oai-pmh-view/updatedInstanceIds")

    def set_enrichedInstance(self, enrichedInstance: dict):
        """Stream instances view data for oai-pmh

        ``POST /oai-pmh-view/enrichedInstances``

        Args:
            enrichedInstance (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/OaiPmhView_set_enrichedInstance_request.schema
            .. literalinclude:: ../files/OaiPmhView_set_enrichedInstance_return.schema 
        """
        return self.call("POST", "/oai-pmh-view/enrichedInstances", data=enrichedInstance)


class IllPolicy(FolioApi):
    """ILL policy API

    This documents the API calls that can be made to query and manage ILL policies of the system
    """

    def get_illPolicies(self, **kwargs):
        """Return a list of ILL policy types

        ``GET /ill-policies``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/IllPolicy_get_illPolicies_return.schema 
        """
        return self.call("GET", "/ill-policies", query=kwargs)

    def set_illPolicy(self, illPolicy: dict):
        """Create a new ILL policy

        ``POST /ill-policies``

        Args:
            illPolicy (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created illPolicy item

        Schema:

            .. literalinclude:: ../files/IllPolicy_set_illPolicy_request.schema
        """
        return self.call("POST", "/ill-policies", data=illPolicy)

    def get_illPolicy(self, illPoliciesId: str):
        """Retrieve illPolicy item with given {illPolicyId}

        ``GET /ill-policies/{illPoliciesId}``

        Args:
            illPoliciesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/IllPolicy_get_illPolicy_return.schema 
        """
        return self.call("GET", f"/ill-policies/{illPoliciesId}")

    def delete_illPolicy(self, illPoliciesId: str):
        """Delete illPolicy item with given {illPolicyId}

        ``DELETE /ill-policies/{illPoliciesId}``

        Args:
            illPoliciesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/ill-policies/{illPoliciesId}")

    def modify_illPolicy(self, illPoliciesId: str, illPolicy: dict):
        """Update illPolicy item with given {illPolicyId}

        ``PUT /ill-policies/{illPoliciesId}``

        Args:
            illPoliciesId (str)
            illPolicy (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/IllPolicy_modify_illPolicy_request.schema
        """
        return self.call("PUT", f"/ill-policies/{illPoliciesId}", data=illPolicy)


class StatisticalCodeType(FolioApi):
    """Statistical code type reference API

    This documents the API calls that can be made to query and manage statistical code types of the system
    """

    def get_statisticalCodeTypes(self, **kwargs):
        """Return a list of statistical code types

        ``GET /statistical-code-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/StatisticalCodeType_get_statisticalCodeTypes_return.schema 
        """
        return self.call("GET", "/statistical-code-types", query=kwargs)

    def set_statisticalCodeType(self, statisticalCodeType: dict):
        """Create a new statistical code type

        ``POST /statistical-code-types``

        Args:
            statisticalCodeType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created statisticalCodeType item

        Schema:

            .. literalinclude:: ../files/StatisticalCodeType_set_statisticalCodeType_request.schema
        """
        return self.call("POST", "/statistical-code-types", data=statisticalCodeType)

    def delete_statisticalCodeTypes(self):
        """

        ``DELETE /statistical-code-types``
        """
        return self.call("DELETE", "/statistical-code-types")

    def get_statisticalCodeType(self, statisticalCodeTypeId: str):
        """Retrieve statisticalCodeType item with given {statisticalCodeTypeId}

        ``GET /statistical-code-types/{statisticalCodeTypeId}``

        Args:
            statisticalCodeTypeId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/StatisticalCodeType_get_statisticalCodeType_return.schema 
        """
        return self.call("GET", f"/statistical-code-types/{statisticalCodeTypeId}")

    def delete_statisticalCodeType(self, statisticalCodeTypeId: str):
        """Delete statisticalCodeType item with given {statisticalCodeTypeId}

        ``DELETE /statistical-code-types/{statisticalCodeTypeId}``

        Args:
            statisticalCodeTypeId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/statistical-code-types/{statisticalCodeTypeId}")

    def modify_statisticalCodeType(self, statisticalCodeTypeId: str, statisticalCodeType: dict):
        """Update statisticalCodeType item with given {statisticalCodeTypeId}

        ``PUT /statistical-code-types/{statisticalCodeTypeId}``

        Args:
            statisticalCodeTypeId (str)
            statisticalCodeType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/StatisticalCodeType_modify_statisticalCodeType_request.schema
        """
        return self.call("PUT", f"/statistical-code-types/{statisticalCodeTypeId}", data=statisticalCodeType)


class AuthoritiesReindex(FolioApi):
    """Authority reindex

    Reindex authorities by generating domain events for them
    """

    def get_reindices(self, **kwargs):
        """Get all reindex jobs

        ``GET /authority-storage/reindex``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/AuthoritiesReindex_get_reindices_return.schema 
        """
        return self.call("GET", "/authority-storage/reindex", query=kwargs)

    def set_reindex(self):
        """

        ``POST /authority-storage/reindex``
        """
        return self.call("POST", "/authority-storage/reindex")

    def get_reindex(self, reindexId: str):
        """Get reindex job by id

        ``GET /authority-storage/reindex/{reindexId}``

        Args:
            reindexId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AuthoritiesReindex_get_reindex_return.schema 
        """
        return self.call("GET", f"/authority-storage/reindex/{reindexId}")

    def delete_reindex(self, reindexId: str):
        """Cancell reindex job by id

        ``DELETE /authority-storage/reindex/{reindexId}``

        Args:
            reindexId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/authority-storage/reindex/{reindexId}")


class HoldingsStorage(FolioApi):
    """Holdings Records Storage API

    **Storage for holdings in the inventory**
    """

    def get_holdings(self, **kwargs):
        """Retrieve a list of holding items.

        ``GET /holdings-storage/holdings``

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
                    
                    by instance ID (using CQL)
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - instanceId="2b94c631-fca9-4892-a730-03ee529ffe2a"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/HoldingsStorage_get_holdings_return.schema 
        """
        return self.call("GET", "/holdings-storage/holdings", query=kwargs)

    def set_holding(self, holding: dict):
        """Create a new holding item.

        ``POST /holdings-storage/holdings``

        Args:
            holding (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created holding item

        Schema:

            .. literalinclude:: ../files/HoldingsStorage_set_holding_request.schema
        """
        return self.call("POST", "/holdings-storage/holdings", data=holding)

    def delete_holdings(self):
        """

        ``DELETE /holdings-storage/holdings``
        """
        return self.call("DELETE", "/holdings-storage/holdings")

    def get_holding(self, holdingsRecordId: str):
        """Retrieve holding item with given {holdingId}

        ``GET /holdings-storage/holdings/{holdingsRecordId}``

        Args:
            holdingsRecordId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/HoldingsStorage_get_holding_return.schema 
        """
        return self.call("GET", f"/holdings-storage/holdings/{holdingsRecordId}")

    def delete_holding(self, holdingsRecordId: str):
        """Delete holding item with given {holdingId}

        ``DELETE /holdings-storage/holdings/{holdingsRecordId}``

        Args:
            holdingsRecordId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/holdings-storage/holdings/{holdingsRecordId}")

    def modify_holding(self, holdingsRecordId: str, holding: dict):
        """Update holding item with given {holdingId}

        ``PUT /holdings-storage/holdings/{holdingsRecordId}``

        Args:
            holdingsRecordId (str)
            holding (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/HoldingsStorage_modify_holding_request.schema
        """
        return self.call("PUT", f"/holdings-storage/holdings/{holdingsRecordId}", data=holding)


class RecordBulk(FolioApi):
    """Inventory Storage records Bulk Download API

    **API for downloading a bulk set of instances or holdings IDs**
    """

    def get_ids(self, **kwargs):
        """Retrieve a list of record IDs.

        ``GET /record-bulk/ids``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/RecordBulk_get_ids_return.schema 
        """
        return self.call("GET", "/record-bulk/ids", query=kwargs)


class AuthoritySourceFile(FolioApi):
    """Authority source files API

    This documents the API calls that can be made to query and manage Authority source files
    """

    def get_authoritySourceFiles(self, **kwargs):
        """Return a list of authority source files

        ``GET /authority-source-files``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/AuthoritySourceFile_get_authoritySourceFiles_return.schema 
        """
        return self.call("GET", "/authority-source-files", query=kwargs)

    def set_authoritySourceFile(self, authoritySourceFile: dict):
        """Create a new authority source file

        ``POST /authority-source-files``

        Args:
            authoritySourceFile (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created authoritySourceFile item

        Schema:

            .. literalinclude:: ../files/AuthoritySourceFile_set_authoritySourceFile_request.schema
        """
        return self.call("POST", "/authority-source-files", data=authoritySourceFile)

    def get_authoritySourceFile(self, authoritySourceFilesId: str):
        """Retrieve authoritySourceFile item with given {authoritySourceFileId}

        ``GET /authority-source-files/{authoritySourceFilesId}``

        Args:
            authoritySourceFilesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AuthoritySourceFile_get_authoritySourceFile_return.schema 
        """
        return self.call("GET", f"/authority-source-files/{authoritySourceFilesId}")

    def delete_authoritySourceFile(self, authoritySourceFilesId: str):
        """Delete authoritySourceFile item with given {authoritySourceFileId}

        ``DELETE /authority-source-files/{authoritySourceFilesId}``

        Args:
            authoritySourceFilesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/authority-source-files/{authoritySourceFilesId}")

    def modify_authoritySourceFile(self, authoritySourceFilesId: str, authoritySourceFile: dict):
        """Update authoritySourceFile item with given {authoritySourceFileId}

        ``PUT /authority-source-files/{authoritySourceFilesId}``

        Args:
            authoritySourceFilesId (str)
            authoritySourceFile (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AuthoritySourceFile_modify_authoritySourceFile_request.schema
        """
        return self.call("PUT", f"/authority-source-files/{authoritySourceFilesId}", data=authoritySourceFile)


class ServicePointsUser(FolioApi):
    """Service Points Users API

    This documents the API calls that can be made to query and manage service points users in the system
    """

    def get_servicePointsUsers(self, **kwargs):
        """Return a list of service points users

        ``GET /service-points-users``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/ServicePointsUser_get_servicePointsUsers_return.schema 
        """
        return self.call("GET", "/service-points-users", query=kwargs)

    def set_servicePointsUser(self, servicePointsUser: dict):
        """Create a new service points user

        ``POST /service-points-users``

        Args:
            servicePointsUser (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created servicePointsUser item

        Schema:

            .. literalinclude:: ../files/ServicePointsUser_set_servicePointsUser_request.schema
        """
        return self.call("POST", "/service-points-users", data=servicePointsUser)

    def delete_servicePointsUsers(self):
        """

        ``DELETE /service-points-users``
        """
        return self.call("DELETE", "/service-points-users")

    def get_servicePointsUser(self, servicePointsUserId: str):
        """Retrieve servicePointsUser item with given {servicePointsUserId}

        ``GET /service-points-users/{servicePointsUserId}``

        Args:
            servicePointsUserId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ServicePointsUser_get_servicePointsUser_return.schema 
        """
        return self.call("GET", f"/service-points-users/{servicePointsUserId}")

    def delete_servicePointsUser(self, servicePointsUserId: str):
        """Delete servicePointsUser item with given {servicePointsUserId}

        ``DELETE /service-points-users/{servicePointsUserId}``

        Args:
            servicePointsUserId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/service-points-users/{servicePointsUserId}")

    def modify_servicePointsUser(self, servicePointsUserId: str, servicePointsUser: dict):
        """Update servicePointsUser item with given {servicePointsUserId}

        ``PUT /service-points-users/{servicePointsUserId}``

        Args:
            servicePointsUserId (str)
            servicePointsUser (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ServicePointsUser_modify_servicePointsUser_request.schema
        """
        return self.call("PUT", f"/service-points-users/{servicePointsUserId}", data=servicePointsUser)


class ItemStorage(FolioApi):
    """Item Storage API

    **Storage for items in the inventory**
    """

    def get_items(self, **kwargs):
        """Retrieve a list of item items.

        ``GET /item-storage/items``

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
                    
                    using CQL (indexes for item and material type)
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - title="*uproot*"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ItemStorage_get_items_return.schema 
        """
        return self.call("GET", "/item-storage/items", query=kwargs)

    def set_item(self, item: dict):
        """Create a new item item.

        ``POST /item-storage/items``

        Args:
            item (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created item item

        Schema:

            .. literalinclude:: ../files/ItemStorage_set_item_request.schema
        """
        return self.call("POST", "/item-storage/items", data=item)

    def delete_items(self):
        """

        ``DELETE /item-storage/items``
        """
        return self.call("DELETE", "/item-storage/items")

    def get_item(self, itemId: str):
        """Retrieve item item with given {itemId}

        ``GET /item-storage/items/{itemId}``

        Args:
            itemId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ItemStorage_get_item_return.schema 
        """
        return self.call("GET", f"/item-storage/items/{itemId}")

    def delete_item(self, itemId: str):
        """Delete item item with given {itemId}

        ``DELETE /item-storage/items/{itemId}``

        Args:
            itemId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/item-storage/items/{itemId}")

    def modify_item(self, itemId: str, item: dict):
        """Update item item with given {itemId}

        ``PUT /item-storage/items/{itemId}``

        Args:
            itemId (str)
            item (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ItemStorage_modify_item_request.schema
        """
        return self.call("PUT", f"/item-storage/items/{itemId}", data=item)


class Location(FolioApi):
    """Locations API

    This documents the API calls that can be made to query and manage (shelf) locations of the system
    """

    def get_locations(self, **kwargs):
        """Return a list of locations

        ``GET /locations``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/Location_get_locations_return.schema 
        """
        return self.call("GET", "/locations", query=kwargs)

    def set_location(self, location: dict):
        """Create a new location

        ``POST /locations``

        Args:
            location (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created location item

        Schema:

            .. literalinclude:: ../files/Location_set_location_request.schema
        """
        return self.call("POST", "/locations", data=location)

    def delete_locations(self):
        """

        ``DELETE /locations``
        """
        return self.call("DELETE", "/locations")

    def get_location(self, locationsId: str):
        """Retrieve location item with given {locationId}

        ``GET /locations/{locationsId}``

        Args:
            locationsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Location_get_location_return.schema 
        """
        return self.call("GET", f"/locations/{locationsId}")

    def delete_location(self, locationsId: str):
        """Delete location item with given {locationId}

        ``DELETE /locations/{locationsId}``

        Args:
            locationsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/locations/{locationsId}")

    def modify_location(self, locationsId: str, location: dict):
        """Update a location by id

        ``PUT /locations/{locationsId}``

        Args:
            locationsId (str)
            location (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Location_modify_location_request.schema
        """
        return self.call("PUT", f"/locations/{locationsId}", data=location)


class HridSettingsStorage(FolioApi):
    """HRID Settings Storage API

    **Storage for Human Readable Identifier (HRID) Settings**
    """

    def get_hridSettings(self):
        """Return the HRID settings

        ``GET /hrid-settings-storage/hrid-settings``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestForbidden: Forbidden
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/HridSettingsStorage_get_hridSettings_return.schema 
        """
        return self.call("GET", "/hrid-settings-storage/hrid-settings")

    def modify_hridSetting(self, hridSetting: dict):
        """Modifies HRID settings

        ``PUT /hrid-settings-storage/hrid-settings``

        Args:
            hridSetting (dict): See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestForbidden: Forbidden
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/HridSettingsStorage_modify_hridSetting_request.schema
        """
        return self.call("PUT", "/hrid-settings-storage/hrid-settings", data=hridSetting)


class MaterialType(FolioApi):
    """Material Types API

    This documents the API calls that can be made to query and manage material types of the system
    """

    def get_materialTypes(self, **kwargs):
        """Return a list of material types

        ``GET /material-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/MaterialType_get_materialTypes_return.schema 
        """
        return self.call("GET", "/material-types", query=kwargs)

    def set_materialType(self, materialType: dict):
        """Create a new material type

        ``POST /material-types``

        Args:
            materialType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created materialType item

        Schema:

            .. literalinclude:: ../files/MaterialType_set_materialType_request.schema
        """
        return self.call("POST", "/material-types", data=materialType)

    def delete_materialTypes(self):
        """

        ``DELETE /material-types``
        """
        return self.call("DELETE", "/material-types")

    def get_materialType(self, materialtypeId: str):
        """Retrieve materialType item with given {materialTypeId}

        ``GET /material-types/{materialtypeId}``

        Args:
            materialtypeId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/MaterialType_get_materialType_return.schema 
        """
        return self.call("GET", f"/material-types/{materialtypeId}")

    def delete_materialType(self, materialtypeId: str):
        """Delete materialType item with given {materialTypeId}

        ``DELETE /material-types/{materialtypeId}``

        Args:
            materialtypeId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/material-types/{materialtypeId}")

    def modify_materialType(self, materialtypeId: str, materialType: dict):
        """Update materialType item with given {materialTypeId}

        ``PUT /material-types/{materialtypeId}``

        Args:
            materialtypeId (str)
            materialType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/MaterialType_modify_materialType_request.schema
        """
        return self.call("PUT", f"/material-types/{materialtypeId}", data=materialType)


class HoldingsNoteType(FolioApi):
    """Holdings note types API

    This documents the API calls that can be made to query and manage holdings note types of the system
    """

    def get_holdingsNoteTypes(self, **kwargs):
        """Return a list of holdings note types

        ``GET /holdings-note-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/HoldingsNoteType_get_holdingsNoteTypes_return.schema 
        """
        return self.call("GET", "/holdings-note-types", query=kwargs)

    def set_holdingsNoteType(self, holdingsNoteType: dict):
        """Create a new holdings note type

        ``POST /holdings-note-types``

        Args:
            holdingsNoteType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created holdingsNoteType item

        Schema:

            .. literalinclude:: ../files/HoldingsNoteType_set_holdingsNoteType_request.schema
        """
        return self.call("POST", "/holdings-note-types", data=holdingsNoteType)

    def get_holdingsNoteType(self, holdingsNoteTypesId: str):
        """Retrieve holdingsNoteType item with given {holdingsNoteTypeId}

        ``GET /holdings-note-types/{holdingsNoteTypesId}``

        Args:
            holdingsNoteTypesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/HoldingsNoteType_get_holdingsNoteType_return.schema 
        """
        return self.call("GET", f"/holdings-note-types/{holdingsNoteTypesId}")

    def delete_holdingsNoteType(self, holdingsNoteTypesId: str):
        """Delete holdingsNoteType item with given {holdingsNoteTypeId}

        ``DELETE /holdings-note-types/{holdingsNoteTypesId}``

        Args:
            holdingsNoteTypesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/holdings-note-types/{holdingsNoteTypesId}")

    def modify_holdingsNoteType(self, holdingsNoteTypesId: str, holdingsNoteType: dict):
        """Update holdingsNoteType item with given {holdingsNoteTypeId}

        ``PUT /holdings-note-types/{holdingsNoteTypesId}``

        Args:
            holdingsNoteTypesId (str)
            holdingsNoteType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/HoldingsNoteType_modify_holdingsNoteType_request.schema
        """
        return self.call("PUT", f"/holdings-note-types/{holdingsNoteTypesId}", data=holdingsNoteType)


class InstanceSync(FolioApi):
    """Inventory Storage Instance Batch Sync API

    **Batch API for synchronously uploading instances into the inventory**
    """

    def set_synchronou(self, synchronou: dict, **kwargs):
        """Create or update a collection of instances in a single synchronous request; if any instance fails the complete batch will be rejected (all or nothing)

        ``POST /instance-storage/batch/synchronous``

        Args:
            synchronou (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            upsert (bool): (default=False) When a record with the same id already exists upsert=true will update it, upsert=false will fail the complete batch. The _version property of each instance to be updated must match the stored _version property (optimistic locking).

        Raises:
            OkapiRequestConflict: Conflict
            OkapiRequestPayloadToLarge: Payload Too Large
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceSync_set_synchronou_request.schema
        """
        return self.call("POST", "/instance-storage/batch/synchronous", data=synchronou, query=kwargs)


class NatureOfContentTerm(FolioApi):
    """Nature of content term API

    This documents the API calls that can be made to query and manage nature-of-content terms of the system
    """

    def get_natureOfContentTerms(self, **kwargs):
        """Return a list of nature-of-content terms

        ``GET /nature-of-content-terms``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/NatureOfContentTerm_get_natureOfContentTerms_return.schema 
        """
        return self.call("GET", "/nature-of-content-terms", query=kwargs)

    def set_natureOfContentTerm(self, natureOfContentTerm: dict):
        """Create a new nature-of-content term

        ``POST /nature-of-content-terms``

        Args:
            natureOfContentTerm (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created natureOfContentTerm item

        Schema:

            .. literalinclude:: ../files/NatureOfContentTerm_set_natureOfContentTerm_request.schema
        """
        return self.call("POST", "/nature-of-content-terms", data=natureOfContentTerm)

    def get_natureOfContentTerm(self, natureOfContentTermsId: str):
        """Retrieve natureOfContentTerm item with given {natureOfContentTermId}

        ``GET /nature-of-content-terms/{natureOfContentTermsId}``

        Args:
            natureOfContentTermsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/NatureOfContentTerm_get_natureOfContentTerm_return.schema 
        """
        return self.call("GET", f"/nature-of-content-terms/{natureOfContentTermsId}")

    def delete_natureOfContentTerm(self, natureOfContentTermsId: str):
        """Delete natureOfContentTerm item with given {natureOfContentTermId}

        ``DELETE /nature-of-content-terms/{natureOfContentTermsId}``

        Args:
            natureOfContentTermsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/nature-of-content-terms/{natureOfContentTermsId}")

    def modify_natureOfContentTerm(self, natureOfContentTermsId: str, natureOfContentTerm: dict):
        """Update natureOfContentTerm item with given {natureOfContentTermId}

        ``PUT /nature-of-content-terms/{natureOfContentTermsId}``

        Args:
            natureOfContentTermsId (str)
            natureOfContentTerm (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/NatureOfContentTerm_modify_natureOfContentTerm_request.schema
        """
        return self.call("PUT", f"/nature-of-content-terms/{natureOfContentTermsId}", data=natureOfContentTerm)


class ContributorNameType(FolioApi):
    """Contributor Name Types API

    This documents the API calls that can be made to query and manage contributor name types
    """

    def get_contributorNameTypes(self, **kwargs):
        """Return a list of contributor name types

        ``GET /contributor-name-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/ContributorNameType_get_contributorNameTypes_return.schema 
        """
        return self.call("GET", "/contributor-name-types", query=kwargs)

    def set_contributorNameType(self, contributorNameType: dict):
        """Create a new contributor name type

        ``POST /contributor-name-types``

        Args:
            contributorNameType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created contributorNameType item

        Schema:

            .. literalinclude:: ../files/ContributorNameType_set_contributorNameType_request.schema
        """
        return self.call("POST", "/contributor-name-types", data=contributorNameType)

    def get_contributorNameType(self, contributorNameTypeId: str):
        """Retrieve contributorNameType item with given {contributorNameTypeId}

        ``GET /contributor-name-types/{contributorNameTypeId}``

        Args:
            contributorNameTypeId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ContributorNameType_get_contributorNameType_return.schema 
        """
        return self.call("GET", f"/contributor-name-types/{contributorNameTypeId}")

    def delete_contributorNameType(self, contributorNameTypeId: str):
        """Delete contributorNameType item with given {contributorNameTypeId}

        ``DELETE /contributor-name-types/{contributorNameTypeId}``

        Args:
            contributorNameTypeId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/contributor-name-types/{contributorNameTypeId}")

    def modify_contributorNameType(self, contributorNameTypeId: str, contributorNameType: dict):
        """Update contributorNameType item with given {contributorNameTypeId}

        ``PUT /contributor-name-types/{contributorNameTypeId}``

        Args:
            contributorNameTypeId (str)
            contributorNameType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ContributorNameType_modify_contributorNameType_request.schema
        """
        return self.call("PUT", f"/contributor-name-types/{contributorNameTypeId}", data=contributorNameType)


class HoldingsType(FolioApi):
    """Holdings types API

    This documents the API calls that can be made to query and manage holdings types of the system
    """

    def get_holdingsTypes(self, **kwargs):
        """Return a list of holdings types

        ``GET /holdings-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/HoldingsType_get_holdingsTypes_return.schema 
        """
        return self.call("GET", "/holdings-types", query=kwargs)

    def set_holdingsType(self, holdingsType: dict):
        """Create a new holdings type

        ``POST /holdings-types``

        Args:
            holdingsType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created holdingsType item

        Schema:

            .. literalinclude:: ../files/HoldingsType_set_holdingsType_request.schema
        """
        return self.call("POST", "/holdings-types", data=holdingsType)

    def get_holdingsType(self, holdingsTypesId: str):
        """Retrieve holdingsType item with given {holdingsTypeId}

        ``GET /holdings-types/{holdingsTypesId}``

        Args:
            holdingsTypesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/HoldingsType_get_holdingsType_return.schema 
        """
        return self.call("GET", f"/holdings-types/{holdingsTypesId}")

    def delete_holdingsType(self, holdingsTypesId: str):
        """Delete holdingsType item with given {holdingsTypeId}

        ``DELETE /holdings-types/{holdingsTypesId}``

        Args:
            holdingsTypesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/holdings-types/{holdingsTypesId}")

    def modify_holdingsType(self, holdingsTypesId: str, holdingsType: dict):
        """Update holdingsType item with given {holdingsTypeId}

        ``PUT /holdings-types/{holdingsTypesId}``

        Args:
            holdingsTypesId (str)
            holdingsType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/HoldingsType_modify_holdingsType_request.schema
        """
        return self.call("PUT", f"/holdings-types/{holdingsTypesId}", data=holdingsType)


class StatisticalCode(FolioApi):
    """Statistical code reference API

    This documents the API calls that can be made to query and manage statistical codes of the system
    """

    def get_statisticalCodes(self, **kwargs):
        """Return a list of statistical codes

        ``GET /statistical-codes``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/StatisticalCode_get_statisticalCodes_return.schema 
        """
        return self.call("GET", "/statistical-codes", query=kwargs)

    def set_statisticalCode(self, statisticalCode: dict):
        """Create a new statistical code

        ``POST /statistical-codes``

        Args:
            statisticalCode (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created statisticalCode item

        Schema:

            .. literalinclude:: ../files/StatisticalCode_set_statisticalCode_request.schema
        """
        return self.call("POST", "/statistical-codes", data=statisticalCode)

    def get_statisticalCode(self, statisticalCodeId: str):
        """Retrieve statisticalCode item with given {statisticalCodeId}

        ``GET /statistical-codes/{statisticalCodeId}``

        Args:
            statisticalCodeId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/StatisticalCode_get_statisticalCode_return.schema 
        """
        return self.call("GET", f"/statistical-codes/{statisticalCodeId}")

    def delete_statisticalCode(self, statisticalCodeId: str):
        """Delete statisticalCode item with given {statisticalCodeId}

        ``DELETE /statistical-codes/{statisticalCodeId}``

        Args:
            statisticalCodeId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/statistical-codes/{statisticalCodeId}")

    def modify_statisticalCode(self, statisticalCodeId: str, statisticalCode: dict):
        """Update statisticalCode item with given {statisticalCodeId}

        ``PUT /statistical-codes/{statisticalCodeId}``

        Args:
            statisticalCodeId (str)
            statisticalCode (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/StatisticalCode_modify_statisticalCode_request.schema
        """
        return self.call("PUT", f"/statistical-codes/{statisticalCodeId}", data=statisticalCode)


class CallNumberType(FolioApi):
    """Call number types API

    This documents the API calls that can be made to query and manage call number types of the system
    """

    def get_callNumberTypes(self, **kwargs):
        """Return a list of call number types

        ``GET /call-number-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/CallNumberType_get_callNumberTypes_return.schema 
        """
        return self.call("GET", "/call-number-types", query=kwargs)

    def set_callNumberType(self, callNumberType: dict):
        """Create a new call number type

        ``POST /call-number-types``

        Args:
            callNumberType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created callNumberType item

        Schema:

            .. literalinclude:: ../files/CallNumberType_set_callNumberType_request.schema
        """
        return self.call("POST", "/call-number-types", data=callNumberType)

    def get_callNumberType(self, callNumberTypesId: str):
        """Retrieve callNumberType item with given {callNumberTypeId}

        ``GET /call-number-types/{callNumberTypesId}``

        Args:
            callNumberTypesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CallNumberType_get_callNumberType_return.schema 
        """
        return self.call("GET", f"/call-number-types/{callNumberTypesId}")

    def delete_callNumberType(self, callNumberTypesId: str):
        """Delete callNumberType item with given {callNumberTypeId}

        ``DELETE /call-number-types/{callNumberTypesId}``

        Args:
            callNumberTypesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/call-number-types/{callNumberTypesId}")

    def modify_callNumberType(self, callNumberTypesId: str, callNumberType: dict):
        """Update callNumberType item with given {callNumberTypeId}

        ``PUT /call-number-types/{callNumberTypesId}``

        Args:
            callNumberTypesId (str)
            callNumberType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CallNumberType_modify_callNumberType_request.schema
        """
        return self.call("PUT", f"/call-number-types/{callNumberTypesId}", data=callNumberType)


class InstanceReindex(FolioApi):
    """Instance reindex

    Reindex instances by generating domain events for them
    """

    def get_reindices(self, **kwargs):
        """Get all reindex jobs

        ``GET /instance-storage/reindex``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/InstanceReindex_get_reindices_return.schema 
        """
        return self.call("GET", "/instance-storage/reindex", query=kwargs)

    def set_reindex(self):
        """

        ``POST /instance-storage/reindex``
        """
        return self.call("POST", "/instance-storage/reindex")

    def get_reindex(self, reindexId: str):
        """Get reindex job by id

        ``GET /instance-storage/reindex/{reindexId}``

        Args:
            reindexId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceReindex_get_reindex_return.schema 
        """
        return self.call("GET", f"/instance-storage/reindex/{reindexId}")

    def delete_reindex(self, reindexId: str):
        """Cancell reindex job by id

        ``DELETE /instance-storage/reindex/{reindexId}``

        Args:
            reindexId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/instance-storage/reindex/{reindexId}")


class HoldingsSources(FolioApi):
    """Holdings Records Sources API

    This documents the API calls that can be made to query and manage holdings records sources
    """

    def get_holdingsSources(self, **kwargs):
        """Return a list of holdings records sources

        ``GET /holdings-sources``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/HoldingsSources_get_holdingsSources_return.schema 
        """
        return self.call("GET", "/holdings-sources", query=kwargs)

    def set_holdingsSource(self, holdingsSource: dict):
        """Create a new holdings records source

        ``POST /holdings-sources``

        Args:
            holdingsSource (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created holdingsSource item

        Schema:

            .. literalinclude:: ../files/HoldingsSources_set_holdingsSource_request.schema
        """
        return self.call("POST", "/holdings-sources", data=holdingsSource)

    def get_holdingsSource(self, holdingsSourcesId: str):
        """Retrieve holdingsSource item with given {holdingsSourceId}

        ``GET /holdings-sources/{holdingsSourcesId}``

        Args:
            holdingsSourcesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/HoldingsSources_get_holdingsSource_return.schema 
        """
        return self.call("GET", f"/holdings-sources/{holdingsSourcesId}")

    def delete_holdingsSource(self, holdingsSourcesId: str):
        """Delete holdingsSource item with given {holdingsSourceId}

        ``DELETE /holdings-sources/{holdingsSourcesId}``

        Args:
            holdingsSourcesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/holdings-sources/{holdingsSourcesId}")

    def modify_holdingsSource(self, holdingsSourcesId: str, holdingsSource: dict):
        """Update holdingsSource item with given {holdingsSourceId}

        ``PUT /holdings-sources/{holdingsSourcesId}``

        Args:
            holdingsSourcesId (str)
            holdingsSource (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/HoldingsSources_modify_holdingsSource_request.schema
        """
        return self.call("PUT", f"/holdings-sources/{holdingsSourcesId}", data=holdingsSource)


class AuthorityNoteType(FolioApi):
    """Authority note types API

    This documents the API calls that can be made to query and manage Authority note types of the system
    """

    def get_authorityNoteTypes(self, **kwargs):
        """Return a list of authority note types

        ``GET /authority-note-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/AuthorityNoteType_get_authorityNoteTypes_return.schema 
        """
        return self.call("GET", "/authority-note-types", query=kwargs)

    def set_authorityNoteType(self, authorityNoteType: dict):
        """Create a new authority note type

        ``POST /authority-note-types``

        Args:
            authorityNoteType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created authorityNoteType item

        Schema:

            .. literalinclude:: ../files/AuthorityNoteType_set_authorityNoteType_request.schema
        """
        return self.call("POST", "/authority-note-types", data=authorityNoteType)

    def get_authorityNoteType(self, authorityNoteTypesId: str):
        """Retrieve authorityNoteType item with given {authorityNoteTypeId}

        ``GET /authority-note-types/{authorityNoteTypesId}``

        Args:
            authorityNoteTypesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AuthorityNoteType_get_authorityNoteType_return.schema 
        """
        return self.call("GET", f"/authority-note-types/{authorityNoteTypesId}")

    def delete_authorityNoteType(self, authorityNoteTypesId: str):
        """Delete authorityNoteType item with given {authorityNoteTypeId}

        ``DELETE /authority-note-types/{authorityNoteTypesId}``

        Args:
            authorityNoteTypesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/authority-note-types/{authorityNoteTypesId}")

    def modify_authorityNoteType(self, authorityNoteTypesId: str, authorityNoteType: dict):
        """Update authorityNoteType item with given {authorityNoteTypeId}

        ``PUT /authority-note-types/{authorityNoteTypesId}``

        Args:
            authorityNoteTypesId (str)
            authorityNoteType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AuthorityNoteType_modify_authorityNoteType_request.schema
        """
        return self.call("PUT", f"/authority-note-types/{authorityNoteTypesId}", data=authorityNoteType)


class Locationunit(FolioApi):
    """Location units

    This documents the API calls that can be made to query and manage location units like institutions, campuses, and libraries
    """

    def get_institutions(self, **kwargs):
        """Return a list of institutions

        ``GET /location-units/institutions``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/Locationunit_get_institutions_return.schema 
        """
        return self.call("GET", "/location-units/institutions", query=kwargs)

    def set_institution(self, institution: dict):
        """Create a new institution

        ``POST /location-units/institutions``

        Args:
            institution (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created institution item

        Schema:

            .. literalinclude:: ../files/Locationunit_set_institution_request.schema
        """
        return self.call("POST", "/location-units/institutions", data=institution)

    def delete_institutions(self):
        """

        ``DELETE /location-units/institutions``
        """
        return self.call("DELETE", "/location-units/institutions")

    def get_institution(self, institutionsId: str):
        """Retrieve institution item with given {institutionId}

        ``GET /location-units/institutions/{institutionsId}``

        Args:
            institutionsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Locationunit_get_institution_return.schema 
        """
        return self.call("GET", f"/location-units/institutions/{institutionsId}")

    def delete_institution(self, institutionsId: str):
        """Delete institution item with given {institutionId}

        ``DELETE /location-units/institutions/{institutionsId}``

        Args:
            institutionsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/location-units/institutions/{institutionsId}")

    def modify_institution(self, institutionsId: str, institution: dict):
        """Update institution item with given {institutionId}

        ``PUT /location-units/institutions/{institutionsId}``

        Args:
            institutionsId (str)
            institution (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Locationunit_modify_institution_request.schema
        """
        return self.call("PUT", f"/location-units/institutions/{institutionsId}", data=institution)

    def get_campuses(self, **kwargs):
        """Return a list of campuses

        ``GET /location-units/campuses``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/Locationunit_get_campuses_return.schema 
        """
        return self.call("GET", "/location-units/campuses", query=kwargs)

    def set_campuse(self, campuse: dict):
        """Create a new campus

        ``POST /location-units/campuses``

        Args:
            campuse (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created campuse item

        Schema:

            .. literalinclude:: ../files/Locationunit_set_campuse_request.schema
        """
        return self.call("POST", "/location-units/campuses", data=campuse)

    def delete_campuses(self):
        """

        ``DELETE /location-units/campuses``
        """
        return self.call("DELETE", "/location-units/campuses")

    def get_campuse(self, campusesId: str):
        """Retrieve campuse item with given {campuseId}

        ``GET /location-units/campuses/{campusesId}``

        Args:
            campusesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Locationunit_get_campuse_return.schema 
        """
        return self.call("GET", f"/location-units/campuses/{campusesId}")

    def delete_campuse(self, campusesId: str):
        """Delete campuse item with given {campuseId}

        ``DELETE /location-units/campuses/{campusesId}``

        Args:
            campusesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/location-units/campuses/{campusesId}")

    def modify_campuse(self, campusesId: str, campuse: dict):
        """Update campuse item with given {campuseId}

        ``PUT /location-units/campuses/{campusesId}``

        Args:
            campusesId (str)
            campuse (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Locationunit_modify_campuse_request.schema
        """
        return self.call("PUT", f"/location-units/campuses/{campusesId}", data=campuse)

    def get_libraries(self, **kwargs):
        """Return a list of libraries

        ``GET /location-units/libraries``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/Locationunit_get_libraries_return.schema 
        """
        return self.call("GET", "/location-units/libraries", query=kwargs)

    def set_library(self, library: dict):
        """Create a new library

        ``POST /location-units/libraries``

        Args:
            library (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created library item

        Schema:

            .. literalinclude:: ../files/Locationunit_set_library_request.schema
        """
        return self.call("POST", "/location-units/libraries", data=library)

    def delete_libraries(self):
        """

        ``DELETE /location-units/libraries``
        """
        return self.call("DELETE", "/location-units/libraries")

    def get_library(self, librariesId: str):
        """Retrieve library item with given {libraryId}

        ``GET /location-units/libraries/{librariesId}``

        Args:
            librariesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Locationunit_get_library_return.schema 
        """
        return self.call("GET", f"/location-units/libraries/{librariesId}")

    def delete_library(self, librariesId: str):
        """Delete library item with given {libraryId}

        ``DELETE /location-units/libraries/{librariesId}``

        Args:
            librariesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/location-units/libraries/{librariesId}")

    def modify_library(self, librariesId: str, library: dict):
        """Update library item with given {libraryId}

        ``PUT /location-units/libraries/{librariesId}``

        Args:
            librariesId (str)
            library (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Locationunit_modify_library_request.schema
        """
        return self.call("PUT", f"/location-units/libraries/{librariesId}", data=library)


class AlternativeTitleType(FolioApi):
    """Alternative title types API

    This documents the API calls that can be made to query and manage alternative title types of the system
    """

    def get_alternativeTitleTypes(self, **kwargs):
        """Return a list of alternative title types

        ``GET /alternative-title-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/AlternativeTitleType_get_alternativeTitleTypes_return.schema 
        """
        return self.call("GET", "/alternative-title-types", query=kwargs)

    def set_alternativeTitleType(self, alternativeTitleType: dict):
        """Create a new alternative title type

        ``POST /alternative-title-types``

        Args:
            alternativeTitleType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created alternativeTitleType item

        Schema:

            .. literalinclude:: ../files/AlternativeTitleType_set_alternativeTitleType_request.schema
        """
        return self.call("POST", "/alternative-title-types", data=alternativeTitleType)

    def get_alternativeTitleType(self, alternativeTitleTypesId: str):
        """Retrieve alternativeTitleType item with given {alternativeTitleTypeId}

        ``GET /alternative-title-types/{alternativeTitleTypesId}``

        Args:
            alternativeTitleTypesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AlternativeTitleType_get_alternativeTitleType_return.schema 
        """
        return self.call("GET", f"/alternative-title-types/{alternativeTitleTypesId}")

    def delete_alternativeTitleType(self, alternativeTitleTypesId: str):
        """Delete alternativeTitleType item with given {alternativeTitleTypeId}

        ``DELETE /alternative-title-types/{alternativeTitleTypesId}``

        Args:
            alternativeTitleTypesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/alternative-title-types/{alternativeTitleTypesId}")

    def modify_alternativeTitleType(self, alternativeTitleTypesId: str, alternativeTitleType: dict):
        """Update alternativeTitleType item with given {alternativeTitleTypeId}

        ``PUT /alternative-title-types/{alternativeTitleTypesId}``

        Args:
            alternativeTitleTypesId (str)
            alternativeTitleType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AlternativeTitleType_modify_alternativeTitleType_request.schema
        """
        return self.call("PUT", f"/alternative-title-types/{alternativeTitleTypesId}", data=alternativeTitleType)


class ItemStorageDereferenced(FolioApi):
    """Item Retrieval API

    **Get dereferenced items data from inventory**
    """

    def get_items(self, **kwargs):
        """Retrieve item item with given {itemId}

        ``GET /item-storage-dereferenced/items``

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
                    
                    using CQL (indexes for item and material type)
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - title="*uproot*"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ItemStorageDereferenced_get_items_return.schema 
        """
        return self.call("GET", "/item-storage-dereferenced/items", query=kwargs)

    def get_item(self, itemId: str):
        """Retrieve item item with given {itemId}

        ``GET /item-storage-dereferenced/items/{itemId}``

        Args:
            itemId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ItemStorageDereferenced_get_item_return.schema 
        """
        return self.call("GET", f"/item-storage-dereferenced/items/{itemId}")


class InstanceNoteType(FolioApi):
    """Instance note types API

    This documents the API calls that can be made to query and manage Instance note types of the system
    """

    def get_instanceNoteTypes(self, **kwargs):
        """Return a list of instance note types

        ``GET /instance-note-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/InstanceNoteType_get_instanceNoteTypes_return.schema 
        """
        return self.call("GET", "/instance-note-types", query=kwargs)

    def set_instanceNoteType(self, instanceNoteType: dict):
        """Create a new instance note type

        ``POST /instance-note-types``

        Args:
            instanceNoteType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created instanceNoteType item

        Schema:

            .. literalinclude:: ../files/InstanceNoteType_set_instanceNoteType_request.schema
        """
        return self.call("POST", "/instance-note-types", data=instanceNoteType)

    def get_instanceNoteType(self, instanceNoteTypesId: str):
        """Retrieve instanceNoteType item with given {instanceNoteTypeId}

        ``GET /instance-note-types/{instanceNoteTypesId}``

        Args:
            instanceNoteTypesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceNoteType_get_instanceNoteType_return.schema 
        """
        return self.call("GET", f"/instance-note-types/{instanceNoteTypesId}")

    def delete_instanceNoteType(self, instanceNoteTypesId: str):
        """Delete instanceNoteType item with given {instanceNoteTypeId}

        ``DELETE /instance-note-types/{instanceNoteTypesId}``

        Args:
            instanceNoteTypesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/instance-note-types/{instanceNoteTypesId}")

    def modify_instanceNoteType(self, instanceNoteTypesId: str, instanceNoteType: dict):
        """Update instanceNoteType item with given {instanceNoteTypeId}

        ``PUT /instance-note-types/{instanceNoteTypesId}``

        Args:
            instanceNoteTypesId (str)
            instanceNoteType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceNoteType_modify_instanceNoteType_request.schema
        """
        return self.call("PUT", f"/instance-note-types/{instanceNoteTypesId}", data=instanceNoteType)


class IdentifierType(FolioApi):
    """Identifier Types API

    This documents the API calls that can be made to query and manage instance identifier types
    """

    def get_identifierTypes(self, **kwargs):
        """Return a list of identifier types

        ``GET /identifier-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/IdentifierType_get_identifierTypes_return.schema 
        """
        return self.call("GET", "/identifier-types", query=kwargs)

    def set_identifierType(self, identifierType: dict):
        """Create a new identifier type

        ``POST /identifier-types``

        Args:
            identifierType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created identifierType item

        Schema:

            .. literalinclude:: ../files/IdentifierType_set_identifierType_request.schema
        """
        return self.call("POST", "/identifier-types", data=identifierType)

    def get_identifierType(self, identifierTypeId: str):
        """Retrieve identifierType item with given {identifierTypeId}

        ``GET /identifier-types/{identifierTypeId}``

        Args:
            identifierTypeId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/IdentifierType_get_identifierType_return.schema 
        """
        return self.call("GET", f"/identifier-types/{identifierTypeId}")

    def delete_identifierType(self, identifierTypeId: str):
        """Delete identifierType item with given {identifierTypeId}

        ``DELETE /identifier-types/{identifierTypeId}``

        Args:
            identifierTypeId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/identifier-types/{identifierTypeId}")

    def modify_identifierType(self, identifierTypeId: str, identifierType: dict):
        """Update identifierType item with given {identifierTypeId}

        ``PUT /identifier-types/{identifierTypeId}``

        Args:
            identifierTypeId (str)
            identifierType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/IdentifierType_modify_identifierType_request.schema
        """
        return self.call("PUT", f"/identifier-types/{identifierTypeId}", data=identifierType)


class ServicePoint(FolioApi):
    """Service Points API

    This documents the API calls that can be made to query and manage service points in the system
    """

    def get_servicePoints(self, **kwargs):
        """Return a list of service points

        ``GET /service-points``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/ServicePoint_get_servicePoints_return.schema 
        """
        return self.call("GET", "/service-points", query=kwargs)

    def set_servicePoint(self, servicePoint: dict):
        """Create a new service point

        ``POST /service-points``

        Args:
            servicePoint (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created servicePoint item

        Schema:

            .. literalinclude:: ../files/ServicePoint_set_servicePoint_request.schema
        """
        return self.call("POST", "/service-points", data=servicePoint)

    def delete_servicePoints(self):
        """

        ``DELETE /service-points``
        """
        return self.call("DELETE", "/service-points")

    def get_servicePoint(self, servicepointId: str):
        """Retrieve servicePoint item with given {servicePointId}

        ``GET /service-points/{servicepointId}``

        Args:
            servicepointId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ServicePoint_get_servicePoint_return.schema 
        """
        return self.call("GET", f"/service-points/{servicepointId}")

    def delete_servicePoint(self, servicepointId: str):
        """Delete servicePoint item with given {servicePointId}

        ``DELETE /service-points/{servicepointId}``

        Args:
            servicepointId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/service-points/{servicepointId}")

    def modify_servicePoint(self, servicepointId: str, servicePoint: dict):
        """Update a service point

        ``PUT /service-points/{servicepointId}``

        Args:
            servicepointId (str)
            servicePoint (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/ServicePoint_modify_servicePoint_request.schema
        """
        return self.call("PUT", f"/service-points/{servicepointId}", data=servicePoint)


class InstanceIteration(FolioApi):
    """Instance iteration

    Iterate instances by generating domain events for them
    """

    def set_iteration(self, iteration: dict):
        """Submit an iteration job

        ``POST /instance-storage/instances/iteration``

        Args:
            iteration (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceIteration_set_iteration_request.schema
            .. literalinclude:: ../files/InstanceIteration_set_iteration_return.schema 
        """
        return self.call("POST", "/instance-storage/instances/iteration", data=iteration)

    def get_iteration(self, iterationId: str):
        """Get iteration job by id

        ``GET /instance-storage/instances/iteration/{iterationId}``

        Args:
            iterationId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceIteration_get_iteration_return.schema 
        """
        return self.call("GET", f"/instance-storage/instances/iteration/{iterationId}")

    def delete_iteration(self, iterationId: str):
        """Cancel iteration job by id

        ``DELETE /instance-storage/instances/iteration/{iterationId}``

        Args:
            iterationId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/instance-storage/instances/iteration/{iterationId}")


class AsyncMigration(FolioApi):
    """Async migrations API

    Running async migrations proceses for inventory enteties
    """

    def get_migrations(self):
        """Avalilible async migrations for the inventory-storage

        ``GET /inventory-storage/migrations``

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AsyncMigration_get_migrations_return.schema 
        """
        return self.call("GET", "/inventory-storage/migrations")

    def get_jobs(self):
        """Get migration jobs

        ``GET /inventory-storage/migrations/jobs``

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AsyncMigration_get_jobs_return.schema 
        """
        return self.call("GET", "/inventory-storage/migrations/jobs")

    def set_job(self, job: dict):
        """Submit a migration job

        ``POST /inventory-storage/migrations/jobs``

        Args:
            job (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AsyncMigration_set_job_request.schema
            .. literalinclude:: ../files/AsyncMigration_set_job_return.schema 
        """
        return self.call("POST", "/inventory-storage/migrations/jobs", data=job)

    def get_job(self, jobsId: str):
        """Get migration job by id

        ``GET /inventory-storage/migrations/jobs/{jobsId}``

        Args:
            jobsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AsyncMigration_get_job_return.schema 
        """
        return self.call("GET", f"/inventory-storage/migrations/jobs/{jobsId}")

    def delete_job(self, jobsId: str):
        """Cancell migration job by id

        ``DELETE /inventory-storage/migrations/jobs/{jobsId}``

        Args:
            jobsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/inventory-storage/migrations/jobs/{jobsId}")


class ItemSyncUnsafe(FolioApi):
    """Inventory Storage Item Batch Sync Unsafe API

    **Batch API for synchronously uploading items into the inventory**
    """

    def set_synchronousUnsafe(self, synchronousUnsafe: dict):
        """Create or update (upsert) a collection of items in a single synchronous request; if any item fails the complete batch will be rejected (all or nothing). Environment variable DB_ALLOW_SUPPRESS_OPTIMISTIC_LOCKING is required, see https://github.com/folio-org/raml-module-builder#environment-variables for details. The _version property is ignored, optimistic locking is disabled - this is known to lead to data loss in some cases, don't use in production, you have been warned!

        ``POST /item-storage/batch/synchronous-unsafe``

        Args:
            synchronousUnsafe (dict): See Schema below

        Raises:
            OkapiRequestPayloadToLarge: Payload Too Large
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ItemSyncUnsafe_set_synchronousUnsafe_request.schema
        """
        return self.call("POST", "/item-storage/batch/synchronous-unsafe", data=synchronousUnsafe)


class LoanType(FolioApi):
    """Loan Types API

    This documents the API calls that can be made to query and manage loan types of the system
    """

    def get_loanTypes(self, **kwargs):
        """Return a list of loan types

        ``GET /loan-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/LoanType_get_loanTypes_return.schema 
        """
        return self.call("GET", "/loan-types", query=kwargs)

    def set_loanType(self, loanType: dict):
        """Create a new loan type

        ``POST /loan-types``

        Args:
            loanType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created loanType item

        Schema:

            .. literalinclude:: ../files/LoanType_set_loanType_request.schema
        """
        return self.call("POST", "/loan-types", data=loanType)

    def delete_loanTypes(self):
        """

        ``DELETE /loan-types``
        """
        return self.call("DELETE", "/loan-types")

    def get_loanType(self, loantypeId: str):
        """Retrieve loanType item with given {loanTypeId}

        ``GET /loan-types/{loantypeId}``

        Args:
            loantypeId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LoanType_get_loanType_return.schema 
        """
        return self.call("GET", f"/loan-types/{loantypeId}")

    def delete_loanType(self, loantypeId: str):
        """Delete loanType item with given {loanTypeId}

        ``DELETE /loan-types/{loantypeId}``

        Args:
            loantypeId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/loan-types/{loantypeId}")

    def modify_loanType(self, loantypeId: str, loanType: dict):
        """Update loanType item with given {loanTypeId}

        ``PUT /loan-types/{loantypeId}``

        Args:
            loantypeId (str)
            loanType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LoanType_modify_loanType_request.schema
        """
        return self.call("PUT", f"/loan-types/{loantypeId}", data=loanType)


class HoldingsSync(FolioApi):
    """Inventory Storage Holdings Batch Sync API

    **Batch API for synchronously uploading holdings records into the inventory**
    """

    def set_synchronou(self, synchronou: dict, **kwargs):
        """Create or update a collection of holdings in a single synchronous request; if any holding fails the complete batch will be rejected (all or nothing)

        ``POST /holdings-storage/batch/synchronous``

        Args:
            synchronou (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            upsert (bool): (default=False) When a record with the same id already exists upsert=true will update it, upsert=false will fail the complete batch. The _version property of each holding to be updated must match the stored _version property (optimistic locking).

        Raises:
            OkapiRequestConflict: Conflict
            OkapiRequestPayloadToLarge: Payload Too Large
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/HoldingsSync_set_synchronou_request.schema
        """
        return self.call("POST", "/holdings-storage/batch/synchronous", data=synchronou, query=kwargs)


class ContributorType(FolioApi):
    """Contributor Types API

    This documents the API calls that can be made to query and manage contributor types
    """

    def get_contributorTypes(self, **kwargs):
        """Return a list of contributor types

        ``GET /contributor-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/ContributorType_get_contributorTypes_return.schema 
        """
        return self.call("GET", "/contributor-types", query=kwargs)

    def set_contributorType(self, contributorType: dict):
        """Create a new contributor type

        ``POST /contributor-types``

        Args:
            contributorType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created contributorType item

        Schema:

            .. literalinclude:: ../files/ContributorType_set_contributorType_request.schema
        """
        return self.call("POST", "/contributor-types", data=contributorType)

    def get_contributorType(self, contributorTypeId: str):
        """Retrieve contributorType item with given {contributorTypeId}

        ``GET /contributor-types/{contributorTypeId}``

        Args:
            contributorTypeId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ContributorType_get_contributorType_return.schema 
        """
        return self.call("GET", f"/contributor-types/{contributorTypeId}")

    def delete_contributorType(self, contributorTypeId: str):
        """Delete contributorType item with given {contributorTypeId}

        ``DELETE /contributor-types/{contributorTypeId}``

        Args:
            contributorTypeId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/contributor-types/{contributorTypeId}")

    def modify_contributorType(self, contributorTypeId: str, contributorType: dict):
        """Update contributorType item with given {contributorTypeId}

        ``PUT /contributor-types/{contributorTypeId}``

        Args:
            contributorTypeId (str)
            contributorType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ContributorType_modify_contributorType_request.schema
        """
        return self.call("PUT", f"/contributor-types/{contributorTypeId}", data=contributorType)


class ClassificationType(FolioApi):
    """Classification Types API

    This documents the API calls that can be made to query and manage classification qualifier resource types
    """

    def get_classificationTypes(self, **kwargs):
        """Return a list of classification qualifiers

        ``GET /classification-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/ClassificationType_get_classificationTypes_return.schema 
        """
        return self.call("GET", "/classification-types", query=kwargs)

    def set_classificationType(self, classificationType: dict):
        """Create a new classification type

        ``POST /classification-types``

        Args:
            classificationType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created classificationType item

        Schema:

            .. literalinclude:: ../files/ClassificationType_set_classificationType_request.schema
        """
        return self.call("POST", "/classification-types", data=classificationType)

    def get_classificationType(self, classificationTypeId: str):
        """Retrieve classificationType item with given {classificationTypeId}

        ``GET /classification-types/{classificationTypeId}``

        Args:
            classificationTypeId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ClassificationType_get_classificationType_return.schema 
        """
        return self.call("GET", f"/classification-types/{classificationTypeId}")

    def delete_classificationType(self, classificationTypeId: str):
        """Delete classificationType item with given {classificationTypeId}

        ``DELETE /classification-types/{classificationTypeId}``

        Args:
            classificationTypeId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/classification-types/{classificationTypeId}")

    def modify_classificationType(self, classificationTypeId: str, classificationType: dict):
        """Update classificationType item with given {classificationTypeId}

        ``PUT /classification-types/{classificationTypeId}``

        Args:
            classificationTypeId (str)
            classificationType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ClassificationType_modify_classificationType_request.schema
        """
        return self.call("PUT", f"/classification-types/{classificationTypeId}", data=classificationType)


class ShelfLocation(FolioApi):
    """DEPRECATED Shelf Locations API (forth-level location unit)

    DEPRECATED - Can report the name and id of a (shelf) location, the forth-level location unit. This is a read-only proxy to the new locations interface at /locations that should be used instead.
    """

    def get_shelfLocations(self, **kwargs):
        """DEPRECATED - return a list of (shelf) locations, the forth-level location unit. This is a read-only proxy to the new locations interface at /locations that should be used instead.

        ``GET /shelf-locations``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/ShelfLocation_get_shelfLocations_return.schema 
        """
        return self.call("GET", "/shelf-locations", query=kwargs)

    def set_shelfLocation(self, shelfLocation: dict):
        """DEPRECATED and NOT IMPLEMENTED - Create a new shelf location

        ``POST /shelf-locations``

        Args:
            shelfLocation (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created shelfLocation item

        Schema:

            .. literalinclude:: ../files/ShelfLocation_set_shelfLocation_request.schema
        """
        return self.call("POST", "/shelf-locations", data=shelfLocation)

    def delete_shelfLocations(self):
        """

        ``DELETE /shelf-locations``
        """
        return self.call("DELETE", "/shelf-locations")

    def get_shelfLocation(self, shelfLocationsId: str):
        """Retrieve shelfLocation item with given {shelfLocationId}

        ``GET /shelf-locations/{shelfLocationsId}``

        Args:
            shelfLocationsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ShelfLocation_get_shelfLocation_return.schema 
        """
        return self.call("GET", f"/shelf-locations/{shelfLocationsId}")

    def delete_shelfLocation(self, shelfLocationsId: str):
        """Delete shelfLocation item with given {shelfLocationId}

        ``DELETE /shelf-locations/{shelfLocationsId}``

        Args:
            shelfLocationsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/shelf-locations/{shelfLocationsId}")

    def modify_shelfLocation(self, shelfLocationsId: str, shelfLocation: dict):
        """Update shelfLocation item with given {shelfLocationId}

        ``PUT /shelf-locations/{shelfLocationsId}``

        Args:
            shelfLocationsId (str)
            shelfLocation (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ShelfLocation_modify_shelfLocation_request.schema
        """
        return self.call("PUT", f"/shelf-locations/{shelfLocationsId}", data=shelfLocation)


class InstanceSet(FolioApi):
    """Instance Set

    Get instances, for each instance get related records
    """

    def get_instanceSets(self, **kwargs):
        """Get instances, for each instance get related records

        ``GET /inventory-view/instance-set``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - hrid=="in007"

        Returns:
            binary: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceSet_get_instanceSets_return.schema 
        """
        return self.call("GET", "/inventory-view/instance-set", query=kwargs)


class BoundWithPart(FolioApi):
    """Bound-With API

    API calls for querying and managing individual parts or all parts of bound-withs
    """

    def get_boundWithParts(self, **kwargs):
        """Return a list of parts of bound-withs

        ``GET /inventory-storage/bound-with-parts``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - itemId=aaa
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

            .. literalinclude:: ../files/BoundWithPart_get_boundWithParts_return.schema 
        """
        return self.call("GET", "/inventory-storage/bound-with-parts", query=kwargs)

    def set_boundWithPart(self, boundWithPart: dict):
        """Add a new part to a bound-with item

        ``POST /inventory-storage/bound-with-parts``

        Args:
            boundWithPart (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created boundWithPart item

        Schema:

            .. literalinclude:: ../files/BoundWithPart_set_boundWithPart_request.schema
        """
        return self.call("POST", "/inventory-storage/bound-with-parts", data=boundWithPart)

    def get_boundWithPart(self, boundWithPartsId: str):
        """Retrieve boundWithPart item with given {boundWithPartId}

        ``GET /inventory-storage/bound-with-parts/{boundWithPartsId}``

        Args:
            boundWithPartsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/BoundWithPart_get_boundWithPart_return.schema 
        """
        return self.call("GET", f"/inventory-storage/bound-with-parts/{boundWithPartsId}")

    def delete_boundWithPart(self, boundWithPartsId: str):
        """Delete boundWithPart item with given {boundWithPartId}

        ``DELETE /inventory-storage/bound-with-parts/{boundWithPartsId}``

        Args:
            boundWithPartsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/inventory-storage/bound-with-parts/{boundWithPartsId}")

    def modify_boundWithPart(self, boundWithPartsId: str, boundWithPart: dict):
        """Update boundWithPart item with given {boundWithPartId}

        ``PUT /inventory-storage/bound-with-parts/{boundWithPartsId}``

        Args:
            boundWithPartsId (str)
            boundWithPart (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/BoundWithPart_modify_boundWithPart_request.schema
        """
        return self.call("PUT", f"/inventory-storage/bound-with-parts/{boundWithPartsId}", data=boundWithPart)

    def modify_boundWith(self, boundWith: dict):
        """Manage the collective set of parts (holdings references) of a bound-with item

        ``PUT /inventory-storage/bound-withs``

        Args:
            boundWith (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/BoundWithPart_modify_boundWith_request.schema
        """
        return self.call("PUT", "/inventory-storage/bound-withs", data=boundWith)


class Authorities(FolioApi):
    """Authority Storage API

    **Storage for authorities in the inventory**
    """

    def get_authorities(self, **kwargs):
        """Retrieve a list of authority items.

        ``GET /authority-storage/authorities``

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
                    
                    using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - personalName="root"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Authorities_get_authorities_return.schema 
        """
        return self.call("GET", "/authority-storage/authorities", query=kwargs)

    def set_authority(self, authority: dict):
        """Create a new authority item.

        ``POST /authority-storage/authorities``

        Args:
            authority (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created authority item

        Schema:

            .. literalinclude:: ../files/Authorities_set_authority_request.schema
        """
        return self.call("POST", "/authority-storage/authorities", data=authority)

    def delete_authorities(self):
        """

        ``DELETE /authority-storage/authorities``
        """
        return self.call("DELETE", "/authority-storage/authorities")

    def get_authority(self, authorityId: str):
        """Retrieve authority Authority with given {authorityId}

        ``GET /authority-storage/authorities/{authorityId}``

        Args:
            authorityId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Authorities_get_authority_return.schema 
        """
        return self.call("GET", f"/authority-storage/authorities/{authorityId}")

    def delete_authority(self, authorityId: str):
        """Delete authority Authority with given {authorityId}

        ``DELETE /authority-storage/authorities/{authorityId}``

        Args:
            authorityId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/authority-storage/authorities/{authorityId}")

    def modify_authority(self, authorityId: str, authority: dict):
        """Update authority Authority with given {authorityId}

        ``PUT /authority-storage/authorities/{authorityId}``

        Args:
            authorityId (str)
            authority (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Authorities_modify_authority_request.schema
        """
        return self.call("PUT", f"/authority-storage/authorities/{authorityId}", data=authority)


class ElectronicAccessRelationship(FolioApi):
    """Electronic access relationship terms reference API

    This documents the API calls that can be made to query and manage electronic access relationship types of the system
    """

    def get_electronicAccessRelationships(self, **kwargs):
        """Return a list of electronic access relationship terms

        ``GET /electronic-access-relationships``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/ElectronicAccessRelationship_get_electronicAccessRelationships_return.schema 
        """
        return self.call("GET", "/electronic-access-relationships", query=kwargs)

    def set_electronicAccessRelationship(self, electronicAccessRelationship: dict):
        """Create a new electronic access relationship term

        ``POST /electronic-access-relationships``

        Args:
            electronicAccessRelationship (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created electronicAccessRelationship item

        Schema:

            .. literalinclude:: ../files/ElectronicAccessRelationship_set_electronicAccessRelationship_request.schema
        """
        return self.call("POST", "/electronic-access-relationships", data=electronicAccessRelationship)

    def get_electronicAccessRelationship(self, electronicAccessRelationshipId: str):
        """Retrieve electronicAccessRelationship item with given {electronicAccessRelationshipId}

        ``GET /electronic-access-relationships/{electronicAccessRelationshipId}``

        Args:
            electronicAccessRelationshipId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ElectronicAccessRelationship_get_electronicAccessRelationship_return.schema 
        """
        return self.call("GET", f"/electronic-access-relationships/{electronicAccessRelationshipId}")

    def delete_electronicAccessRelationship(self, electronicAccessRelationshipId: str):
        """Delete electronicAccessRelationship item with given {electronicAccessRelationshipId}

        ``DELETE /electronic-access-relationships/{electronicAccessRelationshipId}``

        Args:
            electronicAccessRelationshipId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/electronic-access-relationships/{electronicAccessRelationshipId}")

    def modify_electronicAccessRelationship(self, electronicAccessRelationshipId: str, electronicAccessRelationship: dict):
        """Update electronicAccessRelationship item with given {electronicAccessRelationshipId}

        ``PUT /electronic-access-relationships/{electronicAccessRelationshipId}``

        Args:
            electronicAccessRelationshipId (str)
            electronicAccessRelationship (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ElectronicAccessRelationship_modify_electronicAccessRelationship_request.schema
        """
        return self.call("PUT", f"/electronic-access-relationships/{electronicAccessRelationshipId}", data=electronicAccessRelationship)


class InstanceRelationshipType(FolioApi):
    """Instance Relationship Types API

    This documents the API calls that can be made to query and manage instance relationship types
    """

    def get_instanceRelationshipTypes(self, **kwargs):
        """Return a list of relationship types

        ``GET /instance-relationship-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/InstanceRelationshipType_get_instanceRelationshipTypes_return.schema 
        """
        return self.call("GET", "/instance-relationship-types", query=kwargs)

    def set_instanceRelationshipType(self, instanceRelationshipType: dict):
        """Create a new relationship type

        ``POST /instance-relationship-types``

        Args:
            instanceRelationshipType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created instanceRelationshipType item

        Schema:

            .. literalinclude:: ../files/InstanceRelationshipType_set_instanceRelationshipType_request.schema
        """
        return self.call("POST", "/instance-relationship-types", data=instanceRelationshipType)

    def get_instanceRelationshipType(self, relationshipTypeId: str):
        """Retrieve instanceRelationshipType item with given {instanceRelationshipTypeId}

        ``GET /instance-relationship-types/{relationshipTypeId}``

        Args:
            relationshipTypeId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceRelationshipType_get_instanceRelationshipType_return.schema 
        """
        return self.call("GET", f"/instance-relationship-types/{relationshipTypeId}")

    def delete_instanceRelationshipType(self, relationshipTypeId: str):
        """Delete instanceRelationshipType item with given {instanceRelationshipTypeId}

        ``DELETE /instance-relationship-types/{relationshipTypeId}``

        Args:
            relationshipTypeId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/instance-relationship-types/{relationshipTypeId}")

    def modify_instanceRelationshipType(self, relationshipTypeId: str, instanceRelationshipType: dict):
        """Update instanceRelationshipType item with given {instanceRelationshipTypeId}

        ``PUT /instance-relationship-types/{relationshipTypeId}``

        Args:
            relationshipTypeId (str)
            instanceRelationshipType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceRelationshipType_modify_instanceRelationshipType_request.schema
        """
        return self.call("PUT", f"/instance-relationship-types/{relationshipTypeId}", data=instanceRelationshipType)


class ItemNoteType(FolioApi):
    """Item note types API

    This documents the API calls that can be made to query and manage item note types of the system
    """

    def get_itemNoteTypes(self, **kwargs):
        """Return a list of item note types

        ``GET /item-note-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/ItemNoteType_get_itemNoteTypes_return.schema 
        """
        return self.call("GET", "/item-note-types", query=kwargs)

    def set_itemNoteType(self, itemNoteType: dict):
        """Create a new item note type

        ``POST /item-note-types``

        Args:
            itemNoteType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created itemNoteType item

        Schema:

            .. literalinclude:: ../files/ItemNoteType_set_itemNoteType_request.schema
        """
        return self.call("POST", "/item-note-types", data=itemNoteType)

    def get_itemNoteType(self, itemNoteTypesId: str):
        """Retrieve itemNoteType item with given {itemNoteTypeId}

        ``GET /item-note-types/{itemNoteTypesId}``

        Args:
            itemNoteTypesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ItemNoteType_get_itemNoteType_return.schema 
        """
        return self.call("GET", f"/item-note-types/{itemNoteTypesId}")

    def delete_itemNoteType(self, itemNoteTypesId: str):
        """Delete itemNoteType item with given {itemNoteTypeId}

        ``DELETE /item-note-types/{itemNoteTypesId}``

        Args:
            itemNoteTypesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/item-note-types/{itemNoteTypesId}")

    def modify_itemNoteType(self, itemNoteTypesId: str, itemNoteType: dict):
        """Update itemNoteType item with given {itemNoteTypeId}

        ``PUT /item-note-types/{itemNoteTypesId}``

        Args:
            itemNoteTypesId (str)
            itemNoteType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ItemNoteType_modify_itemNoteType_request.schema
        """
        return self.call("PUT", f"/item-note-types/{itemNoteTypesId}", data=itemNoteType)


class InstanceStatus(FolioApi):
    """Instance status reference API

    This documents the API calls that can be made to query and manage instance statuses of the system
    """

    def get_instanceStatuses(self, **kwargs):
        """Return a list of instances statuses

        ``GET /instance-statuses``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/InstanceStatus_get_instanceStatuses_return.schema 
        """
        return self.call("GET", "/instance-statuses", query=kwargs)

    def set_instanceStatus(self, instanceStatus: dict):
        """Create a new instance status

        ``POST /instance-statuses``

        Args:
            instanceStatus (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created instanceStatus item

        Schema:

            .. literalinclude:: ../files/InstanceStatus_set_instanceStatus_request.schema
        """
        return self.call("POST", "/instance-statuses", data=instanceStatus)

    def delete_instanceStatuses(self):
        """

        ``DELETE /instance-statuses``
        """
        return self.call("DELETE", "/instance-statuses")

    def get_instanceStatus(self, instanceStatusId: str):
        """Retrieve instanceStatus item with given {instanceStatusId}

        ``GET /instance-statuses/{instanceStatusId}``

        Args:
            instanceStatusId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceStatus_get_instanceStatus_return.schema 
        """
        return self.call("GET", f"/instance-statuses/{instanceStatusId}")

    def delete_instanceStatus(self, instanceStatusId: str):
        """Delete instanceStatus item with given {instanceStatusId}

        ``DELETE /instance-statuses/{instanceStatusId}``

        Args:
            instanceStatusId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/instance-statuses/{instanceStatusId}")

    def modify_instanceStatus(self, instanceStatusId: str, instanceStatus: dict):
        """Update instanceStatus item with given {instanceStatusId}

        ``PUT /instance-statuses/{instanceStatusId}``

        Args:
            instanceStatusId (str)
            instanceStatus (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceStatus_modify_instanceStatus_request.schema
        """
        return self.call("PUT", f"/instance-statuses/{instanceStatusId}", data=instanceStatus)


class InstanceStorage(FolioApi):
    """Instance Storage API

    **Storage for instances in the inventory**
    """

    def get_instanceRelationships(self, **kwargs):
        """Retrieve a list of instanceRelationship items.

        ``GET /instance-storage/instance-relationships``

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
                    
                    by parent ID or by child ID (using CQL)
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - subInstanceId==83a50dc6-b887-43d9-93ee-28b2c4cd11f8 superInstanceId==30fcc8e7-a019-43f4-b642-2edc389f4501 instanceRelationshipTypeId==758f13db-ffb4-440e-bb10-8a364aa6cb4a AND superInstanceId=30fcc8e7-a019-43f4-b642-2edc389f4501

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceStorage_get_instanceRelationships_return.schema 
        """
        return self.call("GET", "/instance-storage/instance-relationships", query=kwargs)

    def set_instanceRelationship(self, instanceRelationship: dict):
        """Create a new instanceRelationship item.

        ``POST /instance-storage/instance-relationships``

        Args:
            instanceRelationship (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created instanceRelationship item

        Schema:

            .. literalinclude:: ../files/InstanceStorage_set_instanceRelationship_request.schema
        """
        return self.call("POST", "/instance-storage/instance-relationships", data=instanceRelationship)

    def get_instanceRelationship(self, relationshipId: str):
        """Get Instance Relationship

        ``GET /instance-storage/instance-relationships/{relationshipId}``

        Args:
            relationshipId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceStorage_get_instanceRelationship_return.schema 
        """
        return self.call("GET", f"/instance-storage/instance-relationships/{relationshipId}")

    def delete_instanceRelationship(self, relationshipId: str):
        """Delete instanceRelationship item with given {instanceRelationshipId}

        ``DELETE /instance-storage/instance-relationships/{relationshipId}``

        Args:
            relationshipId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/instance-storage/instance-relationships/{relationshipId}")

    def modify_instanceRelationship(self, relationshipId: str, instanceRelationship: dict):
        """Update instanceRelationship item with given {instanceRelationshipId}

        ``PUT /instance-storage/instance-relationships/{relationshipId}``

        Args:
            relationshipId (str)
            instanceRelationship (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceStorage_modify_instanceRelationship_request.schema
        """
        return self.call("PUT", f"/instance-storage/instance-relationships/{relationshipId}", data=instanceRelationship)

    def get_instances(self, **kwargs):
        """Retrieve a list of instance items.

        ``GET /instance-storage/instances``

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
                    
                    by title (using CQL)
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - title="*uproot*"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceStorage_get_instances_return.schema 
        """
        return self.call("GET", "/instance-storage/instances", query=kwargs)

    def set_instance(self, instance: dict):
        """Create a new instance item.

        ``POST /instance-storage/instances``

        Args:
            instance (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created instance item

        Schema:

            .. literalinclude:: ../files/InstanceStorage_set_instance_request.schema
        """
        return self.call("POST", "/instance-storage/instances", data=instance)

    def delete_instances(self):
        """

        ``DELETE /instance-storage/instances``
        """
        return self.call("DELETE", "/instance-storage/instances")

    def get_instance(self, instanceId: str):
        """Get Instance by InstanceId
        Instances are stored and accessed by a hash of key properties. The rules which govern
        how instance hashes are computed are business rules and defined in the service layer.
        the storage layer only knows how to insert or retrieve instance records by ID.

        ``GET /instance-storage/instances/{instanceId}``

        Args:
            instanceId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceStorage_get_instance_return.schema 
        """
        return self.call("GET", f"/instance-storage/instances/{instanceId}")

    def delete_instance(self, instanceId: str):
        """Delete instance item with given {instanceId}

        ``DELETE /instance-storage/instances/{instanceId}``

        Args:
            instanceId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/instance-storage/instances/{instanceId}")

    def modify_instance(self, instanceId: str, instance: dict):
        """Update instance item with given {instanceId}

        ``PUT /instance-storage/instances/{instanceId}``

        Args:
            instanceId (str)
            instance (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceStorage_modify_instance_request.schema
        """
        return self.call("PUT", f"/instance-storage/instances/{instanceId}", data=instance)

    def delete_sourceRecord(self, instanceId: str, **kwargs):
        """Delete the source record.
        Note: When the Inventory instance record is deleted, its source record in mod-inventory-storage is automatically deleted. If the Inventory instance record is linked to a corresponding record in mod-source-record-storage, that SRS record is NOT automatically deleted.

        ``DELETE /instance-storage/instances/{instanceId}/source-record``

        Args:
            instanceId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/instance-storage/instances/{instanceId}/source-record", query=kwargs)

    def get_marcJson(self, instanceId: str):
        """Get Instance Relationship

        ``GET /instance-storage/instances/{instanceId}/source-record/marc-json``

        Args:
            instanceId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceStorage_get_marcJson_return.schema 
        """
        return self.call("GET", f"/instance-storage/instances/{instanceId}/source-record/marc-json")

    def delete_marcJson(self, instanceId: str):
        """Delete marcJson item with given {marcJsonId}

        ``DELETE /instance-storage/instances/{instanceId}/source-record/marc-json``

        Args:
            instanceId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/instance-storage/instances/{instanceId}/source-record/marc-json")

    def modify_marcJson(self, instanceId: str, marcJson: dict):
        """Update marcJson item with given {marcJsonId}

        ``PUT /instance-storage/instances/{instanceId}/source-record/marc-json``

        Args:
            instanceId (str)
            marcJson (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceStorage_modify_marcJson_request.schema
        """
        return self.call("PUT", f"/instance-storage/instances/{instanceId}/source-record/marc-json", data=marcJson)

    def get_mods_by_instance(self, instanceId: str):
        """

        ``GET /instance-storage/instances/{instanceId}/source-record/mods``

        Args:
            instanceId (str)

        Raises:
            OkapiFatalError: Server Error
        """
        return self.call("GET", f"/instance-storage/instances/{instanceId}/source-record/mods")

    def modify_mods(self, instanceId: str):
        """

        ``PUT /instance-storage/instances/{instanceId}/source-record/mods``

        Args:
            instanceId (str)

        Raises:
            OkapiFatalError: Server Error
        """
        return self.call("PUT", f"/instance-storage/instances/{instanceId}/source-record/mods")


class InstanceType(FolioApi):
    """Instance Types API

    This documents the API calls that can be made to query and manage instance resource types
    """

    def get_instanceTypes(self, **kwargs):
        """Return a list of instance types

        ``GET /instance-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
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

            .. literalinclude:: ../files/InstanceType_get_instanceTypes_return.schema 
        """
        return self.call("GET", "/instance-types", query=kwargs)

    def set_instanceType(self, instanceType: dict):
        """Create a new instance type

        ``POST /instance-types``

        Args:
            instanceType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created instanceType item

        Schema:

            .. literalinclude:: ../files/InstanceType_set_instanceType_request.schema
        """
        return self.call("POST", "/instance-types", data=instanceType)

    def get_instanceType(self, instanceTypeId: str):
        """Retrieve instanceType item with given {instanceTypeId}

        ``GET /instance-types/{instanceTypeId}``

        Args:
            instanceTypeId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceType_get_instanceType_return.schema 
        """
        return self.call("GET", f"/instance-types/{instanceTypeId}")

    def delete_instanceType(self, instanceTypeId: str):
        """Delete instanceType item with given {instanceTypeId}

        ``DELETE /instance-types/{instanceTypeId}``

        Args:
            instanceTypeId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/instance-types/{instanceTypeId}")

    def modify_instanceType(self, instanceTypeId: str, instanceType: dict):
        """Update instanceType item with given {instanceTypeId}

        ``PUT /instance-types/{instanceTypeId}``

        Args:
            instanceTypeId (str)
            instanceType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceType_modify_instanceType_request.schema
        """
        return self.call("PUT", f"/instance-types/{instanceTypeId}", data=instanceType)


class InstanceStorageBatch(FolioApi):
    """Deprecated Inventory Storage Instance Batch API

    **Deprecated Batch API for managing Inventory Instances, use /instance-storage/sync instead.**
    """

    def set_instance(self, instance: dict):
        """Create collection of instances in one request - deprecated, use /instance-storage/sync instead

        ``POST /instance-storage/batch/instances``

        Args:
            instance (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InstanceStorageBatch_set_instance_request.schema
            .. literalinclude:: ../files/InstanceStorageBatch_set_instance_return.schema 
        """
        return self.call("POST", "/instance-storage/batch/instances", data=instance)
