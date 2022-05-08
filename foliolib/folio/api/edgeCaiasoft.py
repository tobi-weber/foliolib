# -*- coding: utf-8 -*-
# Generated at 2022-05-05

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.edgeCaiasoft")



class Edgecaiasoft(FolioApi):
    """Edge CasiaSoft API

    
    """

    def getAccessionItem(self, itemBarcode, remoteStorageConfigurationId):
        """

        ``GET /caiasoftService/ItemBarcodes/{itemBarcode}/accessioned/{remoteStorageConfigurationId}``

        Args:
            itemBarcode (str): 
            remoteStorageConfigurationId (str):

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Edgecaiasoft_getAccessionItem_response.schema
        """
        return self.call("GET", "/caiasoftService/ItemBarcodes/{itemBarcode}/accessioned/{remoteStorageConfigurationId}", itemBarcode, remoteStorageConfigurationId)

    def returnItemByBarcode(self, itemBarcode, remoteStorageConfigurationId):
        """Perform item return

        ``POST /caiasoftService/RequestBarcodes/{itemBarcode}/reshelved/{remoteStorageConfigurationId}``

        Args:
            itemBarcode (str): 
            remoteStorageConfigurationId (str):

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Edgecaiasoft_returnItemByBarcode_response.schema
        """
        return self.call("POST", "/caiasoftService/RequestBarcodes/{itemBarcode}/reshelved/{remoteStorageConfigurationId}", itemBarcode, remoteStorageConfigurationId)

    def checkInByHoldId(self, requestId, remoteStorageConfigurationId):
        """

        ``POST /caiasoftService/Requests/{requestId}/route/{remoteStorageConfigurationId}``

        Args:
            requestId (str): 
            remoteStorageConfigurationId (str):

        Raises:
            OkapiFatalError: Internal server error
        """
        return self.call("POST", "/caiasoftService/Requests/{requestId}/route/{remoteStorageConfigurationId}", requestId, remoteStorageConfigurationId)
