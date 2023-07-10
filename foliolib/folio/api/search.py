# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.search")



class Search(FolioApi):
    """Search API

    Search API
    """

    def searchinstances(self, **kwargs):
        """Get a list of instances for CQL query

        ``GET /search/instances``

        Keyword Args:
            query (str): A CQL query string with search conditions.
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 500, default: 100)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, maximum: 9999, default: 0)
            expandAll (bool): Whether to return only basic properties or entire instance. (default: False)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_searchinstances_response.schema
        """
        return self.call("GET", "/search/instances", query=kwargs)

    def getinstanceids(self, **kwargs):
        """Get a list of instance ids for CQL query

        ``GET /search/instances/ids``

        Keyword Args:
            query (str): A CQL query string with search conditions.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException
        """
        return self.call("GET", "/search/instances/ids", query=kwargs)

    def getholdingids(self, **kwargs):
        """Get a list of holding ids linked to instances found by the CQL query

        ``GET /search/holdings/ids``

        Keyword Args:
            query (str): A CQL query string with search conditions.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException
        """
        return self.call("GET", "/search/holdings/ids", query=kwargs)

    def getfacets(self, recordType, **kwargs):
        """Provides list of facets for the record type

        ``GET /search/{recordType}/facets``

        Args:
            recordType (str):  (enum: ['instances', 'authorities', 'contributors'])

        Keyword Args:
            query (str): A CQL query string with search conditions.
            facet (list): List of facet names. (items: (type: string))

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_getfacets_response.schema
        """
        return self.call("GET", f"/search/{recordType}/facets", query=kwargs)

    def searchauthorities(self, **kwargs):
        """Get a list of authorities for CQL query

        ``GET /search/authorities``

        Keyword Args:
            query (str): A CQL query string with search conditions.
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 500, default: 100)
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, maximum: 9999, default: 0)
            expandAll (bool): Whether to return only basic properties or entire instance. (default: False)
            includeNumberOfTitles (bool): Whether to perform a search for a number of linked instances. (default: True)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_searchauthorities_response.schema
        """
        return self.call("GET", "/search/authorities", query=kwargs)

    def getidsjob(self, jobId):
        """Get a job for the stream of resource ids.

        ``GET /search/resources/jobs/{jobId}``

        Args:
            jobId (str): UUID of the job to get

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_getidsjob_response.schema
        """
        return self.call("GET", f"/search/resources/jobs/{jobId}")

    def submitidsjob(self, resourceIdsJob):
        """Creates a job for the stream of resource ids.

        ``POST /search/resources/jobs``

        Args:
            resourceIdsJob (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_submitidsjob_request.schema
        """
        return self.call("POST", f"/search/resources/jobs", resourceIdsJob)

    def getresourceids(self, jobId):
        """Get a list of resource ids by job id

        ``GET /search/resources/jobs/{jobId}/ids``

        Args:
            jobId (str): UUID of the job to get

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException
        """
        return self.call("GET", f"/search/resources/jobs/{jobId}/ids")

    def browseinstancesbycallnumber(self, **kwargs):
        """Provides list of instances for browsing by call number

        ``GET /browse/call-numbers/instances``

        Keyword Args:
            query (str): A CQL query string with search conditions.
            limit (int): Limit the number of elements returned in the browse response. (minimum: 0, maximum: 100, default: 100)
            expandAll (bool): Whether to return only basic properties or entire instance. (default: False)
            highlightMatch (bool): Whether to highlight matched resource by query input or not. (default: True)
            precedingRecordsCount (int): Number of preceding records for browsing around and around-including options (minimum: 1, maximum: 100)
            callNumberType (str): Type of call number (enum: ['lc', 'dewey', 'nlm', 'sudoc', 'other', 'local'])

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_browseinstancesbycallnumber_response.schema
        """
        return self.call("GET", "/browse/call-numbers/instances", query=kwargs)

    def browseinstancesbysubject(self, **kwargs):
        """Provides list of instances for browsing by subject

        ``GET /browse/subjects/instances``

        Keyword Args:
            query (str): A CQL query string with search conditions.
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 500, default: 100)
            highlightMatch (bool): Whether to highlight matched resource by query input or not. (default: True)
            precedingRecordsCount (int): Number of preceding records for browsing around and around-including options (minimum: 1, maximum: 100)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_browseinstancesbysubject_response.schema
        """
        return self.call("GET", "/browse/subjects/instances", query=kwargs)

    def browseinstancesbycontributor(self, **kwargs):
        """Provides list of instances for browsing by contributor

        ``GET /browse/contributors/instances``

        Keyword Args:
            query (str): A CQL query string with search conditions.
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 500, default: 100)
            highlightMatch (bool): Whether to highlight matched resource by query input or not. (default: True)
            precedingRecordsCount (int): Number of preceding records for browsing around and around-including options (minimum: 1, maximum: 100)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_browseinstancesbycontributor_response.schema
        """
        return self.call("GET", "/browse/contributors/instances", query=kwargs)

    def browseauthorities(self, **kwargs):
        """Provides list of authorities by headingRef

        ``GET /browse/authorities``

        Keyword Args:
            query (str): A CQL query string with search conditions.
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 500, default: 100)
            expandAll (bool): Whether to return only basic properties or entire instance. (default: False)
            highlightMatch (bool): Whether to highlight matched resource by query input or not. (default: True)
            precedingRecordsCount (int): Number of preceding records for browsing around and around-including options (minimum: 1, maximum: 100)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_browseauthorities_response.schema
        """
        return self.call("GET", "/browse/authorities", query=kwargs)

    def createindices(self, createIndexRequest):
        """Creates indices for passed resource name and tenant id in request header.

        ``POST /search/index/indices``

        Args:
            createIndexRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_createindices_request.schema
            .. literalinclude:: ../files/Search_createindices_request.schema_response.schema
        """
        return self.call("POST", f"/search/index/indices", createIndexRequest)

    def updatemappings(self, updateMappingsRequest):
        """Creates mappings for passed resource name and tenant id in request header.

        ``POST /search/index/mappings``

        Args:
            updateMappingsRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_updatemappings_request.schema
            .. literalinclude:: ../files/Search_updatemappings_request.schema_response.schema
        """
        return self.call("POST", f"/search/index/mappings", updateMappingsRequest)

    def updateindexdynamicsettings(self, updateIndexDynamicSettingsRequest):
        """Update Index Dynamic Settings data.

        ``PUT /search/index/settings``

        Args:
            updateIndexDynamicSettingsRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_updateindexdynamicsettings_request.schema
            .. literalinclude:: ../files/Search_updateindexdynamicsettings_request.schema_response.schema
        """
        return self.call("PUT", f"/search/index/settings", updateIndexDynamicSettingsRequest)

    def reindexinventoryrecords(self, reindexRequest):
        """Initiates reindex for the inventory records

        ``POST /search/index/inventory/reindex``

        Args:
            reindexRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_reindexinventoryrecords_request.schema
            .. literalinclude:: ../files/Search_reindexinventoryrecords_request.schema_response.schema
        """
        return self.call("POST", f"/search/index/inventory/reindex", reindexRequest)


