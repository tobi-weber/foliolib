# -*- coding: utf-8 -*-
# Generated at 2022-05-05

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.search")



class Search(FolioApi):
    """Search API

    Search API
    """

    def searchInstances(self, **kwargs):
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

            .. literalinclude:: ../files/Search_searchInstances_response.schema
        """
        return self.call("GET", "/search/instances", query=kwargs)

    def getInstanceIds(self, **kwargs):
        """Get a list of instance ids for CQL query

        ``GET /search/instances/ids``

        Keyword Args:
            query (str): A CQL query string with search conditions.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException
        """
        return self.call("GET", "/search/instances/ids", query=kwargs)

    def getHoldingIds(self, **kwargs):
        """Get a list of holding ids linked to instances found by the CQL query

        ``GET /search/holdings/ids``

        Keyword Args:
            query (str): A CQL query string with search conditions.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException
        """
        return self.call("GET", "/search/holdings/ids", query=kwargs)

    def getFacets(self, recordType, **kwargs):
        """Provides list of facets for the record type

        ``GET /search/{recordType}/facets``

        Args:
            recordType (str):  (enum: ['instances', 'authorities'])

        Keyword Args:
            query (str): A CQL query string with search conditions.
            facet (list): List of facet names. (items: (type: string))

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_getFacets_response.schema
        """
        return self.call("GET", "/search/{recordType}/facets", recordType, query=kwargs)

    def searchAuthorities(self, **kwargs):
        """Get a list of authorities for CQL query

        ``GET /search/authorities``

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

            .. literalinclude:: ../files/Search_searchAuthorities_response.schema
        """
        return self.call("GET", "/search/authorities", query=kwargs)

    def getAuthoritiesIdsJob(self, jobId):
        """Get a job for the stream of authority ids.

        ``GET /search/authorities/ids/jobs/{jobId}``

        Args:
            jobId (str): UUID of the job to get

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_getAuthoritiesIdsJob_response.schema
        """
        return self.call("GET", "/search/authorities/ids/jobs/{jobId}", jobId)

    def submitAuthoritiesIdsJob(self, resourceIdsJob):
        """Creates a job for the stream of authority ids.

        ``POST /search/authorities/ids/jobs``

        Args:
            resourceIdsJob (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_submitAuthoritiesIdsJob_request.schema
        """
        return self.call("POST", "/search/authorities/ids/jobs", resourceIdsJob)

    def getAuthorityIds(self, **kwargs):
        """Get a list of authority ids for CQL query

        ``GET /search/authorities/ids``

        Keyword Args:
            query (str): A CQL query string with search conditions.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException
        """
        return self.call("GET", "/search/authorities/ids", query=kwargs)

    def browseInstancesByCallNumber(self, **kwargs):
        """Provides list of instances for browsing by call number

        ``GET /search/browse/call-numbers/instances``

        Keyword Args:
            query (str): A CQL query string with search conditions.
            limit (int): Limit the number of elements returned in the browse response. (minimum: 0, maximum: 100, default: 100)
            expandAll (bool): Whether to return only basic properties or entire instance. (default: False)
            highlightMatch (bool): Whether to highlight matched resource by query input or not. (default: True)
            precedingRecordsCount (int): Number of preceding records for browsing around and around-including options (minimum: 1, maximum: 100)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_browseInstancesByCallNumber_response.schema
        """
        return self.call("GET", "/search/browse/call-numbers/instances", query=kwargs)

    def browseInstancesBySubject(self, **kwargs):
        """Provides list of instances for browsing by subject

        ``GET /search/browse/subjects/instances``

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

            .. literalinclude:: ../files/Search_browseInstancesBySubject_response.schema
        """
        return self.call("GET", "/search/browse/subjects/instances", query=kwargs)

    def browseAuthorities(self, **kwargs):
        """Provides list of authorities by headingRef

        ``GET /search/browse/authorities``

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

            .. literalinclude:: ../files/Search_browseAuthorities_response.schema
        """
        return self.call("GET", "/search/browse/authorities", query=kwargs)

    def createIndices(self, createIndexRequest):
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

            .. literalinclude:: ../files/Search_createIndices_request.schema
            .. literalinclude:: ../files/Search_createIndices_request.schema_response.schema
        """
        return self.call("POST", "/search/index/indices", createIndexRequest)

    def updateMappings(self, updateMappingsRequest):
        """Creates mappings for passed resource name and tenant id in request header.

        ``POST /search/index/mappings``

        Args:
            updateMappingsRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_updateMappings_request.schema
            .. literalinclude:: ../files/Search_updateMappings_request.schema_response.schema
        """
        return self.call("POST", "/search/index/mappings", updateMappingsRequest)

    def reindexInventoryRecords(self, reindexRequest):
        """Initiates reindex for the inventory records

        ``POST /search/index/inventory/reindex``

        Args:
            reindexRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_reindexInventoryRecords_request.schema
            .. literalinclude:: ../files/Search_reindexInventoryRecords_request.schema_response.schema
        """
        return self.call("POST", "/search/index/inventory/reindex", reindexRequest)


class SearchAdmin(FolioAdminApi):
    """Search API
    Administration

    Search API
    """

    def indexRecords(self, indexRecordRequest):
        """Indexes the records into elasticsearch.

        ``POST /search/index/records``

        Args:
            indexRecordRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Search_indexRecords_request.schema
            .. literalinclude:: ../files/Search_indexRecords_request.schema_response.schema
        """
        return self.call("POST", "/search/index/records", indexRecordRequest)

    def createLanguageConfig(self, languageConfig):
        """Save languages that will be used for analyzers

        ``POST /search/config/languages``

        Args:
            languageConfig (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestUnprocessableEntity: Validation error for the request.

        Schema:

            .. literalinclude:: ../files/Search_createLanguageConfig_request.schema
        """
        return self.call("POST", "/search/config/languages", languageConfig)

		
    def getAllLanguageConfigs(self):
        """Get all supported languages

        ``GET /search/config/languages``

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/Search_getAllLanguageConfigs_response.schema
        """
        return self.call("GET", "/search/config/languages")

    def updateLanguageConfig(self, code, languageConfig):
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

            .. literalinclude:: ../files/Search_updateLanguageConfig_request.schema
        """
        return self.call("PUT", "/search/config/languages/{code}", code, languageConfig)

		
    def deleteLanguageConfig(self, code):
        """Delete all supported languages

        ``DELETE /search/config/languages/{code}``

        Args:
            code (str): Language code (pattern: [a-zA-Z]{3})

        Raises:
            OkapiRequestNotFound: No language support is found
        """
        return self.call("DELETE", "/search/config/languages/{code}", code)

    def saveFeatureConfiguration(self, featureConfig):
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

            .. literalinclude:: ../files/Search_saveFeatureConfiguration_request.schema
        """
        return self.call("POST", "/search/config/features", featureConfig)

		
    def getAllFeatures(self):
        """Get all feature configurations per tenant

        ``GET /search/config/features``

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/Search_getAllFeatures_response.schema
        """
        return self.call("GET", "/search/config/features")

    def updateFeatureConfiguration(self, featureId, featureConfig):
        """Update feature configuration settings

        ``PUT /search/config/features/{featureId}``

        Args:
            featureId (str): Feature id (name) (enum: ['search.all.fields', 'browse.cn.intermediate.values'])
            featureConfig (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiRequestUnprocessableEntity: Validation error for the request.

        Schema:

            .. literalinclude:: ../files/Search_updateFeatureConfiguration_request.schema
        """
        return self.call("PUT", "/search/config/features/{featureId}", featureId, featureConfig)

		
    def deleteFeatureConfigurationById(self, featureId):
        """Delete feature configuration by id

        ``DELETE /search/config/features/{featureId}``

        Args:
            featureId (str): Feature id (name) (enum: ['search.all.fields', 'browse.cn.intermediate.values'])

        Raises:
            OkapiRequestNotFound: No feature configuration is found by id
        """
        return self.call("DELETE", "/search/config/features/{featureId}", featureId)
