# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.innReach")



class Contribution(FolioApi):
    """INN-Reach Contribution API

    
    """

    def getcurrentcontributionbyserverid(self, centralServerId):
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

            .. literalinclude:: ../files/Contribution_getcurrentcontributionbyserverid_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/contributions/current")

		
    def cancelcurrentcontributionbyserverid(self, centralServerId):
        """Cancel current INN-Reach contribution for the given central server

        ``DELETE /inn-reach/central-servers/{centralServerId}/contributions/current``

        Args:
            centralServerId (str):  (format: uuid)

        Raises:
            OkapiRequestError: Bad request, e.g. malformed query parameter.
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", f"/inn-reach/central-servers/{centralServerId}/contributions/current")

    def getcontributionhistorybyserverid(self, centralServerId, **kwargs):
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

            .. literalinclude:: ../files/Contribution_getcontributionhistorybyserverid_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/contributions/history", query=kwargs)

    def startinitialcontribution(self, centralServerId):
        """Start initial contribution process

        ``POST /inn-reach/central-servers/{centralServerId}/contributions``

        Args:
            centralServerId (str):  (format: uuid)

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server error
        """
        return self.call("POST", f"/inn-reach/central-servers/{centralServerId}/contributions")



class Settings(FolioApi):
    """INN-Reach Settings API

    
    """

    def postcentralserver(self, centralServerDTO):
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

            .. literalinclude:: ../files/Settings_postcentralserver_request.schema
        """
        return self.call("POST", f"/inn-reach/central-servers", centralServerDTO)

		
    def getcentralservers(self, **kwargs):
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

            .. literalinclude:: ../files/Settings_getcentralservers_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers", query=kwargs)

    def getcentralserverbyid(self, centralServerId):
        """Get central server by id

        ``GET /inn-reach/central-servers/{centralServerId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getcentralserverbyid_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}")

		
    def updatecentralserver(self, centralServerDTO, centralServerId):
        """Update central server

        ``PUT /inn-reach/central-servers/{centralServerId}``

        Args:
            centralServerDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_updatecentralserver_request.schema
        """
        return self.call("PUT", f"/inn-reach/central-servers/{centralServerId}", centralServerDTO)

		
    def deletecentralserver(self, centralServerId):
        """Delete central server

        ``DELETE /inn-reach/central-servers/{centralServerId}``

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", f"/inn-reach/central-servers/{centralServerId}")

    def getmaterialtypemappingsbyserverid(self, centralServerId, **kwargs):
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

            .. literalinclude:: ../files/Settings_getmaterialtypemappingsbyserverid_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/material-type-mappings", query=kwargs)

		
    def postmaterialtypemapping(self, centralServerId, materialTypeMappingDTO):
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

            .. literalinclude:: ../files/Settings_postmaterialtypemapping_request.schema
        """
        return self.call("POST", f"/inn-reach/central-servers/{centralServerId}/material-type-mappings", materialTypeMappingDTO)

		
    def updatematerialtypemappings(self, centralServerId, materialTypeMappingsDTO):
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

            .. literalinclude:: ../files/Settings_updatematerialtypemappings_request.schema
        """
        return self.call("PUT", f"/inn-reach/central-servers/{centralServerId}/material-type-mappings", materialTypeMappingsDTO)

    def getmaterialtypemappingbyid(self, centralServerId, id_):
        """Get material type mapping by id

        ``GET /inn-reach/central-servers/{centralServerId}/material-type-mappings/{id}``

        Args:
            centralServerId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getmaterialtypemappingbyid_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/material-type-mappings/{id_}")

		
    def updatematerialtypemapping(self, centralServerId, materialTypeMappingDTO, id_):
        """Update material type mapping

        ``PUT /inn-reach/central-servers/{centralServerId}/material-type-mappings/{id}``

        Args:
            centralServerId (str):  (format: uuid)
            materialTypeMappingDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_updatematerialtypemapping_request.schema
        """
        return self.call("PUT", f"/inn-reach/central-servers/{centralServerId}/material-type-mappings/{id_}", materialTypeMappingDTO)

		
    def deletematerialtypemapping(self, centralServerId, id_):
        """Delete material type mapping

        ``DELETE /inn-reach/central-servers/{centralServerId}/material-type-mappings/{id}``

        Args:
            centralServerId (str):  (format: uuid)

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", f"/inn-reach/central-servers/{centralServerId}/material-type-mappings/{id_}")

    def postinnreachlocation(self, innReachLocationDTO):
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

            .. literalinclude:: ../files/Settings_postinnreachlocation_request.schema
        """
        return self.call("POST", f"/inn-reach/locations", innReachLocationDTO)

		
    def getlocations(self, **kwargs):
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

            .. literalinclude:: ../files/Settings_getlocations_response.schema
        """
        return self.call("GET", "/inn-reach/locations", query=kwargs)

    def getlocationbyid(self, locationId):
        """Get InnReach location by id

        ``GET /inn-reach/locations/{locationId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getlocationbyid_response.schema
        """
        return self.call("GET", f"/inn-reach/locations/{locationId}")

		
    def updatelocation(self, innReachLocationDTO, locationId):
        """Update InnReach location

        ``PUT /inn-reach/locations/{locationId}``

        Args:
            innReachLocationDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_updatelocation_request.schema
        """
        return self.call("PUT", f"/inn-reach/locations/{locationId}", innReachLocationDTO)

		
    def deletelocation(self, locationId):
        """Delete InnReach location

        ``DELETE /inn-reach/locations/{locationId}``

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", f"/inn-reach/locations/{locationId}")

    def getlibrarymappingsbyserverid(self, centralServerId, **kwargs):
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

            .. literalinclude:: ../files/Settings_getlibrarymappingsbyserverid_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/libraries/location-mappings", query=kwargs)

		
    def putlibrarymappings(self, centralServerId, libraryMappingsDTO):
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

            .. literalinclude:: ../files/Settings_putlibrarymappings_request.schema
        """
        return self.call("PUT", f"/inn-reach/central-servers/{centralServerId}/libraries/location-mappings", libraryMappingsDTO)

    def getlocationmappingsbyserverid(self, centralServerId, libraryId, **kwargs):
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

            .. literalinclude:: ../files/Settings_getlocationmappingsbyserverid_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/libraries/{libraryId}/locations/location-mappings", query=kwargs)

		
    def putlocationmappings(self, centralServerId, libraryId, locationMappingsDTO):
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

            .. literalinclude:: ../files/Settings_putlocationmappings_request.schema
        """
        return self.call("PUT", f"/inn-reach/central-servers/{centralServerId}/libraries/{libraryId}/locations/location-mappings", locationMappingsDTO)

    def getlocationmappingsforalllibrariesbyserverid(self, centralServerId):
        """Get a list of libraries locations to Inn-Reach location mappings for the given central server

        ``GET /inn-reach/central-servers/{centralServerId}/libraries/locations/location-mappings``

        Args:
            centralServerId (str):  (format: uuid)

        Raises:
            OkapiRequestError: Bad request, e.g. malformed query parameter.
            OkapiFatalError: Internal server error
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/libraries/locations/location-mappings")

    def getcriteriabyserverid(self, centralServerId):
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

            .. literalinclude:: ../files/Settings_getcriteriabyserverid_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/contribution-criteria")

		
    def postcontributioncriteria(self, centralServerId, contributionCriteriaDTO):
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

            .. literalinclude:: ../files/Settings_postcontributioncriteria_request.schema
        """
        return self.call("POST", f"/inn-reach/central-servers/{centralServerId}/contribution-criteria", contributionCriteriaDTO)

		
    def deletecriteria(self, centralServerId):
        """Delete Contribution Criteria Configuration

        ``DELETE /inn-reach/central-servers/{centralServerId}/contribution-criteria``

        Args:
            centralServerId (str):  (format: uuid)

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", f"/inn-reach/central-servers/{centralServerId}/contribution-criteria")

		
    def updatecriteria(self, centralServerId, contributionCriteriaDTO):
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

            .. literalinclude:: ../files/Settings_updatecriteria_request.schema
        """
        return self.call("PUT", f"/inn-reach/central-servers/{centralServerId}/contribution-criteria", contributionCriteriaDTO)

    def authenticatelocalserverkeysecret(self, authenticationRequest):
        """Authenticate InnReach local server key/secret pair

        ``POST /inn-reach/authentication``

        Args:
            authenticationRequest (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestUnauthorized: Unauthorized
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_authenticatelocalserverkeysecret_request.schema
        """
        return self.call("POST", f"/inn-reach/authentication", authenticationRequest)

    def getitemcontributionoptionsconfigurationbyid(self, centralServerId):
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

            .. literalinclude:: ../files/Settings_getitemcontributionoptionsconfigurationbyid_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/item-contribution-options")

		
    def updateitemcontributionoptionsconfiguration(self, centralServerId, itemContributionOptionsConfigurationDTO):
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

            .. literalinclude:: ../files/Settings_updateitemcontributionoptionsconfiguration_request.schema
        """
        return self.call("PUT", f"/inn-reach/central-servers/{centralServerId}/item-contribution-options", itemContributionOptionsConfigurationDTO)

		
    def createitemcontributionoptionsconfiguration(self, centralServerId, itemContributionOptionsConfigurationDTO):
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

            .. literalinclude:: ../files/Settings_createitemcontributionoptionsconfiguration_request.schema
        """
        return self.call("POST", f"/inn-reach/central-servers/{centralServerId}/item-contribution-options", itemContributionOptionsConfigurationDTO)

    def getagencymappingsbyserverid(self, centralServerId):
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

            .. literalinclude:: ../files/Settings_getagencymappingsbyserverid_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/agency-mappings")

		
    def putagencymappings(self, centralServerId, agencyLocationMappingDTO):
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

            .. literalinclude:: ../files/Settings_putagencymappings_request.schema
        """
        return self.call("PUT", f"/inn-reach/central-servers/{centralServerId}/agency-mappings", agencyLocationMappingDTO)

    def getmarctransformationoptionssettingsbyid(self, centralServerId):
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

            .. literalinclude:: ../files/Settings_getmarctransformationoptionssettingsbyid_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/marc-transformation-options")

		
    def updatemarctransformationoptionssettings(self, centralServerId, mARCTransformationOptionsSettingsDTO):
        """Update MARC Transformation Options Settings

        ``PUT /inn-reach/central-servers/{centralServerId}/marc-transformation-options``

        Args:
            centralServerId (str):  (format: uuid)
            mARCTransformationOptionsSettingsDTO (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_updatemarctransformationoptionssettings_request.schema
        """
        return self.call("PUT", f"/inn-reach/central-servers/{centralServerId}/marc-transformation-options", mARCTransformationOptionsSettingsDTO)

		
    def createmarctransformationoptionssettings(self, centralServerId, mARCTransformationOptionsSettingsDTO):
        """Add new MARC Transformation Options Settings associated with the central server

        ``POST /inn-reach/central-servers/{centralServerId}/marc-transformation-options``

        Args:
            centralServerId (str):  (format: uuid)
            mARCTransformationOptionsSettingsDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_createmarctransformationoptionssettings_request.schema
        """
        return self.call("POST", f"/inn-reach/central-servers/{centralServerId}/marc-transformation-options", mARCTransformationOptionsSettingsDTO)

		
    def deletemarctransformationoptionssettings(self, centralServerId):
        """Delete Marc Transformation Options Settings

        ``DELETE /inn-reach/central-servers/{centralServerId}/marc-transformation-options``

        Args:
            centralServerId (str):  (format: uuid)

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", f"/inn-reach/central-servers/{centralServerId}/marc-transformation-options")

    def getallmarctransformationoptionssettings(self, **kwargs):
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

            .. literalinclude:: ../files/Settings_getallmarctransformationoptionssettings_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/marc-transformation-options", query=kwargs)

    def getpatrontypemappingsbyserverid(self, centralServerId, **kwargs):
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

            .. literalinclude:: ../files/Settings_getpatrontypemappingsbyserverid_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/patron-type-mappings", query=kwargs)

		
    def updatepatrontypemappings(self, centralServerId, patronTypeMappingsDTO):
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

            .. literalinclude:: ../files/Settings_updatepatrontypemappings_request.schema
        """
        return self.call("PUT", f"/inn-reach/central-servers/{centralServerId}/patron-type-mappings", patronTypeMappingsDTO)

    def transformmarcrecord(self, centralServerId, inventoryInstanceId):
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

            .. literalinclude:: ../files/Settings_transformmarcrecord_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/marc-record-transformation/{inventoryInstanceId}")

    def getitemtypemappingsbyserverid(self, centralServerId, **kwargs):
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

            .. literalinclude:: ../files/Settings_getitemtypemappingsbyserverid_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/item-type-mappings", query=kwargs)

		
    def updateitemtypemappings(self, centralServerId, itemTypeMappingsDTO):
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

            .. literalinclude:: ../files/Settings_updateitemtypemappings_request.schema
        """
        return self.call("PUT", f"/inn-reach/central-servers/{centralServerId}/item-type-mappings", itemTypeMappingsDTO)

    def getusercustomfieldmapping(self, centralServerId):
        """Get a User Custom Field Mapping

        ``GET /inn-reach/central-servers/{centralServerId}/user-custom-field-mappings``

        Args:
            centralServerId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getusercustomfieldmapping_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/user-custom-field-mappings")

		
    def updateusercustomfieldmapping(self, centralServerId, userCustomFieldMappingDTO):
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

            .. literalinclude:: ../files/Settings_updateusercustomfieldmapping_request.schema
        """
        return self.call("PUT", f"/inn-reach/central-servers/{centralServerId}/user-custom-field-mappings", userCustomFieldMappingDTO)

		
    def createusercustomfieldmapping(self, centralServerId, userCustomFieldMappingDTO):
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

            .. literalinclude:: ../files/Settings_createusercustomfieldmapping_request.schema
        """
        return self.call("POST", f"/inn-reach/central-servers/{centralServerId}/user-custom-field-mappings", userCustomFieldMappingDTO)

    def getcentralpatrontypemappings(self, centralServerId, **kwargs):
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

            .. literalinclude:: ../files/Settings_getcentralpatrontypemappings_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/central-patron-type-mappings", query=kwargs)

		
    def updatecentralpatrontypemappings(self, centralServerId, centralPatronTypeMappingsDTO):
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

            .. literalinclude:: ../files/Settings_updatecentralpatrontypemappings_request.schema
        """
        return self.call("PUT", f"/inn-reach/central-servers/{centralServerId}/central-patron-type-mappings", centralPatronTypeMappingsDTO)

    def saveinnreachrecalluser(self, centralServerId, innReachRecallUserDTO):
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

            .. literalinclude:: ../files/Settings_saveinnreachrecalluser_request.schema
        """
        return self.call("POST", f"/inn-reach/central-servers/{centralServerId}/inn-reach-recall-user", innReachRecallUserDTO)

		
    def getcentralserverrecalluser(self, centralServerId):
        """Get Inn-Reach Central server recall user

        ``GET /inn-reach/central-servers/{centralServerId}/inn-reach-recall-user``

        Args:
            centralServerId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getcentralserverrecalluser_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/inn-reach-recall-user")

		
    def updatecentralserverrecalluser(self, centralServerId, innReachRecallUserDTO):
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

            .. literalinclude:: ../files/Settings_updatecentralserverrecalluser_request.schema
        """
        return self.call("PUT", f"/inn-reach/central-servers/{centralServerId}/inn-reach-recall-user", innReachRecallUserDTO)

    def getconfigurationbycentralserverid(self, centralServerId):
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

            .. literalinclude:: ../files/Settings_getconfigurationbycentralserverid_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/visible-patron-field-configuration")

		
    def updateconfiguration(self, centralServerId, visiblePatronFieldConfigurationDTO):
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

            .. literalinclude:: ../files/Settings_updateconfiguration_request.schema
        """
        return self.call("PUT", f"/inn-reach/central-servers/{centralServerId}/visible-patron-field-configuration", visiblePatronFieldConfigurationDTO)

		
    def createconfiguration(self, centralServerId, visiblePatronFieldConfigurationDTO):
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

            .. literalinclude:: ../files/Settings_createconfiguration_request.schema
        """
        return self.call("POST", f"/inn-reach/central-servers/{centralServerId}/visible-patron-field-configuration", visiblePatronFieldConfigurationDTO)

    def getpagingsliptemplate(self, centralServerId):
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

            .. literalinclude:: ../files/Settings_getpagingsliptemplate_response.schema
        """
        return self.call("GET", f"/inn-reach/central-servers/{centralServerId}/paging-slip-template")

		
    def updatepagingsliptemplate(self, centralServerId, pagingSlipTemplateDTO):
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

            .. literalinclude:: ../files/Settings_updatepagingsliptemplate_request.schema
        """
        return self.call("PUT", f"/inn-reach/central-servers/{centralServerId}/paging-slip-template", pagingSlipTemplateDTO)

    def getallpagingsliptemplates(self):
        """Get list of Paging Slip Templates

        ``GET /inn-reach/central-servers/paging-slip-template``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Settings_getallpagingsliptemplates_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/paging-slip-template")




class Circulation(FolioApi):
    """INN-Reach Circulation API

    
    """

    def getcentralserveragencies(self):
        """Get a combined list of agencies available from all configured central servers

        ``GET /inn-reach/central-servers/agencies``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_getcentralserveragencies_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/agencies")

    def getcentralserveritemtypes(self):
        """Get a combined list of item types available from all configured central servers

        ``GET /inn-reach/central-servers/item-types``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_getcentralserveritemtypes_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/item-types")

    def getcentralserverpatrontypes(self):
        """Get a combined list of patron types available from all configured central servers

        ``GET /inn-reach/central-servers/patron-types``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_getcentralserverpatrontypes_response.schema
        """
        return self.call("GET", "/inn-reach/central-servers/patron-types")

    def getbibrecord(self, bibId, centralCode):
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

            .. literalinclude:: ../files/Circulation_getbibrecord_response.schema
        """
        return self.call("POST", f"/inn-reach/d2ir/getbibrecord/{bibId}/{centralCode}")

    def createinnreachtransactionitemhold(self, trackingId, centralCode, transactionHoldDTO):
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

            .. literalinclude:: ../files/Circulation_createinnreachtransactionitemhold_request.schema
            .. literalinclude:: ../files/Circulation_createinnreachtransactionitemhold_request.schema_response.schema
        """
        return self.call("POST", f"/inn-reach/d2ir/circ/itemhold/{trackingId}/{centralCode}", transactionHoldDTO)

    def getalltransactions(self, **kwargs):
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

            .. literalinclude:: ../files/Circulation_getalltransactions_response.schema
        """
        return self.call("GET", "/inn-reach/transactions", query=kwargs)

    def getinnreachtransaction(self, id_):
        """get inn-reach transaction by id

        ``GET /inn-reach/transactions/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_getinnreachtransaction_response.schema
        """
        return self.call("GET", f"/inn-reach/transactions/{id_}")

		
    def updateinnreachtransaction(self, innReachTransactionDTO, id_):
        """update inn-reach transaction by id

        ``PUT /inn-reach/transactions/{id}``

        Args:
            innReachTransactionDTO (dict): See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_updateinnreachtransaction_request.schema
        """
        return self.call("PUT", f"/inn-reach/transactions/{id_}", innReachTransactionDTO)

    def checkinpatronholditem(self, servicePointId, id_):
        """receive item for patron hold transaction

        ``POST /inn-reach/transactions/{id}/receive-item/{servicePointId}``

        Args:
            servicePointId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_checkinpatronholditem_response.schema
        """
        return self.call("POST", f"/inn-reach/transactions/{id_}/receive-item/{servicePointId}")

    def checkinpatronholdunshippeditem(self, servicePointId, itemBarcode, id_):
        """receive un-shipped/unannounced item for patron hold transaction

        ``POST /inn-reach/transactions/{id}/receive-unshipped-item/{servicePointId}/{itemBarcode}``

        Args:
            servicePointId (str):  (format: uuid)
            itemBarcode (str): Barcode of the item

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_checkinpatronholdunshippeditem_response.schema
        """
        return self.call("POST", f"/inn-reach/transactions/{id_}/receive-unshipped-item/{servicePointId}/{itemBarcode}")

    def finalcheckinitemhold(self, servicePointId, id_):
        """Final check-in of an item loaned through INN-Reach

        ``POST /inn-reach/transactions/{id}/itemhold/finalcheckin/{servicePointId}``

        Args:
            servicePointId (str):  (format: uuid)

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error
        """
        return self.call("POST", f"/inn-reach/transactions/{id_}/itemhold/finalcheckin/{servicePointId}")

    def transferitemhold(self, itemId, id_):
        """Transfer item hold to another item

        ``POST /inn-reach/transactions/{id}/itemhold/transfer-item/{itemId}``

        Args:
            itemId (str):  (format: uuid)

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error
        """
        return self.call("POST", f"/inn-reach/transactions/{id_}/itemhold/transfer-item/{itemId}")

    def checkoutpatronholditem(self, servicePointId, id_):
        """Checks out to requesting patron

        ``POST /inn-reach/transactions/{id}/patronhold/check-out-item/{servicePointId}``

        Args:
            servicePointId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_checkoutpatronholditem_response.schema
        """
        return self.call("POST", f"/inn-reach/transactions/{id_}/patronhold/check-out-item/{servicePointId}")

    def checkoutlocalholditem(self, servicePointId, id_):
        """Checks out Local Hold item to requesting patron

        ``POST /inn-reach/transactions/{id}/localhold/check-out-item/{servicePointId}``

        Args:
            servicePointId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_checkoutlocalholditem_response.schema
        """
        return self.call("POST", f"/inn-reach/transactions/{id_}/localhold/check-out-item/{servicePointId}")

    def checkoutitemholditem(self, itemBarcode, servicePointId):
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

            .. literalinclude:: ../files/Circulation_checkoutitemholditem_response.schema
        """
        return self.call("PUT", f"/inn-reach/transactions/{itemBarcode}/check-out-item/{servicePointId}")

    def cancelpatronholdtransaction(self, cancelTransactionHoldDTO, id_):
        """Cancel patron hold transaction with the reason provided

        ``POST /inn-reach/transactions/{id}/patronhold/cancel``

        Args:
            cancelTransactionHoldDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_cancelpatronholdtransaction_request.schema
            .. literalinclude:: ../files/Circulation_cancelpatronholdtransaction_request.schema_response.schema
        """
        return self.call("POST", f"/inn-reach/transactions/{id_}/patronhold/cancel", cancelTransactionHoldDTO)

    def recallitemholdtransaction(self, id_):
        """Recall item hold transaction

        ``POST /inn-reach/transactions/{id}/itemhold/recall``

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error
        """
        return self.call("POST", f"/inn-reach/transactions/{id_}/itemhold/recall")

    def returnpatronholditem(self, servicePointId, id_):
        """Returns Patron Hold item

        ``POST /inn-reach/transactions/{id}/patronhold/return-item/{servicePointId}``

        Args:
            servicePointId (str):  (format: uuid)

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error
        """
        return self.call("POST", f"/inn-reach/transactions/{id_}/patronhold/return-item/{servicePointId}")

    def cancelitemholdtransaction(self, cancelTransactionHoldDTO, id_):
        """Cancel item hold transaction with the reason provided

        ``POST /inn-reach/transactions/{id}/itemhold/cancel``

        Args:
            cancelTransactionHoldDTO (dict): See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_cancelitemholdtransaction_request.schema
        """
        return self.call("POST", f"/inn-reach/transactions/{id_}/itemhold/cancel", cancelTransactionHoldDTO)

    def cancellocalholdtransaction(self, cancelTransactionHoldDTO, id_):
        """Cancel local hold transaction with the reason provided

        ``POST /inn-reach/transactions/{id}/localhold/cancel``

        Args:
            cancelTransactionHoldDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_cancellocalholdtransaction_request.schema
            .. literalinclude:: ../files/Circulation_cancellocalholdtransaction_request.schema_response.schema
        """
        return self.call("POST", f"/inn-reach/transactions/{id_}/localhold/cancel", cancelTransactionHoldDTO)

    def verifypatron(self, patronInfoRequestDTO):
        """Handles D2IR request from central server for patron verification.

        ``POST /inn-reach/d2ir/circ/verifypatron``

        Args:
            patronInfoRequestDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_verifypatron_request.schema
            .. literalinclude:: ../files/Circulation_verifypatron_request.schema_response.schema
        """
        return self.call("POST", f"/inn-reach/d2ir/circ/verifypatron", patronInfoRequestDTO)

    def patronhold(self, trackingId, centralCode, patronHoldDTO):
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

            .. literalinclude:: ../files/Circulation_patronhold_request.schema
            .. literalinclude:: ../files/Circulation_patronhold_request.schema_response.schema
        """
        return self.call("POST", f"/inn-reach/d2ir/circ/patronhold/{trackingId}/{centralCode}", patronHoldDTO)

    def itemshipped(self, trackingId, centralCode, itemShippedDTO):
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

            .. literalinclude:: ../files/Circulation_itemshipped_request.schema
            .. literalinclude:: ../files/Circulation_itemshipped_request.schema_response.schema
        """
        return self.call("PUT", f"/inn-reach/d2ir/circ/itemshipped/{trackingId}/{centralCode}", itemShippedDTO)

    def cancelpatronhold(self, trackingId, centralCode, cancelRequestDTO):
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

            .. literalinclude:: ../files/Circulation_cancelpatronhold_request.schema
            .. literalinclude:: ../files/Circulation_cancelpatronhold_request.schema_response.schema
        """
        return self.call("PUT", f"/inn-reach/d2ir/circ/cancelrequest/{trackingId}/{centralCode}", cancelRequestDTO)

    def transferrequest(self, trackingId, centralCode, transferRequestDTO):
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

            .. literalinclude:: ../files/Circulation_transferrequest_request.schema
            .. literalinclude:: ../files/Circulation_transferrequest_request.schema_response.schema
        """
        return self.call("PUT", f"/inn-reach/d2ir/circ/transferrequest/{trackingId}/{centralCode}", transferRequestDTO)

    def cancelitemhold(self, trackingId, centralCode, baseCircRequestDTO):
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

            .. literalinclude:: ../files/Circulation_cancelitemhold_request.schema
            .. literalinclude:: ../files/Circulation_cancelitemhold_request.schema_response.schema
        """
        return self.call("PUT", f"/inn-reach/d2ir/circ/cancelitemhold/{trackingId}/{centralCode}", baseCircRequestDTO)

    def receiveunshipped(self, trackingId, centralCode, baseCircRequestDTO):
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

            .. literalinclude:: ../files/Circulation_receiveunshipped_request.schema
            .. literalinclude:: ../files/Circulation_receiveunshipped_request.schema_response.schema
        """
        return self.call("PUT", f"/inn-reach/d2ir/circ/receiveunshipped/{trackingId}/{centralCode}", baseCircRequestDTO)

    def itemintransit(self, trackingId, centralCode, baseCircRequestDTO):
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

            .. literalinclude:: ../files/Circulation_itemintransit_request.schema
            .. literalinclude:: ../files/Circulation_itemintransit_request.schema_response.schema
        """
        return self.call("PUT", f"/inn-reach/d2ir/circ/intransit/{trackingId}/{centralCode}", baseCircRequestDTO)

    def returnuncirculated(self, trackingId, centralCode, returnUncirculatedDTO):
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

            .. literalinclude:: ../files/Circulation_returnuncirculated_request.schema
            .. literalinclude:: ../files/Circulation_returnuncirculated_request.schema_response.schema
        """
        return self.call("PUT", f"/inn-reach/d2ir/circ/returnuncirculated/{trackingId}/{centralCode}", returnUncirculatedDTO)

    def createlocalhold(self, trackingId, centralCode, localHoldDTO):
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

            .. literalinclude:: ../files/Circulation_createlocalhold_request.schema
            .. literalinclude:: ../files/Circulation_createlocalhold_request.schema_response.schema
        """
        return self.call("PUT", f"/inn-reach/d2ir/circ/localhold/{trackingId}/{centralCode}", localHoldDTO)

    def itemreceived(self, trackingId, centralCode, itemReceivedDTO):
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

            .. literalinclude:: ../files/Circulation_itemreceived_request.schema
            .. literalinclude:: ../files/Circulation_itemreceived_request.schema_response.schema
        """
        return self.call("PUT", f"/inn-reach/d2ir/circ/itemreceived/{trackingId}/{centralCode}", itemReceivedDTO)

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
        return self.call("PUT", f"/inn-reach/d2ir/circ/recall/{trackingId}/{centralCode}", recallDTO)

    def borrowerrenew(self, trackingId, centralCode, renewLoanDTO):
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

            .. literalinclude:: ../files/Circulation_borrowerrenew_request.schema
            .. literalinclude:: ../files/Circulation_borrowerrenew_request.schema_response.schema
        """
        return self.call("PUT", f"/inn-reach/d2ir/circ/borrowerrenew/{trackingId}/{centralCode}", renewLoanDTO)

    def finalcheckin(self, trackingId, centralCode, baseCircRequestDTO):
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

            .. literalinclude:: ../files/Circulation_finalcheckin_request.schema
            .. literalinclude:: ../files/Circulation_finalcheckin_request.schema_response.schema
        """
        return self.call("PUT", f"/inn-reach/d2ir/circ/finalcheckin/{trackingId}/{centralCode}", baseCircRequestDTO)

    def ownerrenew(self, trackingId, centralCode, renewLoanDTO):
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

            .. literalinclude:: ../files/Circulation_ownerrenew_request.schema
            .. literalinclude:: ../files/Circulation_ownerrenew_request.schema_response.schema
        """
        return self.call("PUT", f"/inn-reach/d2ir/circ/ownerrenew/{trackingId}/{centralCode}", renewLoanDTO)

    def claimsreturned(self, trackingId, centralCode, claimsItemReturnedDTO):
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

            .. literalinclude:: ../files/Circulation_claimsreturned_request.schema
            .. literalinclude:: ../files/Circulation_claimsreturned_request.schema_response.schema
        """
        return self.call("PUT", f"/inn-reach/d2ir/circ/claimsreturned/{trackingId}/{centralCode}", claimsItemReturnedDTO)

    def transferlocalhold(self, itemId, id_):
        """Transfer local hold to another item

        ``POST /inn-reach/transactions/{id}/localhold/transfer-item/{itemId}``

        Args:
            itemId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Item not found
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Circulation_transferlocalhold_response.schema
        """
        return self.call("POST", f"/inn-reach/transactions/{id_}/localhold/transfer-item/{itemId}")

    def getpagingslips(self, servicePointId):
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

            .. literalinclude:: ../files/Circulation_getpagingslips_response.schema
        """
        return self.call("GET", f"/inn-reach/paging-slips/{servicePointId}")
