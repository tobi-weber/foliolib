# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.reservoir")



class Reservoir(FolioApi):
    """Reservoir

    
    """

    def getoaiconfig(self):
        """Get OAI configuration

        ``GET /reservoir/config/oai``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_getoaiconfig_response.schema
        """
        return self.call("GET", "/reservoir/config/oai")

		
    def putoaiconfig(self, oaiConfig):
        """Update OAI configuration.

        ``PUT /reservoir/config/oai``

        Args:
            oaiConfig (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_putoaiconfig_request.schema
        """
        return self.call("PUT", f"/reservoir/config/oai", oaiConfig)

		
    def deleteoaiconfig(self):
        """Update OAI configuration.

        ``DELETE /reservoir/config/oai``

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/reservoir/config/oai")

    def postconfigmatchkey(self, matchKey):
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

            .. literalinclude:: ../files/Reservoir_postconfigmatchkey_request.schema
        """
        return self.call("POST", f"/reservoir/config/matchkeys", matchKey)

		
    def getconfigmatchkeys(self, **kwargs):
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

            .. literalinclude:: ../files/Reservoir_getconfigmatchkeys_response.schema
        """
        return self.call("GET", "/reservoir/config/matchkeys", query=kwargs)

    def getconfigmatchkey(self, id_):
        """Get match key configuration

        ``GET /reservoir/config/matchkeys/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_getconfigmatchkey_response.schema
        """
        return self.call("GET", f"/reservoir/config/matchkeys/{id_}")

		
    def deleteconfigmatchkey(self, id_):
        """Delete match key configuration

        ``DELETE /reservoir/config/matchkeys/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", f"/reservoir/config/matchkeys/{id_}")

		
    def putconfigmatchkey(self, matchKey, id_):
        """Update match key configuration.

        ``PUT /reservoir/config/matchkeys/{id}``

        Args:
            matchKey (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_putconfigmatchkey_request.schema
        """
        return self.call("PUT", f"/reservoir/config/matchkeys/{id_}", matchKey)

    def initializematchkey(self, id_):
        """Recalculate match key across all records.

        ``PUT /reservoir/config/matchkeys/{id}/initialize``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_initializematchkey_response.schema
        """
        return self.call("PUT", f"/reservoir/config/matchkeys/{id_}/initialize")

    def statsmatchkey(self, id_):
        """Get statistics for match key configuration

        ``GET /reservoir/config/matchkeys/{id}/stats``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_statsmatchkey_response.schema
        """
        return self.call("GET", f"/reservoir/config/matchkeys/{id_}/stats")

    def postcodemodule(self, codeModule):
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

            .. literalinclude:: ../files/Reservoir_postcodemodule_request.schema
        """
        return self.call("POST", f"/reservoir/config/modules", codeModule)

		
    def getcodemodules(self, **kwargs):
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

            .. literalinclude:: ../files/Reservoir_getcodemodules_response.schema
        """
        return self.call("GET", "/reservoir/config/modules", query=kwargs)

    def getcodemodule(self, id_):
        """Retrieve a code module by id

        ``GET /reservoir/config/modules/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_getcodemodule_response.schema
        """
        return self.call("GET", f"/reservoir/config/modules/{id_}")

		
    def putcodemodule(self, codeModule, id_):
        """Update code module by id

        ``PUT /reservoir/config/modules/{id}``

        Args:
            codeModule (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_putcodemodule_request.schema
        """
        return self.call("PUT", f"/reservoir/config/modules/{id_}", codeModule)

		
    def deletecodemodule(self, id_):
        """Delete code module by id

        ``DELETE /reservoir/config/modules/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", f"/reservoir/config/modules/{id_}")

    def reloadcodemodule(self, id_):
        """Force module to be reloaded

        ``PUT /reservoir/config/modules/{id}/reload``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("PUT", f"/reservoir/config/modules/{id_}/reload")

    def postsource(self, source):
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

            .. literalinclude:: ../files/Reservoir_postsource_request.schema
        """
        return self.call("POST", f"/reservoir/sources", source)

		
    def getsources(self, **kwargs):
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

            .. literalinclude:: ../files/Reservoir_getsources_response.schema
        """
        return self.call("GET", "/reservoir/sources", query=kwargs)

    def getsource(self, id_):
        """Get source.

        ``GET /reservoir/config/sources/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_getsource_response.schema
        """
        return self.call("GET", f"/reservoir/config/sources/{id_}")

		
    def deletesource(self, id_):
        """Delete source.

        ``DELETE /reservoir/config/sources/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", f"/reservoir/config/sources/{id_}")

    def postingestjob(self, ingestJobRequest):
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

            .. literalinclude:: ../files/Reservoir_postingestjob_request.schema
        """
        return self.call("POST", f"/reservoir/ingest-jobs", ingestJobRequest)

    def ingestjobrecord(self, ingestRecordChunk, id_):
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

            .. literalinclude:: ../files/Reservoir_ingestjobrecord_request.schema
            .. literalinclude:: ../files/Reservoir_ingestjobrecord_request.schema_response.schema
        """
        return self.call("PUT", f"/reservoir/ingest-jobs/{id_}", ingestRecordChunk)

		
    def ingestjobinfo(self, id_):
        """Get ingest job information.

        ``GET /reservoir/ingest-jobs/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_ingestjobinfo_response.schema
        """
        return self.call("GET", f"/reservoir/ingest-jobs/{id_}")

		
    def ingestjobfinish(self, id_, **kwargs):
        """Finish ingest job with either rollback of commit.

        ``DELETE /reservoir/ingest-jobs/{id}``

        Keyword Args:
            commit (bool): whether to commit (default: False)

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", f"/reservoir/ingest-jobs/{id_}", query=kwargs)

    def uploadrecords(self, filePath):
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

            .. literalinclude:: ../files/Reservoir_uploadrecords_response.schema
        """
        import os
        headers = {}
        headers["Content-Type"] = "application/octet-stream"
        headers["Content-length"] = str(os.path.getsize(filePath))
        headers["Content-Disposition"] = "attachment; filename=%s" % os.path.basename(
            filePath)
        with open(filePath, 'rb') as f:
            data = f.read()
        
        return self.call("POST", f"/reservoir/upload", data=data)

    def getglobalrecords(self, **kwargs):
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

            .. literalinclude:: ../files/Reservoir_getglobalrecords_response.schema
        """
        return self.call("GET", "/reservoir/records", query=kwargs)

		
    def putglobalrecords(self, ingestRecordRequest):
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

            .. literalinclude:: ../files/Reservoir_putglobalrecords_request.schema
            .. literalinclude:: ../files/Reservoir_putglobalrecords_request.schema_response.schema
        """
        return self.call("PUT", f"/reservoir/records", ingestRecordRequest)

		
    def deleteglobalrecords(self, **kwargs):
        """Delete global records.

        ``DELETE /reservoir/records``

        Keyword Args:
            query (str): CQL query

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/reservoir/records", query=kwargs)

    def getglobalrecord(self, globalId):
        """Get record with global identifier.

        ``GET /reservoir/records/{globalId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_getglobalrecord_response.schema
        """
        return self.call("GET", f"/reservoir/records/{globalId}")

    def getclusters(self):
        """Get clusters based on matchkeyid. Query is CQL with the following fields supported: matchValue, clusterId, globalId, localId, sourceId, sourceVersion.


        ``GET /reservoir/clusters``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_getclusters_response.schema
        """
        return self.call("GET", "/reservoir/clusters")

    def touchclusters(self, **kwargs):
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

            .. literalinclude:: ../files/Reservoir_touchclusters_response.schema
        """
        return self.call("POST", "/reservoir/clusters/touch", query=kwargs)

    def getcluster(self, clusterId):
        """Get cluster by identifier

        ``GET /reservoir/clusters/{clusterId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_getcluster_response.schema
        """
        return self.call("GET", f"/reservoir/clusters/{clusterId}")

    def oaiservice(self):
        """OAI service

        ``GET /reservoir/oai``

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error
        """
        return self.call("GET", "/reservoir/oai")

    def postoaipmhclient(self, oaiPmhClient):
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

            .. literalinclude:: ../files/Reservoir_postoaipmhclient_request.schema
        """
        return self.call("POST", f"/reservoir/pmh-clients", oaiPmhClient)

		
    def getcollectionoaipmhclient(self):
        """Get all OAI PMH client jobs

        ``GET /reservoir/pmh-clients``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_getcollectionoaipmhclient_response.schema
        """
        return self.call("GET", "/reservoir/pmh-clients")

    def getoaipmhclient(self, id_):
        """Get OAI-PMH client

        ``GET /reservoir/pmh-clients/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_getoaipmhclient_response.schema
        """
        return self.call("GET", f"/reservoir/pmh-clients/{id_}")

		
    def putoaipmhclient(self, oaiPmhClient, id_):
        """Update OAI-PMH client

        ``PUT /reservoir/pmh-clients/{id}``

        Args:
            oaiPmhClient (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_putoaipmhclient_request.schema
        """
        return self.call("PUT", f"/reservoir/pmh-clients/{id_}", oaiPmhClient)

		
    def deleteoaipmhclient(self, id_):
        """Delete OAI-PMH client

        ``DELETE /reservoir/pmh-clients/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", f"/reservoir/pmh-clients/{id_}")

    def startoaipmhclient(self, id_):
        """Start OAI PMH client job

        ``POST /reservoir/pmh-clients/{id}/start``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("POST", f"/reservoir/pmh-clients/{id_}/start")

    def stopoaipmhclient(self, id_):
        """Stop OAI PMH client job

        ``POST /reservoir/pmh-clients/{id}/stop``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("POST", f"/reservoir/pmh-clients/{id_}/stop")

    def statusoaipmhclient(self, id_):
        """Get OAI PMH client status

        ``GET /reservoir/pmh-clients/{id}/status``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Reservoir_statusoaipmhclient_response.schema
        """
        return self.call("GET", f"/reservoir/pmh-clients/{id_}/status")
