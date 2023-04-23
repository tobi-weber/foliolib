# -*- coding: utf-8 -*-
# Generated at 2023-04-16

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.settings")



class SettingsAdmin(FolioAdminApi):
    """Settings
    Administration

    
    """

    def getSettings(self):
        """Get settings with optional CQL query. If X-Okapi-Permissions includes settings.global.read then settings without a userId are returned. If X-Okapi-Permissions includes settings.users.read then settings with a userId are returned. If X-Okapi-Permissions includes settings.owner.read then settings with userId = current-user are returned.


        ``GET /settings/entries``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Settings_getSettings_response.schema
        """
        return self.call("GET", "/settings/entries")

		
    def postSetting(self, entry):
        """Create setting entry. If X-Okapi-Permissions includes settings.global.write, then a setting without a userId may be created. If X-Okapi-Permissions includes settings.users.write, then a setting with a userId may be created. If X-Okapi-Permissions includes settings.owner.write, then a setting with userId = current-user may be created.


        ``POST /settings/entries``

        Args:
            entry (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestForbidden: Forbidden
            OkapiRequestPayloadToLarge: Payload Too Large
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Settings_postSetting_request.schema
        """
        return self.call("POST", "/settings/entries", entry)

    def getSetting(self):
        """Get setting. If X-Okapi-Permissions includes settings.global.read, then a setting without a userId may be retrieved. If X-Okapi-Permissions includes settings.users.read, then a setting with a userId may be retrieved. If X-Okapi-Permissions includes settings.owner.read, then a setting with userId = current-user may be retrieved.


        ``GET /settings/entries/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestForbidden: Forbidden
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Settings_getSetting_response.schema
        """
        return self.call("GET", "/settings/entries/{id}")

		
    def putSetting(self, entry):
        """Update setting. If X-Okapi-Permissions includes settings.global.write, then a setting without a userId may be updated. If X-Okapi-Permissions includes settings.users.write, then a setting with a userId may be updated. If X-Okapi-Permissions includes settings.owner.write, then a setting with userId = current-user may be updated.


        ``PUT /settings/entries/{id}``

        Args:
            entry (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestForbidden: Forbidden
            OkapiRequestNotFound: Not Found
            OkapiRequestPayloadToLarge: Payload Too Large
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Settings_putSetting_request.schema
        """
        return self.call("PUT", "/settings/entries/{id}", entry)

		
    def deleteSetting(self):
        """Delete setting. If X-Okapi-Permissions includes settings.global.write, then a setting without a userId may be deleted. If X-Okapi-Permissions includes settings.users.write, then a setting with a userId may be deleted. If X-Okapi-Permissions includes settings.owner.write, then a setting with userId = current-user may be deleted.


        ``DELETE /settings/entries/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/settings/entries/{id}")

    def uploadSettings(self, uploadRequest):
        """Upload settings. The entries are inserted or updated depending on whether key, scope, userId already. Each entry gets a unique identifier assigned if it's a new setting. The id must not be supplied. If X-Okapi-Permissions includes settings.global.write, then a setting without a userId may be created/updated. If X-Okapi-Permissions includes settings.users.write, then a setting with a userId may be created/updated. If X-Okapi-Permissions includes settings.owner.write, then a setting with userId = current-user may be created/updated.


        ``PUT /settings/upload``

        Args:
            uploadRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestForbidden: Forbidden
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Settings_uploadSettings_request.schema
            .. literalinclude:: ../files/Settings_uploadSettings_request.schema_response.schema
        """
        return self.call("PUT", "/settings/upload", uploadRequest)