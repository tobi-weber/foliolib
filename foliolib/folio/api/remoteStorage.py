# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.remoteStorage")



class Remotestorage(FolioApi):
    """Remote storages API

    
    """

    def getconfigurations(self, **kwargs):
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

            .. literalinclude:: ../files/Remotestorage_getconfigurations_response.schema
        """
        return self.call("GET", "/remote-storage/configurations", query=kwargs)

		
    def postconfiguration(self, storageConfiguration):
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

            .. literalinclude:: ../files/Remotestorage_postconfiguration_request.schema
        """
        return self.call("POST", f"/remote-storage/configurations", storageConfiguration)

    def getconfigurationbyid(self, configId):
        """

        ``GET /remote-storage/configurations/{configId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Configuration not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_getconfigurationbyid_response.schema
        """
        return self.call("GET", f"/remote-storage/configurations/{configId}")

		
    def putconfiguration(self, storageConfiguration, configId):
        """Change the remote storage configuration

        ``PUT /remote-storage/configurations/{configId}``

        Args:
            storageConfiguration (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Configuration not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_putconfiguration_request.schema
        """
        return self.call("PUT", f"/remote-storage/configurations/{configId}", storageConfiguration)

		
    def deleteconfigurationbyid(self, configId):
        """

        ``DELETE /remote-storage/configurations/{configId}``

        Raises:
            OkapiRequestNotFound: Configuration not found
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", f"/remote-storage/configurations/{configId}")

    def postmapping(self, remoteLocationConfigurationMapping):
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

            .. literalinclude:: ../files/Remotestorage_postmapping_request.schema
        """
        return self.call("POST", f"/remote-storage/mappings", remoteLocationConfigurationMapping)

		
    def getmappings(self, **kwargs):
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

            .. literalinclude:: ../files/Remotestorage_getmappings_response.schema
        """
        return self.call("GET", "/remote-storage/mappings", query=kwargs)

    def getmappingbyid(self, folioLocationId):
        """

        ``GET /remote-storage/mappings/{folioLocationId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Mapping not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_getmappingbyid_response.schema
        """
        return self.call("GET", f"/remote-storage/mappings/{folioLocationId}")

		
    def deletemappingbyid(self, folioLocationId):
        """

        ``DELETE /remote-storage/mappings/{folioLocationId}``

        Raises:
            OkapiRequestNotFound: Mapping not found
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", f"/remote-storage/mappings/{folioLocationId}")

    def postextendedremotelocationconfigurationmapping(self, extendedRemoteLocationConfigurationMapping):
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

            .. literalinclude:: ../files/Remotestorage_postextendedremotelocationconfigurationmapping_request.schema
        """
        return self.call("POST", f"/remote-storage/extended-mappings", extendedRemoteLocationConfigurationMapping)

		
    def getextendedremotelocationconfigurationmappings(self, **kwargs):
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

            .. literalinclude:: ../files/Remotestorage_getextendedremotelocationconfigurationmappings_response.schema
        """
        return self.call("GET", "/remote-storage/extended-mappings", query=kwargs)

    def getextendedremotelocationconfigurationmappingsbyid(self, finalLocationId):
        """

        ``GET /remote-storage/extended-mappings/{finalLocationId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Mapping not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_getextendedremotelocationconfigurationmappingsbyid_response.schema
        """
        return self.call("GET", f"/remote-storage/extended-mappings/{finalLocationId}")

    def deleteoriginallocationbyremotestorageconfigurationidandoriginallocationid(self, remoteStorageConfigurationId, originalLocationId):
        """

        ``DELETE /remote-storage/extended-mappings/{remoteStorageConfigurationId}/{originalLocationId}``

        Args:
            remoteStorageConfigurationId (str): uuid
            originalLocationId (str): uuid

        Raises:
            OkapiRequestNotFound: Mapping not found
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", f"/remote-storage/extended-mappings/{remoteStorageConfigurationId}/{originalLocationId}")

    def getextendedremotelocationconfigurationmappingslocations(self, **kwargs):
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

            .. literalinclude:: ../files/Remotestorage_getextendedremotelocationconfigurationmappingslocations_response.schema
        """
        return self.call("GET", "/remote-storage/extended-mappings/locations", query=kwargs)

    def getproviders(self):
        """Get a list of providers

        ``GET /remote-storage/providers``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Remotestorage_getproviders_response.schema
        """
        return self.call("GET", "/remote-storage/providers")

    def postaccession(self, accessionRequest):
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

            .. literalinclude:: ../files/Remotestorage_postaccession_request.schema
            .. literalinclude:: ../files/Remotestorage_postaccession_request.schema_response.schema
        """
        return self.call("POST", f"/remote-storage/accessions", accessionRequest)

		
    def getaccessions(self, **kwargs):
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

            .. literalinclude:: ../files/Remotestorage_getaccessions_response.schema
        """
        return self.call("GET", "/remote-storage/accessions", query=kwargs)

    def setaccessionedbyid(self, accessionId):
        """Set accessioned date by accession queue id

        ``PUT /remote-storage/accessions/id/{accessionId}``

        Args:
            accessionId (str): uuid
        """
        return self.call("PUT", f"/remote-storage/accessions/id/{accessionId}")

    def setaccessionedbybarcode(self, barcode):
        """Set accessioned date by item barcode

        ``PUT /remote-storage/accessions/barcode/{barcode}``

        Args:
            barcode (str): 
        """
        return self.call("PUT", f"/remote-storage/accessions/barcode/{barcode}")

    def logrecordevent(self, pubSubEvent):
        """

        ``POST /remote-storage/pub-sub-handlers/log-record-event``

        Args:
            pubSubEvent (dict): See Schema below.

        Schema:

            .. literalinclude:: ../files/Remotestorage_logrecordevent_request.schema
        """
        return self.call("POST", f"/remote-storage/pub-sub-handlers/log-record-event", pubSubEvent)

    def getretrievals(self, **kwargs):
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

            .. literalinclude:: ../files/Remotestorage_getretrievals_response.schema
        """
        return self.call("GET", "/remote-storage/retrievals", query=kwargs)

    def setretrievedbyid(self, retrievalId):
        """Set retrieval date by retrieval queue id

        ``PUT /remote-storage/retrievals/id/{retrievalId}``

        Args:
            retrievalId (str): uuid
        """
        return self.call("PUT", f"/remote-storage/retrievals/id/{retrievalId}")

    def setretrievedbybarcode(self, barcode):
        """Set retrieved date by item barcode

        ``PUT /remote-storage/retrievals/barcode/{barcode}``

        Args:
            barcode (str): 
        """
        return self.call("PUT", f"/remote-storage/retrievals/barcode/{barcode}")

    def checkinitembybarcodewithremotestorageconfigurationid(self, remoteStorageConfigurationId, checkInItem):
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

            .. literalinclude:: ../files/Remotestorage_checkinitembybarcodewithremotestorageconfigurationid_request.schema
        """
        return self.call("POST", f"/remote-storage/retrieve/{remoteStorageConfigurationId}/checkInItem", checkInItem)

    def checkinitembyholdidwithremotestorageconfigurationid(self, remoteStorageConfigurationId, checkInItemByHoldId):
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

            .. literalinclude:: ../files/Remotestorage_checkinitembyholdidwithremotestorageconfigurationid_request.schema
        """
        return self.call("POST", f"/remote-storage/retrieve/{remoteStorageConfigurationId}/checkInItemByHoldId", checkInItemByHoldId)

    def returnitembybarcode(self, remoteStorageConfigurationId, checkInItem):
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

            .. literalinclude:: ../files/Remotestorage_returnitembybarcode_request.schema
            .. literalinclude:: ../files/Remotestorage_returnitembybarcode_request.schema_response.schema
        """
        return self.call("POST", f"/remote-storage/return/{remoteStorageConfigurationId}", checkInItem)

    def markitemasmissingbybarcode(self, barcode):
        """Mark item as missing

        ``POST /remote-storage/items/barcode/{barcode}/markAsMissing``

        Args:
            barcode (str): 

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server error
        """
        return self.call("POST", f"/remote-storage/items/barcode/{barcode}/markAsMissing")
