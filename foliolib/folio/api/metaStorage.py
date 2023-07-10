# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.metaStorage")



class Metastorage(FolioApi):
    """Meta Storage

    
    """

    def getoaiconfig(self):
        """Get OAI configuration

        ``GET /meta-storage/config/oai``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getoaiconfig_response.schema
        """
        return self.call("GET", "/meta-storage/config/oai")

		
    def putoaiconfig(self, oaiConfig):
        """Update OAI configuration.

        ``PUT /meta-storage/config/oai``

        Args:
            oaiConfig (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_putoaiconfig_request.schema
        """
        return self.call("PUT", f"/meta-storage/config/oai", oaiConfig)

		
    def deleteoaiconfig(self):
        """Update OAI configuration.

        ``DELETE /meta-storage/config/oai``

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/meta-storage/config/oai")

    def postconfigmatchkey(self, matchKey):
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

            .. literalinclude:: ../files/Metastorage_postconfigmatchkey_request.schema
        """
        return self.call("POST", f"/meta-storage/config/matchkeys", matchKey)

		
    def getconfigmatchkeys(self, **kwargs):
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

            .. literalinclude:: ../files/Metastorage_getconfigmatchkeys_response.schema
        """
        return self.call("GET", "/meta-storage/config/matchkeys", query=kwargs)

    def getconfigmatchkey(self, id_):
        """Get match key configuration

        ``GET /meta-storage/config/matchkeys/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getconfigmatchkey_response.schema
        """
        return self.call("GET", f"/meta-storage/config/matchkeys/{id_}")

		
    def deleteconfigmatchkey(self, id_):
        """Delete match key configuration

        ``DELETE /meta-storage/config/matchkeys/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", f"/meta-storage/config/matchkeys/{id_}")

		
    def putconfigmatchkey(self, matchKey, id_):
        """Update match key configuration.

        ``PUT /meta-storage/config/matchkeys/{id}``

        Args:
            matchKey (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_putconfigmatchkey_request.schema
        """
        return self.call("PUT", f"/meta-storage/config/matchkeys/{id_}", matchKey)

    def initializematchkey(self, id_):
        """Recalculate match key across all records.

        ``PUT /meta-storage/config/matchkeys/{id}/initialize``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_initializematchkey_response.schema
        """
        return self.call("PUT", f"/meta-storage/config/matchkeys/{id_}/initialize")

    def statsmatchkey(self, id_):
        """Get statistics for match key configuration

        ``GET /meta-storage/config/matchkeys/{id}/stats``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_statsmatchkey_response.schema
        """
        return self.call("GET", f"/meta-storage/config/matchkeys/{id_}/stats")

    def postcodemodule(self, codeModule):
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

            .. literalinclude:: ../files/Metastorage_postcodemodule_request.schema
        """
        return self.call("POST", f"/meta-storage/config/modules", codeModule)

		
    def getcodemodules(self, **kwargs):
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

            .. literalinclude:: ../files/Metastorage_getcodemodules_response.schema
        """
        return self.call("GET", "/meta-storage/config/modules", query=kwargs)

    def getcodemodule(self, id_):
        """Retrieve a code module by id

        ``GET /meta-storage/config/modules/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getcodemodule_response.schema
        """
        return self.call("GET", f"/meta-storage/config/modules/{id_}")

		
    def putcodemodule(self, codeModule, id_):
        """Update code module by id

        ``PUT /meta-storage/config/modules/{id}``

        Args:
            codeModule (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_putcodemodule_request.schema
        """
        return self.call("PUT", f"/meta-storage/config/modules/{id_}", codeModule)

		
    def deletecodemodule(self, id_):
        """Delete code module by id

        ``DELETE /meta-storage/config/modules/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", f"/meta-storage/config/modules/{id_}")

    def reloadcodemodule(self, id_):
        """Force module to be reloaded

        ``PUT /meta-storage/config/modules/{id}/reload``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("PUT", f"/meta-storage/config/modules/{id_}/reload")

    def postsource(self, source):
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

            .. literalinclude:: ../files/Metastorage_postsource_request.schema
        """
        return self.call("POST", f"/meta-storage/sources", source)

		
    def getsources(self, **kwargs):
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

            .. literalinclude:: ../files/Metastorage_getsources_response.schema
        """
        return self.call("GET", "/meta-storage/sources", query=kwargs)

    def getsource(self, id_):
        """Get source.

        ``GET /meta-storage/config/sources/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getsource_response.schema
        """
        return self.call("GET", f"/meta-storage/config/sources/{id_}")

		
    def deletesource(self, id_):
        """Delete source.

        ``DELETE /meta-storage/config/sources/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", f"/meta-storage/config/sources/{id_}")

    def postingestjob(self, ingestJobRequest):
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

            .. literalinclude:: ../files/Metastorage_postingestjob_request.schema
        """
        return self.call("POST", f"/meta-storage/ingest-jobs", ingestJobRequest)

    def ingestjobrecord(self, ingestRecordChunk, id_):
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

            .. literalinclude:: ../files/Metastorage_ingestjobrecord_request.schema
            .. literalinclude:: ../files/Metastorage_ingestjobrecord_request.schema_response.schema
        """
        return self.call("PUT", f"/meta-storage/ingest-jobs/{id_}", ingestRecordChunk)

		
    def ingestjobinfo(self, id_):
        """Get ingest job information.

        ``GET /meta-storage/ingest-jobs/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_ingestjobinfo_response.schema
        """
        return self.call("GET", f"/meta-storage/ingest-jobs/{id_}")

		
    def ingestjobfinish(self, id_, **kwargs):
        """Finish ingest job with either rollback of commit.

        ``DELETE /meta-storage/ingest-jobs/{id}``

        Keyword Args:
            commit (bool): whether to commit (default: False)

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", f"/meta-storage/ingest-jobs/{id_}", query=kwargs)

    def getglobalrecords(self, **kwargs):
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

            .. literalinclude:: ../files/Metastorage_getglobalrecords_response.schema
        """
        return self.call("GET", "/meta-storage/records", query=kwargs)

		
    def putglobalrecords(self, ingestRecordRequest):
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

            .. literalinclude:: ../files/Metastorage_putglobalrecords_request.schema
            .. literalinclude:: ../files/Metastorage_putglobalrecords_request.schema_response.schema
        """
        return self.call("PUT", f"/meta-storage/records", ingestRecordRequest)

		
    def deleteglobalrecords(self, **kwargs):
        """Delete global records.

        ``DELETE /meta-storage/records``

        Keyword Args:
            query (str): CQL query

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/meta-storage/records", query=kwargs)

    def getglobalrecord(self, globalId):
        """Get record with global identifier.

        ``GET /meta-storage/records/{globalId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getglobalrecord_response.schema
        """
        return self.call("GET", f"/meta-storage/records/{globalId}")

    def getclusters(self):
        """Get clusters with matchkeyid. CQL query with matchValue, clusterId fields

        ``GET /meta-storage/clusters``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getclusters_response.schema
        """
        return self.call("GET", "/meta-storage/clusters")

    def getcluster(self, clusterId):
        """Get cluster by identifier

        ``GET /meta-storage/clusters/{clusterId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getcluster_response.schema
        """
        return self.call("GET", f"/meta-storage/clusters/{clusterId}")

    def oaiservice(self):
        """OAI service

        ``GET /meta-storage/oai``

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error
        """
        return self.call("GET", "/meta-storage/oai")

    def postoaipmhclient(self, oai_pmh_client):
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

            .. literalinclude:: ../files/Metastorage_postoaipmhclient_request.schema
        """
        return self.call("POST", f"/meta-storage/pmh-clients", oai_pmh_client)

		
    def getcollectionoaipmhclient(self):
        """Get all OAI PMH client jobs

        ``GET /meta-storage/pmh-clients``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getcollectionoaipmhclient_response.schema
        """
        return self.call("GET", "/meta-storage/pmh-clients")

    def getoaipmhclient(self, id_):
        """Get OAI-PMH client

        ``GET /meta-storage/pmh-clients/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_getoaipmhclient_response.schema
        """
        return self.call("GET", f"/meta-storage/pmh-clients/{id_}")

		
    def putoaipmhclient(self, oai_pmh_client, id_):
        """Update OAI-PMH client

        ``PUT /meta-storage/pmh-clients/{id}``

        Args:
            oai-pmh-client (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_putoaipmhclient_request.schema
        """
        return self.call("PUT", f"/meta-storage/pmh-clients/{id_}", oai_pmh_client)

		
    def deleteoaipmhclient(self, id_):
        """Delete OAI-PMH client

        ``DELETE /meta-storage/pmh-clients/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_deleteoaipmhclient_response.schema
        """
        return self.call("DELETE", f"/meta-storage/pmh-clients/{id_}")

    def startoaipmhclient(self, id_):
        """Start OAI PMH client job

        ``POST /meta-storage/pmh-clients/{id}/start``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("POST", f"/meta-storage/pmh-clients/{id_}/start")

    def stopoaipmhclient(self, id_):
        """Stop OAI PMH client job

        ``POST /meta-storage/pmh-clients/{id}/stop``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("POST", f"/meta-storage/pmh-clients/{id_}/stop")

    def statusoaipmhclient(self, id_):
        """Get OAI PMH client status

        ``GET /meta-storage/pmh-clients/{id}/status``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Metastorage_statusoaipmhclient_response.schema
        """
        return self.call("GET", f"/meta-storage/pmh-clients/{id_}/status")
