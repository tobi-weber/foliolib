# -*- coding: utf-8 -*-
# Generated at 2022-05-05

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.metaStorage")



class MetastorageAdmin(FolioAdminApi):
    """Meta Storage
    Administration

    
    """

    def postConfigMatchKey(self, matchKey):
        """Create match key

        ``POST /meta-storage/config/matchkeys``

        Args:
            matchKey (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_postConfigMatchKey_request.schema
        """
        return self.call("POST", "/meta-storage/config/matchkeys", matchKey)

		
    def getConfigMatchKeys(self, **kwargs):
        """Get match key configurations

        ``GET /meta-storage/config/matchkeys``

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

            .. literalinclude:: ../files/Metastorage_getConfigMatchKeys_response.schema
        """
        return self.call("GET", "/meta-storage/config/matchkeys", query=kwargs)

    def getConfigMatchKey(self):
        """Get match key configuration

        ``GET /meta-storage/config/matchkeys/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getConfigMatchKey_response.schema
        """
        return self.call("GET", "/meta-storage/config/matchkeys/{id}")

		
    def putConfigMatchKey(self, matchKey):
        """Update match key configuration.

        ``PUT /meta-storage/config/matchkeys/{id}``

        Args:
            matchKey (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_putConfigMatchKey_request.schema
        """
        return self.call("PUT", "/meta-storage/config/matchkeys/{id}", matchKey)

		
    def deleteConfigMatchKey(self):
        """Delete match key configuration

        ``DELETE /meta-storage/config/matchkeys/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/meta-storage/config/matchkeys/{id}")

    def initializeMatchKey(self):
        """Recalculate match key across all records.

        ``PUT /meta-storage/config/matchkeys/{id}/initialize``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_initializeMatchKey_response.schema
        """
        return self.call("PUT", "/meta-storage/config/matchkeys/{id}/initialize")

    def postSource(self, source):
        """Create source.

        ``POST /meta-storage/sources``

        Args:
            source (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_postSource_request.schema
        """
        return self.call("POST", "/meta-storage/sources", source)

		
    def getSources(self, **kwargs):
        """Get sources.

        ``GET /meta-storage/sources``

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

            .. literalinclude:: ../files/Metastorage_getSources_response.schema
        """
        return self.call("GET", "/meta-storage/sources", query=kwargs)

    def getSource(self):
        """Get source.

        ``GET /meta-storage/config/sources/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getSource_response.schema
        """
        return self.call("GET", "/meta-storage/config/sources/{id}")

		
    def deleteSource(self):
        """Delete source.

        ``DELETE /meta-storage/config/sources/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/meta-storage/config/sources/{id}")

    def postIngestJob(self, ingestJobRequest):
        """Create ingest job

        ``POST /meta-storage/ingest-jobs``

        Args:
            ingestJobRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_postIngestJob_request.schema
        """
        return self.call("POST", "/meta-storage/ingest-jobs", ingestJobRequest)

    def ingestJobRecord(self, ingestRecordChunk):
        """Put records for job.

        ``PUT /meta-storage/ingest-jobs/{id}``

        Args:
            ingestRecordChunk (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_ingestJobRecord_request.schema
            .. literalinclude:: ../files/Metastorage_ingestJobRecord_request.schema_response.schema
        """
        return self.call("PUT", "/meta-storage/ingest-jobs/{id}", ingestRecordChunk)

		
    def ingestJobInfo(self):
        """Get ingest job information.

        ``GET /meta-storage/ingest-jobs/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_ingestJobInfo_response.schema
        """
        return self.call("GET", "/meta-storage/ingest-jobs/{id}")

		
    def ingestJobFinish(self, **kwargs):
        """Finish ingest job with either rollback of commit.

        ``DELETE /meta-storage/ingest-jobs/{id}``

        Keyword Args:
            commit (bool): whether to commit (default: False)

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/meta-storage/ingest-jobs/{id}", query=kwargs)

    def getGlobalRecords(self):
        """Get records that satisfy CQL query with fields localId, sourceId, globalId.

        ``GET /meta-storage/records``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getGlobalRecords_response.schema
        """
        return self.call("GET", "/meta-storage/records")

		
    def putGlobalRecords(self, ingestRecordRequest):
        """Create or update records.

        ``PUT /meta-storage/records``

        Args:
            ingestRecordRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_putGlobalRecords_request.schema
            .. literalinclude:: ../files/Metastorage_putGlobalRecords_request.schema_response.schema
        """
        return self.call("PUT", "/meta-storage/records", ingestRecordRequest)

		
    def deleteGlobalRecords(self):
        """Delete global records.

        ``DELETE /meta-storage/records``

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/meta-storage/records")

    def getGlobalRecord(self):
        """Get record with global identifier.

        ``GET /meta-storage/records/{globalId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getGlobalRecord_response.schema
        """
        return self.call("GET", "/meta-storage/records/{globalId}")

    def getClusters(self):
        """Get clusters with matchkeyid. CQL query with matchValue, clusterId fields

        ``GET /meta-storage/clusters``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getClusters_response.schema
        """
        return self.call("GET", "/meta-storage/clusters")

    def getCluster(self):
        """Get cluster by identifier

        ``GET /meta-storage/clusters/{clusterId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getCluster_response.schema
        """
        return self.call("GET", "/meta-storage/clusters/{clusterId}")

    def oaiService(self):
        """OAI service

        ``GET /meta-storage/oai``

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error
        """
        return self.call("GET", "/meta-storage/oai")