class SearchAdmin(FolioAdminApi):
    """Search API
    Administration

    Search API
    """

    def indexrecords(self, indexRecordRequest):
        """Indexes the records into elasticsearch.

        ``POST /search/index/records``

        Args:
            indexRecordRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_indexrecords_request.schema
            .. literalinclude:: ../files/Search_indexrecords_request.schema_response.schema
        """
        return self.call("POST", f"/search/index/records", indexRecordRequest)

    def createlanguageconfig(self, languageConfig):
        """Save languages that will be used for analyzers

        ``POST /search/config/languages``

        Args:
            languageConfig (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestUnprocessableEntity: Validation error for the request.

        Schema:

            .. literalinclude:: ../files/Search_createlanguageconfig_request.schema
        """
        return self.call("POST", f"/search/config/languages", languageConfig)

		
    def getalllanguageconfigs(self):
        """Get all supported languages

        ``GET /search/config/languages``

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/Search_getalllanguageconfigs_response.schema
        """
        return self.call("GET", "/search/config/languages")

    def updatelanguageconfig(self, code, languageConfig):
        """Update language config settings

        ``PUT /search/config/languages/{code}``

        Args:
            code (str): Language code (pattern: [a-zA-Z]{3})
            languageConfig (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestUnprocessableEntity: Validation error for the request.

        Schema:

            .. literalinclude:: ../files/Search_updatelanguageconfig_request.schema
        """
        return self.call("PUT", f"/search/config/languages/{code}", languageConfig)

		
    def deletelanguageconfig(self, code):
        """Delete all supported languages

        ``DELETE /search/config/languages/{code}``

        Args:
            code (str): Language code (pattern: [a-zA-Z]{3})

        Raises:
            OkapiRequestNotFound: No language support is found
        """
        return self.call("DELETE", f"/search/config/languages/{code}")

    def savefeatureconfiguration(self, featureConfig):
        """Save feature configuration (enables or disables pre-defined optional search options)

        ``POST /search/config/features``

        Args:
            featureConfig (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiRequestUnprocessableEntity: Validation error for the request.

        Schema:

            .. literalinclude:: ../files/Search_savefeatureconfiguration_request.schema
        """
        return self.call("POST", f"/search/config/features", featureConfig)

		
    def getallfeatures(self):
        """Get all feature configurations per tenant

        ``GET /search/config/features``

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/Search_getallfeatures_response.schema
        """
        return self.call("GET", "/search/config/features")

    def updatefeatureconfiguration(self, featureId, featureConfig):
        """Update feature configuration settings

        ``PUT /search/config/features/{featureId}``

        Args:
            featureId (str): Feature id (name) (enum: ['search.all.fields', 'browse.cn.intermediate.values', 'browse.cn.intermediate.remove.duplicates'])
            featureConfig (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiRequestUnprocessableEntity: Validation error for the request.

        Schema:

            .. literalinclude:: ../files/Search_updatefeatureconfiguration_request.schema
        """
        return self.call("PUT", f"/search/config/features/{featureId}", featureConfig)

		
    def deletefeatureconfigurationbyid(self, featureId):
        """Delete feature configuration by id

        ``DELETE /search/config/features/{featureId}``

        Args:
            featureId (str): Feature id (name) (enum: ['search.all.fields', 'browse.cn.intermediate.values', 'browse.cn.intermediate.remove.duplicates'])

        Raises:
            OkapiRequestNotFound: No feature configuration is found by id
        """
        return self.call("DELETE", f"/search/config/features/{featureId}")
