# -*- coding: utf-8 -*-
# Generated at 2020-11-29

import logging

from foliolib.folio import FolioApi

log = logging.getLogger("foliolib.folio.api.sourceRecordManager")


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
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - status=RUNNING
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

    def get_log(self, jobExecutionId: str):
        """

        ``GET /metadata-provider/logs/{jobExecutionId}``

        Args:
            jobExecutionId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/MetadataProvider_get_log_return.schema 
        """
        return self.call("GET", f"/metadata-provider/logs/{jobExecutionId}")

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


class ChangeManager(FolioApi):
    """Change Manager API

    API for accessing ChangeManager's bussiness logic
    """

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

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
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
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields: for example status=PARSING_IN_PROGRESS
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - status=PARSING_IN_PROGRESS
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

    def set_record(self, jobExecutionsId: str, record: dict, **kwargs):
        """Receive chunk of raw records

        ``POST /change-manager/jobExecutions/{jobExecutionsId}/records``

        Args:
            jobExecutionsId (str)
            record (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            defaultMapping (bool): (default=False) Boolean value which defines a mapping

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/ChangeManager_set_record_request.schema
        """
        return self.call("POST", f"/change-manager/jobExecutions/{jobExecutionsId}/records", data=record, query=kwargs)

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
        """Retrieve ParsedRecord by instanceId

        ``GET /change-manager/parsedRecords``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            instanceId (str (^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$):):  instanceId parameter

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


class ChangeManagerHandlers(FolioApi):
    """Source Record Manager event handlers API

    API for event handling
    """

    def set_createdInventoryInstance(self, createdInventoryInstance: dict):
        """

        ``POST /change-manager/handlers/created-inventory-instance``

        Args:
            createdInventoryInstance (dict): See Schema below

        Schema:

            .. literalinclude:: ../files/ChangeManagerHandlers_set_createdInventoryInstance_request.schema
        """
        return self.call("POST", "/change-manager/handlers/created-inventory-instance", data=createdInventoryInstance)

    def set_processingResult(self, processingResult: dict):
        """

        ``POST /change-manager/handlers/processing-result``

        Args:
            processingResult (dict): See Schema below

        Schema:

            .. literalinclude:: ../files/ChangeManagerHandlers_set_processingResult_request.schema
        """
        return self.call("POST", "/change-manager/handlers/processing-result", data=processingResult)

    def set_qmCompleted(self, qmCompleted: dict):
        """

        ``POST /change-manager/handlers/qm-completed``

        Args:
            qmCompleted (dict): See Schema below

        Schema:

            .. literalinclude:: ../files/ChangeManagerHandlers_set_qmCompleted_request.schema
        """
        return self.call("POST", "/change-manager/handlers/qm-completed", data=qmCompleted)

    def set_qmError(self, qmError: dict):
        """

        ``POST /change-manager/handlers/qm-error``

        Args:
            qmError (dict): See Schema below

        Schema:

            .. literalinclude:: ../files/ChangeManagerHandlers_set_qmError_request.schema
        """
        return self.call("POST", "/change-manager/handlers/qm-error", data=qmError)


class MappingRulesProvider(FolioApi):
    """Mapping rules Provider API

    API for accessing mapping rules
    """

    def get_mappingRules(self):
        """

        ``GET /mapping-rules``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/MappingRulesProvider_get_mappingRules_return.schema 
        """
        return self.call("GET", "/mapping-rules")

    def modify_mappingRule(self, mappingRule: dict):
        """

        ``PUT /mapping-rules``

        Args:
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
        return self.call("PUT", "/mapping-rules", data=mappingRule)

    def modify_restore(self):
        """

        ``PUT /mapping-rules/restore``

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/MappingRulesProvider_modify_restore_return.schema 
        """
        return self.call("PUT", "/mapping-rules/restore")
