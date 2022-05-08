# -*- coding: utf-8 -*-
# Generated at 2022-05-05

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.edgeDematic")



class Edgedematic(FolioApi):
    """Edge Dematic API

    
    """

    def getAsrItems(self, remoteStorageConfigurationId):
        """Get a list of items

        ``GET /asrService/asr/lookupNewAsrItems/{remoteStorageConfigurationId}``

        Args:
            remoteStorageConfigurationId (str): 

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Edgedematic_getAsrItems_response.schema
        """
        return self.call("GET", "/asrService/asr/lookupNewAsrItems/{remoteStorageConfigurationId}", remoteStorageConfigurationId)

    def getAsrRequests(self, remoteStorageConfigurationId):
        """Get a list of requests

        ``GET /asrService/asr/lookupAsrRequests/{remoteStorageConfigurationId}``

        Args:
            remoteStorageConfigurationId (str): 

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Edgedematic_getAsrRequests_response.schema
        """
        return self.call("GET", "/asrService/asr/lookupAsrRequests/{remoteStorageConfigurationId}", remoteStorageConfigurationId)

    def updateAsrItemCheckIn(self, remoteStorageConfigurationId, updateAsrItem):
        """Chek-in item

        ``POST /asrService/asr/updateASRItemStatusBeingRetrieved/{remoteStorageConfigurationId}``

        Args:
            remoteStorageConfigurationId (str): 
            updateAsrItem (dict): See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Edgedematic_updateAsrItemCheckIn_request.schema
        """
        return self.call("POST", "/asrService/asr/updateASRItemStatusBeingRetrieved/{remoteStorageConfigurationId}", remoteStorageConfigurationId, updateAsrItem)

    def updateAsrItemReturn(self, remoteStorageConfigurationId, updateAsrItem):
        """Return item

        ``POST /asrService/asr/updateASRItemStatusAvailable/{remoteStorageConfigurationId}``

        Args:
            remoteStorageConfigurationId (str): 
            updateAsrItem (dict): See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Edgedematic_updateAsrItemReturn_request.schema
        """
        return self.call("POST", "/asrService/asr/updateASRItemStatusAvailable/{remoteStorageConfigurationId}", remoteStorageConfigurationId, updateAsrItem)
