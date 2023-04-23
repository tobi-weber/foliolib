# -*- coding: utf-8 -*-
# Generated at 2023-04-16

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.remoteStorage")



class RemotestorageAdmin(FolioAdminApi):
    """Remote storages API
    Administration

    
    """

    def getConfigurations(self, **kwargs):
        """Get a list of remote storage configurations

        ``GET /remote-storage/configurations``

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)
            query (str): A query string to filter rules based on matching criteria in fields.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_getConfigurations_response.schema
        """
        return self.call("GET", "/remote-storage/configurations", query=kwargs)

		
    def postConfiguration(self, storageConfiguration):
        """Add new remote storage configuration

        ``POST /remote-storage/configurations``

        Args:
            storageConfiguration (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_postConfiguration_request.schema
        """
        return self.call("POST", "/remote-storage/configurations", storageConfiguration)

    def getConfigurationById(self):
        """

        ``GET /remote-storage/configurations/{configId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Configuration not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_getConfigurationById_response.schema
        """
        return self.call("GET", "/remote-storage/configurations/{configId}")

		
    def putConfiguration(self, storageConfiguration):
        """Change the remote storage configuration

        ``PUT /remote-storage/configurations/{configId}``

        Args:
            storageConfiguration (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Configuration not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_putConfiguration_request.schema
        """
        return self.call("PUT", "/remote-storage/configurations/{configId}", storageConfiguration)

		
    def deleteConfigurationById(self):
        """

        ``DELETE /remote-storage/configurations/{configId}``

        Raises:
            OkapiRequestNotFound: Configuration not found
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", "/remote-storage/configurations/{configId}")

    def postMapping(self, remoteLocationConfigurationMapping):
        """Add/update a mapping between remote and Folio locations

        ``POST /remote-storage/mappings``

        Args:
            remoteLocationConfigurationMapping (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_postMapping_request.schema
        """
        return self.call("POST", "/remote-storage/mappings", remoteLocationConfigurationMapping)

		
    def getMappings(self, **kwargs):
        """Get a list of location mappings

        ``GET /remote-storage/mappings``

        Keyword Args:
            finalLocationId (str): Final location id
            remoteStorageConfigurationId (str): Remote storage configuration id
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_getMappings_response.schema
        """
        return self.call("GET", "/remote-storage/mappings", query=kwargs)

    def getMappingById(self):
        """

        ``GET /remote-storage/mappings/{folioLocationId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Mapping not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_getMappingById_response.schema
        """
        return self.call("GET", "/remote-storage/mappings/{folioLocationId}")

		
    def deleteMappingById(self):
        """

        ``DELETE /remote-storage/mappings/{folioLocationId}``

        Raises:
            OkapiRequestNotFound: Mapping not found
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", "/remote-storage/mappings/{folioLocationId}")

    def postExtendedRemoteLocationConfigurationMapping(self, extendedRemoteLocationConfigurationMapping):
        """Add/update a mapping between remote and Folio locations

        ``POST /remote-storage/extended-mappings``

        Args:
            extendedRemoteLocationConfigurationMapping (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_postExtendedRemoteLocationConfigurationMapping_request.schema
        """
        return self.call("POST", "/remote-storage/extended-mappings", extendedRemoteLocationConfigurationMapping)

		
    def getExtendedRemoteLocationConfigurationMappings(self, **kwargs):
        """Get a list of location mappings

        ``GET /remote-storage/extended-mappings``

        Keyword Args:
            finalLocationId (str): Final location id
            remoteStorageConfigurationId (str): Remote storage configuration id
            originalLocationId (str): Original location id
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_getExtendedRemoteLocationConfigurationMappings_response.schema
        """
        return self.call("GET", "/remote-storage/extended-mappings", query=kwargs)

    def getExtendedRemoteLocationConfigurationMappingsById(self):
        """

        ``GET /remote-storage/extended-mappings/{finalLocationId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Mapping not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_getExtendedRemoteLocationConfigurationMappingsById_response.schema
        """
        return self.call("GET", "/remote-storage/extended-mappings/{finalLocationId}")

    def deleteOriginalLocationByRemoteStorageConfigurationIdAndOriginalLocationId(self, remoteStorageConfigurationId, originalLocationId):
        """

        ``DELETE /remote-storage/extended-mappings/{remoteStorageConfigurationId}/{originalLocationId}``

        Args:
            remoteStorageConfigurationId (str): uuid
            originalLocationId (str): uuid

        Raises:
            OkapiRequestNotFound: Mapping not found
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", "/remote-storage/extended-mappings/{remoteStorageConfigurationId}/{originalLocationId}", remoteStorageConfigurationId, originalLocationId)

    def getExtendedRemoteLocationConfigurationMappingsLocations(self, **kwargs):
        """Get a list of location mappings

        ``GET /remote-storage/extended-mappings/locations``

        Keyword Args:
            remoteStorageConfigurationId (str): Remote storage configuration id
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_getExtendedRemoteLocationConfigurationMappingsLocations_response.schema
        """
        return self.call("GET", "/remote-storage/extended-mappings/locations", query=kwargs)

    def getProviders(self):
        """Get a list of providers

        ``GET /remote-storage/providers``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_getProviders_response.schema
        """
        return self.call("GET", "/remote-storage/providers")

    def postAccession(self, accessionRequest):
        """Perform remote storage initiated accession

        ``POST /remote-storage/accessions``

        Args:
            accessionRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_postAccession_request.schema
            .. literalinclude:: ../files/Remotestorage_postAccession_request.schema_response.schema
        """
        return self.call("POST", "/remote-storage/accessions", accessionRequest)

		
    def getAccessions(self, **kwargs):
        """Get a list of accession records

        ``GET /remote-storage/accessions``

        Keyword Args:
            accessioned (bool): Flag to indicate, that accession queue record was accessioned and has accesion date
            storageId (str): Remote storage id
            createdDate (str): Date of accession queue record creation
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_getAccessions_response.schema
        """
        return self.call("GET", "/remote-storage/accessions", query=kwargs)

    def setAccessionedById(self, accessionId):
        """Set accessioned date by accession queue id

        ``PUT /remote-storage/accessions/id/{accessionId}``

        Args:
            accessionId (str): uuid
        """
        return self.call("PUT", "/remote-storage/accessions/id/{accessionId}", accessionId)

    def setAccessionedByBarcode(self, barcode):
        """Set accessioned date by item barcode

        ``PUT /remote-storage/accessions/barcode/{barcode}``

        Args:
            barcode (str): 
        """
        return self.call("PUT", "/remote-storage/accessions/barcode/{barcode}", barcode)

    def logRecordEvent(self, pubSubEvent):
        """

        ``POST /remote-storage/pub-sub-handlers/log-record-event``

        Args:
            pubSubEvent (dict): See Schema below.

        Schema:

            .. literalinclude:: ../files/Remotestorage_logRecordEvent_request.schema
        """
        return self.call("POST", "/remote-storage/pub-sub-handlers/log-record-event", pubSubEvent)

    def getRetrievals(self, **kwargs):
        """Get a list of retrieval records

        ``GET /remote-storage/retrievals``

        Keyword Args:
            retrieved (bool): Flag to indicate, that retrievals queue record was retrieved and has retrievals date
            storageId (str): Remote storage id
            createdDate (str): Date of accession queue record creation
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_getRetrievals_response.schema
        """
        return self.call("GET", "/remote-storage/retrievals", query=kwargs)

    def setRetrievedById(self, retrievalId):
        """Set retrieval date by retrieval queue id

        ``PUT /remote-storage/retrievals/id/{retrievalId}``

        Args:
            retrievalId (str): uuid
        """
        return self.call("PUT", "/remote-storage/retrievals/id/{retrievalId}", retrievalId)

    def setRetrievedByBarcode(self, barcode):
        """Set retrieved date by item barcode

        ``PUT /remote-storage/retrievals/barcode/{barcode}``

        Args:
            barcode (str): 
        """
        return self.call("PUT", "/remote-storage/retrievals/barcode/{barcode}", barcode)

    def checkInItemByBarcodeWithRemoteStorageConfigurationId(self, remoteStorageConfigurationId, checkInItem):
        """Check-in the item in the primary service by barcode value

        ``POST /remote-storage/retrieve/{remoteStorageConfigurationId}/checkInItem``

        Args:
            remoteStorageConfigurationId (str): uuid
            checkInItem (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_checkInItemByBarcodeWithRemoteStorageConfigurationId_request.schema
        """
        return self.call("POST", "/remote-storage/retrieve/{remoteStorageConfigurationId}/checkInItem", remoteStorageConfigurationId, checkInItem)

    def checkInItemByHoldIdWithRemoteStorageConfigurationId(self, remoteStorageConfigurationId, checkInItemByHoldId):
        """Check-in the item in the primary service by barcode value

        ``POST /remote-storage/retrieve/{remoteStorageConfigurationId}/checkInItemByHoldId``

        Args:
            remoteStorageConfigurationId (str): 
            checkInItemByHoldId (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_checkInItemByHoldIdWithRemoteStorageConfigurationId_request.schema
        """
        return self.call("POST", "/remote-storage/retrieve/{remoteStorageConfigurationId}/checkInItemByHoldId", remoteStorageConfigurationId, checkInItemByHoldId)

    def returnItemByBarcode(self, remoteStorageConfigurationId, checkInItem):
        """Return the item by barcode

        ``POST /remote-storage/return/{remoteStorageConfigurationId}``

        Args:
            remoteStorageConfigurationId (str): 
            checkInItem (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_returnItemByBarcode_request.schema
            .. literalinclude:: ../files/Remotestorage_returnItemByBarcode_request.schema_response.schema
        """
        return self.call("POST", "/remote-storage/return/{remoteStorageConfigurationId}", remoteStorageConfigurationId, checkInItem)

    def markItemAsMissingByBarcode(self, barcode):
        """Mark item as missing

        ``POST /remote-storage/items/barcode/{barcode}/markAsMissing``

        Args:
            barcode (str): 

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server error
        """
        return self.call("POST", "/remote-storage/items/barcode/{barcode}/markAsMissing", barcode)
