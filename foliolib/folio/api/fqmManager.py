# -*- coding: utf-8 -*-
# Generated at 2024-03-01

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.fqmManager")



class Fqmmanager(FolioApi):
    """mod-fqm-manager API

    mod-fqm-manager API
    """

    def getentitytypesummary(self, **kwargs):
        """Get names for a list of entity type ids.

        ``GET /fqm/entity-types``

        Keyword Args:
            ids (list): List of entity type ids (items: (type: string, format: UUID))

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiRequestFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Fqmmanager_getentitytypesummary_response.schema
        """
        return self.call("GET", "/fqm/entity-types", query=kwargs)

    def deleteoldqueries(self):
        """Deletes all queries that are older than the configured duration.

        ``POST /fqm/query/purge``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiRequestFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Fqmmanager_deleteoldqueries_response.schema
        """
        return self.call("POST", "/fqm/query/purge")

    def refreshmaterializedviews(self):
        """Refresh all materialized views for a tenant.

        ``POST /fqm/entity-types/materialized-views/refresh``

        Raises:
            OkapiRequestError: Validation errors
            OkapiRequestFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException
        """
        return self.call("POST", "/fqm/entity-types/materialized-views/refresh")
