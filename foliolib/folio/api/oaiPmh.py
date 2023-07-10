# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.oaiPmh")


class CleanupJob(FolioApi):
    """OAI-PMH Business Logic API

    provides endpoint for triggering clean up process of expired instances from instances table.
    """

    def set_cleanUpInstance(self):
        """

        ``POST /oai-pmh/clean-up-instances``

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("POST", "/oai-pmh/clean-up-instances")


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


class RequestMetadata(FolioApi):
    """Request Metadata API

    API for retrieving MARC21_WITHHOLDINGS harvesting request metadata.
    """

    def get_requestMetadata(self, **kwargs):
        """Get list of request metadata

        ``GET /oai/request-metadata``

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
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/RequestMetadata_get_requestMetadata_return.schema 
        """
        return self.call("GET", "/oai/request-metadata", query=kwargs)

    def get_failedToSaveInstances(self, requestId: str, **kwargs):
        """Get list of failed to save instances UUIDs

        ``GET /oai/request-metadata/{requestId}/failed-to-save-instances``

        Args:
            requestId (str)
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
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/RequestMetadata_get_failedToSaveInstances_return.schema 
        """
        return self.call("GET", f"/oai/request-metadata/{requestId}/failed-to-save-instances", query=kwargs)

    def get_skippedInstances(self, requestId: str, **kwargs):
        """Get list of skipped instances UUIDs

        ``GET /oai/request-metadata/{requestId}/skipped-instances``

        Args:
            requestId (str)
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
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/RequestMetadata_get_skippedInstances_return.schema 
        """
        return self.call("GET", f"/oai/request-metadata/{requestId}/skipped-instances", query=kwargs)

    def get_failedInstances(self, requestId: str, **kwargs):
        """Get list of failed instances UUIDs

        ``GET /oai/request-metadata/{requestId}/failed-instances``

        Args:
            requestId (str)
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
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/RequestMetadata_get_failedInstances_return.schema 
        """
        return self.call("GET", f"/oai/request-metadata/{requestId}/failed-instances", query=kwargs)

    def get_suppressedFromDiscoveryInstances(self, requestId: str, **kwargs):
        """Get list of suppressed from discovery instances UUIDs

        ``GET /oai/request-metadata/{requestId}/suppressed-from-discovery-instances``

        Args:
            requestId (str)
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
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/RequestMetadata_get_suppressedFromDiscoveryInstances_return.schema 
        """
        return self.call("GET", f"/oai/request-metadata/{requestId}/suppressed-from-discovery-instances", query=kwargs)


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


class CleanupErrorLogs(FolioApi):
    """OAI-PMH Error Logs Cleaning API

    provides endpoint for triggering clean up process of old error logs.
    """

    def set_cleanUpErrorLog(self):
        """

        ``POST /oai-pmh/clean-up-error-logs``

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("POST", "/oai-pmh/clean-up-error-logs")


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
