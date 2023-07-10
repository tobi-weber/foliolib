# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.dataExportSpring")



class Jobs(FolioApi):
    """Data Export Spring Jobs

    
    """

    def getjobs(self, **kwargs):
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

            .. literalinclude:: ../files/Jobs_getjobs_response.schema
        """
        return self.call("GET", "/data-export-spring/jobs", query=kwargs)

		
    def upsertjob(self, job):
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

            .. literalinclude:: ../files/Jobs_upsertjob_request.schema
        """
        return self.call("POST", f"/data-export-spring/jobs", job)

    def getjobbyid(self, id_):
        """Get a job by the job ID

        ``GET /data-export-spring/jobs/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter. Details of the errors (e.g. name of the parameter or line/character number with malformed data) provided in the response.
            OkapiRequestNotFound: Job with a given ID not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Jobs_getjobbyid_response.schema
        """
        return self.call("GET", f"/data-export-spring/jobs/{id_}")

    def resendexportedfile(self, id_):
        """resend exported file by the job ID

        ``POST /data-export-spring/jobs/{id}/resend``

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: ExportFile with a given Job ID not found
            OkapiFatalError: Internal server errors
        """
        return self.call("POST", f"/data-export-spring/jobs/{id_}/resend")

    def downloadexportedfilebyjobid(self, id_):
        """Download exported file by the job ID

        ``GET /data-export-spring/jobs/{id}/download``
        """
        return self.call("GET", f"/data-export-spring/jobs/{id_}/download")



class Exportconfigs(FolioApi):
    """Data Export Spring Configurations

    
    """

    def getexportconfigs(self, **kwargs):
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

            .. literalinclude:: ../files/Exportconfigs_getexportconfigs_response.schema
        """
        return self.call("GET", "/data-export-spring/configs", query=kwargs)

		
    def postexportconfig(self, exportConfig):
        """Add an export configuration

        ``POST /data-export-spring/configs``

        Args:
            exportConfig (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Exportconfigs_postexportconfig_request.schema
        """
        return self.call("POST", f"/data-export-spring/configs", exportConfig)

    def getconfigbyid(self, id_):
        """Get a export configuration by the export configuration ID

        ``GET /data-export-spring/configs/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request, e.g. malformed request body or query parameter. Details of the errors (e.g. name of the parameter or line/character number with malformed data) provided in the response.
            OkapiRequestNotFound: Export configuration with a given ID not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Exportconfigs_getconfigbyid_response.schema
        """
        return self.call("GET", f"/data-export-spring/configs/{id_}")

		
    def putexportconfig(self, exportConfig, id_):
        """Change an export configuration

        ``PUT /data-export-spring/configs/{id}``

        Args:
            exportConfig (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Export config not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration

        Schema:

            .. literalinclude:: ../files/Exportconfigs_putexportconfig_request.schema
        """
        return self.call("PUT", f"/data-export-spring/configs/{id_}", exportConfig)

		
    def deleteexportconfigbyid(self, id_):
        """Delete export configuration by UUID

        ``DELETE /data-export-spring/configs/{id}``

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Export config not found
            OkapiFatalError: Internal server errors, e.g. due to misconfiguration
        """
        return self.call("DELETE", f"/data-export-spring/configs/{id_}")
