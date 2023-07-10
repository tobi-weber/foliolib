# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.inventory")


class InventoryBatch(FolioApi):
    """Batch API

    **API for interacting with an inventory of physical resources**
    """

    def set_batch(self, batch: dict):
        """Create collection of instances in one request

        ``POST /inventory/instances/batch``

        Args:
            batch (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InventoryBatch_set_batch_request.schema
            .. literalinclude:: ../files/InventoryBatch_set_batch_return.schema 
        """
        return self.call("POST", "/inventory/instances/batch", data=batch)


class InventoryConfig(FolioApi):
    """Inventory configuration API

    **API for interacting with configuration for Instances, Items, Holdings**
    """

    def get_blockedFields_instances(self):
        """Provides configuration with blocked fields of instance

        ``GET /inventory/config/instances/blocked-fields``

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InventoryConfig_get_blockedFields_instances_return.schema 
        """
        return self.call("GET", "/inventory/config/instances/blocked-fields")

    def get_blockedFields_holdings(self):
        """Provides configuration with blocked fields of holdings

        ``GET /inventory/config/holdings/blocked-fields``

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InventoryConfig_get_blockedFields_holdings_return.schema 
        """
        return self.call("GET", "/inventory/config/holdings/blocked-fields")


class InventoryMove(FolioApi):
    """Inventory Move API

    **API for moving items between holdings and holdings between instances**
    """

    def set_move_items(self, move: dict):
        """

        ``POST /inventory/items/move``

        Args:
            move (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/InventoryMove_set_move_items_request.schema
            .. literalinclude:: ../files/InventoryMove_set_move_items_return.schema 
        """
        return self.call("POST", "/inventory/items/move", data=move)

    def set_move_holdings(self, move: dict):
        """

        ``POST /inventory/holdings/move``

        Args:
            move (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/InventoryMove_set_move_holdings_request.schema
            .. literalinclude:: ../files/InventoryMove_set_move_holdings_return.schema 
        """
        return self.call("POST", "/inventory/holdings/move", data=move)


class Isbn(FolioApi):
    """ISBN API

    **API for validation and conversion of ISBN-10 and ISBN-13 numbers **
    """

    def get_convertTo13s(self, **kwargs):
        """Converts an ISBN code to an ISBN-13 code

        ``GET /isbn/convertTo13``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            isbn (str):  
                    
                    Example:
                    
                     - 091698477X
            hyphens (bool): (default=False) 

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request

        Schema:

            .. literalinclude:: ../files/Isbn_get_convertTo13s_return.schema 
        """
        return self.call("GET", "/isbn/convertTo13", query=kwargs)

    def get_convertTo10s(self, **kwargs):
        """Converts an ISBN-13 code to an ISBN-10 code

        ``GET /isbn/convertTo10``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            isbn (str):  
                    
                    Example:
                    
                     - 978-1-930110-99-1
            hyphens (bool): (default=False) 

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request

        Schema:

            .. literalinclude:: ../files/Isbn_get_convertTo10s_return.schema 
        """
        return self.call("GET", "/isbn/convertTo10", query=kwargs)

    def get_validators(self, **kwargs):
        """Checks the code is a valid ISBN code.

        ``GET /isbn/validator``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            /^(isbn|isbn10|isbn13)$/ ():  

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request

        Schema:

            .. literalinclude:: ../files/Isbn_get_validators_return.schema 
        """
        return self.call("GET", "/isbn/validator", query=kwargs)


class InventoryEventHandlers(FolioApi):
    """Inventory Event Handlers API

    **API for handling events**
    """

    def set_instance(self):
        """Handler for Instance update events

        ``POST /inventory/handlers/instances``

        Raises:
            OkapiFatalError: Server Error
        """
        return self.call("POST", "/inventory/handlers/instances")


