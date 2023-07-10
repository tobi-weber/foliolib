# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.inventoryUpdate")


class InventoryUpdate(FolioApi):
    """Inventory update APIs

    **Provides various schemes for creating, updating and deleting instances, holdings records and items in Inventory storage**
    """

    def modify_inventoryUpsertHrid(self, inventoryUpsertHrid: dict):
        """

        ``PUT /inventory-upsert-hrid``

        Args:
            inventoryUpsertHrid (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InventoryUpdate_modify_inventoryUpsertHrid_request.schema
            .. literalinclude:: ../files/InventoryUpdate_modify_inventoryUpsertHrid_return.schema 
        """
        return self.call("PUT", "/inventory-upsert-hrid", data=inventoryUpsertHrid)

    def delete_inventoryUpsertHrids(self, inventoryUpsertHrid: dict):
        """

        ``DELETE /inventory-upsert-hrid``

        Args:
            inventoryUpsertHrid (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InventoryUpdate_delete_inventoryUpsertHrids_request.schema
            .. literalinclude:: ../files/InventoryUpdate_delete_inventoryUpsertHrids_return.schema 
        """
        return self.call("DELETE", "/inventory-upsert-hrid", data=inventoryUpsertHrid)

    def modify_inventoryBatchUpsertHrid(self, inventoryBatchUpsertHrid: dict):
        """

        ``PUT /inventory-batch-upsert-hrid``

        Args:
            inventoryBatchUpsertHrid (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InventoryUpdate_modify_inventoryBatchUpsertHrid_request.schema
            .. literalinclude:: ../files/InventoryUpdate_modify_inventoryBatchUpsertHrid_return.schema 
        """
        return self.call("PUT", "/inventory-batch-upsert-hrid", data=inventoryBatchUpsertHrid)

    def modify_sharedInventoryUpsertMatchkey(self, sharedInventoryUpsertMatchkey: dict):
        """

        ``PUT /shared-inventory-upsert-matchkey``

        Args:
            sharedInventoryUpsertMatchkey (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InventoryUpdate_modify_sharedInventoryUpsertMatchkey_request.schema
            .. literalinclude:: ../files/InventoryUpdate_modify_sharedInventoryUpsertMatchkey_return.schema 
        """
        return self.call("PUT", "/shared-inventory-upsert-matchkey", data=sharedInventoryUpsertMatchkey)

    def delete_sharedInventoryUpsertMatchkeys(self, sharedInventoryUpsertMatchkey: dict):
        """

        ``DELETE /shared-inventory-upsert-matchkey``

        Args:
            sharedInventoryUpsertMatchkey (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InventoryUpdate_delete_sharedInventoryUpsertMatchkeys_request.schema
            .. literalinclude:: ../files/InventoryUpdate_delete_sharedInventoryUpsertMatchkeys_return.schema 
        """
        return self.call("DELETE", "/shared-inventory-upsert-matchkey", data=sharedInventoryUpsertMatchkey)

    def get_fetch_by_fetchId(self, fetchId: str):
        """

        ``GET /inventory-upsert-hrid/fetch/{fetchId}``

        Args:
            fetchId (str)

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/InventoryUpdate_get_fetch_by_fetchId_return.schema 
        """
        return self.call("GET", f"/inventory-upsert-hrid/fetch/{fetchId}")

    def get_fetch(self, fetchId: str):
        """

        ``GET /shared-inventory-upsert-matchkey/fetch/{fetchId}``

        Args:
            fetchId (str)

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/InventoryUpdate_get_fetch_return.schema 
        """
        return self.call("GET", f"/shared-inventory-upsert-matchkey/fetch/{fetchId}")

    def modify_sharedInventoryBatchUpsertMatchkey(self, sharedInventoryBatchUpsertMatchkey: dict):
        """

        ``PUT /shared-inventory-batch-upsert-matchkey``

        Args:
            sharedInventoryBatchUpsertMatchkey (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/InventoryUpdate_modify_sharedInventoryBatchUpsertMatchkey_request.schema
            .. literalinclude:: ../files/InventoryUpdate_modify_sharedInventoryBatchUpsertMatchkey_return.schema 
        """
        return self.call("PUT", "/shared-inventory-batch-upsert-matchkey", data=sharedInventoryBatchUpsertMatchkey)
