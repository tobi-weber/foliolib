# -*- coding: utf-8 -*-
# Generated at 2023-04-16

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.dataExportSpring")



class JobsAdmin(FolioAdminApi):
    """Data Export Spring Jobs
    Administration

    
    """

    def getJobs(self, **kwargs):
        """Get jobs fy filter

        ``GET /data-export-spring/jobs``

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query (default: 0, minimum: 0, maximum: 2147483647)
            limit (int): Limit the number of elements returned in the response (default: 10, minimum: 0, maximum: 2147483647)
            query (str): A query string to filter rules based on matching criteria in fields.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter. Details of the errors (e.g. name of the parameter or line/character number with malformed data) provided in the response.
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Jobs_getJobs_response.schema
        """
        return self.call("GET", "/data-export-spring/jobs", query=kwargs)

		
    def upsertJob(self, job):
        """Create or update a job

        ``POST /data-export-spring/jobs``

        Args:
            job (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Jobs_upsertJob_request.schema
        """
        return self.call("POST", "/data-export-spring/jobs", job)

    def getJobById(self, id_):
        """Get a job by the job ID

        ``GET /data-export-spring/jobs/{id}``

        Args:
            id_ (str): UUID of the job (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter. Details of the errors (e.g. name of the parameter or line/character number with malformed data) provided in the response.
            OkapiRequestNotFound: Job with a given ID not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Jobs_getJobById_response.schema
        """
        return self.call("GET", "/data-export-spring/jobs/{id}", id_)

    def resendExportedFile(self, id_):
        """resend exported file by the job ID

        ``POST /data-export-spring/jobs/{id}/resend``

        Args:
            id_ (str): UUID of the job (format: uuid)

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: ExportFile with a given Job ID not found
            OkapiFatalError: Internal server errors
        """
        return self.call("POST", "/data-export-spring/jobs/{id}/resend", id_)

    def downloadExportedFileByJobId(self, id_):
        """Download exported file by the job ID

        ``GET /data-export-spring/jobs/{id}/download``

        Args:
            id_ (str): UUID of the job (format: uuid)
        """
        return self.call("GET", "/data-export-spring/jobs/{id}/download", id_)



class ExportconfigsAdmin(FolioAdminApi):
    """Data Export Spring Configurations
    Administration

    
    """

    def getExportConfigs(self, **kwargs):
        """Get a list of data export configurations

        ``GET /data-export-spring/configs``

        Keyword Args:
            query (str): A query string to filter rules based on matching criteria in fields.
            limit (int): Limit the number of elements returned in the response (default: 10)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Exportconfigs_getExportConfigs_response.schema
        """
        return self.call("GET", "/data-export-spring/configs", query=kwargs)

		
    def postExportConfig(self, exportConfig):
        """Add an export configuration

        ``POST /data-export-spring/configs``

        Args:
            exportConfig (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Exportconfigs_postExportConfig_request.schema
        """
        return self.call("POST", "/data-export-spring/configs", exportConfig)

    def getConfigById(self, id_):
        """Get a export configuration by the export configuration ID

        ``GET /data-export-spring/configs/{id}``

        Args:
            id_ (str): UUID of the export configuration

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter. Details of the errors (e.g. name of the parameter or line/character number with malformed data) provided in the response.
            OkapiRequestNotFound: Export configuration with a given ID not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Exportconfigs_getConfigById_response.schema
        """
        return self.call("GET", "/data-export-spring/configs/{id}", id_)

		
    def putExportConfig(self, id_, exportConfig):
        """Change an export configuration

        ``PUT /data-export-spring/configs/{id}``

        Args:
            id_ (str): 
            exportConfig (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Export config not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Exportconfigs_putExportConfig_request.schema
        """
        return self.call("PUT", "/data-export-spring/configs/{id}", id_, exportConfig)

		
    def deleteExportConfigById(self, id_):
        """Delete export configuration by UUID

        ``DELETE /data-export-spring/configs/{id}``

        Args:
            id_ (str): 

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Export config not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration
        """
        return self.call("DELETE", "/data-export-spring/configs/{id}", id_)
