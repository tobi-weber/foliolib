# -*- coding: utf-8 -*-
# Generated at 2020-11-29

import logging

from foliolib.folio import FolioApi

log = logging.getLogger("foliolib.folio.api.notes")


class Link(FolioApi):
    """mod-notes Links API

    This documents the API calls that can be made to query and manage note links of the system
    """

    def modify_noteLink(self, type_: str, id_: str, noteLink: dict):
        """Add links to specified list of notes

        ``PUT /note-links/type/{type_}/id/{id_}``

        Args:
            type_ (str)
            id_ (str)
            noteLink (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Link_modify_noteLink_request.schema
        """
        return self.call("PUT", f"/note-links/type/{type_}/id/{id_}", data=noteLink)

    def get_domains(self, domain: str, type_: str, id_: str, **kwargs):
        """Return a list of notes by status

        ``GET /note-links/domain/{domain}/type/{type_}/id/{id_}``

        Args:
            domain (str)
            type_ (str)
            id_ (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            title (str):  Search string for note title. Note is returned only if it contains specified word or sequence of words anywhere in the title. Search is case-insensitive.
                    
                    Example:
                    
                     - important
            noteType (list):  Search string for note type. Note(s) is returned only if it equals to specified word or sequence of words in the titleseparated by com type name. Multiple types should be declared with query parameter sequentially as follows "noteType=a&noteType=b". Search is case sensitive.
                    
                    Example:
                    
                     - ['General support']
            status (str): (default=ALL) Filtering records by status. Possible values are ASSIGNED, UNASSIGNED, ALL.
                    
                    Example:
                    
                     - ASSIGNED
            orderBy (str): (default=status) Field by which notes are ordered. Possible values are status, title, content, linksNumber, noteType, updatedDate. The default ascending sorting is applied for status, title, content, linksNumber, noteType parameters. For updatedDate is descending. Explicit selection of sorting can be set by using order query parameter.
            order (str): (default=default) indicates order of notes. Possible values asc, desc.
                    
                    Example:
                    
                     - asc
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

            .. literalinclude:: ../files/Link_get_domains_return.schema 
        """
        return self.call("GET", f"/note-links/domain/{domain}/type/{type_}/id/{id_}", query=kwargs)


class Note(FolioApi):
    """mod-notes API

    This documents the API calls that can be made to query and manage notes about all kind of objects
    """

    def get_notes(self, **kwargs):
        """Retrieve a list of note items.

        ``GET /notes``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example link.id = 1234
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - link.id=1234
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

            .. literalinclude:: ../files/Note_get_notes_return.schema 
        """
        return self.call("GET", "/notes", query=kwargs)

    def set_note(self, note: dict):
        """Create a new note item.

        ``POST /notes``

        Args:
            note (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created note item

        Schema:

            .. literalinclude:: ../files/Note_set_note_request.schema
        """
        return self.call("POST", "/notes", data=note)

    def get_note(self, notesId: str):
        """Retrieve note item with given {noteId}

        ``GET /notes/{notesId}``

        Args:
            notesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Note_get_note_return.schema 
        """
        return self.call("GET", f"/notes/{notesId}")

    def delete_note(self, notesId: str):
        """Delete note item with given {noteId}

        ``DELETE /notes/{notesId}``

        Args:
            notesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("DELETE", f"/notes/{notesId}")

    def modify_note(self, notesId: str, note: dict):
        """Update note item with given {noteId}

        ``PUT /notes/{notesId}``

        Args:
            notesId (str)
            note (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Note_modify_note_request.schema
        """
        return self.call("PUT", f"/notes/{notesId}", data=note)


class Types(FolioApi):
    """mod-notes Type API

    This documents the API calls that can be made to query and manage note types of the system
    """

    def get_noteTypes(self, **kwargs):
        """Return a list of note types

        ``GET /note-types``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - type=*high*
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

        Schema:

            .. literalinclude:: ../files/Types_get_noteTypes_return.schema 
        """
        return self.call("GET", "/note-types", query=kwargs)

    def set_noteType(self, noteType: dict):
        """Create a note type

        ``POST /note-types``

        Args:
            noteType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created noteType item

        Schema:

            .. literalinclude:: ../files/Types_set_noteType_request.schema
        """
        return self.call("POST", "/note-types", data=noteType)

    def get_noteType(self, typeId: str):
        """Retrieve noteType item with given {noteTypeId}

        ``GET /note-types/{typeId}``

        Args:
            typeId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Types_get_noteType_return.schema 
        """
        return self.call("GET", f"/note-types/{typeId}")

    def delete_noteType(self, typeId: str):
        """Delete noteType item with given {noteTypeId}

        ``DELETE /note-types/{typeId}``

        Args:
            typeId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/note-types/{typeId}")

    def modify_noteType(self, typeId: str, noteType: dict):
        """Update noteType item with given {noteTypeId}

        ``PUT /note-types/{typeId}``

        Args:
            typeId (str)
            noteType (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Types_modify_noteType_request.schema
        """
        return self.call("PUT", f"/note-types/{typeId}", data=noteType)
