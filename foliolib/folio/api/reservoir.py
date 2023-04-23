# -*- coding: utf-8 -*-
# Generated at 2023-04-16

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.reservoir")



class ReservoirAdmin(FolioAdminApi):
    """Reservoir
    Administration

    
    """

    def getOaiConfig(self):
        """Get OAI configuration

        ``GET /reservoir/config/oai``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_getOaiConfig_response.schema
        """
        return self.call("GET", "/reservoir/config/oai")

		
    def putOaiConfig(self, oaiConfig):
        """Update OAI configuration.

        ``PUT /reservoir/config/oai``

        Args:
            oaiConfig (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_putOaiConfig_request.schema
        """
        return self.call("PUT", "/reservoir/config/oai", oaiConfig)

		
    def deleteOaiConfig(self):
        """Update OAI configuration.

        ``DELETE /reservoir/config/oai``

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/reservoir/config/oai")

    def postConfigMatchKey(self, matchKey):
        """Create match key

        ``POST /reservoir/config/matchkeys``

        Args:
            matchKey (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_postConfigMatchKey_request.schema
        """
        return self.call("POST", "/reservoir/config/matchkeys", matchKey)

		
    def getConfigMatchKeys(self, **kwargs):
        """Get match key configurations

        ``GET /reservoir/config/matchkeys``

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

            .. literalinclude:: ../files/Reservoir_getConfigMatchKeys_response.schema
        """
        return self.call("GET", "/reservoir/config/matchkeys", query=kwargs)

    def getConfigMatchKey(self):
        """Get match key configuration

        ``GET /reservoir/config/matchkeys/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_getConfigMatchKey_response.schema
        """
        return self.call("GET", "/reservoir/config/matchkeys/{id}")

		
    def deleteConfigMatchKey(self):
        """Delete match key configuration

        ``DELETE /reservoir/config/matchkeys/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/reservoir/config/matchkeys/{id}")

		
    def putConfigMatchKey(self, matchKey):
        """Update match key configuration.

        ``PUT /reservoir/config/matchkeys/{id}``

        Args:
            matchKey (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_putConfigMatchKey_request.schema
        """
        return self.call("PUT", "/reservoir/config/matchkeys/{id}", matchKey)

    def initializeMatchKey(self):
        """Recalculate match key across all records.

        ``PUT /reservoir/config/matchkeys/{id}/initialize``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_initializeMatchKey_response.schema
        """
        return self.call("PUT", "/reservoir/config/matchkeys/{id}/initialize")

    def statsMatchKey(self):
        """Get statistics for match key configuration

        ``GET /reservoir/config/matchkeys/{id}/stats``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_statsMatchKey_response.schema
        """
        return self.call("GET", "/reservoir/config/matchkeys/{id}/stats")

    def postCodeModule(self, codeModule):
        """Create a new code module

        ``POST /reservoir/config/modules``

        Args:
            codeModule (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_postCodeModule_request.schema
        """
        return self.call("POST", "/reservoir/config/modules", codeModule)

		
    def getCodeModules(self, **kwargs):
        """Retrieve all code modules

        ``GET /reservoir/config/modules``

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

            .. literalinclude:: ../files/Reservoir_getCodeModules_response.schema
        """
        return self.call("GET", "/reservoir/config/modules", query=kwargs)

    def getCodeModule(self):
        """Retrieve a code module by id

        ``GET /reservoir/config/modules/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_getCodeModule_response.schema
        """
        return self.call("GET", "/reservoir/config/modules/{id}")

		
    def putCodeModule(self, codeModule):
        """Update code module by id

        ``PUT /reservoir/config/modules/{id}``

        Args:
            codeModule (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_putCodeModule_request.schema
        """
        return self.call("PUT", "/reservoir/config/modules/{id}", codeModule)

		
    def deleteCodeModule(self):
        """Delete code module by id

        ``DELETE /reservoir/config/modules/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/reservoir/config/modules/{id}")

    def reloadCodeModule(self):
        """Force module to be reloaded

        ``PUT /reservoir/config/modules/{id}/reload``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("PUT", "/reservoir/config/modules/{id}/reload")

    def postSource(self, source):
        """Create source.

        ``POST /reservoir/sources``

        Args:
            source (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_postSource_request.schema
        """
        return self.call("POST", "/reservoir/sources", source)

		
    def getSources(self, **kwargs):
        """Get sources.

        ``GET /reservoir/sources``

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

            .. literalinclude:: ../files/Reservoir_getSources_response.schema
        """
        return self.call("GET", "/reservoir/sources", query=kwargs)

    def getSource(self):
        """Get source.

        ``GET /reservoir/config/sources/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_getSource_response.schema
        """
        return self.call("GET", "/reservoir/config/sources/{id}")

		
    def deleteSource(self):
        """Delete source.

        ``DELETE /reservoir/config/sources/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/reservoir/config/sources/{id}")

    def postIngestJob(self, ingestJobRequest):
        """Create ingest job

        ``POST /reservoir/ingest-jobs``

        Args:
            ingestJobRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_postIngestJob_request.schema
        """
        return self.call("POST", "/reservoir/ingest-jobs", ingestJobRequest)

    def ingestJobRecord(self, ingestRecordChunk):
        """Put records for job.

        ``PUT /reservoir/ingest-jobs/{id}``

        Args:
            ingestRecordChunk (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_ingestJobRecord_request.schema
            .. literalinclude:: ../files/Reservoir_ingestJobRecord_request.schema_response.schema
        """
        return self.call("PUT", "/reservoir/ingest-jobs/{id}", ingestRecordChunk)

		
    def ingestJobInfo(self):
        """Get ingest job information.

        ``GET /reservoir/ingest-jobs/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_ingestJobInfo_response.schema
        """
        return self.call("GET", "/reservoir/ingest-jobs/{id}")

		
    def ingestJobFinish(self, **kwargs):
        """Finish ingest job with either rollback of commit.

        ``DELETE /reservoir/ingest-jobs/{id}``

        Keyword Args:
            commit (bool): whether to commit (default: False)

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/reservoir/ingest-jobs/{id}", query=kwargs)

    def uploadRecords(self, filePath):
        """Upload MARC binary and MARCXML records.

        ``POST /reservoir/upload``

        Args:
            filePath (str): Path of file to upload.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestForbidden: Forbidden
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_uploadRecords_response.schema
        """
        import os
        headers = {}
        headers["Content-Type"] = "application/octet-stream"
        headers["Content-length"] = str(os.path.getsize(filePath))
        headers["Content-Disposition"] = "attachment; filename=%s" % os.path.basename(
            filePath)
        with open(filePath, 'rb') as f:
            data = f.read()
        
        return self.call("POST", "/reservoir/upload", data=data)

    def getGlobalRecords(self, **kwargs):
        """Get records that satisfy CQL query with fields localId, sourceId, globalId.

        ``GET /reservoir/records``

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

            .. literalinclude:: ../files/Reservoir_getGlobalRecords_response.schema
        """
        return self.call("GET", "/reservoir/records", query=kwargs)

		
    def putGlobalRecords(self, ingestRecordRequest):
        """Create or update records.

        ``PUT /reservoir/records``

        Args:
            ingestRecordRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_putGlobalRecords_request.schema
            .. literalinclude:: ../files/Reservoir_putGlobalRecords_request.schema_response.schema
        """
        return self.call("PUT", "/reservoir/records", ingestRecordRequest)

		
    def deleteGlobalRecords(self, **kwargs):
        """Delete global records.

        ``DELETE /reservoir/records``

        Keyword Args:
            query (str): CQL query

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/reservoir/records", query=kwargs)

    def getGlobalRecord(self):
        """Get record with global identifier.

        ``GET /reservoir/records/{globalId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_getGlobalRecord_response.schema
        """
        return self.call("GET", "/reservoir/records/{globalId}")

    def getClusters(self):
        """Get clusters based on matchkeyid. Query is CQL with the following fields supported: matchValue, clusterId, globalId, localId, sourceId, sourceVersion.


        ``GET /reservoir/clusters``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_getClusters_response.schema
        """
        return self.call("GET", "/reservoir/clusters")

    def touchClusters(self, **kwargs):
        """Update cluster timestamps. CQL must specify at least matchkeyId and sourceId. The sourceVersion and clusterId are optional.

        ``POST /reservoir/clusters/touch``

        Keyword Args:
            query (str): CQL query

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_touchClusters_response.schema
        """
        return self.call("POST", "/reservoir/clusters/touch", query=kwargs)

    def getCluster(self):
        """Get cluster by identifier

        ``GET /reservoir/clusters/{clusterId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_getCluster_response.schema
        """
        return self.call("GET", "/reservoir/clusters/{clusterId}")

    def oaiService(self):
        """OAI service

        ``GET /reservoir/oai``

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error
        """
        return self.call("GET", "/reservoir/oai")

    def postOaiPmhClient(self, oaiPmhClient):
        """Create OAI PMH client job

        ``POST /reservoir/pmh-clients``

        Args:
            oaiPmhClient (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_postOaiPmhClient_request.schema
        """
        return self.call("POST", "/reservoir/pmh-clients", oaiPmhClient)

		
    def getCollectionOaiPmhClient(self):
        """Get all OAI PMH client jobs

        ``GET /reservoir/pmh-clients``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_getCollectionOaiPmhClient_response.schema
        """
        return self.call("GET", "/reservoir/pmh-clients")

    def getOaiPmhClient(self):
        """Get OAI-PMH client

        ``GET /reservoir/pmh-clients/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_getOaiPmhClient_response.schema
        """
        return self.call("GET", "/reservoir/pmh-clients/{id}")

		
    def putOaiPmhClient(self, oaiPmhClient):
        """Update OAI-PMH client

        ``PUT /reservoir/pmh-clients/{id}``

        Args:
            oaiPmhClient (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_putOaiPmhClient_request.schema
        """
        return self.call("PUT", "/reservoir/pmh-clients/{id}", oaiPmhClient)

		
    def deleteOaiPmhClient(self):
        """Delete OAI-PMH client

        ``DELETE /reservoir/pmh-clients/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/reservoir/pmh-clients/{id}")

    def startOaiPmhClient(self):
        """Start OAI PMH client job

        ``POST /reservoir/pmh-clients/{id}/start``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("POST", "/reservoir/pmh-clients/{id}/start")

    def stopOaiPmhClient(self):
        """Stop OAI PMH client job

        ``POST /reservoir/pmh-clients/{id}/stop``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("POST", "/reservoir/pmh-clients/{id}/stop")

    def statusOaiPmhClient(self):
        """Get OAI PMH client status

        ``GET /reservoir/pmh-clients/{id}/status``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_statusOaiPmhClient_response.schema
        """
        return self.call("GET", "/reservoir/pmh-clients/{id}/status")
