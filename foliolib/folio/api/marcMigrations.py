# -*- coding: utf-8 -*-
# Generated at 2024-03-23

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.marcMigrations")



class Marcmigrations(FolioApi):
    """MARC migrations API

    Manage MARC migrations
    """

    def createmarcmigrations(self, newMigrationOperation):
        """

        ``POST /marc-migrations``

        Args:
            newMigrationOperation (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestUnprocessableEntity: Unexpected request body
            OkapiRequestFatalError: Unexpected error

        Schema:

            .. literalinclude:: ../files/Marcmigrations_createmarcmigrations_request.schema
            .. literalinclude:: ../files/Marcmigrations_createmarcmigrations_request.schema_response.schema
        """
        return self.call("POST", f"/marc-migrations", newMigrationOperation)

    def getmarcmigrationbyid(self, operationId):
        """

        ``GET /marc-migrations/{operationId}``

        Args:
            operationId (str): The UUID of a MARC migration operation (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: MARC migration operation was not found
            OkapiRequestFatalError: Unexpected error

        Schema:

            .. literalinclude:: ../files/Marcmigrations_getmarcmigrationbyid_response.schema
        """
        return self.call("GET", f"/marc-migrations/{operationId}")
