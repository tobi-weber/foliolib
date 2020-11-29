# -*- coding: utf-8 -*-
# Generated at 2020-11-29

import logging

from foliolib.folio import FolioApi

log = logging.getLogger("foliolib.folio.api.calendar")


class Calendar(FolioApi):
    """mod-calendar API

    This module provides a backend for the calendar functionalities
    """

    def get_periods(self, **kwargs):
        """List actual opening hours including exceptions for custom date range. Mainly used by calendar display and provides opening information for loan rules. The response contains only the openings closed times are not included.

        ``GET /calendar/periods``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            servicePointId (str):  Filter for service point. In case of parameter absence all service point will be included in response.
            startDate (str):  Filter for start date (ISO 8601 date format). The parameter is inclusive.
                    
                    Example:
                    
                     - 2018-05-01
            endDate (str):  Filter for end date (ISO 8601 date format). The parameter is inclusive.
                    
                    Example:
                    
                     - 2018-05-31
            includeClosedDays (bool): (default=True) In case of true all days will have value even if it is closing time or not
            actualOpening (bool): (default=True) In case of true exceptional openings are overriding regular opening and in this case regular opening is not included in the response
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
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/Calendar_get_periods_return.schema 
        """
        return self.call("GET", "/calendar/periods", query=kwargs)

    def get_periods_for_servicePoint(self, servicePointId: str, **kwargs):
        """List library hours period. The default response contains the period names and its dates.

        ``GET /calendar/periods/{servicePointId}/period``

        Args:
            servicePointId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            withOpeningDays (bool): (default=False) Include opening days in response.
            showPast (bool): (default=False) Include past openings in response.
            showExceptional (bool): (default=False) Filter for exceptional library hours periods.

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/Calendar_get_periods_for_servicePoint_return.schema 
        """
        return self.call("GET", f"/calendar/periods/{servicePointId}/period", query=kwargs)

    def set_period(self, servicePointId: str, period: dict):
        """Saves the new library period

        ``POST /calendar/periods/{servicePointId}/period``

        Args:
            servicePointId (str)
            period (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created period item

        Schema:

            .. literalinclude:: ../files/Calendar_set_period_request.schema
        """
        return self.call("POST", f"/calendar/periods/{servicePointId}/period", data=period)

    def get_period(self, servicePointId: str, periodId: str):
        """List opening hours for given periodId.

        ``GET /calendar/periods/{servicePointId}/period/{periodId}``

        Args:
            servicePointId (str)
            periodId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Calendar_get_period_return.schema 
        """
        return self.call("GET", f"/calendar/periods/{servicePointId}/period/{periodId}")

    def delete_period(self, servicePointId: str, periodId: str):
        """Delete Opening hours by Id

        ``DELETE /calendar/periods/{servicePointId}/period/{periodId}``

        Args:
            servicePointId (str)
            periodId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/calendar/periods/{servicePointId}/period/{periodId}")

    def modify_period(self, servicePointId: str, periodId: str, period: dict):
        """Update library period by periodId

        ``PUT /calendar/periods/{servicePointId}/period/{periodId}``

        Args:
            servicePointId (str)
            periodId (str)
            period (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Calendar_modify_period_request.schema
        """
        return self.call("PUT", f"/calendar/periods/{servicePointId}/period/{periodId}", data=period)

    def get_calculateopening_by_servicePoint(self, servicePointId: str, **kwargs):
        """This endpoint helps to calculate due date. The response contains three openings: the requested day, next and previous dates openings which are closest to the requested day.

        ``GET /calendar/periods/{servicePointId}/calculateopening``

        Args:
            servicePointId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            requestedDate (str):  requested date
                    
                    Example:
                    
                     - 2019-01-31
            lang (str): (default=en) Requested language. Optional. [lang=en]
                    

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Calendar_get_calculateopening_by_servicePoint_return.schema 
        """
        return self.call("GET", f"/calendar/periods/{servicePointId}/calculateopening", query=kwargs)
