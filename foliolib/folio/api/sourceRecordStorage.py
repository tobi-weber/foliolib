# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.sourceRecordStorage")


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
            externalId (str):  Filter by external entity Id
                    
                    Example:
                    
                     - 8b07da70-8ea7-4acd-83a0-44d83979c73b
            externalHrid (str):  Filter by external entity Hrid
                    
                    Example:
                    
                     - 12345
            instanceId (str):  Filter by Instance Id
                    
                    Example:
                    
                     - 8b07da70-8ea7-4acd-83a0-44d83979c73b
            instanceHrid (str):  Filter by Instance Hrid
                    
                    Example:
                    
                     - 12345
            holdingsId (str):  Filter by Holdings Id
                    
                    Example:
                    
                     - 8b07da70-8ea7-4acd-83a0-44d83979c73b
            holdingsHrid (str):  Filter by Holdings Hrid
                    
                    Example:
                    
                     - 12345
            recordType (str): (default=MARC_BIB) Filter by Record Type
                    
                    Example:
                    
                     - MARC_BIB
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
            recordType (str): (default=MARC_BIB) Filter by Record Type
                    
                    Example:
                    
                     - MARC_BIB
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
            state (str): (default=ACTUAL) State of the looking record
                    
                    Example:
                    
                     - DELETED

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


class SourceRecordStorageBatch(FolioApi):
    """Source Record Storage Batch API

    Batch API for managing records
    """

    def set_verifiedRecord(self, verifiedRecord: dict):
        """Get a list of invalid Marc Bib Record IDs, which doesn't exists in the system

        ``POST /source-storage/batch/verified-records``

        Args:
            verifiedRecord (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageBatch_set_verifiedRecord_request.schema
            .. literalinclude:: ../files/SourceRecordStorageBatch_set_verifiedRecord_return.schema 
        """
        return self.call("POST", "/source-storage/batch/verified-records", data=verifiedRecord)

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

    def set_fetch(self, fetch: dict):
        """Fetch exact fields of parsed records by external IDs.

        ``POST /source-storage/batch/parsed-records/fetch``

        Args:
            fetch (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageBatch_set_fetch_request.schema
            .. literalinclude:: ../files/SourceRecordStorageBatch_set_fetch_return.schema 
        """
        return self.call("POST", "/source-storage/batch/parsed-records/fetch", data=fetch)


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


class SourceRecordStorageStream(FolioApi):
    """Source Record Storage Stream API

    Streaming API for searching records
    """

    def get_records(self, **kwargs):
        """Stream collection of records; including raw record, parsed record, and error record if applicable

        ``GET /source-storage/stream/records``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            snapshotId (str):  Filter by Snapshot Id
                    
                    Example:
                    
                     - e5ddbbdc-90b3-498f-bb8f-49367ca4c142
            recordType (str): (default=MARC_BIB) Filter by Record Type
                    
                    Example:
                    
                     - MARC_BIB
            state (str):  Filter by State
                    
                    Example:
                    
                     - ACTUAL
            orderBy (list):  Sort Records
                    
                    Example:
                    
                     - ['order,ASC']
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("GET", "/source-storage/stream/records", query=kwargs)

    def get_sourceRecords(self, **kwargs):
        """Stream collection of source records; including only latest generation and parsed record

        ``GET /source-storage/stream/source-records``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            recordId (str):  Filter by Record Id
                    
                    Example:
                    
                     - 876270bc-fbb4-409d-b8b0-3f59b1cb61f2
            snapshotId (str):  Filter by Snapshot Id
                    
                    Example:
                    
                     - 7a8fbd77-5b2a-496c-93e7-cd04478f4fcc
            externalId (str):  Filter by external entity Id
                    
                    Example:
                    
                     - 8b07da70-8ea7-4acd-83a0-44d83979c73b
            externalHrid (str):  Filter by external entity Hrid
                    
                    Example:
                    
                     - 12345
            instanceId (str):  Filter by Instance Id
                    
                    Example:
                    
                     - 8b07da70-8ea7-4acd-83a0-44d83979c73b
            instanceHrid (str):  Filter by Instance Hrid
                    
                    Example:
                    
                     - 12345
            holdingsId (str):  Filter by Holdings Id
                    
                    Example:
                    
                     - 8b07da70-8ea7-4acd-83a0-44d83979c73b
            holdingsHrid (str):  Filter by Holdings Hrid
                    
                    Example:
                    
                     - 12345
            recordType (str): (default=MARC_BIB) Filter by Record Type
                    
                    Example:
                    
                     - MARC_BIB
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
            totalRecords (str): (default=auto) How to calculate the totalRecords property. "exact" for the correct number, "estimated" for an estimation, "auto" to automatically select "exact" or "estimated", "none" for suppressing the totalRecords property. For details see https://github.com/folio-org/raml-module-builder#estimated-totalrecords
                    
                    Example:
                    
                     - none
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("GET", "/source-storage/stream/source-records", query=kwargs)

    def set_marcRecordIdentifier(self, marcRecordIdentifier: dict):
        """Get a list of Marc Record IDs using post method

        ``POST /source-storage/stream/marc-record-identifiers``

        Args:
            marcRecordIdentifier (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageStream_set_marcRecordIdentifier_request.schema
        """
        return self.call("POST", "/source-storage/stream/marc-record-identifiers", data=marcRecordIdentifier)


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

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
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


class SourceRecordStorageMigrationsJobs(FolioApi):
    """Source Record Storage Migration Jobs API

    API for managing asynchronous migration jobs
    """

    def set_job(self, job: dict):
        """Initiate a migration job

        ``POST /source-storage/migrations/jobs``

        Args:
            job (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageMigrationsJobs_set_job_request.schema
            .. literalinclude:: ../files/SourceRecordStorageMigrationsJobs_set_job_return.schema 
        """
        return self.call("POST", "/source-storage/migrations/jobs", data=job)

    def get_job(self, jobsId: str):
        """Get a migration job

        ``GET /source-storage/migrations/jobs/{jobsId}``

        Args:
            jobsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageMigrationsJobs_get_job_return.schema 
        """
        return self.call("GET", f"/source-storage/migrations/jobs/{jobsId}")


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

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/SourceRecordStorageSnapshots_modify_snapshot_request.schema
        """
        return self.call("PUT", f"/source-storage/snapshots/{jobExecutionId}", data=snapshot)
