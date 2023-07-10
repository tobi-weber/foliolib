# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.userImport")


class Import(FolioApi):
    """mod-user-import API

    This documents the API calls that can be made to import users into the system
    """

    def set_userImport(self, userImport: dict):
        """Create or update a list of users

        ``POST /user-import``

        Args:
            userImport (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Import_set_userImport_request.schema
            .. literalinclude:: ../files/Import_set_userImport_return.schema 
        """
        return self.call("POST", "/user-import", data=userImport)
