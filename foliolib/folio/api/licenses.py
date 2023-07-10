# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.licenses")


class Licenses(FolioApi):
    """mod-licenses API

    This documents the API calls that can be made to query and manage licenses
    """

    def get_licenses(self):
        """List current licenses

        ``GET /licenses/licenses``
        """
        return self.call("GET", "/licenses/licenses")

    def set_license(self, license: dict):
        """Create a new license

        ``POST /licenses/licenses``

        Args:
            license (dict): See Schema below

        Schema:

            .. literalinclude:: ../files/Licenses_set_license_request.schema
        """
        return self.call("POST", "/licenses/licenses", data=license)

    def get_license(self, licenseId: str):
        """Retrieve a specific license

        ``GET /licenses/licenses/{licenseId}``

        Args:
            licenseId (str)
        """
        return self.call("GET", f"/licenses/licenses/{licenseId}")

    def modify_license(self, licenseId: str):
        """Update a specific license

        ``PUT /licenses/licenses/{licenseId}``

        Args:
            licenseId (str)
        """
        return self.call("PUT", f"/licenses/licenses/{licenseId}")
