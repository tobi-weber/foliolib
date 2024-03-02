# -*- coding: utf-8 -*-
# Generated at 2024-03-01

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.lists")



class List(FolioApi):
    """ListEntity API

    ListEntity API description
    """

    def getalllists(self, **kwargs):
        """

        ``GET /lists``

        Keyword Args:
            ids (list): List of ids to retrieve information for (items: (type: string, format: UUID))
            entityTypeIds (list): List of entityTypeIds to retrieve information for (items: (type: string, format: UUID))
            offset (int): Offset to start retrieving list information for (format: int32, default: 0)
            size (int): how many item to return (format: int32, default: 100)
            active (bool): Indicates whether list should be active or not
            private (bool): Indicates whether list should be private or not
            includeDeleted (bool): Indicates if deleted lists should be included in the results (default false)
            updatedAsOf (str): Indicates the minimum create/update timestamp to filter lists by (format: offset-date-time)

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/List_getalllists_response.schema
        """
        return self.call("GET", "/lists", query=kwargs)

		
    def createlist(self, listRequestDTO):
        """

        ``POST /lists``

        Args:
            listRequestDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/List_createlist_request.schema
            .. literalinclude:: ../files/List_createlist_request.schema_response.schema
        """
        return self.call("POST", f"/lists", listRequestDTO)

    def deletelist(self, id_):
        """delete the list with the specific id (if exists).

        ``DELETE /lists/{id}``

        Raises:
            OkapiRequestNotFound: List with id not found
        """
        return self.call("DELETE", f"/lists/{id_}")

		
    def getlistbyid(self, id_):
        """gets the specific list information (if exists).

        ``GET /lists/{id}``

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/List_getlistbyid_response.schema
        """
        return self.call("GET", f"/lists/{id_}")

		
    def updatelist(self, listUpdateRequestDTO, id_):
        """

        ``PUT /lists/{id}``

        Args:
            listUpdateRequestDTO (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/List_updatelist_request.schema
            .. literalinclude:: ../files/List_updatelist_request.schema_response.schema
        """
        return self.call("PUT", f"/lists/{id_}", listUpdateRequestDTO)

    def performrefresh(self, id_):
        """Perform refresh of the list.

        ``POST /lists/{id}/refresh``

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/List_performrefresh_response.schema
        """
        return self.call("POST", f"/lists/{id_}/refresh")

		
    def cancelrefresh(self, id_):
        """Cancel refresh of the list.

        ``DELETE /lists/{id}/refresh``
        """
        return self.call("DELETE", f"/lists/{id_}/refresh")

    def getlistcontents(self, id_, **kwargs):
        """gets the list contents (if exists).

        ``GET /lists/{id}/contents``

        Keyword Args:
            offset (int): Offset to start retrieving items from (format: int32, default: 0)
            size (int): How many items to return (format: int32, default: 100)

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/List_getlistcontents_response.schema
        """
        return self.call("GET", f"/lists/{id_}/contents", query=kwargs)

    def exportlist(self, id_):
        """Exports the list.

        ``POST /lists/{id}/exports``

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/List_exportlist_response.schema
        """
        return self.call("POST", f"/lists/{id_}/exports")

    def getexportdetails(self, exportId, id_):
        """Get details of an export request

        ``GET /lists/{id}/exports/{exportId}``

        Args:
            exportId (str): exportId of the list (format: UUID)

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/List_getexportdetails_response.schema
        """
        return self.call("GET", f"/lists/{id_}/exports/{exportId}")

    def cancelexport(self, exportId, id_):
        """Cancel the export.

        ``POST /lists/{id}/exports/{exportId}/cancel``

        Args:
            exportId (str): exportId of the list (format: UUID)
        """
        return self.call("POST", f"/lists/{id_}/exports/{exportId}/cancel")

    def downloadlist(self, exportId, id_):
        """Download the exported file.

        ``GET /lists/{id}/exports/{exportId}/download``

        Args:
            exportId (str): exportId of the list (format: UUID)
        """
        return self.call("GET", f"/lists/{id_}/exports/{exportId}/download")

    def getlistconfiguration(self):
        """Get list app configuration.

        ``GET /lists/configuration``

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/List_getlistconfiguration_response.schema
        """
        return self.call("GET", "/lists/configuration")

    def getlistversions(self, id_):
        """Get all the historic versions of the specified list.

        ``GET /lists/{id}/versions``
        """
        return self.call("GET", f"/lists/{id_}/versions")

    def getlistversion(self, versionNumber, id_):
        """Get a specific historic version of the specified list.

        ``GET /lists/{id}/versions/{versionNumber}``

        Args:
            versionNumber (int): Integer number of the requested version (minimum: 1)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: List or version not found

        Schema:

            .. literalinclude:: ../files/List_getlistversion_response.schema
        """
        return self.call("GET", f"/lists/{id_}/versions/{versionNumber}")
