# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.eusageReports")



class Eusagereports(FolioApi):
    """EUsage Reports

    
    """

    def getreporttitles(self):
        """Get titles with links to KB. The response contains facets response with facet type "status" and counts for values "matched", "ignored", "unmatched. The resulting set can be limited by parameter query (CQL) as well as counterReportId and providerId (these are NOT part of CQL). The CQL query itself supports fields "cql.allRecords", "id", "counterReportTitle", "ISBN", "printISSN", "onlineISSN", "kbTitleId" and "kbManualMatch".

        ``GET /eusage-reports/report-titles``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Eusagereports_getreporttitles_response.schema
        """
        return self.call("GET", "/eusage-reports/report-titles")

		
    def postreporttitles(self, reportTitles):
        """POST titles with links to KB

        ``POST /eusage-reports/report-titles``

        Args:
            reportTitles (dict): See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Eusagereports_postreporttitles_request.schema
        """
        return self.call("POST", f"/eusage-reports/report-titles", reportTitles)

    def getreportpackages(self):
        """Get KB title - package relationship.

        ``GET /eusage-reports/report-packages``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Eusagereports_getreportpackages_response.schema
        """
        return self.call("GET", "/eusage-reports/report-packages")

    def postfromcounter(self, fromCounterRequest):
        """Parse counter reports

        ``POST /eusage-reports/report-titles/from-counter``

        Args:
            fromCounterRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Eusagereports_postfromcounter_request.schema
            .. literalinclude:: ../files/Eusagereports_postfromcounter_request.schema_response.schema
        """
        return self.call("POST", f"/eusage-reports/report-titles/from-counter", fromCounterRequest)

    def gettitledata(self):
        """Get counter report title data.

        ``GET /eusage-reports/title-data``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Eusagereports_gettitledata_response.schema
        """
        return self.call("GET", "/eusage-reports/title-data")

    def getreportdata(self):
        """This returns data for parsed agreements.

        ``GET /eusage-reports/report-data``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Eusagereports_getreportdata_response.schema
        """
        return self.call("GET", "/eusage-reports/report-data")

    def postfromagreement(self, fromAgreementRequest):
        """Parse agreements and populate report data

        ``POST /eusage-reports/report-data/from-agreement``

        Args:
            fromAgreementRequest (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Eusagereports_postfromagreement_request.schema
            .. literalinclude:: ../files/Eusagereports_postfromagreement_request.schema_response.schema
        """
        return self.call("POST", f"/eusage-reports/report-data/from-agreement", fromAgreementRequest)

    def getuseovertime(self):
        """Return usage data over time, where usageDateRange falls within startDate, endDate

        ``GET /eusage-reports/stored-reports/use-over-time``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Eusagereports_getuseovertime_response.schema
        """
        return self.call("GET", "/eusage-reports/stored-reports/use-over-time")

    def getreqsbydateofuse(self):
        """Return requests by date of use; this is like use over time but additionally groups by publication year.

        ``GET /eusage-reports/stored-reports/reqs-by-date-of-use``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Eusagereports_getreqsbydateofuse_response.schema
        """
        return self.call("GET", "/eusage-reports/stored-reports/reqs-by-date-of-use")

    def getreqsbypubyear(self):
        """Return requests by publication year where usageDateRange falls within startDate, endDate. Grouping controlled by periodOfUse. "accessCountPeriods" array lists the publication years to be used as column labels for numbers in the "totalItemRequestsByPeriod", "uniqueItemRequestsByPeriod" and "accessCountsByPeriod" arrays.

        ``GET /eusage-reports/stored-reports/reqs-by-pub-year``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Eusagereports_getreqsbypubyear_response.schema
        """
        return self.call("GET", "/eusage-reports/stored-reports/reqs-by-pub-year")

    def getcostperuse(self):
        """Return cost per where usageDateRange falls within startDate, endDate. The report is structured in periods, typically months, and the cost-per-use in a period is invoiced amount divided by download count (unique or total) and further divided in number of periods where any title has downloads. This way the cost for download is divided into periods (with non-zero use) and then evenly divided across titles within those periods. Consider agreement that has two titles, titleA and titleB where titleA has downloads in May and June. titleB has downloads in June only. In May, the title count is 1. In June, the title count is 2. The total periods where any title occurs is p = 2+1 = 3. Cost per download for titleA in May is (paidAmount/p) / downloads(TitleA,May) and in June (paidAmount/p) / downloads(TitleA,June). Cost per download for titleB in June is paidAmount/p / downloads(TitleB,June).

        ``GET /eusage-reports/stored-reports/cost-per-use``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Eusagereports_getcostperuse_response.schema
        """
        return self.call("GET", "/eusage-reports/stored-reports/cost-per-use")

    def getreportstatus(self, id_):
        """Return status of operation associated with identifier.

        ``GET /eusage-reports/report-data/status/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Bad request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Internal error

        Schema:

            .. literalinclude:: ../files/Eusagereports_getreportstatus_response.schema
        """
        return self.call("GET", f"/eusage-reports/report-data/status/{id_}")
