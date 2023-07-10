# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.circulationStorage")


class RequestStorageBatch(FolioApi):
    """Batch Request Storage API

    **Batch request operations**
    """

    def set_request(self, request: dict):
        """

        ``POST /request-storage-batch/requests``

        Args:
            request (dict): See Schema below

        Raises:
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/RequestStorageBatch_set_request_request.schema
        """
        return self.call("POST", "/request-storage-batch/requests", data=request)


class TlrFeatureToggleJob(FolioApi):
    """TLR Feature Toggle Job API

    **Storage for TLR feature toggle job**
    """

    def get_tlrFeatureToggleJobs(self, **kwargs):
        """Retrieve a list of tlrFeatureToggleJob items.

        ``GET /tlr-feature-toggle-job-storage/tlr-feature-toggle-jobs``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    by using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - status="in-progress"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/TlrFeatureToggleJob_get_tlrFeatureToggleJobs_return.schema 
        """
        return self.call("GET", "/tlr-feature-toggle-job-storage/tlr-feature-toggle-jobs", query=kwargs)

    def set_tlrFeatureToggleJob(self, tlrFeatureToggleJob: dict):
        """Create a new tlrFeatureToggleJob item.

        ``POST /tlr-feature-toggle-job-storage/tlr-feature-toggle-jobs``

        Args:
            tlrFeatureToggleJob (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created tlrFeatureToggleJob item

        Schema:

            .. literalinclude:: ../files/TlrFeatureToggleJob_set_tlrFeatureToggleJob_request.schema
        """
        return self.call("POST", "/tlr-feature-toggle-job-storage/tlr-feature-toggle-jobs", data=tlrFeatureToggleJob)

    def get_tlrFeatureToggleJob(self, tlrFeatureToggleJobsId: str):
        """Checks status of TLR feature toggle job

        ``GET /tlr-feature-toggle-job-storage/tlr-feature-toggle-jobs/{tlrFeatureToggleJobsId}``

        Args:
            tlrFeatureToggleJobsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/TlrFeatureToggleJob_get_tlrFeatureToggleJob_return.schema 
        """
        return self.call("GET", f"/tlr-feature-toggle-job-storage/tlr-feature-toggle-jobs/{tlrFeatureToggleJobsId}")

    def delete_tlrFeatureToggleJob(self, tlrFeatureToggleJobsId: str, **kwargs):
        """Removes TLR feature toggle job

        ``DELETE /tlr-feature-toggle-job-storage/tlr-feature-toggle-jobs/{tlrFeatureToggleJobsId}``

        Args:
            tlrFeatureToggleJobsId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/tlr-feature-toggle-job-storage/tlr-feature-toggle-jobs/{tlrFeatureToggleJobsId}", query=kwargs)

    def modify_tlrFeatureToggleJob(self, tlrFeatureToggleJobsId: str, tlrFeatureToggleJob: dict):
        """Updates TLR feature toggle job

        ``PUT /tlr-feature-toggle-job-storage/tlr-feature-toggle-jobs/{tlrFeatureToggleJobsId}``

        Args:
            tlrFeatureToggleJobsId (str)
            tlrFeatureToggleJob (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/TlrFeatureToggleJob_modify_tlrFeatureToggleJob_request.schema
        """
        return self.call("PUT", f"/tlr-feature-toggle-job-storage/tlr-feature-toggle-jobs/{tlrFeatureToggleJobsId}", data=tlrFeatureToggleJob)

    def set_start(self):
        """

        ``POST /tlr-feature-toggle-job/start``
        """
        return self.call("POST", "/tlr-feature-toggle-job/start")


class RequestPolicyStorage(FolioApi):
    """Request Policy Storage API

    **Storage for request policies**
    """

    def get_requestPolicies(self, **kwargs):
        """Retrieve a list of requestPolicy items.

        ``GET /request-policy-storage/request-policies``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    searchable using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - id="cf23adf0-61ba-4887-bf82-956c4aae2260"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/RequestPolicyStorage_get_requestPolicies_return.schema 
        """
        return self.call("GET", "/request-policy-storage/request-policies", query=kwargs)

    def set_requestPolicy(self, requestPolicy: dict):
        """Create a new requestPolicy item.

        ``POST /request-policy-storage/request-policies``

        Args:
            requestPolicy (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created requestPolicy item

        Schema:

            .. literalinclude:: ../files/RequestPolicyStorage_set_requestPolicy_request.schema
        """
        return self.call("POST", "/request-policy-storage/request-policies", data=requestPolicy)

    def delete_requestPolicies(self):
        """

        ``DELETE /request-policy-storage/request-policies``
        """
        return self.call("DELETE", "/request-policy-storage/request-policies")

    def get_requestPolicy(self, requestPolicyId: str):
        """Retrieve requestPolicy item with given {requestPolicyId}

        ``GET /request-policy-storage/request-policies/{requestPolicyId}``

        Args:
            requestPolicyId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/RequestPolicyStorage_get_requestPolicy_return.schema 
        """
        return self.call("GET", f"/request-policy-storage/request-policies/{requestPolicyId}")

    def delete_requestPolicy(self, requestPolicyId: str):
        """Delete requestPolicy item with given {requestPolicyId}

        ``DELETE /request-policy-storage/request-policies/{requestPolicyId}``

        Args:
            requestPolicyId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/request-policy-storage/request-policies/{requestPolicyId}")

    def modify_requestPolicy(self, requestPolicyId: str, requestPolicy: dict):
        """Update requestPolicy item with given {requestPolicyId}

        ``PUT /request-policy-storage/request-policies/{requestPolicyId}``

        Args:
            requestPolicyId (str)
            requestPolicy (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/RequestPolicyStorage_modify_requestPolicy_request.schema
        """
        return self.call("PUT", f"/request-policy-storage/request-policies/{requestPolicyId}", data=requestPolicy)


class PatronActionSession(FolioApi):
    """Patron Action Session API

    **Storage for patron action sessions**
    """

    def get_patronActionSessions(self, **kwargs):
        """Retrieve a list of patronActionSession items.

        ``GET /patron-action-session-storage/patron-action-sessions``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    searchable using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name="undergrad*"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PatronActionSession_get_patronActionSessions_return.schema 
        """
        return self.call("GET", "/patron-action-session-storage/patron-action-sessions", query=kwargs)

    def set_patronActionSession(self, patronActionSession: dict):
        """Create a new patronActionSession item.

        ``POST /patron-action-session-storage/patron-action-sessions``

        Args:
            patronActionSession (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created patronActionSession item

        Schema:

            .. literalinclude:: ../files/PatronActionSession_set_patronActionSession_request.schema
        """
        return self.call("POST", "/patron-action-session-storage/patron-action-sessions", data=patronActionSession)

    def get_patronActionSession(self, patronSessionId: str):
        """Retrieve patronActionSession item with given {patronActionSessionId}

        ``GET /patron-action-session-storage/patron-action-sessions/{patronSessionId}``

        Args:
            patronSessionId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PatronActionSession_get_patronActionSession_return.schema 
        """
        return self.call("GET", f"/patron-action-session-storage/patron-action-sessions/{patronSessionId}")

    def delete_patronActionSession(self, patronSessionId: str):
        """Delete patronActionSession item with given {patronActionSessionId}

        ``DELETE /patron-action-session-storage/patron-action-sessions/{patronSessionId}``

        Args:
            patronSessionId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/patron-action-session-storage/patron-action-sessions/{patronSessionId}")

    def modify_patronActionSession(self, patronSessionId: str, patronActionSession: dict):
        """Update patronActionSession item with given {patronActionSessionId}

        ``PUT /patron-action-session-storage/patron-action-sessions/{patronSessionId}``

        Args:
            patronSessionId (str)
            patronActionSession (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/PatronActionSession_modify_patronActionSession_request.schema
        """
        return self.call("PUT", f"/patron-action-session-storage/patron-action-sessions/{patronSessionId}", data=patronActionSession)

    def get_expiredSessionPatronIds(self, **kwargs):
        """

        ``GET /patron-action-session-storage/expired-session-patron-ids``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            action_type (str):  Parameter to filter expired sessions by patron action type
            session_inactivity_time_limit (str):  This parameter defines time up to which all sessions are considered as expired. Conforms to the ISO 8601 date and time format
                    
                    Example:
                    
                     - 2018-11-29 13:23:36+00:00
            limit (int): (default=10) Limit the number of sessions returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/PatronActionSession_get_expiredSessionPatronIds_return.schema 
        """
        return self.call("GET", "/patron-action-session-storage/expired-session-patron-ids", query=kwargs)


class StaffSlips(FolioApi):
    """Staff Slips Storage API

    **Storage for staff slips**
    """

    def get_staffSlips(self, **kwargs):
        """Retrieve a list of staffSlip items.

        ``GET /staff-slips-storage/staff-slips``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    by using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - id="6406fd34-9ae3-46f8-aca3-bf07455635ea"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/StaffSlips_get_staffSlips_return.schema 
        """
        return self.call("GET", "/staff-slips-storage/staff-slips", query=kwargs)

    def set_staffSlip(self, staffSlip: dict):
        """Create a new staffSlip item.

        ``POST /staff-slips-storage/staff-slips``

        Args:
            staffSlip (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI to the created staffSlip item

        Schema:

            .. literalinclude:: ../files/StaffSlips_set_staffSlip_request.schema
        """
        return self.call("POST", "/staff-slips-storage/staff-slips", data=staffSlip)

    def delete_staffSlips(self):
        """

        ``DELETE /staff-slips-storage/staff-slips``
        """
        return self.call("DELETE", "/staff-slips-storage/staff-slips")

    def get_staffSlip(self, staffSlipId: str):
        """Retrieve staffSlip item with given {staffSlipId}

        ``GET /staff-slips-storage/staff-slips/{staffSlipId}``

        Args:
            staffSlipId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/StaffSlips_get_staffSlip_return.schema 
        """
        return self.call("GET", f"/staff-slips-storage/staff-slips/{staffSlipId}")

    def delete_staffSlip(self, staffSlipId: str):
        """Delete staffSlip item with given {staffSlipId}

        ``DELETE /staff-slips-storage/staff-slips/{staffSlipId}``

        Args:
            staffSlipId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/staff-slips-storage/staff-slips/{staffSlipId}")

    def modify_staffSlip(self, staffSlipId: str, staffSlip: dict):
        """Update staffSlip item with given {staffSlipId}

        ``PUT /staff-slips-storage/staff-slips/{staffSlipId}``

        Args:
            staffSlipId (str)
            staffSlip (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/StaffSlips_modify_staffSlip_request.schema
        """
        return self.call("PUT", f"/staff-slips-storage/staff-slips/{staffSlipId}", data=staffSlip)


class ScheduledNoticeStorage(FolioApi):
    """Scheduled Notice Storage API

    **Storage for scheduled notices**
    """

    def get_scheduledNotices(self, **kwargs):
        """Retrieve a list of scheduledNotice items.

        ``GET /scheduled-notice-storage/scheduled-notices``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - loanId=188522a4-a2df-4a48-ab3d-44b62daef27f

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ScheduledNoticeStorage_get_scheduledNotices_return.schema 
        """
        return self.call("GET", "/scheduled-notice-storage/scheduled-notices", query=kwargs)

    def set_scheduledNotice(self, scheduledNotice: dict):
        """Create a new scheduledNotice item.

        ``POST /scheduled-notice-storage/scheduled-notices``

        Args:
            scheduledNotice (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created scheduledNotice item

        Schema:

            .. literalinclude:: ../files/ScheduledNoticeStorage_set_scheduledNotice_request.schema
        """
        return self.call("POST", "/scheduled-notice-storage/scheduled-notices", data=scheduledNotice)

    def delete_scheduledNotices(self):
        """

        ``DELETE /scheduled-notice-storage/scheduled-notices``
        """
        return self.call("DELETE", "/scheduled-notice-storage/scheduled-notices")

    def get_scheduledNotice(self, scheduledNoticeId: str):
        """Retrieve scheduledNotice item with given {scheduledNoticeId}

        ``GET /scheduled-notice-storage/scheduled-notices/{scheduledNoticeId}``

        Args:
            scheduledNoticeId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ScheduledNoticeStorage_get_scheduledNotice_return.schema 
        """
        return self.call("GET", f"/scheduled-notice-storage/scheduled-notices/{scheduledNoticeId}")

    def delete_scheduledNotice(self, scheduledNoticeId: str):
        """Delete scheduledNotice item with given {scheduledNoticeId}

        ``DELETE /scheduled-notice-storage/scheduled-notices/{scheduledNoticeId}``

        Args:
            scheduledNoticeId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/scheduled-notice-storage/scheduled-notices/{scheduledNoticeId}")

    def modify_scheduledNotice(self, scheduledNoticeId: str, scheduledNotice: dict):
        """Update scheduledNotice item with given {scheduledNoticeId}

        ``PUT /scheduled-notice-storage/scheduled-notices/{scheduledNoticeId}``

        Args:
            scheduledNoticeId (str)
            scheduledNotice (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/ScheduledNoticeStorage_modify_scheduledNotice_request.schema
        """
        return self.call("PUT", f"/scheduled-notice-storage/scheduled-notices/{scheduledNoticeId}", data=scheduledNotice)


class RequestPreferenceStorage(FolioApi):
    """Request Preference Storage API

    **Storage for request oreferences**
    """

    def get_requestPreferences(self, **kwargs):
        """Retrieve a list of requestPreference items.

        ``GET /request-preference-storage/request-preference``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    searchable using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - userId==1e425b93-501e-44b0-a4c7-b3e66a25c42e

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/RequestPreferenceStorage_get_requestPreferences_return.schema 
        """
        return self.call("GET", "/request-preference-storage/request-preference", query=kwargs)

    def set_requestPreference(self, requestPreference: dict):
        """Create a new requestPreference item.

        ``POST /request-preference-storage/request-preference``

        Args:
            requestPreference (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created requestPreference item

        Schema:

            .. literalinclude:: ../files/RequestPreferenceStorage_set_requestPreference_request.schema
        """
        return self.call("POST", "/request-preference-storage/request-preference", data=requestPreference)

    def get_requestPreference(self, requestPreferenceId: str):
        """Retrieve requestPreference item with given {requestPreferenceId}

        ``GET /request-preference-storage/request-preference/{requestPreferenceId}``

        Args:
            requestPreferenceId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/RequestPreferenceStorage_get_requestPreference_return.schema 
        """
        return self.call("GET", f"/request-preference-storage/request-preference/{requestPreferenceId}")

    def delete_requestPreference(self, requestPreferenceId: str):
        """Delete requestPreference item with given {requestPreferenceId}

        ``DELETE /request-preference-storage/request-preference/{requestPreferenceId}``

        Args:
            requestPreferenceId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/request-preference-storage/request-preference/{requestPreferenceId}")

    def modify_requestPreference(self, requestPreferenceId: str, requestPreference: dict):
        """Update requestPreference item with given {requestPreferenceId}

        ``PUT /request-preference-storage/request-preference/{requestPreferenceId}``

        Args:
            requestPreferenceId (str)
            requestPreference (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/RequestPreferenceStorage_modify_requestPreference_request.schema
        """
        return self.call("PUT", f"/request-preference-storage/request-preference/{requestPreferenceId}", data=requestPreference)


class CancellationReason(FolioApi):
    """Cancellation Reasons API

    **Storage for cancellation reasons**
    """

    def get_cancellationReasons(self, **kwargs):
        """Retrieve a list of cancellationReason items.

        ``GET /cancellation-reason-storage/cancellation-reasons``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - cancellationReason=lost

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/CancellationReason_get_cancellationReasons_return.schema 
        """
        return self.call("GET", "/cancellation-reason-storage/cancellation-reasons", query=kwargs)

    def set_cancellationReason(self, cancellationReason: dict):
        """Create a new cancellationReason item.

        ``POST /cancellation-reason-storage/cancellation-reasons``

        Args:
            cancellationReason (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created cancellationReason item

        Schema:

            .. literalinclude:: ../files/CancellationReason_set_cancellationReason_request.schema
        """
        return self.call("POST", "/cancellation-reason-storage/cancellation-reasons", data=cancellationReason)

    def delete_cancellationReasons(self):
        """

        ``DELETE /cancellation-reason-storage/cancellation-reasons``
        """
        return self.call("DELETE", "/cancellation-reason-storage/cancellation-reasons")

    def get_cancellationReason(self, cancellationReasonId: str):
        """Retrieve cancellationReason item with given {cancellationReasonId}

        ``GET /cancellation-reason-storage/cancellation-reasons/{cancellationReasonId}``

        Args:
            cancellationReasonId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CancellationReason_get_cancellationReason_return.schema 
        """
        return self.call("GET", f"/cancellation-reason-storage/cancellation-reasons/{cancellationReasonId}")

    def delete_cancellationReason(self, cancellationReasonId: str):
        """Delete cancellationReason item with given {cancellationReasonId}

        ``DELETE /cancellation-reason-storage/cancellation-reasons/{cancellationReasonId}``

        Args:
            cancellationReasonId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/cancellation-reason-storage/cancellation-reasons/{cancellationReasonId}")

    def modify_cancellationReason(self, cancellationReasonId: str, cancellationReason: dict):
        """Update cancellationReason item with given {cancellationReasonId}

        ``PUT /cancellation-reason-storage/cancellation-reasons/{cancellationReasonId}``

        Args:
            cancellationReasonId (str)
            cancellationReason (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CancellationReason_modify_cancellationReason_request.schema
        """
        return self.call("PUT", f"/cancellation-reason-storage/cancellation-reasons/{cancellationReasonId}", data=cancellationReason)


class FixedDueDateSchedule(FolioApi):
    """Fixed Due Date Schedule Storage API

    **Storage for fixed due date schedules**
    """

    def get_fixedDueDateSchedules(self, **kwargs):
        """Retrieve a list of fixedDueDateSchedule items.

        ``GET /fixed-due-date-schedule-storage/fixed-due-date-schedules``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=semester

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/FixedDueDateSchedule_get_fixedDueDateSchedules_return.schema 
        """
        return self.call("GET", "/fixed-due-date-schedule-storage/fixed-due-date-schedules", query=kwargs)

    def set_fixedDueDateSchedule(self, fixedDueDateSchedule: dict):
        """Create a new fixedDueDateSchedule item.

        ``POST /fixed-due-date-schedule-storage/fixed-due-date-schedules``

        Args:
            fixedDueDateSchedule (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created fixedDueDateSchedule item

        Schema:

            .. literalinclude:: ../files/FixedDueDateSchedule_set_fixedDueDateSchedule_request.schema
        """
        return self.call("POST", "/fixed-due-date-schedule-storage/fixed-due-date-schedules", data=fixedDueDateSchedule)

    def delete_fixedDueDateSchedules(self):
        """

        ``DELETE /fixed-due-date-schedule-storage/fixed-due-date-schedules``
        """
        return self.call("DELETE", "/fixed-due-date-schedule-storage/fixed-due-date-schedules")

    def get_fixedDueDateSchedule(self, fixedDueDateScheduleId: str):
        """Retrieve fixedDueDateSchedule item with given {fixedDueDateScheduleId}

        ``GET /fixed-due-date-schedule-storage/fixed-due-date-schedules/{fixedDueDateScheduleId}``

        Args:
            fixedDueDateScheduleId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FixedDueDateSchedule_get_fixedDueDateSchedule_return.schema 
        """
        return self.call("GET", f"/fixed-due-date-schedule-storage/fixed-due-date-schedules/{fixedDueDateScheduleId}")

    def delete_fixedDueDateSchedule(self, fixedDueDateScheduleId: str):
        """Delete fixedDueDateSchedule item with given {fixedDueDateScheduleId}

        ``DELETE /fixed-due-date-schedule-storage/fixed-due-date-schedules/{fixedDueDateScheduleId}``

        Args:
            fixedDueDateScheduleId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/fixed-due-date-schedule-storage/fixed-due-date-schedules/{fixedDueDateScheduleId}")

    def modify_fixedDueDateSchedule(self, fixedDueDateScheduleId: str, fixedDueDateSchedule: dict):
        """Update fixedDueDateSchedule item with given {fixedDueDateScheduleId}

        ``PUT /fixed-due-date-schedule-storage/fixed-due-date-schedules/{fixedDueDateScheduleId}``

        Args:
            fixedDueDateScheduleId (str)
            fixedDueDateSchedule (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/FixedDueDateSchedule_modify_fixedDueDateSchedule_request.schema
        """
        return self.call("PUT", f"/fixed-due-date-schedule-storage/fixed-due-date-schedules/{fixedDueDateScheduleId}", data=fixedDueDateSchedule)


class ActualCostRecordStorage(FolioApi):
    """Actual cost record API

    **Storage for actual cost record**
    """

    def get_actualCostRecords(self, **kwargs):
        """Retrieve a list of actualCostRecord items.

        ``GET /actual-cost-record-storage/actual-cost-records``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    by using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - lossType="Aged to lost"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ActualCostRecordStorage_get_actualCostRecords_return.schema 
        """
        return self.call("GET", "/actual-cost-record-storage/actual-cost-records", query=kwargs)

    def set_actualCostRecord(self, actualCostRecord: dict):
        """Create a new actualCostRecord item.

        ``POST /actual-cost-record-storage/actual-cost-records``

        Args:
            actualCostRecord (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created actualCostRecord item

        Schema:

            .. literalinclude:: ../files/ActualCostRecordStorage_set_actualCostRecord_request.schema
        """
        return self.call("POST", "/actual-cost-record-storage/actual-cost-records", data=actualCostRecord)

    def get_actualCostRecord(self, actualCostRecordsId: str):
        """Get actual cost record

        ``GET /actual-cost-record-storage/actual-cost-records/{actualCostRecordsId}``

        Args:
            actualCostRecordsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/ActualCostRecordStorage_get_actualCostRecord_return.schema 
        """
        return self.call("GET", f"/actual-cost-record-storage/actual-cost-records/{actualCostRecordsId}")

    def delete_actualCostRecord(self, actualCostRecordsId: str, **kwargs):
        """Delete actual cost record

        ``DELETE /actual-cost-record-storage/actual-cost-records/{actualCostRecordsId}``

        Args:
            actualCostRecordsId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/actual-cost-record-storage/actual-cost-records/{actualCostRecordsId}", query=kwargs)

    def modify_actualCostRecord(self, actualCostRecordsId: str, actualCostRecord: dict):
        """Update actual cost record

        ``PUT /actual-cost-record-storage/actual-cost-records/{actualCostRecordsId}``

        Args:
            actualCostRecordsId (str)
            actualCostRecord (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/ActualCostRecordStorage_modify_actualCostRecord_request.schema
        """
        return self.call("PUT", f"/actual-cost-record-storage/actual-cost-records/{actualCostRecordsId}", data=actualCostRecord)


class CirculationRulesStorage(FolioApi):
    """Circulation Rules Storage API

    **Storage for circulation rules**
    """

    def get_circulationRulesStorages(self):
        """Get the circulation rules

        ``GET /circulation-rules-storage``

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CirculationRulesStorage_get_circulationRulesStorages_return.schema 
        """
        return self.call("GET", "/circulation-rules-storage")

    def modify_circulationRulesStorage(self, circulationRulesStorage: dict):
        """Set the circulation rules

        ``PUT /circulation-rules-storage``

        Args:
            circulationRulesStorage (dict): See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CirculationRulesStorage_modify_circulationRulesStorage_request.schema
        """
        return self.call("PUT", "/circulation-rules-storage", data=circulationRulesStorage)


class CheckInStorage(FolioApi):
    """Check-in Storage API

    **Storage for check-ins**
    """

    def get_checkIns(self, **kwargs):
        """Retrieve a list of checkIn items.

        ``GET /check-in-storage/check-ins``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    by using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - itemId="cf23adf0-61ba-4887-bf82-956c4aae2260"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CheckInStorage_get_checkIns_return.schema 
        """
        return self.call("GET", "/check-in-storage/check-ins", query=kwargs)

    def set_checkIn(self, checkIn: dict):
        """Create a new checkIn item.

        ``POST /check-in-storage/check-ins``

        Args:
            checkIn (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created checkIn item

        Schema:

            .. literalinclude:: ../files/CheckInStorage_set_checkIn_request.schema
        """
        return self.call("POST", "/check-in-storage/check-ins", data=checkIn)

    def get_checkIn(self, checkInId: str):
        """Retrieve checkIn item with given {checkInId}

        ``GET /check-in-storage/check-ins/{checkInId}``

        Args:
            checkInId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CheckInStorage_get_checkIn_return.schema 
        """
        return self.call("GET", f"/check-in-storage/check-ins/{checkInId}")


class LoanStorage(FolioApi):
    """Loan Storage API

    **Storage for loans**
    """

    def get_loans(self, **kwargs):
        """Retrieve a list of loan items.

        ``GET /loan-storage/loans``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    searchable using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - requesterId="cf23adf0-61ba-4887-bf82-956c4aae2260"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LoanStorage_get_loans_return.schema 
        """
        return self.call("GET", "/loan-storage/loans", query=kwargs)

    def set_loan(self, loan: dict):
        """Create a new loan item.

        ``POST /loan-storage/loans``

        Args:
            loan (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created loan item

        Schema:

            .. literalinclude:: ../files/LoanStorage_set_loan_request.schema
        """
        return self.call("POST", "/loan-storage/loans", data=loan)

    def delete_loans(self):
        """

        ``DELETE /loan-storage/loans``
        """
        return self.call("DELETE", "/loan-storage/loans")

    def set_anonymize(self, userId: str):
        """

        ``POST /loan-storage/loans/anonymize/{userId}``

        Args:
            userId (str)

        Raises:
            OkapiFatalError: Server Error
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("POST", f"/loan-storage/loans/anonymize/{userId}")

    def get_loan(self, loanId: str):
        """Retrieve loan item with given {loanId}

        ``GET /loan-storage/loans/{loanId}``

        Args:
            loanId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LoanStorage_get_loan_return.schema 
        """
        return self.call("GET", f"/loan-storage/loans/{loanId}")

    def delete_loan(self, loanId: str):
        """Delete loan item with given {loanId}

        ``DELETE /loan-storage/loans/{loanId}``

        Args:
            loanId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/loan-storage/loans/{loanId}")

    def modify_loan(self, loanId: str, loan: dict):
        """Update loan item with given {loanId}

        ``PUT /loan-storage/loans/{loanId}``

        Args:
            loanId (str)
            loan (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/LoanStorage_modify_loan_request.schema
        """
        return self.call("PUT", f"/loan-storage/loans/{loanId}", data=loan)

    def get_loanHistories(self, **kwargs):
        """Retrieve a list of loanHistory items.

        ``GET /loan-storage/loan-history``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - loan.status.name==Closed

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LoanStorage_get_loanHistories_return.schema 
        """
        return self.call("GET", "/loan-storage/loan-history", query=kwargs)


class LoanPolicyStorage(FolioApi):
    """Loan Policy Storage API

    **Storage for loan policies**
    """

    def get_loanPolicies(self, **kwargs):
        """Retrieve a list of loanPolicy items.

        ``GET /loan-policy-storage/loan-policies``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    searchable using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - id="cf23adf0-61ba-4887-bf82-956c4aae2260"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LoanPolicyStorage_get_loanPolicies_return.schema 
        """
        return self.call("GET", "/loan-policy-storage/loan-policies", query=kwargs)

    def set_loanPolicy(self, loanPolicy: dict):
        """Create a new loanPolicy item.

        ``POST /loan-policy-storage/loan-policies``

        Args:
            loanPolicy (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created loanPolicy item

        Schema:

            .. literalinclude:: ../files/LoanPolicyStorage_set_loanPolicy_request.schema
        """
        return self.call("POST", "/loan-policy-storage/loan-policies", data=loanPolicy)

    def delete_loanPolicies(self):
        """

        ``DELETE /loan-policy-storage/loan-policies``
        """
        return self.call("DELETE", "/loan-policy-storage/loan-policies")

    def get_loanPolicy(self, loanPolicyId: str):
        """Retrieve loanPolicy item with given {loanPolicyId}

        ``GET /loan-policy-storage/loan-policies/{loanPolicyId}``

        Args:
            loanPolicyId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LoanPolicyStorage_get_loanPolicy_return.schema 
        """
        return self.call("GET", f"/loan-policy-storage/loan-policies/{loanPolicyId}")

    def delete_loanPolicy(self, loanPolicyId: str):
        """Delete loanPolicy item with given {loanPolicyId}

        ``DELETE /loan-policy-storage/loan-policies/{loanPolicyId}``

        Args:
            loanPolicyId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/loan-policy-storage/loan-policies/{loanPolicyId}")

    def modify_loanPolicy(self, loanPolicyId: str, loanPolicy: dict):
        """Update loanPolicy item with given {loanPolicyId}

        ``PUT /loan-policy-storage/loan-policies/{loanPolicyId}``

        Args:
            loanPolicyId (str)
            loanPolicy (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/LoanPolicyStorage_modify_loanPolicy_request.schema
        """
        return self.call("PUT", f"/loan-policy-storage/loan-policies/{loanPolicyId}", data=loanPolicy)


class AnonymizeStorageLoans(FolioApi):
    """Anonymize loans API

    **Anonymize loans API**
    """

    def set_anonymizeStorageLoan(self, anonymizeStorageLoan: dict):
        """

        ``POST /anonymize-storage-loans``

        Args:
            anonymizeStorageLoan (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AnonymizeStorageLoans_set_anonymizeStorageLoan_request.schema
            .. literalinclude:: ../files/AnonymizeStorageLoans_set_anonymizeStorageLoan_return.schema 
        """
        return self.call("POST", "/anonymize-storage-loans", data=anonymizeStorageLoan)


class PatronNoticePolicy(FolioApi):
    """Patron Notice Policies API

    **Storage for Patron Notice Policies**
    """

    def get_patronNoticePolicies(self, **kwargs):
        """Get Patron Notice Policy list

        ``GET /patron-notice-policy-storage/patron-notice-policies``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    searchable using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name="undergrad*"

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PatronNoticePolicy_get_patronNoticePolicies_return.schema 
        """
        return self.call("GET", "/patron-notice-policy-storage/patron-notice-policies", query=kwargs)

    def set_patronNoticePolicy(self, patronNoticePolicy: dict):
        """Create new Patron Notice Policy

        ``POST /patron-notice-policy-storage/patron-notice-policies``

        Args:
            patronNoticePolicy (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PatronNoticePolicy_set_patronNoticePolicy_request.schema
        """
        return self.call("POST", "/patron-notice-policy-storage/patron-notice-policies", data=patronNoticePolicy)

    def get_patronNoticePolicy(self, patronNoticePolicyId: str):
        """Get Patron Notice Policy by id

        ``GET /patron-notice-policy-storage/patron-notice-policies/{patronNoticePolicyId}``

        Args:
            patronNoticePolicyId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PatronNoticePolicy_get_patronNoticePolicy_return.schema 
        """
        return self.call("GET", f"/patron-notice-policy-storage/patron-notice-policies/{patronNoticePolicyId}")

    def delete_patronNoticePolicy(self, patronNoticePolicyId: str):
        """Delete Patron Notice Policy by id

        ``DELETE /patron-notice-policy-storage/patron-notice-policies/{patronNoticePolicyId}``

        Args:
            patronNoticePolicyId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/patron-notice-policy-storage/patron-notice-policies/{patronNoticePolicyId}")

    def modify_patronNoticePolicy(self, patronNoticePolicyId: str, patronNoticePolicy: dict):
        """Update Patron Notice Policy by id

        ``PUT /patron-notice-policy-storage/patron-notice-policies/{patronNoticePolicyId}``

        Args:
            patronNoticePolicyId (str)
            patronNoticePolicy (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/PatronNoticePolicy_modify_patronNoticePolicy_request.schema
        """
        return self.call("PUT", f"/patron-notice-policy-storage/patron-notice-policies/{patronNoticePolicyId}", data=patronNoticePolicy)


class RequestStorage(FolioApi):
    """Request Storage API

    **Storage for requests**
    """

    def get_requests(self, **kwargs):
        """Retrieve a list of request items.

        ``GET /request-storage/requests``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    by using CQL
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - requesterId="cf23adf0-61ba-4887-bf82-956c4aae2260"

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/RequestStorage_get_requests_return.schema 
        """
        return self.call("GET", "/request-storage/requests", query=kwargs)

    def set_request(self, request: dict):
        """Create a new request item.

        ``POST /request-storage/requests``

        Args:
            request (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created request item

        Schema:

            .. literalinclude:: ../files/RequestStorage_set_request_request.schema
        """
        return self.call("POST", "/request-storage/requests", data=request)

    def delete_requests(self):
        """

        ``DELETE /request-storage/requests``
        """
        return self.call("DELETE", "/request-storage/requests")

    def get_request(self, requestId: str):
        """Retrieve request item with given {requestId}

        ``GET /request-storage/requests/{requestId}``

        Args:
            requestId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/RequestStorage_get_request_return.schema 
        """
        return self.call("GET", f"/request-storage/requests/{requestId}")

    def delete_request(self, requestId: str):
        """Delete request item with given {requestId}

        ``DELETE /request-storage/requests/{requestId}``

        Args:
            requestId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/request-storage/requests/{requestId}")

    def modify_request(self, requestId: str, request: dict):
        """Update request item with given {requestId}

        ``PUT /request-storage/requests/{requestId}``

        Args:
            requestId (str)
            request (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/RequestStorage_modify_request_request.schema
        """
        return self.call("PUT", f"/request-storage/requests/{requestId}", data=request)
