# -*- coding: utf-8 -*-
# Generated at 2023-04-16

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.metaStorage")



class MetastorageAdmin(FolioAdminApi):
    """Meta Storage
    Administration

    
    """

    def getOaiConfig(self):
        """Get OAI configuration

        ``GET /meta-storage/config/oai``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getOaiConfig_response.schema
        """
        return self.call("GET", "/meta-storage/config/oai")

		
    def putOaiConfig(self, oaiConfig):
        """Update OAI configuration.

        ``PUT /meta-storage/config/oai``

        Args:
            oaiConfig (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_putOaiConfig_request.schema
        """
        return self.call("PUT", "/meta-storage/config/oai", oaiConfig)

		
    def deleteOaiConfig(self):
        """Update OAI configuration.

        ``DELETE /meta-storage/config/oai``

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/meta-storage/config/oai")

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
            count (str): control of counting in queries (default: none, enum: ['exact', 'none'])
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

		
    def deleteConfigMatchKey(self):
        """Delete match key configuration

        ``DELETE /meta-storage/config/matchkeys/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/meta-storage/config/matchkeys/{id}")

		
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

    def statsMatchKey(self):
        """Get statistics for match key configuration

        ``GET /meta-storage/config/matchkeys/{id}/stats``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_statsMatchKey_response.schema
        """
        return self.call("GET", "/meta-storage/config/matchkeys/{id}/stats")

    def postCodeModule(self, codeModule):
        """Create a new code module

        ``POST /meta-storage/config/modules``

        Args:
            codeModule (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_postCodeModule_request.schema
        """
        return self.call("POST", "/meta-storage/config/modules", codeModule)

		
    def getCodeModules(self, **kwargs):
        """Retrieve all code modules

        ``GET /meta-storage/config/modules``

        Keyword Args:
            count (str): control of counting in queries (default: none, enum: ['exact', 'none'])
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0)
            query (str): CQL query
            offset (int): Skip over number of elements (default is first element) (default: 0, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getCodeModules_response.schema
        """
        return self.call("GET", "/meta-storage/config/modules", query=kwargs)

    def getCodeModule(self):
        """Retrieve a code module by id

        ``GET /meta-storage/config/modules/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getCodeModule_response.schema
        """
        return self.call("GET", "/meta-storage/config/modules/{id}")

		
    def putCodeModule(self, codeModule):
        """Update code module by id

        ``PUT /meta-storage/config/modules/{id}``

        Args:
            codeModule (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_putCodeModule_request.schema
        """
        return self.call("PUT", "/meta-storage/config/modules/{id}", codeModule)

		
    def deleteCodeModule(self):
        """Delete code module by id

        ``DELETE /meta-storage/config/modules/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/meta-storage/config/modules/{id}")

    def reloadCodeModule(self):
        """Force module to be reloaded

        ``PUT /meta-storage/config/modules/{id}/reload``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("PUT", "/meta-storage/config/modules/{id}/reload")

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

    def getGlobalRecords(self, **kwargs):
        """Get records that satisfy CQL query with fields localId, sourceId, globalId.

        ``GET /meta-storage/records``

        Keyword Args:
            count (str): control of counting in queries (default: none, enum: ['exact', 'none'])
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0)
            query (str): CQL query
            offset (int): Skip over number of elements (default is first element) (default: 0, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getGlobalRecords_response.schema
        """
        return self.call("GET", "/meta-storage/records", query=kwargs)

		
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

		
    def deleteGlobalRecords(self, **kwargs):
        """Delete global records.

        ``DELETE /meta-storage/records``

        Keyword Args:
            query (str): CQL query

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/meta-storage/records", query=kwargs)

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

    def postOaiPmhClient(self, oai_pmh_client):
        """Create OAI PMH client job

        ``POST /meta-storage/pmh-clients``

        Args:
            oai-pmh-client (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_postOaiPmhClient_request.schema
        """
        return self.call("POST", "/meta-storage/pmh-clients", oai_pmh_client)

		
    def getCollectionOaiPmhClient(self):
        """Get all OAI PMH client jobs

        ``GET /meta-storage/pmh-clients``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getCollectionOaiPmhClient_response.schema
        """
        return self.call("GET", "/meta-storage/pmh-clients")

    def getOaiPmhClient(self):
        """Get OAI-PMH client

        ``GET /meta-storage/pmh-clients/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getOaiPmhClient_response.schema
        """
        return self.call("GET", "/meta-storage/pmh-clients/{id}")

		
    def putOaiPmhClient(self, oai_pmh_client):
        """Update OAI-PMH client

        ``PUT /meta-storage/pmh-clients/{id}``

        Args:
            oai-pmh-client (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_putOaiPmhClient_request.schema
        """
        return self.call("PUT", "/meta-storage/pmh-clients/{id}", oai_pmh_client)

		
    def deleteOaiPmhClient(self):
        """Delete OAI-PMH client

        ``DELETE /meta-storage/pmh-clients/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_deleteOaiPmhClient_response.schema
        """
        return self.call("DELETE", "/meta-storage/pmh-clients/{id}")

    def startOaiPmhClient(self):
        """Start OAI PMH client job

        ``POST /meta-storage/pmh-clients/{id}/start``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("POST", "/meta-storage/pmh-clients/{id}/start")

    def stopOaiPmhClient(self):
        """Stop OAI PMH client job

        ``POST /meta-storage/pmh-clients/{id}/stop``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("POST", "/meta-storage/pmh-clients/{id}/stop")

    def statusOaiPmhClient(self):
        """Get OAI PMH client status

        ``GET /meta-storage/pmh-clients/{id}/status``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_statusOaiPmhClient_response.schema
        """
        return self.call("GET", "/meta-storage/pmh-clients/{id}/status")
