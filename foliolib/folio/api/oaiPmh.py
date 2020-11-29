# -*- coding: utf-8 -*-
# Generated at 2020-11-29

import logging

from foliolib.folio import FolioApi

log = logging.getLogger("foliolib.folio.api.oaiPmh")


class FolioSet(FolioApi):
    """Set API

    API for managing sets and filtering conditions that is used as part of metadata harvesting protocol implementation
    """

    def get_sets(self, **kwargs):
        """Retrieve a list of set items.

        ``GET /oai-pmh/sets``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
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

            .. literalinclude:: ../files/FolioSet_get_sets_return.schema 
        """
        return self.call("GET", "/oai-pmh/sets", query=kwargs)

    def set_set(self, set: dict):
        """Create a new set item.

        ``POST /oai-pmh/sets``

        Args:
            set (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created set item

        Schema:

            .. literalinclude:: ../files/FolioSet_set_set_request.schema
        """
        return self.call("POST", "/oai-pmh/sets", data=set)

    def get_set(self, setsId: str):
        """Retrieve set item with given {setId}

        ``GET /oai-pmh/sets/{setsId}``

        Args:
            setsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FolioSet_get_set_return.schema 
        """
        return self.call("GET", f"/oai-pmh/sets/{setsId}")

    def delete_set(self, setsId: str):
        """Delete set item with given {setId}

        ``DELETE /oai-pmh/sets/{setsId}``

        Args:
            setsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/oai-pmh/sets/{setsId}")

    def modify_set(self, setsId: str, set: dict):
        """Update set item with given {setId}

        ``PUT /oai-pmh/sets/{setsId}``

        Args:
            setsId (str)
            set (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/FolioSet_modify_set_request.schema
        """
        return self.call("PUT", f"/oai-pmh/sets/{setsId}", data=set)


class FolioSetFilteringConditions(FolioApi):
    """Set API

    API for retirieving filtering condition values
    """

    def get_filteringConditions(self):
        """

        ``GET /oai-pmh/filtering-conditions``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FolioSetFilteringConditions_get_filteringConditions_return.schema 
        """
        return self.call("GET", "/oai-pmh/filtering-conditions")


class OaiPmh(FolioApi):
    """OAI-PMH Business Logic API

    The Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) provides
		an application-independent interoperability framework based on metadata harvesting.
		This module supports the OAI-PMH as a means of exposing FOLIO metadata.
    """

    def get_records(self, **kwargs):
        """

        ``GET /oai/records``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            verb (str):  verb that specifies oai-pmh request type
            identifier (str):  parameter that is used for GetRecord and ListMetadataFormats requests
            resumptionToken (str):  flow control token returned by a ListIdentifiers request that issued an incomplete list
            from (str):  UTC datetime value, which specifies a lower bound for datestamp-based selective harvesting
                    
                    Example:
                    
                     - 2018-10-15 15:16:17+00:00
            until (str):  UTC datetime value, which specifies a upper bound for datestamp-based selective harvesting
                    
                    Example:
                    
                     - 2018-10-22 23:22:21+00:00
            set (str):  setSpec value, which specifies set criteria for selective harvesting
            metadataPrefix (str):  metadata prefix of the format that should be included in the metadata part of the returned record

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error
        """
        return self.call("GET", "/oai/records", query=kwargs)
