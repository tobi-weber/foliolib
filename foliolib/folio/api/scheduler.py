# -*- coding: utf-8 -*-
# Generated at 2024-03-23

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.scheduler")



class Scheduler(FolioApi):
    """Mod Scheduler API

    Mod Scheduler API
    """

    def getschedulertimers(self, **kwargs):
        """Retrieve timer list

        ``GET /scheduler/timers``

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, default: 0)
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 500, default: 10)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Scheduler_getschedulertimers_response.schema
        """
        return self.call("GET", "/scheduler/timers", query=kwargs)

		
    def createschedulertimers(self, timerDescriptor):
        """Create timer for a module

        ``POST /scheduler/timers``

        Args:
            timerDescriptor (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response in JSON format for validation errors.
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Scheduler_createschedulertimers_request.schema
        """
        return self.call("POST", f"/scheduler/timers", timerDescriptor)

    def getschedulertimerbyid(self, id_):
        """Retrieve scheduler timer by id

        ``GET /scheduler/timers/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Scheduler_getschedulertimerbyid_response.schema
        """
        return self.call("GET", f"/scheduler/timers/{id_}")

		
    def updateschedulertimerbyid(self, timerDescriptor, id_):
        """Update scheduler timer by id

        ``PUT /scheduler/timers/{id}``

        Args:
            timerDescriptor (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Scheduler_updateschedulertimerbyid_request.schema
        """
        return self.call("PUT", f"/scheduler/timers/{id_}", timerDescriptor)

		
    def deleteschedulertimerbyid(self, id_):
        """delete scheduler timer by id

        ``DELETE /scheduler/timers/{id}``

        Raises:
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.
        """
        return self.call("DELETE", f"/scheduler/timers/{id_}")
