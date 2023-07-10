# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.calendar")



class Calendar(FolioApi):
    """Calendar Opening Hours API

    
    """

    def searchcalendars(self, **kwargs):
        """Get all calendars that match the given query

        ``GET /calendar/calendars``

        Keyword Args:
            id (list): The list of calendar IDs to retrieve, sent as separate parameters (?id=aaaa&id=bbbb...).  If this list is passed, calendars must have an ID in this list in addition to any additional criteria. (items: (type: string, format: uuid))
            servicePointId (list): Filter for calendars that are assigned to a certain service point.  If this parameter is excluded, all service points will be considered/included in the response.  Multiple service points may be specified with form-style query expansions; in this case, calendars that are assigned to any of the provided service points will be returned. (items: (type: string, format: uuid))
            startDate (str): The first date (YYYY-MM-DD) to consider, inclusively (format: date)
            endDate (str): The last date (YYYY-MM-DD) to consider, inclusively (format: date)
            offset (int): Skip a certain number of the first values; used for pagination (default: 0, minimum: 0)
            limit (int): The maximum number of elements returned in the response, used for pagination.  A limit of zero will not include any results (however, totalRecords will still be included) -- to include all results, use a large number such as 2147483647. (default: 10, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Invalid request or parameters
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Calendar_searchcalendars_response.schema
        """
        return self.call("GET", "/calendar/calendars", query=kwargs)

		
    def createcalendar(self, calendar):
        """Create a new calendar from a provided body.  If an ID is provided for the calendar, it will be ignored (and a new one generated).

        ``POST /calendar/calendars``

        Args:
            calendar (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Invalid request or parameters
            OkapiRequestConflict: A calendar creation/update cannot be performed due to an existing assignment overlapping with the provided date range
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Calendar_createcalendar_request.schema
        """
        return self.call("POST", f"/calendar/calendars", calendar)

		
    def deletecalendars(self, **kwargs):
        """Delete a calendar by its ID.

        ``DELETE /calendar/calendars``

        Keyword Args:
            id (list): A list of calendars to delete, sent as separate parameters (?id=aaaa&id=bbbb...).  If any calendars are missing, a 404 will be returned and nothing modified. (items: (type: string, format: uuid), minItems: 1)

        Raises:
            OkapiRequestError: Invalid request or parameters
            OkapiRequestNotFound: A calendar with the given UUID could not be found.
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", "/calendar/calendars", query=kwargs)

    def getcalendar(self, calendarId):
        """Get a calendar's information by its ID.

        ``GET /calendar/calendars/{calendarId}``

        Args:
            calendarId (str): The calendar ID to retrieve (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Invalid request or parameters
            OkapiRequestNotFound: A calendar with the given UUID could not be found.
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Calendar_getcalendar_response.schema
        """
        return self.call("GET", f"/calendar/calendars/{calendarId}")

		
    def updatecalendar(self, calendarId, calendar):
        """Overwrite an existing calendar with the provided payload.  The provided calendar must already exist (attempting to overwrite a calendar that does not yet exist will result in a 404).  If the payload includes any IDs, they will be ignored, and the existing calendar ID reused.

        ``PUT /calendar/calendars/{calendarId}``

        Args:
            calendarId (str): The calendar ID to replace (format: uuid)
            calendar (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Invalid request or parameters
            OkapiRequestNotFound: A calendar with the given UUID could not be found.
            OkapiRequestConflict: A calendar creation/update cannot be performed due to an existing assignment overlapping with the provided date range
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Calendar_updatecalendar_request.schema
        """
        return self.call("PUT", f"/calendar/calendars/{calendarId}", calendar)

		
    def deletecalendar(self, calendarId):
        """Delete a calendar by its ID.

        ``DELETE /calendar/calendars/{calendarId}``

        Args:
            calendarId (str): The calendar ID to operate on. (format: uuid)

        Raises:
            OkapiRequestError: Invalid request or parameters
            OkapiRequestNotFound: A calendar with the given UUID could not be found.
            OkapiFatalError: Internal server error
        """
        return self.call("DELETE", f"/calendar/calendars/{calendarId}")

    def getsurroundingopenings(self, servicePointId, **kwargs):
        """Calculate openings nearest to a given date for a specified service point

        ``GET /calendar/dates/{servicePointId}/surrounding-openings``

        Args:
            servicePointId (str): The service point to calculate openings on (format: uuid)

        Keyword Args:
            date (str): The date (YYYY-MM-DD) to calculate openings around (format: date)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Invalid request or parameters
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Calendar_getsurroundingopenings_response.schema
        """
        return self.call("GET", f"/calendar/dates/{servicePointId}/surrounding-openings", query=kwargs)

    def getallopenings(self, servicePointId, **kwargs):
        """Calculate the opening information for each date within a range

        ``GET /calendar/dates/{servicePointId}/all-openings``

        Args:
            servicePointId (str): The service point to calculate openings on (format: uuid)

        Keyword Args:
            startDate (str): The first date (YYYY-MM-DD) to include, inclusive (format: date)
            endDate (str): The last date (YYYY-MM-DD) to include, inclusive (format: date)
            includeClosed (bool): Whether or not the results should include days where the service point is closed.  Exceptional closures will always be returned
            offset (int): Skip a certain number of the first values; used for pagination (default: 0, minimum: 0)
            limit (int): The maximum number of elements returned in the response, used for pagination.  A limit of zero will not include any results (however, totalRecords will still be included) -- to include all results, use a large number such as 2147483647. (default: 10, minimum: 0)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Invalid request or parameters
            OkapiFatalError: Internal server error

        Schema:

            .. literalinclude:: ../files/Calendar_getallopenings_response.schema
        """
        return self.call("GET", f"/calendar/dates/{servicePointId}/all-openings", query=kwargs)
