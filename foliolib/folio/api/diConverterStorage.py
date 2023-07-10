# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.diConverterStorage")


class FieldProtectionSettings(FolioApi):
    """Field Protection Settings API

    API for managing field protection settings
    """

    def get_marcs(self, **kwargs):
        """Retrieve a list of marc items.

        ``GET /field-protection-settings/marc``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example source=SYSTEM
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - source=SYSTEM
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/FieldProtectionSettings_get_marcs_return.schema 
        """
        return self.call("GET", "/field-protection-settings/marc", query=kwargs)

    def set_marc(self, marc: dict):
        """Create a new marc item.

        ``POST /field-protection-settings/marc``

        Args:
            marc (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created marc item

        Schema:

            .. literalinclude:: ../files/FieldProtectionSettings_set_marc_request.schema
        """
        return self.call("POST", "/field-protection-settings/marc", data=marc)

    def get_marc(self, marcId: str):
        """Retrieve marc item with given {marcId}

        ``GET /field-protection-settings/marc/{marcId}``

        Args:
            marcId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FieldProtectionSettings_get_marc_return.schema 
        """
        return self.call("GET", f"/field-protection-settings/marc/{marcId}")

    def delete_marc(self, marcId: str):
        """Delete marc item with given {marcId}

        ``DELETE /field-protection-settings/marc/{marcId}``

        Args:
            marcId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/field-protection-settings/marc/{marcId}")

    def modify_marc(self, marcId: str, marc: dict):
        """Update marc item with given {marcId}

        ``PUT /field-protection-settings/marc/{marcId}``

        Args:
            marcId (str)
            marc (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/FieldProtectionSettings_modify_marc_request.schema
        """
        return self.call("PUT", f"/field-protection-settings/marc/{marcId}", data=marc)


class FormConfigsStorage(FolioApi):
    """Forms Configs Storage API

    API for accessing flexible forms configs
    """

    def get_configs(self):
        """Retrieve a list of config items.

        ``GET /converter-storage/forms/configs``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FormConfigsStorage_get_configs_return.schema 
        """
        return self.call("GET", "/converter-storage/forms/configs")

    def set_config(self, config: dict):
        """Create new form config

        ``POST /converter-storage/forms/configs``

        Args:
            config (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created config item

        Schema:

            .. literalinclude:: ../files/FormConfigsStorage_set_config_request.schema
        """
        return self.call("POST", "/converter-storage/forms/configs", data=config)

    def get_config(self, formName: str):
        """Retrieve config item with given {configId}

        ``GET /converter-storage/forms/configs/{formName}``

        Args:
            formName (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FormConfigsStorage_get_config_return.schema 
        """
        return self.call("GET", f"/converter-storage/forms/configs/{formName}")

    def delete_config(self, formName: str):
        """Delete config item with given {configId}

        ``DELETE /converter-storage/forms/configs/{formName}``

        Args:
            formName (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/converter-storage/forms/configs/{formName}")

    def modify_config(self, formName: str, config: dict):
        """Update config item with given {configId}

        ``PUT /converter-storage/forms/configs/{formName}``

        Args:
            formName (str)
            config (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/FormConfigsStorage_modify_config_request.schema
        """
        return self.call("PUT", f"/converter-storage/forms/configs/{formName}", data=config)


class DataImportConverterStorage(FolioApi):
    """Data Import Converter Storage API

    API for managing data import profiles
    """

    def get_jobProfiles(self, **kwargs):
        """Retrieve a list of jobProfile items.

        ``GET /data-import-profiles/jobProfiles``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example userInfo.lastName=Doe
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - userInfo.lastName=Doe
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_get_jobProfiles_return.schema 
        """
        return self.call("GET", "/data-import-profiles/jobProfiles", query=kwargs)

    def set_jobProfile(self, jobProfile: dict):
        """Create a new jobProfile item.

        ``POST /data-import-profiles/jobProfiles``

        Args:
            jobProfile (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created jobProfile item

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_set_jobProfile_request.schema
        """
        return self.call("POST", "/data-import-profiles/jobProfiles", data=jobProfile)

    def get_jobProfile(self, jobProfilesId: str):
        """Retrieve jobProfile item with given {jobProfileId}

        ``GET /data-import-profiles/jobProfiles/{jobProfilesId}``

        Args:
            jobProfilesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_get_jobProfile_return.schema 
        """
        return self.call("GET", f"/data-import-profiles/jobProfiles/{jobProfilesId}")

    def delete_jobProfile(self, jobProfilesId: str):
        """Delete jobProfile item with given {jobProfileId}

        ``DELETE /data-import-profiles/jobProfiles/{jobProfilesId}``

        Args:
            jobProfilesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestConflict: Conflict
        """
        return self.call("DELETE", f"/data-import-profiles/jobProfiles/{jobProfilesId}")

    def modify_jobProfile(self, jobProfilesId: str, jobProfile: dict):
        """Update jobProfile item with given {jobProfileId}

        ``PUT /data-import-profiles/jobProfiles/{jobProfilesId}``

        Args:
            jobProfilesId (str)
            jobProfile (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_modify_jobProfile_request.schema
        """
        return self.call("PUT", f"/data-import-profiles/jobProfiles/{jobProfilesId}", data=jobProfile)

    def get_matchProfiles(self, **kwargs):
        """Retrieve a list of matchProfile items.

        ``GET /data-import-profiles/matchProfiles``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example userInfo.lastName=Doe
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - userInfo.lastName=Doe
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_get_matchProfiles_return.schema 
        """
        return self.call("GET", "/data-import-profiles/matchProfiles", query=kwargs)

    def set_matchProfile(self, matchProfile: dict):
        """Create a new matchProfile item.

        ``POST /data-import-profiles/matchProfiles``

        Args:
            matchProfile (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created matchProfile item

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_set_matchProfile_request.schema
        """
        return self.call("POST", "/data-import-profiles/matchProfiles", data=matchProfile)

    def get_matchProfile(self, matchProfilesId: str):
        """Retrieve matchProfile item with given {matchProfileId}

        ``GET /data-import-profiles/matchProfiles/{matchProfilesId}``

        Args:
            matchProfilesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_get_matchProfile_return.schema 
        """
        return self.call("GET", f"/data-import-profiles/matchProfiles/{matchProfilesId}")

    def delete_matchProfile(self, matchProfilesId: str):
        """Delete matchProfile item with given {matchProfileId}

        ``DELETE /data-import-profiles/matchProfiles/{matchProfilesId}``

        Args:
            matchProfilesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestConflict: Conflict
        """
        return self.call("DELETE", f"/data-import-profiles/matchProfiles/{matchProfilesId}")

    def modify_matchProfile(self, matchProfilesId: str, matchProfile: dict):
        """Update matchProfile item with given {matchProfileId}

        ``PUT /data-import-profiles/matchProfiles/{matchProfilesId}``

        Args:
            matchProfilesId (str)
            matchProfile (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_modify_matchProfile_request.schema
        """
        return self.call("PUT", f"/data-import-profiles/matchProfiles/{matchProfilesId}", data=matchProfile)

    def get_mappingProfiles(self, **kwargs):
        """Retrieve a list of mappingProfile items.

        ``GET /data-import-profiles/mappingProfiles``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example userInfo.lastName=Doe
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - userInfo.lastName=Doe
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_get_mappingProfiles_return.schema 
        """
        return self.call("GET", "/data-import-profiles/mappingProfiles", query=kwargs)

    def set_mappingProfile(self, mappingProfile: dict):
        """Create a new mappingProfile item.

        ``POST /data-import-profiles/mappingProfiles``

        Args:
            mappingProfile (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created mappingProfile item

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_set_mappingProfile_request.schema
        """
        return self.call("POST", "/data-import-profiles/mappingProfiles", data=mappingProfile)

    def get_mappingProfile(self, mappingProfilesId: str):
        """Retrieve mappingProfile item with given {mappingProfileId}

        ``GET /data-import-profiles/mappingProfiles/{mappingProfilesId}``

        Args:
            mappingProfilesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_get_mappingProfile_return.schema 
        """
        return self.call("GET", f"/data-import-profiles/mappingProfiles/{mappingProfilesId}")

    def delete_mappingProfile(self, mappingProfilesId: str):
        """Delete mappingProfile item with given {mappingProfileId}

        ``DELETE /data-import-profiles/mappingProfiles/{mappingProfilesId}``

        Args:
            mappingProfilesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestConflict: Conflict
        """
        return self.call("DELETE", f"/data-import-profiles/mappingProfiles/{mappingProfilesId}")

    def modify_mappingProfile(self, mappingProfilesId: str, mappingProfile: dict):
        """Update mappingProfile item with given {mappingProfileId}

        ``PUT /data-import-profiles/mappingProfiles/{mappingProfilesId}``

        Args:
            mappingProfilesId (str)
            mappingProfile (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_modify_mappingProfile_request.schema
        """
        return self.call("PUT", f"/data-import-profiles/mappingProfiles/{mappingProfilesId}", data=mappingProfile)

    def get_actionProfiles(self, **kwargs):
        """Retrieve a list of actionProfile items.

        ``GET /data-import-profiles/actionProfiles``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example userInfo.lastName=Doe
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - userInfo.lastName=Doe
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
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
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_get_actionProfiles_return.schema 
        """
        return self.call("GET", "/data-import-profiles/actionProfiles", query=kwargs)

    def set_actionProfile(self, actionProfile: dict):
        """Create a new actionProfile item.

        ``POST /data-import-profiles/actionProfiles``

        Args:
            actionProfile (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created actionProfile item

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_set_actionProfile_request.schema
        """
        return self.call("POST", "/data-import-profiles/actionProfiles", data=actionProfile)

    def get_actionProfile(self, actionProfilesId: str):
        """Retrieve actionProfile item with given {actionProfileId}

        ``GET /data-import-profiles/actionProfiles/{actionProfilesId}``

        Args:
            actionProfilesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_get_actionProfile_return.schema 
        """
        return self.call("GET", f"/data-import-profiles/actionProfiles/{actionProfilesId}")

    def delete_actionProfile(self, actionProfilesId: str):
        """Delete actionProfile item with given {actionProfileId}

        ``DELETE /data-import-profiles/actionProfiles/{actionProfilesId}``

        Args:
            actionProfilesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestConflict: Conflict
        """
        return self.call("DELETE", f"/data-import-profiles/actionProfiles/{actionProfilesId}")

    def modify_actionProfile(self, actionProfilesId: str, actionProfile: dict):
        """Update actionProfile item with given {actionProfileId}

        ``PUT /data-import-profiles/actionProfiles/{actionProfilesId}``

        Args:
            actionProfilesId (str)
            actionProfile (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_modify_actionProfile_request.schema
        """
        return self.call("PUT", f"/data-import-profiles/actionProfiles/{actionProfilesId}", data=actionProfile)

    def get_profileAssociations(self):
        """Retrieve a list of profileAssociation items.

        ``GET /data-import-profiles/profileAssociations``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_get_profileAssociations_return.schema 
        """
        return self.call("GET", "/data-import-profiles/profileAssociations")

    def set_profileAssociation(self, profileAssociation: dict):
        """Create a new profileAssociation item.

        ``POST /data-import-profiles/profileAssociations``

        Args:
            profileAssociation (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created profileAssociation item

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_set_profileAssociation_request.schema
        """
        return self.call("POST", "/data-import-profiles/profileAssociations", data=profileAssociation)

    def get_profileAssociation(self, profileAssociationsId: str):
        """Retrieve profileAssociation item with given {profileAssociationId}

        ``GET /data-import-profiles/profileAssociations/{profileAssociationsId}``

        Args:
            profileAssociationsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_get_profileAssociation_return.schema 
        """
        return self.call("GET", f"/data-import-profiles/profileAssociations/{profileAssociationsId}")

    def delete_profileAssociation(self, profileAssociationsId: str):
        """Delete profileAssociation item with given {profileAssociationId}

        ``DELETE /data-import-profiles/profileAssociations/{profileAssociationsId}``

        Args:
            profileAssociationsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestConflict: Conflict
        """
        return self.call("DELETE", f"/data-import-profiles/profileAssociations/{profileAssociationsId}")

    def modify_profileAssociation(self, profileAssociationsId: str, profileAssociation: dict):
        """Update profileAssociation item with given {profileAssociationId}

        ``PUT /data-import-profiles/profileAssociations/{profileAssociationsId}``

        Args:
            profileAssociationsId (str)
            profileAssociation (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_modify_profileAssociation_request.schema
        """
        return self.call("PUT", f"/data-import-profiles/profileAssociations/{profileAssociationsId}", data=profileAssociation)

    def get_details_by_profileAssociation(self, profileAssociationsId: str, **kwargs):
        """

        ``GET /data-import-profiles/profileAssociations/{profileAssociationsId}/details``

        Args:
            profileAssociationsId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            masterType (str):  It needs to identify master profile type for an id
                    
                    Example:
                    
                     - JOB_PROFILE, ACTION_PROFILE, MATCH_PROFILE
            detailType (str):  It filters returned type of details. For example you need to get only MATCH_PROFILEs for a JOB_PROFILE but the JOB_PROFILE has ACTION_PROFILEs too. So use it as filter for a return type
                    
                    Example:
                    
                     - ACTION_PROFILE, MATCH_PROFILE, MAPPING_PROFILE
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example userInfo.lastName=Doe
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - userInfo.lastName=Doe
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_get_details_by_profileAssociation_return.schema 
        """
        return self.call("GET", f"/data-import-profiles/profileAssociations/{profileAssociationsId}/details", query=kwargs)

    def get_masters_by_profileAssociation(self, profileAssociationsId: str, **kwargs):
        """

        ``GET /data-import-profiles/profileAssociations/{profileAssociationsId}/masters``

        Args:
            profileAssociationsId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            detailType (str):  Type of detail profile
                    
                    Example:
                    
                     - JOB_PROFILE, ACTION_PROFILE, MATCH_PROFILE, MAPPING_PROFILE
            masterType (str):  It filters returned type of masters. For example you need to get only JOB_PROFILEs for a MATCH_PROFILE but the MATCH_PROFILE has ACTION_PROFILEs too. So use it as filter for a return type
                    
                    Example:
                    
                     - JOB_PROFILE, ACTION_PROFILE, MATCH_PROFILE, MAPPING_PROFILE
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example userInfo.lastName=Doe
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - userInfo.lastName=Doe
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_get_masters_by_profileAssociation_return.schema 
        """
        return self.call("GET", f"/data-import-profiles/profileAssociations/{profileAssociationsId}/masters", query=kwargs)

    def get_jobProfileSnapshot(self, jobProfileSnapshotsId: str):
        """Method to get Job Profile Snapshot by id

        ``GET /data-import-profiles/jobProfileSnapshots/{jobProfileSnapshotsId}``

        Args:
            jobProfileSnapshotsId (str)

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_get_jobProfileSnapshot_return.schema 
        """
        return self.call("GET", f"/data-import-profiles/jobProfileSnapshots/{jobProfileSnapshotsId}")

    def set_jobProfileSnapshot(self, jobProfileSnapshotsId: str):
        """Method to create Job Profile Snapshot by Job Profile id

        ``POST /data-import-profiles/jobProfileSnapshots/{jobProfileSnapshotsId}``

        Args:
            jobProfileSnapshotsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_set_jobProfileSnapshot_return.schema 
        """
        return self.call("POST", f"/data-import-profiles/jobProfileSnapshots/{jobProfileSnapshotsId}")

    def get_entityTypes(self):
        """Get a list of entity types

        ``GET /data-import-profiles/entityTypes``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_get_entityTypes_return.schema 
        """
        return self.call("GET", "/data-import-profiles/entityTypes")

    def get_profileSnapshot(self, profileId: str, **kwargs):
        """Get a profile snapshot structure for specified profile id and type. Acceptable profileType values are JOB_PROFILE, ACTION_PROFILE, MATCH_PROFILE, MAPPING_PROFILE.

        ``GET /data-import-profiles/profileSnapshots/{profileId}``

        Args:
            profileId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            profileType (str):  Indicates profile type
                    
                    Example:
                    
                     - JOB_PROFILE
            jobProfileId (str):  Indicates job profile id, should be specified when {profileType} parameter has value JOB_PROFILE or MATCH_PROFILE

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/DataImportConverterStorage_get_profileSnapshot_return.schema 
        """
        return self.call("GET", f"/data-import-profiles/profileSnapshots/{profileId}", query=kwargs)
