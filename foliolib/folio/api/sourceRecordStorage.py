# -*- coding: utf-8 -*-
# Generated at 2020-11-29

import logging

from foliolib.folio import FolioApi

log = logging.getLogger("foliolib.folio.api.sourceRecordStorage")


class SourceRecordStorageBatch(FolioApi):
    """Source Record Storage Batch API

    Batch API for managing records
    """

    def set_record(self, record: dict):
        """Creates records from a record collection. It returns both saved records and error messages for records that were not saved.

        ``POST /source-storage/batch/records``

        Args:
            record (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageBatch_set_record_request.schema
            .. literalinclude:: ../files/SourceRecordStorageBatch_set_record_return.schema 
        """
        return self.call("POST", "/source-storage/batch/records", data=record)

    def modify_parsedRecord(self, parsedRecord: dict):
        """Updates parsed records from a collection. It returns both updated records and error messages for records that were not updated.

        ``PUT /source-storage/batch/parsed-records``

        Args:
            parsedRecord (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageBatch_modify_parsedRecord_request.schema
            .. literalinclude:: ../files/SourceRecordStorageBatch_modify_parsedRecord_return.schema 
        """
        return self.call("PUT", "/source-storage/batch/parsed-records", data=parsedRecord)


class SourceRecordStorageSnapshots(FolioApi):
    """Source Record Storage Snapshot API

    API for managing snapshots
    """

    def get_snapshots(self, **kwargs):
        """Retrieve a list of snapshot items.

        ``GET /source-storage/snapshots``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            status (str):  Snapshot status to filter by
                    
                    Example:
                    
                     - NEW
            orderBy (list):  Sort Snapshots
                    
                    Example:
                    
                     - ['status,ASC', 'processingStartedDate,DESC']
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
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageSnapshots_get_snapshots_return.schema 
        """
        return self.call("GET", "/source-storage/snapshots", query=kwargs)

    def set_snapshot(self, snapshot: dict):
        """Create a new snapshot item.

        ``POST /source-storage/snapshots``

        Args:
            snapshot (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created snapshot item

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageSnapshots_set_snapshot_request.schema
        """
        return self.call("POST", "/source-storage/snapshots", data=snapshot)

    def get_snapshot(self, jobExecutionId: str):
        """Retrieve snapshot item with given {snapshotId}

        ``GET /source-storage/snapshots/{jobExecutionId}``

        Args:
            jobExecutionId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageSnapshots_get_snapshot_return.schema 
        """
        return self.call("GET", f"/source-storage/snapshots/{jobExecutionId}")

    def delete_snapshot(self, jobExecutionId: str):
        """Deletes snapshot and all related records

        ``DELETE /source-storage/snapshots/{jobExecutionId}``

        Args:
            jobExecutionId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/source-storage/snapshots/{jobExecutionId}")

    def modify_snapshot(self, jobExecutionId: str, snapshot: dict):
        """Update snapshot item with given {snapshotId}

        ``PUT /source-storage/snapshots/{jobExecutionId}``

        Args:
            jobExecutionId (str)
            snapshot (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageSnapshots_modify_snapshot_request.schema
        """
        return self.call("PUT", f"/source-storage/snapshots/{jobExecutionId}", data=snapshot)


class SourceRecordStorageTestRecords(FolioApi):
    """Source Record Storage Test Record API

    API for managing test records
    """

    def set_populateTestMarcRecord(self, populateTestMarcRecord: dict):
        """A non-production endpoint to populate MARC records for testing purposes. Available only in case deployment tenant parameter "loadSample" is set to true

        ``POST /source-storage/populate-test-marc-records``

        Args:
            populateTestMarcRecord (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageTestRecords_set_populateTestMarcRecord_request.schema
        """
        return self.call("POST", "/source-storage/populate-test-marc-records", data=populateTestMarcRecord)


class SourceRecordStorageSourceRecords(FolioApi):
    """Source Record Storage Source Record API

    API for fetching source records
    """

    def get_sourceRecords(self, **kwargs):
        """Get a list of Source Records

        ``GET /source-storage/source-records``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            recordId (str):  Filter by Record Id
                    
                    Example:
                    
                     - 876270bc-fbb4-409d-b8b0-3f59b1cb61f2
            snapshotId (str):  Filter by Snapshot Id
                    
                    Example:
                    
                     - 7a8fbd77-5b2a-496c-93e7-cd04478f4fcc
            instanceId (str):  Filter by Instance Id
                    
                    Example:
                    
                     - 8b07da70-8ea7-4acd-83a0-44d83979c73b
            instanceHrid (str):  Filter by Instance Hrid
                    
                    Example:
                    
                     - 12345
            recordType (str):  Filter by Record Type
                    
                    Example:
                    
                     - MARC
            suppressFromDiscovery (bool):  Filter by suppress from discovery
                    
                    Example:
                    
                     - True
            deleted (bool): (default=False) Filter by records with state ACTUAL OR state DELETED OR leader 05 status d, s, or x
                    
                    Example:
                    
                     - True
            leaderRecordStatus (str):  Filter by MARC leader 05 status
                    
                    Example:
                    
                     - n
            updatedAfter (datetime):  Start date to filter after, inclusive
            updatedBefore (datetime):  End date to filter before, inclusive
            orderBy (list):  Sort records
                    
                    Example:
                    
                     - ['order,ASC']
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
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageSourceRecords_get_sourceRecords_return.schema 
        """
        return self.call("GET", "/source-storage/source-records", query=kwargs)

    def set_sourceRecord(self, sourceRecord: dict, **kwargs):
        """Get a list of Source Records from list of ids

        ``POST /source-storage/source-records``

        Args:
            sourceRecord (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            idType (str): (default=RECORD) Type of id for Record lookup
                    
                    Example:
                    
                     - INSTANCE
            deleted (bool): (default=False) Filter by records with state ACTUAL OR state DELETED OR leader 05 status d, s, or x
                    
                    Example:
                    
                     - True

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageSourceRecords_set_sourceRecord_request.schema
            .. literalinclude:: ../files/SourceRecordStorageSourceRecords_set_sourceRecord_return.schema 
        """
        return self.call("POST", "/source-storage/source-records", data=sourceRecord, query=kwargs)

    def get_sourceRecord(self, sourceRecordsId: str, **kwargs):
        """selection condition of sourceRecords by which id will be searched record

        ``GET /source-storage/source-records/{sourceRecordsId}``

        Args:
            sourceRecordsId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            idType (str): (default=RECORD) Type of id for record lookup
                    
                    Example:
                    
                     - INSTANCE

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageSourceRecords_get_sourceRecord_return.schema 
        """
        return self.call("GET", f"/source-storage/source-records/{sourceRecordsId}", query=kwargs)


class SourceRecordStorageHandlers(FolioApi):
    """Source Record Storage Event Handlers API

    API for event handling
    """

    def set_dataImport(self, dataImport: dict):
        """

        ``POST /source-storage/handlers/data-import``

        Args:
            dataImport (dict): See Schema below

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageHandlers_set_dataImport_request.schema
        """
        return self.call("POST", "/source-storage/handlers/data-import", data=dataImport)

    def set_updatedRecord(self, updatedRecord: dict):
        """

        ``POST /source-storage/handlers/updated-record``

        Args:
            updatedRecord (dict): See Schema below

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageHandlers_set_updatedRecord_request.schema
        """
        return self.call("POST", "/source-storage/handlers/updated-record", data=updatedRecord)


class SourceRecordStorageRecords(FolioApi):
    """Source Record Storage Record API

    API for managing records
    """

    def get_records(self, **kwargs):
        """Retrieve a list of record items.

        ``GET /source-storage/records``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            snapshotId (str):  Filter by Snapshot Id
                    
                    Example:
                    
                     - e5ddbbdc-90b3-498f-bb8f-49367ca4c142
            state (str):  Filter by State
                    
                    Example:
                    
                     - ACTUAL
            orderBy (list):  Sort Records
                    
                    Example:
                    
                     - ['order,ASC']
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
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageRecords_get_records_return.schema 
        """
        return self.call("GET", "/source-storage/records", query=kwargs)

    def set_record(self, record: dict):
        """Create a new record item.

        ``POST /source-storage/records``

        Args:
            record (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created record item

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageRecords_set_record_request.schema
        """
        return self.call("POST", "/source-storage/records", data=record)

    def get_record(self, recordsId: str):
        """Retrieve record item with given {recordId}

        ``GET /source-storage/records/{recordsId}``

        Args:
            recordsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageRecords_get_record_return.schema 
        """
        return self.call("GET", f"/source-storage/records/{recordsId}")

    def delete_record(self, recordsId: str):
        """Delete record item with given {recordId}

        ``DELETE /source-storage/records/{recordsId}``

        Args:
            recordsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/source-storage/records/{recordsId}")

    def modify_record(self, recordsId: str, record: dict):
        """Update record item with given {recordId}

        ``PUT /source-storage/records/{recordsId}``

        Args:
            recordsId (str)
            record (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageRecords_modify_record_request.schema
        """
        return self.call("PUT", f"/source-storage/records/{recordsId}", data=record)

    def get_formatted_by_record(self, recordsId: str, **kwargs):
        """Get Record with formatted content

        ``GET /source-storage/records/{recordsId}/formatted``

        Args:
            recordsId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            idType (str): (default=RECORD) Type of Id for Record lookup
                    
                    Example:
                    
                     - INSTANCE

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageRecords_get_formatted_by_record_return.schema 
        """
        return self.call("GET", f"/source-storage/records/{recordsId}/formatted", query=kwargs)

    def modify_suppressFromDiscovery(self, recordsId: str, **kwargs):
        """Update Record suppress from discovery additional information

        ``PUT /source-storage/records/{recordsId}/suppress-from-discovery``

        Args:
            recordsId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            idType (str): (default=RECORD) Type of Id for Record lookup
                    
                    Example:
                    
                     - INSTANCE
            suppress (bool): (default=True) Whether to suppress or unsuppress from discovery
                    
                    Example:
                    
                     - False

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
        """
        return self.call("PUT", f"/source-storage/records/{recordsId}/suppress-from-discovery", query=kwargs)
