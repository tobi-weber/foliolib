# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.sharedIndex")



class Sharedindex(FolioApi):
    """Shared Index

    
    """

    def postconfigmatchkey(self, matchKey):
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

            .. literalinclude:: ../files/Sharedindex_postconfigmatchkey_request.schema
        """
        return self.call("POST", f"/shared-index/config/matchkeys", matchKey)

		
    def getconfigmatchkeys(self, **kwargs):
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

            .. literalinclude:: ../files/Sharedindex_getconfigmatchkeys_response.schema
        """
        return self.call("GET", "/shared-index/config/matchkeys", query=kwargs)

    def getconfigmatchkey(self, id_):
        """Get match key configuration

        ``GET /shared-index/config/matchkeys/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_getconfigmatchkey_response.schema
        """
        return self.call("GET", f"/shared-index/config/matchkeys/{id_}")

		
    def putconfigmatchkey(self, matchKey, id_):
        """Update match key configuration.

        ``PUT /shared-index/config/matchkeys/{id}``

        Args:
            matchKey (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_putconfigmatchkey_request.schema
        """
        return self.call("PUT", f"/shared-index/config/matchkeys/{id_}", matchKey)

		
    def deleteconfigmatchkey(self, id_):
        """Delete match key configuration

        ``DELETE /shared-index/config/matchkeys/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", f"/shared-index/config/matchkeys/{id_}")

    def initializematchkey(self, id_):
        """Recalculate match key across all records.

        ``PUT /shared-index/config/matchkeys/{id}/initialize``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_initializematchkey_response.schema
        """
        return self.call("PUT", f"/shared-index/config/matchkeys/{id_}/initialize")

    def postsource(self, source):
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

            .. literalinclude:: ../files/Sharedindex_postsource_request.schema
        """
        return self.call("POST", f"/shared-index/sources", source)

		
    def getsources(self, **kwargs):
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

            .. literalinclude:: ../files/Sharedindex_getsources_response.schema
        """
        return self.call("GET", "/shared-index/sources", query=kwargs)

    def getsource(self, id_):
        """Get source.

        ``GET /shared-index/config/sources/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_getsource_response.schema
        """
        return self.call("GET", f"/shared-index/config/sources/{id_}")

		
    def deletesource(self, id_):
        """Delete source.

        ``DELETE /shared-index/config/sources/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", f"/shared-index/config/sources/{id_}")

    def postingestjob(self, ingestJobRequest):
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

            .. literalinclude:: ../files/Sharedindex_postingestjob_request.schema
        """
        return self.call("POST", f"/shared-index/shared-index/ingest-jobs", ingestJobRequest)

    def ingestjobrecord(self, ingestRecordChunk, id_):
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

            .. literalinclude:: ../files/Sharedindex_ingestjobrecord_request.schema
            .. literalinclude:: ../files/Sharedindex_ingestjobrecord_request.schema_response.schema
        """
        return self.call("PUT", f"/shared-index/shared-index/ingest-jobs/{id_}", ingestRecordChunk)

		
    def ingestjobinfo(self, id_):
        """Get ingest job information.

        ``GET /shared-index/shared-index/ingest-jobs/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_ingestjobinfo_response.schema
        """
        return self.call("GET", f"/shared-index/shared-index/ingest-jobs/{id_}")

		
    def ingestjobfinish(self, id_, **kwargs):
        """Finish ingest job with either rollback of commit.

        ``DELETE /shared-index/shared-index/ingest-jobs/{id}``

        Keyword Args:
            commit (bool): whether to commit (default: False)

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", f"/shared-index/shared-index/ingest-jobs/{id_}", query=kwargs)

    def getglobalrecords(self):
        """Get records that satisfy CQL query with fields localId, sourceId, globalId.

        ``GET /shared-index/records``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_getglobalrecords_response.schema
        """
        return self.call("GET", "/shared-index/records")

		
    def putglobalrecords(self, ingestRecordRequest):
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

            .. literalinclude:: ../files/Sharedindex_putglobalrecords_request.schema
            .. literalinclude:: ../files/Sharedindex_putglobalrecords_request.schema_response.schema
        """
        return self.call("PUT", f"/shared-index/records", ingestRecordRequest)

		
    def deleteglobalrecords(self):
        """Delete global records.

        ``DELETE /shared-index/records``

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error
        """
        return self.call("DELETE", "/shared-index/records")

    def getglobalrecord(self, globalId):
        """Get record with global identifier.

        ``GET /shared-index/records/{globalId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_getglobalrecord_response.schema
        """
        return self.call("GET", f"/shared-index/records/{globalId}")

    def getclusters(self):
        """Get clusters with matchkeyid. CQL query with matchValue, clusterId fields

        ``GET /shared-index/clusters``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_getclusters_response.schema
        """
        return self.call("GET", "/shared-index/clusters")

    def getcluster(self, clusterId):
        """Get cluster by identifier

        ``GET /shared-index/clusters/{clusterId}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Sharedindex_getcluster_response.schema
        """
        return self.call("GET", f"/shared-index/clusters/{clusterId}")

    def oaiservice(self):
        """OAI service

        ``GET /shared-index/oai``

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error
        """
        return self.call("GET", "/shared-index/oai")
