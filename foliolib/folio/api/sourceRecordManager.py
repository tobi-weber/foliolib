# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.sourceRecordManager")


class MappingMetadataProvider(FolioApi):
    """Mapping Metadata Provider API

    API for accessing mapping rules and mapping parameters
    """

    def get_mappingMetadatum_for_jobExecution(self, jobExecutionId: str):
        """

        ``GET /mapping-metadata/{jobExecutionId}``

        Args:
            jobExecutionId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/MappingMetadataProvider_get_mappingMetadatum_for_jobExecution_return.schema 
        """
        return self.call("GET", f"/mapping-metadata/{jobExecutionId}")

    def get_mappingMetadatum(self, recordType: str):
        """

        ``GET /mapping-metadata/type/{recordType}``

        Args:
            recordType (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/MappingMetadataProvider_get_mappingMetadatum_return.schema 
        """
        return self.call("GET", f"/mapping-metadata/type/{recordType}")


class ChangeManager(FolioApi):
    """Change Manager API

    API for accessing ChangeManager's bussiness logic
    """

    def delete_jobExecutions(self, jobExecution: dict):
        """Delete JobExecution by multiple IDs

        ``DELETE /change-manager/jobExecutions``

        Args:
            jobExecution (dict): See Schema below

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/ChangeManager_delete_jobExecutions_request.schema
            .. literalinclude:: ../files/ChangeManager_delete_jobExecutions_return.schema 
        """
        return self.call("DELETE", "/change-manager/jobExecutions", data=jobExecution)

    def set_jobExecution(self, jobExecution: dict):
        """Initialize JobExecutions

        ``POST /change-manager/jobExecutions``

        Args:
            jobExecution (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ChangeManager_set_jobExecution_request.schema
            .. literalinclude:: ../files/ChangeManager_set_jobExecution_return.schema 
        """
        return self.call("POST", "/change-manager/jobExecutions", data=jobExecution)

    def get_jobExecution(self, jobExecutionsId: str):
        """Get JobExecution by id

        ``GET /change-manager/jobExecutions/{jobExecutionsId}``

        Args:
            jobExecutionsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ChangeManager_get_jobExecution_return.schema 
        """
        return self.call("GET", f"/change-manager/jobExecutions/{jobExecutionsId}")

    def delete_jobExecution(self, jobExecutionsId: str):
        """Delete jobExecution item with given {jobExecutionId}

        ``DELETE /change-manager/jobExecutions/{jobExecutionsId}``

        Args:
            jobExecutionsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/change-manager/jobExecutions/{jobExecutionsId}")

    def modify_jobExecution(self, jobExecutionsId: str, jobExecution: dict):
        """Update jobExecution item with given {jobExecutionId}

        ``PUT /change-manager/jobExecutions/{jobExecutionsId}``

        Args:
            jobExecutionsId (str)
            jobExecution (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/ChangeManager_modify_jobExecution_request.schema
        """
        return self.call("PUT", f"/change-manager/jobExecutions/{jobExecutionsId}", data=jobExecution)

    def get_children(self, jobExecutionsId: str, **kwargs):
        """Get children JobExecutions by parent id, by default returns all existing children JobExecutions, in order to limit the collection parameter limit should be explicitly specified

        ``GET /change-manager/jobExecutions/{jobExecutionsId}/children``

        Args:
            jobExecutionsId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/ChangeManager_get_children_return.schema 
        """
        return self.call("GET", f"/change-manager/jobExecutions/{jobExecutionsId}/children", query=kwargs)

    def modify_status(self, jobExecutionsId: str, status: dict):
        """Update JobExecution status

        ``PUT /change-manager/jobExecutions/{jobExecutionsId}/status``

        Args:
            jobExecutionsId (str)
            status (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/ChangeManager_modify_status_request.schema
            .. literalinclude:: ../files/ChangeManager_modify_status_return.schema 
        """
        return self.call("PUT", f"/change-manager/jobExecutions/{jobExecutionsId}/status", data=status)

    def modify_jobProfile(self, jobExecutionsId: str, jobProfile: dict):
        """Set JobProfile for JobExecution

        ``PUT /change-manager/jobExecutions/{jobExecutionsId}/jobProfile``

        Args:
            jobExecutionsId (str)
            jobProfile (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/ChangeManager_modify_jobProfile_request.schema
            .. literalinclude:: ../files/ChangeManager_modify_jobProfile_return.schema 
        """
        return self.call("PUT", f"/change-manager/jobExecutions/{jobExecutionsId}/jobProfile", data=jobProfile)

    def set_record(self, jobExecutionsId: str, record: dict):
        """Receive chunk of raw records

        ``POST /change-manager/jobExecutions/{jobExecutionsId}/records``

        Args:
            jobExecutionsId (str)
            record (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/ChangeManager_set_record_request.schema
        """
        return self.call("POST", f"/change-manager/jobExecutions/{jobExecutionsId}/records", data=record)

    def delete_record(self, jobExecutionsId: str):
        """Delete JobExecution and associated records in SRS

        ``DELETE /change-manager/jobExecutions/{jobExecutionsId}/records``

        Args:
            jobExecutionsId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/change-manager/jobExecutions/{jobExecutionsId}/records")

    def get_parsedRecords(self, **kwargs):
        """Retrieve ParsedRecord by externalId

        ``GET /change-manager/parsedRecords``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            externalId (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  externalId parameter

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ChangeManager_get_parsedRecords_return.schema 
        """
        return self.call("GET", "/change-manager/parsedRecords", query=kwargs)

    def modify_parsedRecord(self, parsedRecordsId: str, parsedRecord: dict):
        """

        ``PUT /change-manager/parsedRecords/{parsedRecordsId}``

        Args:
            parsedRecordsId (str)
            parsedRecord (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/ChangeManager_modify_parsedRecord_request.schema
        """
        return self.call("PUT", f"/change-manager/parsedRecords/{parsedRecordsId}", data=parsedRecord)


class MetadataProvider(FolioApi):
    """Metadata Provider API

    API for accessing metadata
    """

    def get_jobExecutions(self, **kwargs):
        """

        ``GET /metadata-provider/jobExecutions``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            statusAny (list):  JobExecution statuses to filter by
                    
                    Example:
                    
                     - ['COMMITTED', 'ERROR']
            profileIdNotAny (list):  Filter by specified job profile ids
                    
                    Example:
                    
                     - ['d0ebb7b0-2f0f-11eb-adc1-0242ac120002', '91f9b8d6-d80e-4727-9783-73fb53e3c786']
            statusNot (str):  Filter by status not equal to
                    
                    Example:
                    
                     - COMPLETED
            uiStatusAny (list):  JobExecution statuses to filter by
                    
                    Example:
                    
                     - ['READY_FOR_PREVIEW']
            hrId (str):  Filter by jobExecution hrid
                    
                    Example:
                    
                     - 123
            fileName (str):  Filter by jobExecution file name
                    
                    Example:
                    
                     - importBib1.bib
            fileNameNotAny (list):  Filter by specified file names
                    
                    Example:
                    
                     - ['No file name']
            profileIdAny (list):  Filter by specified job profile ids
                    
                    Example:
                    
                     - ['d0ebb7b0-2f0f-11eb-adc1-0242ac120002', '91f9b8d6-d80e-4727-9783-73fb53e3c786']
            userId (str):  Filter by user id
                    
                    Example:
                    
                     - d0ebb7b0-2f0f-11eb-adc1-0242ac120002
            completedAfter (datetime):  Start date to filter after, inclusive
            completedBefore (datetime):  End date to filter before, inclusive
            sortBy (list): (default=['completed_date,asc']) Sorting jobExecutions by field: completed_date, progress_total, file_name, status, job_profile_name, hrid, job_user_first_name, job_user_last_name
                    
                    Example:
                    
                     - ['completed_date,asc']
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/MetadataProvider_get_jobExecutions_return.schema 
        """
        return self.call("GET", "/metadata-provider/jobExecutions", query=kwargs)

    def get_journalRecords(self, jobExecutionId: str, **kwargs):
        """get journal records by job execution id

        ``GET /metadata-provider/journalRecords/{jobExecutionId}``

        Args:
            jobExecutionId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            sortBy (str):  sort criteria
                    
                    Example:
                    
                     - source_record_order, action_type, error
            order (str (asc|desc):): (default=asc) sort direction
                    
                    Example:
                    
                     - desc

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/MetadataProvider_get_journalRecords_return.schema 
        """
        return self.call("GET", f"/metadata-provider/journalRecords/{jobExecutionId}", query=kwargs)

    def get_jobLogEntries(self, jobExecutionId: str, **kwargs):
        """get journal records by job execution id

        ``GET /metadata-provider/jobLogEntries/{jobExecutionId}``

        Args:
            jobExecutionId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            sortBy (str): (default=source_record_order) sorting by field: source_record_order, title, source_record_action_status, instance_action_status, holdings_action_status, item_action_status, order_action_status, invoice_action_status, error
                    
                    Example:
                    
                     - source_record_order
            order (str (asc|desc):): (default=asc) sorting direction
                    
                    Example:
                    
                     - desc
            errorsOnly (bool): (default=False) Filter by occurrence of error field
                    
                    Example:
                    
                     - True
            entityType (str (MARC|INSTANCE|HOLDINGS|AUTHORITY|ITEM|ORDER|INVOICE|ALL):): (default=ALL) Filter by entity type: MARC, INSTANCE, HOLDINGS, AUTHORITY, ITEM, ORDER, INVOICE
                    
                    Example:
                    
                     - MARC
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request

        Schema:

            .. literalinclude:: ../files/MetadataProvider_get_jobLogEntries_return.schema 
        """
        return self.call("GET", f"/metadata-provider/jobLogEntries/{jobExecutionId}", query=kwargs)

    def get_record(self, jobExecutionId: str, recordId: str):
        """get record processing log dto by job execution id and record id (to get EDIFACT import log data a journal record id is expected)

        ``GET /metadata-provider/jobLogEntries/{jobExecutionId}/records/{recordId}``

        Args:
            jobExecutionId (str)
            recordId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/MetadataProvider_get_record_return.schema 
        """
        return self.call("GET", f"/metadata-provider/jobLogEntries/{jobExecutionId}/records/{recordId}")

    def get_jobSummary(self, jobExecutionId: str):
        """get summary result for import job

        ``GET /metadata-provider/jobSummary/{jobExecutionId}``

        Args:
            jobExecutionId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/MetadataProvider_get_jobSummary_return.schema 
        """
        return self.call("GET", f"/metadata-provider/jobSummary/{jobExecutionId}")

    def get_jobProfiles(self, **kwargs):
        """

        ``GET /metadata-provider/jobExecutions/jobProfiles``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/MetadataProvider_get_jobProfiles_return.schema 
        """
        return self.call("GET", "/metadata-provider/jobExecutions/jobProfiles", query=kwargs)

    def get_users(self, **kwargs):
        """get unique users for job JobExecutions

        ``GET /metadata-provider/jobExecutions/users``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/MetadataProvider_get_users_return.schema 
        """
        return self.call("GET", "/metadata-provider/jobExecutions/users", query=kwargs)


class MappingRulesProvider(FolioApi):
    """Mapping rules Provider API

    API for accessing mapping rules
    """

    def get_mappingRule(self, recordType: str):
        """

        ``GET /mapping-rules/{recordType}``

        Args:
            recordType (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/MappingRulesProvider_get_mappingRule_return.schema 
        """
        return self.call("GET", f"/mapping-rules/{recordType}")

    def modify_mappingRule(self, recordType: str, mappingRule: dict):
        """

        ``PUT /mapping-rules/{recordType}``

        Args:
            recordType (str)
            mappingRule (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/MappingRulesProvider_modify_mappingRule_request.schema
        """
        return self.call("PUT", f"/mapping-rules/{recordType}", data=mappingRule)

    def modify_restore(self, recordType: str):
        """

        ``PUT /mapping-rules/{recordType}/restore``

        Args:
            recordType (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/MappingRulesProvider_modify_restore_return.schema 
        """
        return self.call("PUT", f"/mapping-rules/{recordType}/restore")
