# -*- coding: utf-8 -*-
# Generated at 2023-04-16

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.innReach")



class ContributionAdmin(FolioAdminApi):
    """INN-Reach Contribution API
    Administration

    
    """

    def getCurrentContributionByServerId(self, centralServerId):
        """Get current INN-Reach contribution for the given central server

        ``GET /inn-reach/central-servers/{centralServerId}/contributions/current``

        Args:
            centralServerId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed query parameter.
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Contribution_getCurrentContributionByServerId_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/contributions/current", centralServerId)

		
    def cancelCurrentContributionByServerId(self, centralServerId):
        """Cancel current INN-Reach contribution for the given central server

        ``DELETE /inn-reach/central-servers/{centralServerId}/contributions/current``

        Args:
            centralServerId (str):  (format: uuid)

        Raises:
            OkapiRequestError: Bad request, e.g. malformed query parameter.
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", "/inn-reach/central-servers/{centralServerId}/contributions/current", centralServerId)

    def getContributionHistoryByServerId(self, centralServerId, **kwargs):
        """Get a list of Inn-Reach contributions for the given central server

        ``GET /inn-reach/central-servers/{centralServerId}/contributions/history``

        Args:
            centralServerId (str):  (format: uuid)

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed query parameter.
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Contribution_getContributionHistoryByServerId_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/contributions/history", centralServerId, query=kwargs)

    def startInitialContribution(self, centralServerId):
        """Start initial contribution process

        ``POST /inn-reach/central-servers/{centralServerId}/contributions``

        Args:
            centralServerId (str):  (format: uuid)

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server error
        """
        return self.call("POST", "/inn-reach/central-servers/{centralServerId}/contributions", centralServerId)



class SettingsAdmin(FolioAdminApi):
    """INN-Reach Settings API
    Administration

    
    """

    def postCentralServer(self, centralServerDTO):
        """Add new central server

        ``POST /inn-reach/central-servers``

        Args:
            centralServerDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestConflict: Item state conflict
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_postCentralServer_request.schema
        """
        return self.call("POST", "/inn-reach/central-servers", centralServerDTO)

		
    def getCentralServers(self, **kwargs):
        """Get a list of central servers

        ``GET /inn-reach/central-servers``

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getCentralServers_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers", query=kwargs)

    def getCentralServerById(self, id_):
        """Get central server by id

        ``GET /inn-reach/central-servers/{centralServerId}``

        Args:
            id_ (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getCentralServerById_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}", id_)

		
    def updateCentralServer(self, id_, centralServerDTO):
        """Update central server

        ``PUT /inn-reach/central-servers/{centralServerId}``

        Args:
            id_ (str):  (format: uuid)
            centralServerDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_updateCentralServer_request.schema
        """
        return self.call("PUT", "/inn-reach/central-servers/{centralServerId}", id_, centralServerDTO)

		
    def deleteCentralServer(self, id_):
        """Delete central server

        ``DELETE /inn-reach/central-servers/{centralServerId}``

        Args:
            id_ (str):  (format: uuid)

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", "/inn-reach/central-servers/{centralServerId}", id_)

    def getMaterialTypeMappingsByServerId(self, centralServerId, **kwargs):
        """Get a list of material type mappings for the given central server

        ``GET /inn-reach/central-servers/{centralServerId}/material-type-mappings``

        Args:
            centralServerId (str):  (format: uuid)

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed query parameter.
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getMaterialTypeMappingsByServerId_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/material-type-mappings", centralServerId, query=kwargs)

		
    def postMaterialTypeMapping(self, centralServerId, materialTypeMappingDTO):
        """Add new material type mapping associated with the central server

        ``POST /inn-reach/central-servers/{centralServerId}/material-type-mappings``

        Args:
            centralServerId (str):  (format: uuid)
            materialTypeMappingDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestConflict: Item state conflict
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_postMaterialTypeMapping_request.schema
        """
        return self.call("POST", "/inn-reach/central-servers/{centralServerId}/material-type-mappings", centralServerId, materialTypeMappingDTO)

		
    def updateMaterialTypeMappings(self, centralServerId, materialTypeMappingsDTO):
        """Update (replace) the entire collection of material type mappings associated with the central server

        ``PUT /inn-reach/central-servers/{centralServerId}/material-type-mappings``

        Args:
            centralServerId (str):  (format: uuid)
            materialTypeMappingsDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestConflict: Item state conflict
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_updateMaterialTypeMappings_request.schema
        """
        return self.call("PUT", "/inn-reach/central-servers/{centralServerId}/material-type-mappings", centralServerId, materialTypeMappingsDTO)

    def getMaterialTypeMappingById(self, centralServerId, id_):
        """Get material type mapping by id

        ``GET /inn-reach/central-servers/{centralServerId}/material-type-mappings/{id}``

        Args:
            centralServerId (str):  (format: uuid)
            id_ (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getMaterialTypeMappingById_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/material-type-mappings/{id}", centralServerId, id_)

		
    def updateMaterialTypeMapping(self, centralServerId, id_, materialTypeMappingDTO):
        """Update material type mapping

        ``PUT /inn-reach/central-servers/{centralServerId}/material-type-mappings/{id}``

        Args:
            centralServerId (str):  (format: uuid)
            id_ (str):  (format: uuid)
            materialTypeMappingDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_updateMaterialTypeMapping_request.schema
        """
        return self.call("PUT", "/inn-reach/central-servers/{centralServerId}/material-type-mappings/{id}", centralServerId, id_, materialTypeMappingDTO)

		
    def deleteMaterialTypeMapping(self, centralServerId, id_):
        """Delete material type mapping

        ``DELETE /inn-reach/central-servers/{centralServerId}/material-type-mappings/{id}``

        Args:
            centralServerId (str):  (format: uuid)
            id_ (str):  (format: uuid)

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", "/inn-reach/central-servers/{centralServerId}/material-type-mappings/{id}", centralServerId, id_)

    def postInnReachLocation(self, innReachLocationDTO):
        """Add new InnReach location

        ``POST /inn-reach/locations``

        Args:
            innReachLocationDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_postInnReachLocation_request.schema
        """
        return self.call("POST", "/inn-reach/locations", innReachLocationDTO)

		
    def getLocations(self, **kwargs):
        """Get a list of InnReach locations

        ``GET /inn-reach/locations``

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getLocations_response.schema
        """
        return self.call("GET", "/inn-reach/locations", query=kwargs)

    def getLocationById(self, id_):
        """Get InnReach location by id

        ``GET /inn-reach/locations/{locationId}``

        Args:
            id_ (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getLocationById_response.schema
        """
        return self.call("GET", "/inn-reach/locations/{locationId}", id_)

		
    def updateLocation(self, id_, innReachLocationDTO):
        """Update InnReach location

        ``PUT /inn-reach/locations/{locationId}``

        Args:
            id_ (str):  (format: uuid)
            innReachLocationDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_updateLocation_request.schema
        """
        return self.call("PUT", "/inn-reach/locations/{locationId}", id_, innReachLocationDTO)

		
    def deleteLocation(self, id_):
        """Delete InnReach location

        ``DELETE /inn-reach/locations/{locationId}``

        Args:
            id_ (str):  (format: uuid)

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", "/inn-reach/locations/{locationId}", id_)

    def getLibraryMappingsByServerId(self, centralServerId, **kwargs):
        """Get a list of library to Inn-Reach location mappings for the given central server

        ``GET /inn-reach/central-servers/{centralServerId}/libraries/location-mappings``

        Args:
            centralServerId (str):  (format: uuid)

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed query parameter.
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getLibraryMappingsByServerId_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/libraries/location-mappings", centralServerId, query=kwargs)

		
    def putLibraryMappings(self, centralServerId, libraryMappingsDTO):
        """Update (replace) the entire collection of library to Inn-Reach location mappings associated with the central server

        ``PUT /inn-reach/central-servers/{centralServerId}/libraries/location-mappings``

        Args:
            centralServerId (str):  (format: uuid)
            libraryMappingsDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestConflict: Item state conflict
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_putLibraryMappings_request.schema
        """
        return self.call("PUT", "/inn-reach/central-servers/{centralServerId}/libraries/location-mappings", centralServerId, libraryMappingsDTO)

    def getLocationMappingsByServerId(self, centralServerId, libraryId, **kwargs):
        """Get a list of library location to Inn-Reach location mappings for the given central server

        ``GET /inn-reach/central-servers/{centralServerId}/libraries/{libraryId}/locations/location-mappings``

        Args:
            centralServerId (str):  (format: uuid)
            libraryId (str):  (format: uuid)

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed query parameter.
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getLocationMappingsByServerId_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/libraries/{libraryId}/locations/location-mappings", centralServerId, libraryId, query=kwargs)

		
    def putLocationMappings(self, centralServerId, libraryId, locationMappingsDTO):
        """Update (replace) the entire collection of library location to Inn-Reach location mappings associated with the central server

        ``PUT /inn-reach/central-servers/{centralServerId}/libraries/{libraryId}/locations/location-mappings``

        Args:
            centralServerId (str):  (format: uuid)
            libraryId (str):  (format: uuid)
            locationMappingsDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestConflict: Item state conflict
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_putLocationMappings_request.schema
        """
        return self.call("PUT", "/inn-reach/central-servers/{centralServerId}/libraries/{libraryId}/locations/location-mappings", centralServerId, libraryId, locationMappingsDTO)

    def getLocationMappingsForAllLibrariesByServerId(self, centralServerId):
        """Get a list of libraries locations to Inn-Reach location mappings for the given central server

        ``GET /inn-reach/central-servers/{centralServerId}/libraries/locations/location-mappings``

        Args:
            centralServerId (str):  (format: uuid)

        Raises:
            OkapiRequestError: Bad request, e.g. malformed query parameter.
            OkapiFatalError: Internal server error
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/libraries/locations/location-mappings", centralServerId)

    def getCriteriaByServerId(self, centralServerId):
        """Get Contribution Criteria by Central Server id

        ``GET /inn-reach/central-servers/{centralServerId}/contribution-criteria``

        Args:
            centralServerId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getCriteriaByServerId_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/contribution-criteria", centralServerId)

		
    def postContributionCriteria(self, centralServerId, contributionCriteriaDTO):
        """Create new contribution criteria for Central Server

        ``POST /inn-reach/central-servers/{centralServerId}/contribution-criteria``

        Args:
            centralServerId (str):  (format: uuid)
            contributionCriteriaDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestConflict: Item state conflict
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_postContributionCriteria_request.schema
        """
        return self.call("POST", "/inn-reach/central-servers/{centralServerId}/contribution-criteria", centralServerId, contributionCriteriaDTO)

		
    def deleteCriteria(self, centralServerId):
        """Delete Contribution Criteria Configuration

        ``DELETE /inn-reach/central-servers/{centralServerId}/contribution-criteria``

        Args:
            centralServerId (str):  (format: uuid)

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", "/inn-reach/central-servers/{centralServerId}/contribution-criteria", centralServerId)

		
    def updateCriteria(self, centralServerId, contributionCriteriaDTO):
        """Update Contribution Criteria Configuration

        ``PUT /inn-reach/central-servers/{centralServerId}/contribution-criteria``

        Args:
            centralServerId (str):  (format: uuid)
            contributionCriteriaDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Item not found
            OkapiRequestConflict: Item state conflict
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_updateCriteria_request.schema
        """
        return self.call("PUT", "/inn-reach/central-servers/{centralServerId}/contribution-criteria", centralServerId, contributionCriteriaDTO)

    def authenticateLocalServerKeySecret(self, authenticationRequest):
        """Authenticate InnReach local server key/secret pair

        ``POST /inn-reach/authentication``

        Args:
            authenticationRequest (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestUnauthorized: Unauthorized
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_authenticateLocalServerKeySecret_request.schema
        """
        return self.call("POST", "/inn-reach/authentication", authenticationRequest)

    def getItemContributionOptionsConfigurationById(self, centralServerId):
        """Get Item Contribution Options Configuration by id

        ``GET /inn-reach/central-servers/{centralServerId}/item-contribution-options``

        Args:
            centralServerId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getItemContributionOptionsConfigurationById_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/item-contribution-options", centralServerId)

		
    def updateItemContributionOptionsConfiguration(self, centralServerId, itemContributionOptionsConfigurationDTO):
        """Update Item Contribution Options Configuration

        ``PUT /inn-reach/central-servers/{centralServerId}/item-contribution-options``

        Args:
            centralServerId (str):  (format: uuid)
            itemContributionOptionsConfigurationDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_updateItemContributionOptionsConfiguration_request.schema
        """
        return self.call("PUT", "/inn-reach/central-servers/{centralServerId}/item-contribution-options", centralServerId, itemContributionOptionsConfigurationDTO)

		
    def createItemContributionOptionsConfiguration(self, centralServerId, itemContributionOptionsConfigurationDTO):
        """Add new item contribution options configuration associated with the central server

        ``POST /inn-reach/central-servers/{centralServerId}/item-contribution-options``

        Args:
            centralServerId (str):  (format: uuid)
            itemContributionOptionsConfigurationDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_createItemContributionOptionsConfiguration_request.schema
        """
        return self.call("POST", "/inn-reach/central-servers/{centralServerId}/item-contribution-options", centralServerId, itemContributionOptionsConfigurationDTO)

    def getAgencyMappingsByServerId(self, centralServerId):
        """Get a list of Inn-Reach Agency to FOLIO location mappings for the given central server

        ``GET /inn-reach/central-servers/{centralServerId}/agency-mappings``

        Args:
            centralServerId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed query parameter.
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getAgencyMappingsByServerId_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/agency-mappings", centralServerId)

		
    def putAgencyMappings(self, centralServerId, agencyLocationMappingDTO):
        """Update (add) INN-Reach Agency to FOLIO location mappings associated with the central server

        ``PUT /inn-reach/central-servers/{centralServerId}/agency-mappings``

        Args:
            centralServerId (str):  (format: uuid)
            agencyLocationMappingDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestConflict: Item state conflict
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_putAgencyMappings_request.schema
        """
        return self.call("PUT", "/inn-reach/central-servers/{centralServerId}/agency-mappings", centralServerId, agencyLocationMappingDTO)

    def getMARCTransformationOptionsSettingsById(self, centralServerId):
        """Get MARC Transformation Options Settings by id

        ``GET /inn-reach/central-servers/{centralServerId}/marc-transformation-options``

        Args:
            centralServerId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getMARCTransformationOptionsSettingsById_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/marc-transformation-options", centralServerId)

		
    def updateMARCTransformationOptionsSettings(self, centralServerId, MARCTransformationOptionsSettingsDTO):
        """Update MARC Transformation Options Settings

        ``PUT /inn-reach/central-servers/{centralServerId}/marc-transformation-options``

        Args:
            centralServerId (str):  (format: uuid)
            MARCTransformationOptionsSettingsDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_updateMARCTransformationOptionsSettings_request.schema
        """
        return self.call("PUT", "/inn-reach/central-servers/{centralServerId}/marc-transformation-options", centralServerId, MARCTransformationOptionsSettingsDTO)

		
    def createMARCTransformationOptionsSettings(self, centralServerId, MARCTransformationOptionsSettingsDTO):
        """Add new MARC Transformation Options Settings associated with the central server

        ``POST /inn-reach/central-servers/{centralServerId}/marc-transformation-options``

        Args:
            centralServerId (str):  (format: uuid)
            MARCTransformationOptionsSettingsDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_createMARCTransformationOptionsSettings_request.schema
        """
        return self.call("POST", "/inn-reach/central-servers/{centralServerId}/marc-transformation-options", centralServerId, MARCTransformationOptionsSettingsDTO)

		
    def deleteMARCTransformationOptionsSettings(self, centralServerId):
        """Delete Marc Transformation Options Settings

        ``DELETE /inn-reach/central-servers/{centralServerId}/marc-transformation-options``

        Args:
            centralServerId (str):  (format: uuid)

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", "/inn-reach/central-servers/{centralServerId}/marc-transformation-options", centralServerId)

    def getAllMARCTransformationOptionsSettings(self, **kwargs):
        """Get a list of Marc Transformation Options Settings

        ``GET /inn-reach/central-servers/marc-transformation-options``

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getAllMARCTransformationOptionsSettings_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/marc-transformation-options", query=kwargs)

    def getPatronTypeMappingsByServerId(self, centralServerId, **kwargs):
        """Get a list of Patron Type Mappings

        ``GET /inn-reach/central-servers/{centralServerId}/patron-type-mappings``

        Args:
            centralServerId (str):  (format: uuid)

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getPatronTypeMappingsByServerId_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/patron-type-mappings", centralServerId, query=kwargs)

		
    def updatePatronTypeMappings(self, centralServerId, patronTypeMappingsDTO):
        """Update Patron Type Mappings

        ``PUT /inn-reach/central-servers/{centralServerId}/patron-type-mappings``

        Args:
            centralServerId (str):  (format: uuid)
            patronTypeMappingsDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_updatePatronTypeMappings_request.schema
        """
        return self.call("PUT", "/inn-reach/central-servers/{centralServerId}/patron-type-mappings", centralServerId, patronTypeMappingsDTO)

    def transformMARCRecord(self, centralServerId, inventoryInstanceId):
        """Transform MARC record by Id according to CentralServer settings

        ``GET /inn-reach/central-servers/{centralServerId}/marc-record-transformation/{inventoryInstanceId}``

        Args:
            centralServerId (str):  (format: uuid)
            inventoryInstanceId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_transformMARCRecord_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/marc-record-transformation/{inventoryInstanceId}", centralServerId, inventoryInstanceId)

    def getItemTypeMappingsByServerId(self, centralServerId, **kwargs):
        """Get a list of Item Type Mappings

        ``GET /inn-reach/central-servers/{centralServerId}/item-type-mappings``

        Args:
            centralServerId (str):  (format: uuid)

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getItemTypeMappingsByServerId_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/item-type-mappings", centralServerId, query=kwargs)

		
    def updateItemTypeMappings(self, centralServerId, itemTypeMappingsDTO):
        """Update Item Type Mappings

        ``PUT /inn-reach/central-servers/{centralServerId}/item-type-mappings``

        Args:
            centralServerId (str):  (format: uuid)
            itemTypeMappingsDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_updateItemTypeMappings_request.schema
        """
        return self.call("PUT", "/inn-reach/central-servers/{centralServerId}/item-type-mappings", centralServerId, itemTypeMappingsDTO)

    def getUserCustomFieldMapping(self, centralServerId):
        """Get a User Custom Field Mapping

        ``GET /inn-reach/central-servers/{centralServerId}/user-custom-field-mappings``

        Args:
            centralServerId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getUserCustomFieldMapping_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/user-custom-field-mappings", centralServerId)

		
    def updateUserCustomFieldMapping(self, centralServerId, userCustomFieldMappingDTO):
        """Update User Custom Field Mapping

        ``PUT /inn-reach/central-servers/{centralServerId}/user-custom-field-mappings``

        Args:
            centralServerId (str):  (format: uuid)
            userCustomFieldMappingDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_updateUserCustomFieldMapping_request.schema
        """
        return self.call("PUT", "/inn-reach/central-servers/{centralServerId}/user-custom-field-mappings", centralServerId, userCustomFieldMappingDTO)

		
    def createUserCustomFieldMapping(self, centralServerId, userCustomFieldMappingDTO):
        """Add new User Custom Field Mapping associated with the central server

        ``POST /inn-reach/central-servers/{centralServerId}/user-custom-field-mappings``

        Args:
            centralServerId (str):  (format: uuid)
            userCustomFieldMappingDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_createUserCustomFieldMapping_request.schema
        """
        return self.call("POST", "/inn-reach/central-servers/{centralServerId}/user-custom-field-mappings", centralServerId, userCustomFieldMappingDTO)

    def getCentralPatronTypeMappings(self, centralServerId, **kwargs):
        """Get a list of Central Patron Type Mappings

        ``GET /inn-reach/central-servers/{centralServerId}/central-patron-type-mappings``

        Args:
            centralServerId (str):  (format: uuid)

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getCentralPatronTypeMappings_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/central-patron-type-mappings", centralServerId, query=kwargs)

		
    def updateCentralPatronTypeMappings(self, centralServerId, centralPatronTypeMappingsDTO):
        """Update Central Patron Type Mappings

        ``PUT /inn-reach/central-servers/{centralServerId}/central-patron-type-mappings``

        Args:
            centralServerId (str):  (format: uuid)
            centralPatronTypeMappingsDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_updateCentralPatronTypeMappings_request.schema
        """
        return self.call("PUT", "/inn-reach/central-servers/{centralServerId}/central-patron-type-mappings", centralServerId, centralPatronTypeMappingsDTO)

    def saveInnReachRecallUser(self, centralServerId, innReachRecallUserDTO):
        """Add new Inn-Reach recall user to central server

        ``POST /inn-reach/central-servers/{centralServerId}/inn-reach-recall-user``

        Args:
            centralServerId (str):  (format: uuid)
            innReachRecallUserDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_saveInnReachRecallUser_request.schema
        """
        return self.call("POST", "/inn-reach/central-servers/{centralServerId}/inn-reach-recall-user", centralServerId, innReachRecallUserDTO)

		
    def getCentralServerRecallUser(self, centralServerId):
        """Get Inn-Reach Central server recall user

        ``GET /inn-reach/central-servers/{centralServerId}/inn-reach-recall-user``

        Args:
            centralServerId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getCentralServerRecallUser_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/inn-reach-recall-user", centralServerId)

		
    def updateCentralServerRecallUser(self, centralServerId, innReachRecallUserDTO):
        """Update Inn-Reach Central server recall user

        ``PUT /inn-reach/central-servers/{centralServerId}/inn-reach-recall-user``

        Args:
            centralServerId (str):  (format: uuid)
            innReachRecallUserDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_updateCentralServerRecallUser_request.schema
        """
        return self.call("PUT", "/inn-reach/central-servers/{centralServerId}/inn-reach-recall-user", centralServerId, innReachRecallUserDTO)

    def getConfigurationByCentralServerId(self, centralServerId):
        """Get Visible Patron Field Configuration by Central Server id

        ``GET /inn-reach/central-servers/{centralServerId}/visible-patron-field-configuration``

        Args:
            centralServerId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getConfigurationByCentralServerId_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/visible-patron-field-configuration", centralServerId)

		
    def updateConfiguration(self, centralServerId, visiblePatronFieldConfigurationDTO):
        """Update Visible Patron Field Configuration

        ``PUT /inn-reach/central-servers/{centralServerId}/visible-patron-field-configuration``

        Args:
            centralServerId (str):  (format: uuid)
            visiblePatronFieldConfigurationDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_updateConfiguration_request.schema
        """
        return self.call("PUT", "/inn-reach/central-servers/{centralServerId}/visible-patron-field-configuration", centralServerId, visiblePatronFieldConfigurationDTO)

		
    def createConfiguration(self, centralServerId, visiblePatronFieldConfigurationDTO):
        """Add new Visible Patron Field Configuration associated with the central server

        ``POST /inn-reach/central-servers/{centralServerId}/visible-patron-field-configuration``

        Args:
            centralServerId (str):  (format: uuid)
            visiblePatronFieldConfigurationDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_createConfiguration_request.schema
        """
        return self.call("POST", "/inn-reach/central-servers/{centralServerId}/visible-patron-field-configuration", centralServerId, visiblePatronFieldConfigurationDTO)

    def getPagingSlipTemplate(self, centralServerId):
        """Get Paging Slip Template

        ``GET /inn-reach/central-servers/{centralServerId}/paging-slip-template``

        Args:
            centralServerId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getPagingSlipTemplate_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/{centralServerId}/paging-slip-template", centralServerId)

		
    def updatePagingSlipTemplate(self, centralServerId, pagingSlipTemplateDTO):
        """Update Paging Slip Template

        ``PUT /inn-reach/central-servers/{centralServerId}/paging-slip-template``

        Args:
            centralServerId (str):  (format: uuid)
            pagingSlipTemplateDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_updatePagingSlipTemplate_request.schema
        """
        return self.call("PUT", "/inn-reach/central-servers/{centralServerId}/paging-slip-template", centralServerId, pagingSlipTemplateDTO)

    def getAllPagingSlipTemplates(self):
        """Get list of Paging Slip Templates

        ``GET /inn-reach/central-servers/paging-slip-template``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getAllPagingSlipTemplates_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/paging-slip-template")




class CirculationAdmin(FolioAdminApi):
    """INN-Reach Circulation API
    Administration

    
    """

    def getCentralServerAgencies(self):
        """Get a combined list of agencies available from all configured central servers

        ``GET /inn-reach/central-servers/agencies``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_getCentralServerAgencies_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/agencies")

    def getCentralServerItemTypes(self):
        """Get a combined list of item types available from all configured central servers

        ``GET /inn-reach/central-servers/item-types``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_getCentralServerItemTypes_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/item-types")

    def getCentralServerPatronTypes(self):
        """Get a combined list of patron types available from all configured central servers

        ``GET /inn-reach/central-servers/patron-types``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_getCentralServerPatronTypes_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/patron-types")

    def getBibRecord(self, bibId, centralCode):
        """Handles D2IR request from central server for an already-contributed Bib record.

        ``POST /inn-reach/d2ir/getbibrecord/{bibId}/{centralCode}``

        Args:
            bibId (str): 32-character, alphanumeric id corresponding to a FOLIO instance record HRID
            centralCode (str): Unique code that identifies the central server (match against value stored in Central Server settings, used to determine contribution status) (pattern: [a-z,0-9]{3,5})

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_getBibRecord_response.schema
        """
        return self.call("POST", "/inn-reach/d2ir/getbibrecord/{bibId}/{centralCode}", bibId, centralCode)

    def createInnReachTransactionItemHold(self, trackingId, centralCode, transactionHoldDTO):
        """Originates an item hold at the owning site

        ``POST /inn-reach/d2ir/circ/itemhold/{trackingId}/{centralCode}``

        Args:
            trackingId (str): 
            centralCode (str): Unique code that identifies the central server (match against value stored in Central Server settings, used to determine contribution status) (pattern: [a-z,0-9]{3,5})
            transactionHoldDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: An error occurred during creation of transaction record
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_createInnReachTransactionItemHold_request.schema
            .. literalinclude:: ../files/Circulation_createInnReachTransactionItemHold_request.schema_response.schema
        """
        return self.call("POST", "/inn-reach/d2ir/circ/itemhold/{trackingId}/{centralCode}", trackingId, centralCode, transactionHoldDTO)

    def getAllTransactions(self, **kwargs):
        """Get a list of transactions for the given central server

        ``GET /inn-reach/transactions``

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)
            parameters (str): Query parameters to filter transactions.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed query parameter.
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_getAllTransactions_response.schema
        """
        return self.call("GET", "/inn-reach/transactions", query=kwargs)

    def getInnReachTransaction(self, id_):
        """get inn-reach transaction by id

        ``GET /inn-reach/transactions/{id}``

        Args:
            id_ (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_getInnReachTransaction_response.schema
        """
        return self.call("GET", "/inn-reach/transactions/{id}", id_)

		
    def updateInnReachTransaction(self, id_, innReachTransactionDTO):
        """update inn-reach transaction by id

        ``PUT /inn-reach/transactions/{id}``

        Args:
            id_ (str):  (format: uuid)
            innReachTransactionDTO (dict): See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_updateInnReachTransaction_request.schema
        """
        return self.call("PUT", "/inn-reach/transactions/{id}", id_, innReachTransactionDTO)

    def checkInPatronHoldItem(self, id_, servicePointId):
        """receive item for patron hold transaction

        ``POST /inn-reach/transactions/{id}/receive-item/{servicePointId}``

        Args:
            id_ (str):  (format: uuid)
            servicePointId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_checkInPatronHoldItem_response.schema
        """
        return self.call("POST", "/inn-reach/transactions/{id}/receive-item/{servicePointId}", id_, servicePointId)

    def checkInPatronHoldUnshippedItem(self, id_, servicePointId, itemBarcode):
        """receive un-shipped/unannounced item for patron hold transaction

        ``POST /inn-reach/transactions/{id}/receive-unshipped-item/{servicePointId}/{itemBarcode}``

        Args:
            id_ (str):  (format: uuid)
            servicePointId (str):  (format: uuid)
            itemBarcode (str): Barcode of the item

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_checkInPatronHoldUnshippedItem_response.schema
        """
        return self.call("POST", "/inn-reach/transactions/{id}/receive-unshipped-item/{servicePointId}/{itemBarcode}", id_, servicePointId, itemBarcode)

    def finalCheckInItemHold(self, id_, servicePointId):
        """Final check-in of an item loaned through INN-Reach

        ``POST /inn-reach/transactions/{id}/itemhold/finalcheckin/{servicePointId}``

        Args:
            id_ (str):  (format: uuid)
            servicePointId (str):  (format: uuid)

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error
        """
        return self.call("POST", "/inn-reach/transactions/{id}/itemhold/finalcheckin/{servicePointId}", id_, servicePointId)

    def transferItemHold(self, id_, itemId):
        """Transfer item hold to another item

        ``POST /inn-reach/transactions/{id}/itemhold/transfer-item/{itemId}``

        Args:
            id_ (str):  (format: uuid)
            itemId (str):  (format: uuid)

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error
        """
        return self.call("POST", "/inn-reach/transactions/{id}/itemhold/transfer-item/{itemId}", id_, itemId)

    def checkOutPatronHoldItem(self, id_, servicePointId):
        """Checks out to requesting patron

        ``POST /inn-reach/transactions/{id}/patronhold/check-out-item/{servicePointId}``

        Args:
            id_ (str):  (format: uuid)
            servicePointId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_checkOutPatronHoldItem_response.schema
        """
        return self.call("POST", "/inn-reach/transactions/{id}/patronhold/check-out-item/{servicePointId}", id_, servicePointId)

    def checkOutLocalHoldItem(self, id_, servicePointId):
        """Checks out Local Hold item to requesting patron

        ``POST /inn-reach/transactions/{id}/localhold/check-out-item/{servicePointId}``

        Args:
            id_ (str):  (format: uuid)
            servicePointId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_checkOutLocalHoldItem_response.schema
        """
        return self.call("POST", "/inn-reach/transactions/{id}/localhold/check-out-item/{servicePointId}", id_, servicePointId)

    def checkOutItemHoldItem(self, itemBarcode, servicePointId):
        """checks out an item from the owning site to the borrowing site for an Item Hold transaction

        ``PUT /inn-reach/transactions/{itemBarcode}/check-out-item/{servicePointId}``

        Args:
            itemBarcode (str): Barcode of the item
            servicePointId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_checkOutItemHoldItem_response.schema
        """
        return self.call("PUT", "/inn-reach/transactions/{itemBarcode}/check-out-item/{servicePointId}", itemBarcode, servicePointId)

    def cancelPatronHoldTransaction(self, id_, cancelTransactionHoldDTO):
        """Cancel patron hold transaction with the reason provided

        ``POST /inn-reach/transactions/{id}/patronhold/cancel``

        Args:
            id_ (str):  (format: uuid)
            cancelTransactionHoldDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_cancelPatronHoldTransaction_request.schema
            .. literalinclude:: ../files/Circulation_cancelPatronHoldTransaction_request.schema_response.schema
        """
        return self.call("POST", "/inn-reach/transactions/{id}/patronhold/cancel", id_, cancelTransactionHoldDTO)

    def recallItemHoldTransaction(self, id_):
        """Recall item hold transaction

        ``POST /inn-reach/transactions/{id}/itemhold/recall``

        Args:
            id_ (str):  (format: uuid)

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error
        """
        return self.call("POST", "/inn-reach/transactions/{id}/itemhold/recall", id_)

    def returnPatronHoldItem(self, id_, servicePointId):
        """Returns Patron Hold item

        ``POST /inn-reach/transactions/{id}/patronhold/return-item/{servicePointId}``

        Args:
            id_ (str):  (format: uuid)
            servicePointId (str):  (format: uuid)

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error
        """
        return self.call("POST", "/inn-reach/transactions/{id}/patronhold/return-item/{servicePointId}", id_, servicePointId)

    def cancelItemHoldTransaction(self, id_, cancelTransactionHoldDTO):
        """Cancel item hold transaction with the reason provided

        ``POST /inn-reach/transactions/{id}/itemhold/cancel``

        Args:
            id_ (str):  (format: uuid)
            cancelTransactionHoldDTO (dict): See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_cancelItemHoldTransaction_request.schema
        """
        return self.call("POST", "/inn-reach/transactions/{id}/itemhold/cancel", id_, cancelTransactionHoldDTO)

    def cancelLocalHoldTransaction(self, id_, cancelTransactionHoldDTO):
        """Cancel local hold transaction with the reason provided

        ``POST /inn-reach/transactions/{id}/localhold/cancel``

        Args:
            id_ (str):  (format: uuid)
            cancelTransactionHoldDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_cancelLocalHoldTransaction_request.schema
            .. literalinclude:: ../files/Circulation_cancelLocalHoldTransaction_request.schema_response.schema
        """
        return self.call("POST", "/inn-reach/transactions/{id}/localhold/cancel", id_, cancelTransactionHoldDTO)

    def verifyPatron(self, patronInfoRequestDTO):
        """Handles D2IR request from central server for patron verification.

        ``POST /inn-reach/d2ir/circ/verifypatron``

        Args:
            patronInfoRequestDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_verifyPatron_request.schema
            .. literalinclude:: ../files/Circulation_verifyPatron_request.schema_response.schema
        """
        return self.call("POST", "/inn-reach/d2ir/circ/verifypatron", patronInfoRequestDTO)

    def patronHold(self, trackingId, centralCode, patronHoldDTO):
        """Originate a patron hold

        ``POST /inn-reach/d2ir/circ/patronhold/{trackingId}/{centralCode}``

        Args:
            trackingId (str): 
            centralCode (str): Unique code that identifies the central server (match against value stored in Central Server settings, used to determine contribution status) (pattern: [a-z,0-9]{3,5})
            patronHoldDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: An error occurred during processing the request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_patronHold_request.schema
            .. literalinclude:: ../files/Circulation_patronHold_request.schema_response.schema
        """
        return self.call("POST", "/inn-reach/d2ir/circ/patronhold/{trackingId}/{centralCode}", trackingId, centralCode, patronHoldDTO)

    def itemShipped(self, trackingId, centralCode, itemShippedDTO):
        """Process shipped item

        ``PUT /inn-reach/d2ir/circ/itemshipped/{trackingId}/{centralCode}``

        Args:
            trackingId (str): 
            centralCode (str): Unique code that identifies the central server (match against value stored in Central Server settings, used to determine contribution status) (pattern: [a-z,0-9]{3,5})
            itemShippedDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: An error occurred during processing the request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_itemShipped_request.schema
            .. literalinclude:: ../files/Circulation_itemShipped_request.schema_response.schema
        """
        return self.call("PUT", "/inn-reach/d2ir/circ/itemshipped/{trackingId}/{centralCode}", trackingId, centralCode, itemShippedDTO)

    def cancelPatronHold(self, trackingId, centralCode, cancelRequestDTO):
        """Cancel Patron Hold transaction

        ``PUT /inn-reach/d2ir/circ/cancelrequest/{trackingId}/{centralCode}``

        Args:
            trackingId (str): 
            centralCode (str): Unique code that identifies the central server (match against value stored in Central Server settings, used to determine contribution status) (pattern: [a-z,0-9]{3,5})
            cancelRequestDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: An error occurred during processing the request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_cancelPatronHold_request.schema
            .. literalinclude:: ../files/Circulation_cancelPatronHold_request.schema_response.schema
        """
        return self.call("PUT", "/inn-reach/d2ir/circ/cancelrequest/{trackingId}/{centralCode}", trackingId, centralCode, cancelRequestDTO)

    def transferRequest(self, trackingId, centralCode, transferRequestDTO):
        """Put transfer request

        ``PUT /inn-reach/d2ir/circ/transferrequest/{trackingId}/{centralCode}``

        Args:
            trackingId (str): 
            centralCode (str): Unique code that identifies the central server (match against value stored in Central Server settings, used to determine contribution status) (pattern: [a-z,0-9]{3,5})
            transferRequestDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: An error occurred during processing the request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_transferRequest_request.schema
            .. literalinclude:: ../files/Circulation_transferRequest_request.schema_response.schema
        """
        return self.call("PUT", "/inn-reach/d2ir/circ/transferrequest/{trackingId}/{centralCode}", trackingId, centralCode, transferRequestDTO)

    def cancelItemHold(self, trackingId, centralCode, baseCircRequestDTO):
        """Cancel an item request

        ``PUT /inn-reach/d2ir/circ/cancelitemhold/{trackingId}/{centralCode}``

        Args:
            trackingId (str): 
            centralCode (str): Unique code that identifies the central server (match against value stored in Central Server settings, used to determine contribution status) (pattern: [a-z,0-9]{3,5})
            baseCircRequestDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: An error occurred during processing the request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_cancelItemHold_request.schema
            .. literalinclude:: ../files/Circulation_cancelItemHold_request.schema_response.schema
        """
        return self.call("PUT", "/inn-reach/d2ir/circ/cancelitemhold/{trackingId}/{centralCode}", trackingId, centralCode, baseCircRequestDTO)

    def receiveUnshipped(self, trackingId, centralCode, baseCircRequestDTO):
        """Report unshipped item received to owning site for item hold

        ``PUT /inn-reach/d2ir/circ/receiveunshipped/{trackingId}/{centralCode}``

        Args:
            trackingId (str): 
            centralCode (str): Unique code that identifies the central server (match against value stored in Central Server settings, used to determine contribution status) (pattern: [a-z,0-9]{3,5})
            baseCircRequestDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: An error occurred during processing the request

        Schema:

            .. literalinclude:: ../files/Circulation_receiveUnshipped_request.schema
            .. literalinclude:: ../files/Circulation_receiveUnshipped_request.schema_response.schema
        """
        return self.call("PUT", "/inn-reach/d2ir/circ/receiveunshipped/{trackingId}/{centralCode}", trackingId, centralCode, baseCircRequestDTO)

    def itemInTransit(self, trackingId, centralCode, baseCircRequestDTO):
        """Receives message from central server to owning site indicating that a loaned item is being returned after being loaned to the borrowing patron.

        ``PUT /inn-reach/d2ir/circ/intransit/{trackingId}/{centralCode}``

        Args:
            trackingId (str): 
            centralCode (str): Unique code that identifies the central server (match against value stored in Central Server settings, used to determine contribution status) (pattern: [a-z,0-9]{3,5})
            baseCircRequestDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: An error occurred during processing the request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_itemInTransit_request.schema
            .. literalinclude:: ../files/Circulation_itemInTransit_request.schema_response.schema
        """
        return self.call("PUT", "/inn-reach/d2ir/circ/intransit/{trackingId}/{centralCode}", trackingId, centralCode, baseCircRequestDTO)

    def returnUncirculated(self, trackingId, centralCode, returnUncirculatedDTO):
        """Return uncirculated message for item hold

        ``PUT /inn-reach/d2ir/circ/returnuncirculated/{trackingId}/{centralCode}``

        Args:
            trackingId (str): 
            centralCode (str): Unique code that identifies the central server (match against value stored in Central Server settings, used to determine contribution status) (pattern: [a-z,0-9]{3,5})
            returnUncirculatedDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: An error occurred during processing the request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_returnUncirculated_request.schema
            .. literalinclude:: ../files/Circulation_returnUncirculated_request.schema_response.schema
        """
        return self.call("PUT", "/inn-reach/d2ir/circ/returnuncirculated/{trackingId}/{centralCode}", trackingId, centralCode, returnUncirculatedDTO)

    def createLocalHold(self, trackingId, centralCode, localHoldDTO):
        """Create Local Hold - Central server to owning site when a local patron of that site requests an item through central.

        ``PUT /inn-reach/d2ir/circ/localhold/{trackingId}/{centralCode}``

        Args:
            trackingId (str): 
            centralCode (str): Unique code that identifies the central server (match against value stored in Central Server settings, used to determine contribution status) (pattern: [a-z,0-9]{3,5})
            localHoldDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: An error occurred during processing the request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_createLocalHold_request.schema
            .. literalinclude:: ../files/Circulation_createLocalHold_request.schema_response.schema
        """
        return self.call("PUT", "/inn-reach/d2ir/circ/localhold/{trackingId}/{centralCode}", trackingId, centralCode, localHoldDTO)

    def itemReceived(self, trackingId, centralCode, itemReceivedDTO):
        """Shipped item has been received

        ``PUT /inn-reach/d2ir/circ/itemreceived/{trackingId}/{centralCode}``

        Args:
            trackingId (str): 
            centralCode (str): Unique code that identifies the central server (match against value stored in Central Server settings, used to determine contribution status) (pattern: [a-z,0-9]{3,5})
            itemReceivedDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: An error occurred during processing the request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_itemReceived_request.schema
            .. literalinclude:: ../files/Circulation_itemReceived_request.schema_response.schema
        """
        return self.call("PUT", "/inn-reach/d2ir/circ/itemreceived/{trackingId}/{centralCode}", trackingId, centralCode, itemReceivedDTO)

    def recall(self, trackingId, centralCode, recallDTO):
        """Item has been recalled

        ``PUT /inn-reach/d2ir/circ/recall/{trackingId}/{centralCode}``

        Args:
            trackingId (str): 
            centralCode (str): Unique code that identifies the central server (match against value stored in Central Server settings, used to determine contribution status) (pattern: [a-z,0-9]{3,5})
            recallDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: An error occurred during processing the request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_recall_request.schema
            .. literalinclude:: ../files/Circulation_recall_request.schema_response.schema
        """
        return self.call("PUT", "/inn-reach/d2ir/circ/recall/{trackingId}/{centralCode}", trackingId, centralCode, recallDTO)

    def borrowerRenew(self, trackingId, centralCode, renewLoanDTO):
        """Borrower Renew Message for Item Hold

        ``PUT /inn-reach/d2ir/circ/borrowerrenew/{trackingId}/{centralCode}``

        Args:
            trackingId (str): 
            centralCode (str): Unique code that identifies the central server (match against value stored in Central Server settings, used to determine contribution status) (pattern: [a-z,0-9]{3,5})
            renewLoanDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: An error occurred during processing the request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_borrowerRenew_request.schema
            .. literalinclude:: ../files/Circulation_borrowerRenew_request.schema_response.schema
        """
        return self.call("PUT", "/inn-reach/d2ir/circ/borrowerrenew/{trackingId}/{centralCode}", trackingId, centralCode, renewLoanDTO)

    def finalCheckIn(self, trackingId, centralCode, baseCircRequestDTO):
        """Indicating that a returned item has been received by its owning site. This is a terminating transaction.

        ``PUT /inn-reach/d2ir/circ/finalcheckin/{trackingId}/{centralCode}``

        Args:
            trackingId (str): 
            centralCode (str): Unique code that identifies the central server (match against value stored in Central Server settings, used to determine contribution status) (pattern: [a-z,0-9]{3,5})
            baseCircRequestDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: An error occurred during processing the request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_finalCheckIn_request.schema
            .. literalinclude:: ../files/Circulation_finalCheckIn_request.schema_response.schema
        """
        return self.call("PUT", "/inn-reach/d2ir/circ/finalcheckin/{trackingId}/{centralCode}", trackingId, centralCode, baseCircRequestDTO)

    def ownerRenew(self, trackingId, centralCode, renewLoanDTO):
        """Owner Renew loan

        ``PUT /inn-reach/d2ir/circ/ownerrenew/{trackingId}/{centralCode}``

        Args:
            trackingId (str): 
            centralCode (str): Unique code that identifies the central server (match against value stored in Central Server settings, used to determine contribution status) (pattern: [a-z,0-9]{3,5})
            renewLoanDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: An error occurred during processing the request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_ownerRenew_request.schema
            .. literalinclude:: ../files/Circulation_ownerRenew_request.schema_response.schema
        """
        return self.call("PUT", "/inn-reach/d2ir/circ/ownerrenew/{trackingId}/{centralCode}", trackingId, centralCode, renewLoanDTO)

    def claimsReturned(self, trackingId, centralCode, claimsItemReturnedDTO):
        """Borrower claims item returned

        ``PUT /inn-reach/d2ir/circ/claimsreturned/{trackingId}/{centralCode}``

        Args:
            trackingId (str): 
            centralCode (str): Unique code that identifies the central server (match against value stored in Central Server settings, used to determine contribution status) (pattern: [a-z,0-9]{3,5})
            claimsItemReturnedDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: An error occurred during processing the request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_claimsReturned_request.schema
            .. literalinclude:: ../files/Circulation_claimsReturned_request.schema_response.schema
        """
        return self.call("PUT", "/inn-reach/d2ir/circ/claimsreturned/{trackingId}/{centralCode}", trackingId, centralCode, claimsItemReturnedDTO)

    def transferLocalHold(self, id_, itemId):
        """Transfer local hold to another item

        ``POST /inn-reach/transactions/{id}/localhold/transfer-item/{itemId}``

        Args:
            id_ (str):  (format: uuid)
            itemId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_transferLocalHold_response.schema
        """
        return self.call("POST", "/inn-reach/transactions/{id}/localhold/transfer-item/{itemId}", id_, itemId)

    def getPagingSlips(self, servicePointId):
        """Get a list of available tokens for INN-Reach paging slips

        ``GET /inn-reach/paging-slips/{servicePointId}``

        Args:
            servicePointId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_getPagingSlips_response.schema
        """
        return self.call("GET", "/inn-reach/paging-slips/{servicePointId}", servicePointId)
