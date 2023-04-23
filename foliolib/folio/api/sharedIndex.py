# -*- coding: utf-8 -*-
# Generated at 2023-04-16

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.sharedIndex")



class SharedindexAdmin(FolioAdminApi):
    """Shared Index
    Administration

    
    """

    def postConfigMatchKey(self, matchKey):
        """Create match key

        ``POST /shared-index/config/matchkeys``

        Args:
            matchKey (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_postConfigMatchKey_request.schema
        """
        return self.call("POST", "/shared-index/config/matchkeys", matchKey)

		
    def getConfigMatchKeys(self, **kwargs):
        """Get match key configurations

        ``GET /shared-index/config/matchkeys``

        Keyword Args:
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0)
            query (str): CQL query
            offset (int): Skip over number of elements (default is first element) (default: 0, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_getConfigMatchKeys_response.schema
        """
        return self.call("GET", "/shared-index/config/matchkeys", query=kwargs)

    def getConfigMatchKey(self):
        """Get match key configuration

        ``GET /shared-index/config/matchkeys/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_getConfigMatchKey_response.schema
        """
        return self.call("GET", "/shared-index/config/matchkeys/{id}")

		
    def putConfigMatchKey(self, matchKey):
        """Update match key configuration.

        ``PUT /shared-index/config/matchkeys/{id}``

        Args:
            matchKey (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_putConfigMatchKey_request.schema
        """
        return self.call("PUT", "/shared-index/config/matchkeys/{id}", matchKey)

		
    def deleteConfigMatchKey(self):
        """Delete match key configuration

        ``DELETE /shared-index/config/matchkeys/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/shared-index/config/matchkeys/{id}")

    def initializeMatchKey(self):
        """Recalculate match key across all records.

        ``PUT /shared-index/config/matchkeys/{id}/initialize``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_initializeMatchKey_response.schema
        """
        return self.call("PUT", "/shared-index/config/matchkeys/{id}/initialize")

    def postSource(self, source):
        """Create source.

        ``POST /shared-index/sources``

        Args:
            source (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_postSource_request.schema
        """
        return self.call("POST", "/shared-index/sources", source)

		
    def getSources(self, **kwargs):
        """Get sources.

        ``GET /shared-index/sources``

        Keyword Args:
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0)
            query (str): CQL query
            offset (int): Skip over number of elements (default is first element) (default: 0, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_getSources_response.schema
        """
        return self.call("GET", "/shared-index/sources", query=kwargs)

    def getSource(self):
        """Get source.

        ``GET /shared-index/config/sources/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_getSource_response.schema
        """
        return self.call("GET", "/shared-index/config/sources/{id}")

		
    def deleteSource(self):
        """Delete source.

        ``DELETE /shared-index/config/sources/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/shared-index/config/sources/{id}")

    def postIngestJob(self, ingestJobRequest):
        """Create ingest job

        ``POST /shared-index/shared-index/ingest-jobs``

        Args:
            ingestJobRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_postIngestJob_request.schema
        """
        return self.call("POST", "/shared-index/shared-index/ingest-jobs", ingestJobRequest)

    def ingestJobRecord(self, ingestRecordChunk):
        """Put records for job.

        ``PUT /shared-index/shared-index/ingest-jobs/{id}``

        Args:
            ingestRecordChunk (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_ingestJobRecord_request.schema
            .. literalinclude:: ../files/Sharedindex_ingestJobRecord_request.schema_response.schema
        """
        return self.call("PUT", "/shared-index/shared-index/ingest-jobs/{id}", ingestRecordChunk)

		
    def ingestJobInfo(self):
        """Get ingest job information.

        ``GET /shared-index/shared-index/ingest-jobs/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_ingestJobInfo_response.schema
        """
        return self.call("GET", "/shared-index/shared-index/ingest-jobs/{id}")

		
    def ingestJobFinish(self, **kwargs):
        """Finish ingest job with either rollback of commit.

        ``DELETE /shared-index/shared-index/ingest-jobs/{id}``

        Keyword Args:
            commit (bool): whether to commit (default: False)

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/shared-index/shared-index/ingest-jobs/{id}", query=kwargs)

    def getGlobalRecords(self):
        """Get records that satisfy CQL query with fields localId, sourceId, globalId.

        ``GET /shared-index/records``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_getGlobalRecords_response.schema
        """
        return self.call("GET", "/shared-index/records")

		
    def putGlobalRecords(self, ingestRecordRequest):
        """Create or update records.

        ``PUT /shared-index/records``

        Args:
            ingestRecordRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_putGlobalRecords_request.schema
            .. literalinclude:: ../files/Sharedindex_putGlobalRecords_request.schema_response.schema
        """
        return self.call("PUT", "/shared-index/records", ingestRecordRequest)

		
    def deleteGlobalRecords(self):
        """Delete global records.

        ``DELETE /shared-index/records``

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/shared-index/records")

    def getGlobalRecord(self):
        """Get record with global identifier.

        ``GET /shared-index/records/{globalId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_getGlobalRecord_response.schema
        """
        return self.call("GET", "/shared-index/records/{globalId}")

    def getClusters(self):
        """Get clusters with matchkeyid. CQL query with matchValue, clusterId fields

        ``GET /shared-index/clusters``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_getClusters_response.schema
        """
        return self.call("GET", "/shared-index/clusters")

    def getCluster(self):
        """Get cluster by identifier

        ``GET /shared-index/clusters/{clusterId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_getCluster_response.schema
        """
        return self.call("GET", "/shared-index/clusters/{clusterId}")

    def oaiService(self):
        """OAI service

        ``GET /shared-index/oai``

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error
        """
        return self.call("GET", "/shared-index/oai")