class Inventory(FolioApi):
    """Inventory API

    **API for interacting with an inventory of physical resources**
    """

    def get_items(self, **kwargs):
        """Retrieve a list of item items.

        ``GET /inventory/items``

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
                    
                     - barcode=="65345656554"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Inventory_get_items_return.schema 
        """
        return self.call("GET", "/inventory/items", query=kwargs)

    def set_item(self, item: dict):
        """Create a new item item.

        ``POST /inventory/items``

        Args:
            item (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created item item

        Schema:

            .. literalinclude:: ../files/Inventory_set_item_request.schema
        """
        return self.call("POST", "/inventory/items", data=item)

    def delete_items(self):
        """

        ``DELETE /inventory/items``
        """
        return self.call("DELETE", "/inventory/items")

    def get_item(self, itemId: str):
        """Retrieve item item with given {itemId}

        ``GET /inventory/items/{itemId}``

        Args:
            itemId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Inventory_get_item_return.schema 
        """
        return self.call("GET", f"/inventory/items/{itemId}")

    def delete_item(self, itemId: str):
        """Delete item item with given {itemId}

        ``DELETE /inventory/items/{itemId}``

        Args:
            itemId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/inventory/items/{itemId}")

    def modify_item(self, itemId: str, item: dict):
        """Update item item with given {itemId}

        ``PUT /inventory/items/{itemId}``

        Args:
            itemId (str)
            item (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Inventory_modify_item_request.schema
        """
        return self.call("PUT", f"/inventory/items/{itemId}", data=item)

    def set_markWithdrawn(self, itemId: str):
        """

        ``POST /inventory/items/{itemId}/mark-withdrawn``

        Args:
            itemId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Inventory_set_markWithdrawn_return.schema 
        """
        return self.call("POST", f"/inventory/items/{itemId}/mark-withdrawn")

    def set_markInProcess(self, itemId: str):
        """

        ``POST /inventory/items/{itemId}/mark-in-process``

        Args:
            itemId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Inventory_set_markInProcess_return.schema 
        """
        return self.call("POST", f"/inventory/items/{itemId}/mark-in-process")

    def set_markInProcessNonRequestable(self, itemId: str):
        """

        ``POST /inventory/items/{itemId}/mark-in-process-non-requestable``

        Args:
            itemId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Inventory_set_markInProcessNonRequestable_return.schema 
        """
        return self.call("POST", f"/inventory/items/{itemId}/mark-in-process-non-requestable")

    def set_markIntellectualItem(self, itemId: str):
        """

        ``POST /inventory/items/{itemId}/mark-intellectual-item``

        Args:
            itemId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Inventory_set_markIntellectualItem_return.schema 
        """
        return self.call("POST", f"/inventory/items/{itemId}/mark-intellectual-item")

    def set_markLongMissing(self, itemId: str):
        """

        ``POST /inventory/items/{itemId}/mark-long-missing``

        Args:
            itemId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Inventory_set_markLongMissing_return.schema 
        """
        return self.call("POST", f"/inventory/items/{itemId}/mark-long-missing")

    def set_markMissing(self, itemId: str):
        """

        ``POST /inventory/items/{itemId}/mark-missing``

        Args:
            itemId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Inventory_set_markMissing_return.schema 
        """
        return self.call("POST", f"/inventory/items/{itemId}/mark-missing")

    def set_markRestricted(self, itemId: str):
        """

        ``POST /inventory/items/{itemId}/mark-restricted``

        Args:
            itemId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Inventory_set_markRestricted_return.schema 
        """
        return self.call("POST", f"/inventory/items/{itemId}/mark-restricted")

    def set_markUnavailable(self, itemId: str):
        """

        ``POST /inventory/items/{itemId}/mark-unavailable``

        Args:
            itemId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Inventory_set_markUnavailable_return.schema 
        """
        return self.call("POST", f"/inventory/items/{itemId}/mark-unavailable")

    def set_markUnknown(self, itemId: str):
        """

        ``POST /inventory/items/{itemId}/mark-unknown``

        Args:
            itemId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Inventory_set_markUnknown_return.schema 
        """
        return self.call("POST", f"/inventory/items/{itemId}/mark-unknown")

    def get_itemsByHoldingsIds(self, **kwargs):
        """Retrieve a list of itemsByHoldingsId items.

        ``GET /inventory/items-by-holdings-id``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    query by holdings record ID. This is a mandatory query parameter. An optional parameter, 'relations', can be passed outside of the query to restrict what Items are returned based on their type of relationship with the holdings record. Possible values of the 'relations' parameter are: 'onlyBoundWiths', 'onlyBoundWithsSkipDirectlyLinkedItem'
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - holdingsRecordId=="[UUID]"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Inventory_get_itemsByHoldingsIds_return.schema 
        """
        return self.call("GET", "/inventory/items-by-holdings-id", query=kwargs)

    def set_itemsByHoldingsId(self, itemsByHoldingsId: dict):
        """Create a new itemsByHoldingsId item.

        ``POST /inventory/items-by-holdings-id``

        Args:
            itemsByHoldingsId (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created itemsByHoldingsId item

        Schema:

            .. literalinclude:: ../files/Inventory_set_itemsByHoldingsId_request.schema
        """
        return self.call("POST", "/inventory/items-by-holdings-id", data=itemsByHoldingsId)

    def delete_itemsByHoldingsIds(self):
        """

        ``DELETE /inventory/items-by-holdings-id``
        """
        return self.call("DELETE", "/inventory/items-by-holdings-id")

    def modify_holding(self, holdingsId: str, holding: dict):
        """Update Holdings by holdingsId

        ``PUT /inventory/holdings/{holdingsId}``

        Args:
            holdingsId (str)
            holding (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Inventory_modify_holding_request.schema
        """
        return self.call("PUT", f"/inventory/holdings/{holdingsId}", data=holding)

    def get_instances(self, **kwargs):
        """Retrieve a list of instance items.

        ``GET /inventory/instances``

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
                    
                     - title="uproot*"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Inventory_get_instances_return.schema 
        """
        return self.call("GET", "/inventory/instances", query=kwargs)

    def set_instance(self, instance: dict):
        """Create a new instance item.

        ``POST /inventory/instances``

        Args:
            instance (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created instance item

        Schema:

            .. literalinclude:: ../files/Inventory_set_instance_request.schema
        """
        return self.call("POST", "/inventory/instances", data=instance)

    def delete_instances(self):
        """

        ``DELETE /inventory/instances``
        """
        return self.call("DELETE", "/inventory/instances")

    def get_instance(self, instanceId: str):
        """Retrieve instance item with given {instanceId}

        ``GET /inventory/instances/{instanceId}``

        Args:
            instanceId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Inventory_get_instance_return.schema 
        """
        return self.call("GET", f"/inventory/instances/{instanceId}")

    def delete_instance(self, instanceId: str):
        """Delete instance item with given {instanceId}

        ``DELETE /inventory/instances/{instanceId}``

        Args:
            instanceId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/inventory/instances/{instanceId}")

    def modify_instance(self, instanceId: str, instance: dict):
        """Update instance item with given {instanceId}

        ``PUT /inventory/instances/{instanceId}``

        Args:
            instanceId (str)
            instance (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Inventory_modify_instance_request.schema
        """
        return self.call("PUT", f"/inventory/instances/{instanceId}", data=instance)
