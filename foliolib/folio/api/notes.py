# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.notes")



class Notes(FolioApi):
    """Notes API

    
    """

    def getnotetypecollection(self, **kwargs):
        """Return a list of note types

        ``GET /note-types``

        Keyword Args:
            query (str): A query expressed as a CQL string, for details see [Note Types API](https://github.com/folio-org/mod-notes/blob/master/docs/api-guide.md#note-types-api) (default: cql.allRecords=1)
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 1000, minimum: 1, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestUnauthorized: Not authorized to perform requested action
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Unexpected error

        Schema:

            .. literalinclude:: ../files/Notes_getnotetypecollection_response.schema
        """
        return self.call("GET", "/note-types", query=kwargs)

		
    def createnotetype(self, noteType):
        """Create a new note type.

        ``POST /note-types``

        Args:
            noteType (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestUnauthorized: Not authorized to perform requested action
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Unexpected error

        Schema:

            .. literalinclude:: ../files/Notes_createnotetype_request.schema
        """
        return self.call("POST", f"/note-types", noteType)

    def getnotetype(self, id_):
        """Retrieve note type with given ID

        ``GET /note-types/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestUnauthorized: Not authorized to perform requested action
            OkapiRequestNotFound: Resource with a given ID not found
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Unexpected error

        Schema:

            .. literalinclude:: ../files/Notes_getnotetype_response.schema
        """
        return self.call("GET", f"/note-types/{id_}")

		
    def updatenotetype(self, noteType, id_):
        """Update note type with given ID

        ``PUT /note-types/{id}``

        Args:
            noteType (dict): See Schema below.

        Raises:
            OkapiRequestUnauthorized: Not authorized to perform requested action
            OkapiRequestNotFound: Resource with a given ID not found
            OkapiFatalError: Unexpected error

        Schema:

            .. literalinclude:: ../files/Notes_updatenotetype_request.schema
        """
        return self.call("PUT", f"/note-types/{id_}", noteType)

		
    def deletenotetype(self, id_):
        """Delete note type with given ID

        ``DELETE /note-types/{id}``

        Raises:
            OkapiRequestUnauthorized: Not authorized to perform requested action
            OkapiRequestNotFound: Resource with a given ID not found
            OkapiFatalError: Unexpected error
        """
        return self.call("DELETE", f"/note-types/{id_}")

    def getnotecollection(self, **kwargs):
        """Return a list of notes

        ``GET /notes``

        Keyword Args:
            query (str): A query expressed as a CQL string, for details see [Notes API](https://github.com/folio-org/mod-notes/blob/master/docs/api-guide.md#notes-api) (default: cql.allRecords=1)
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 1000, minimum: 1, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestUnauthorized: Not authorized to perform requested action
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Unexpected error

        Schema:

            .. literalinclude:: ../files/Notes_getnotecollection_response.schema
        """
        return self.call("GET", "/notes", query=kwargs)

		
    def createnote(self, note):
        """Create a new note.

        ``POST /notes``

        Args:
            note (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestUnauthorized: Not authorized to perform requested action
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Unexpected error

        Schema:

            .. literalinclude:: ../files/Notes_createnote_request.schema
        """
        return self.call("POST", f"/notes", note)

    def getnote(self, id_):
        """Retrieve note with given ID

        ``GET /notes/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestUnauthorized: Not authorized to perform requested action
            OkapiRequestNotFound: Resource with a given ID not found
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Unexpected error

        Schema:

            .. literalinclude:: ../files/Notes_getnote_response.schema
        """
        return self.call("GET", f"/notes/{id_}")

		
    def updatenote(self, note, id_):
        """Update note with given ID

        ``PUT /notes/{id}``

        Args:
            note (dict): See Schema below.

        Raises:
            OkapiRequestUnauthorized: Not authorized to perform requested action
            OkapiRequestNotFound: Resource with a given ID not found
            OkapiFatalError: Unexpected error

        Schema:

            .. literalinclude:: ../files/Notes_updatenote_request.schema
        """
        return self.call("PUT", f"/notes/{id_}", note)

		
    def deletenote(self, id_):
        """Delete note with given ID

        ``DELETE /notes/{id}``

        Raises:
            OkapiRequestUnauthorized: Not authorized to perform requested action
            OkapiRequestNotFound: Resource with a given ID not found
            OkapiFatalError: Unexpected error
        """
        return self.call("DELETE", f"/notes/{id_}")

    def updatelinks(self, noteLinkUpdateCollection, objectType, objectId):
        """Add or delete links to specified list of notes

        ``PUT /note-links/type/{objectType}/id/{objectId}``

        Args:
            noteLinkUpdateCollection (dict): See Schema below.

        Raises:
            OkapiRequestUnauthorized: Not authorized to perform requested action
            OkapiRequestNotFound: Resource with a given ID not found
            OkapiFatalError: Unexpected error

        Schema:

            .. literalinclude:: ../files/Notes_updatelinks_request.schema
        """
        return self.call("PUT", f"/note-links/type/{objectType}/id/{objectId}", noteLinkUpdateCollection)

    def getnotecollectionbylink(self, domain, objectType, objectId, **kwargs):
        """Return a list of notes by status. A maximum of 1000 notes can be returned per request.

        ``GET /note-links/domain/{domain}/type/{objectType}/id/{objectId}``

        Keyword Args:
            search (str): Partial match case-insensitive search term for note title and note content
            noteType (list): Search string for note type. Note(s) is returned only if it equals to specified word or sequence of words in the titleseparated by com type name. Multiple types should be declared with query parameter sequentially as follows "noteType=a&noteType=b". (items: (type: string))
            status (str):
            orderBy (str):
            order (str):
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 1000, minimum: 1, maximum: 2147483647)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestUnauthorized: Not authorized to perform requested action
            OkapiRequestUnprocessableEntity: Validation errors
            OkapiFatalError: Unexpected error

        Schema:

            .. literalinclude:: ../files/Notes_getnotecollectionbylink_response.schema
        """
        return self.call("GET", f"/note-links/domain/{domain}/type/{objectType}/id/{objectId}", query=kwargs)
