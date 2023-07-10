# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.ermUsage")


class Files(FolioApi):
    """mod-erm-usage API

    This documents the API calls that can be made to query and manage files in module erm-usage
    """

    def upload_file(self, filePath: str):
        """Upload/update a file in module erm-usage.

        ``POST /erm-usage/files``

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        import os
        headers = {}
        headers["Content-Type"] = "application/octet-stream"
        headers["Content-length"] = str(os.path.getsize(filePath))
        headers["Content-Disposition"] = "attachment; filename=%s" % os.path.basename(
            filePath)
        with open(filePath, 'rb') as f:
            data = f.read()
        
        return self.call("POST", "/erm-usage/files", headers=headers, data=data)

    def get_file(self, filesId: str):
        """Get file by id

        ``GET /erm-usage/files/{filesId}``

        Args:
            filesId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("GET", f"/erm-usage/files/{filesId}")

    def delete_file(self, filesId: str):
        """Delete a file identified by id

        ``DELETE /erm-usage/files/{filesId}``

        Args:
            filesId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/erm-usage/files/{filesId}")


class Customreports(FolioApi):
    """mod-erm-usage API

    This documents the API calls that can be made to query and manage custom reports
    """

    def get_customReports(self, **kwargs):
        """Get all reports.

        ``GET /custom-reports``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - year=2018
            orderBy (str):  Order by field: 
                    
            order (str (desc|asc):): (default=desc) Order
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

        Schema:

            .. literalinclude:: ../files/Customreports_get_customReports_return.schema 
        """
        return self.call("GET", "/custom-reports", query=kwargs)

    def set_customReport(self, customReport: dict):
        """Post new report

        ``POST /custom-reports``

        Args:
            customReport (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created customReport item

        Schema:

            .. literalinclude:: ../files/Customreports_set_customReport_request.schema
        """
        return self.call("POST", "/custom-reports", data=customReport)

    def get_customReport(self, customReportsId: str):
        """Get one report identified by id

        ``GET /custom-reports/{customReportsId}``

        Args:
            customReportsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Customreports_get_customReport_return.schema 
        """
        return self.call("GET", f"/custom-reports/{customReportsId}")

    def delete_customReport(self, customReportsId: str):
        """Delete report identified by id

        ``DELETE /custom-reports/{customReportsId}``

        Args:
            customReportsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/custom-reports/{customReportsId}")

    def modify_customReport(self, customReportsId: str, customReport: dict):
        """Put report identified by id

        ``PUT /custom-reports/{customReportsId}``

        Args:
            customReportsId (str)
            customReport (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Customreports_modify_customReport_request.schema
        """
        return self.call("PUT", f"/custom-reports/{customReportsId}", data=customReport)


class Counterreports(FolioApi):
    """mod-erm-usage API

    This documents the API calls that can be made to query and manage counter reports
    """

    def get_counterReports(self, **kwargs):
        """Get all reports. If query parameter tiny is set to true, the reports' metadata is returned without the actual counter reports.

        ``GET /counter-reports``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - yearMonth="2018-03" and reportName="JR1"
            orderBy (str):  Order by field: 
                    
            order (str (desc|asc):): (default=desc) Order
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

        Schema:

            .. literalinclude:: ../files/Counterreports_get_counterReports_return.schema 
        """
        return self.call("GET", "/counter-reports", query=kwargs)

    def set_counterReport(self, counterReport: dict):
        """Post new report

        ``POST /counter-reports``

        Args:
            counterReport (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created counterReport item

        Schema:

            .. literalinclude:: ../files/Counterreports_set_counterReport_request.schema
        """
        return self.call("POST", "/counter-reports", data=counterReport)

    def get_counterReport(self, counterReportsId: str):
        """Get one report identified by id

        ``GET /counter-reports/{counterReportsId}``

        Args:
            counterReportsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Counterreports_get_counterReport_return.schema 
        """
        return self.call("GET", f"/counter-reports/{counterReportsId}")

    def delete_counterReport(self, counterReportsId: str):
        """Delete report identified by id

        ``DELETE /counter-reports/{counterReportsId}``

        Args:
            counterReportsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/counter-reports/{counterReportsId}")

    def modify_counterReport(self, counterReportsId: str, counterReport: dict):
        """Put report identified by id

        ``PUT /counter-reports/{counterReportsId}``

        Args:
            counterReportsId (str)
            counterReport (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Counterreports_modify_counterReport_request.schema
        """
        return self.call("PUT", f"/counter-reports/{counterReportsId}", data=counterReport)

    def get_download_by_counterReport(self, counterReportsId: str):
        """Download report in its original format

        ``GET /counter-reports/{counterReportsId}/download``

        Args:
            counterReportsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("GET", f"/counter-reports/{counterReportsId}/download")

    def get_sorted(self, udpId: str):
        """Get counter reports sorted by year and report

        ``GET /counter-reports/sorted/{udpId}``

        Args:
            udpId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Counterreports_get_sorted_return.schema 
        """
        return self.call("GET", f"/counter-reports/sorted/{udpId}")

    def get_export(self, exportId: str, **kwargs):
        """Get the report identified by id as specified format (default is CSV)

        ``GET /counter-reports/export/{exportId}``

        Args:
            exportId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            format (str): (default=csv) 

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("GET", f"/counter-reports/export/{exportId}", query=kwargs)

    def get_to(self, providerId: str, name: str, aversion: str, begin: str, end: str, **kwargs):
        """Get report for several months as specified format (default is CSV)

        ``GET /counter-reports/export/provider/{providerId}/report/{name}/version/{aversion}/from/{begin}/to/{end}``

        Args:
            providerId (str)
            name (str)
            aversion (str)
            begin (str)
            end (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            format (str): (default=csv) 

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("GET", f"/counter-reports/export/provider/{providerId}/report/{name}/version/{aversion}/from/{begin}/to/{end}", query=kwargs)

    def set_provider(self, providerId: str, provider: dict, **kwargs):
        """

        ``POST /counter-reports/upload/provider/{providerId}``

        Args:
            providerId (str)
            provider (dict)
            **kwargs (properties): Keyword Arguments: See Schema below

        Keyword Args:
            overwrite (bool): (default=False) Overwrite existing reports?

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Counterreports_set_provider_request.schema
        """
        return self.call("POST", f"/counter-reports/upload/provider/{providerId}", data=provider, query=kwargs)

    def get_codes(self):
        """Get counter/sushi error codes existent in counter reports

        ``GET /counter-reports/errors/codes``

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Counterreports_get_codes_return.schema 
        """
        return self.call("GET", "/counter-reports/errors/codes")

    def get_types(self):
        """Get report types of available counter reports

        ``GET /counter-reports/reports/types``

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Counterreports_get_types_return.schema 
        """
        return self.call("GET", "/counter-reports/reports/types")

    def set_delete(self, delete: dict):
        """Delete multiple counter reports

        ``POST /counter-reports/reports/delete``

        Args:
            delete (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Counterreports_set_delete_request.schema
        """
        return self.call("POST", "/counter-reports/reports/delete", data=delete)


class Usagedataproviders(FolioApi):
    """mod-erm-usage API

    This documents the API calls that can be made to query and manage usage data providers
    """

    def get_usageDataProviders(self, **kwargs):
        """Get all usage data providers

        ``GET /usage-data-providers``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - ((label="Journal*" or vendor="Journal*" or platform="Journal*" or harvestingConfig.aggregator.name="Journal*") and harvestingConfig.harvestingStatus="active" and harvestingConfig.harvestVia="sushi" and hasFailedReport="no") sortby label
            orderBy (str):  Order by field: label, harvestingConfig.harvestingStatus, latestReport, harvestingConfig.aggregator.name
                    
            order (str (desc|asc):): (default=desc) Order
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

        Schema:

            .. literalinclude:: ../files/Usagedataproviders_get_usageDataProviders_return.schema 
        """
        return self.call("GET", "/usage-data-providers", query=kwargs)

    def set_usageDataProvider(self, usageDataProvider: dict):
        """Post new usage data providers

        ``POST /usage-data-providers``

        Args:
            usageDataProvider (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created usageDataProvider item

        Schema:

            .. literalinclude:: ../files/Usagedataproviders_set_usageDataProvider_request.schema
        """
        return self.call("POST", "/usage-data-providers", data=usageDataProvider)

    def get_usageDataProvider(self, usageDataProvidersId: str):
        """Get one usage data provider identified by id

        ``GET /usage-data-providers/{usageDataProvidersId}``

        Args:
            usageDataProvidersId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Usagedataproviders_get_usageDataProvider_return.schema 
        """
        return self.call("GET", f"/usage-data-providers/{usageDataProvidersId}")

    def delete_usageDataProvider(self, usageDataProvidersId: str):
        """Delete an usage data provider identified by id

        ``DELETE /usage-data-providers/{usageDataProvidersId}``

        Args:
            usageDataProvidersId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/usage-data-providers/{usageDataProvidersId}")

    def modify_usageDataProvider(self, usageDataProvidersId: str, usageDataProvider: dict):
        """Put an usage data provider identified by id

        ``PUT /usage-data-providers/{usageDataProvidersId}``

        Args:
            usageDataProvidersId (str)
            usageDataProvider (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Usagedataproviders_modify_usageDataProvider_request.schema
        """
        return self.call("PUT", f"/usage-data-providers/{usageDataProvidersId}", data=usageDataProvider)


class Aggregatorsettings(FolioApi):
    """mod-erm-usage API

    This documents the API calls that can be made to query and manage aggregator settings
    """

    def get_aggregatorSettings(self, **kwargs):
        """Get all aggregator settings

        ``GET /aggregator-settings``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - (label="Server*") and aggregatorConfig.reportRelease="4"
            orderBy (str):  Order by field: label
                    
            order (str (desc|asc):): (default=desc) Order
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

        Schema:

            .. literalinclude:: ../files/Aggregatorsettings_get_aggregatorSettings_return.schema 
        """
        return self.call("GET", "/aggregator-settings", query=kwargs)

    def set_aggregatorSetting(self, aggregatorSetting: dict):
        """Post new aggregator settings

        ``POST /aggregator-settings``

        Args:
            aggregatorSetting (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created aggregatorSetting item

        Schema:

            .. literalinclude:: ../files/Aggregatorsettings_set_aggregatorSetting_request.schema
        """
        return self.call("POST", "/aggregator-settings", data=aggregatorSetting)

    def get_aggregatorSetting(self, aggregatorSettingsId: str):
        """Get one aggregator setting identified by id

        ``GET /aggregator-settings/{aggregatorSettingsId}``

        Args:
            aggregatorSettingsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Aggregatorsettings_get_aggregatorSetting_return.schema 
        """
        return self.call("GET", f"/aggregator-settings/{aggregatorSettingsId}")

    def delete_aggregatorSetting(self, aggregatorSettingsId: str):
        """Delete aggregator setting identified by id

        ``DELETE /aggregator-settings/{aggregatorSettingsId}``

        Args:
            aggregatorSettingsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/aggregator-settings/{aggregatorSettingsId}")

    def modify_aggregatorSetting(self, aggregatorSettingsId: str, aggregatorSetting: dict):
        """Put aggregator setting identified by id

        ``PUT /aggregator-settings/{aggregatorSettingsId}``

        Args:
            aggregatorSettingsId (str)
            aggregatorSetting (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Aggregatorsettings_modify_aggregatorSetting_request.schema
        """
        return self.call("PUT", f"/aggregator-settings/{aggregatorSettingsId}", data=aggregatorSetting)

    def get_exportcredentials_by_aggregatorSetting(self, aggregatorSettingsId: str, **kwargs):
        """Get SushiCredentials associated with this aggregator

        ``GET /aggregator-settings/{aggregatorSettingsId}/exportcredentials``

        Args:
            aggregatorSettingsId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            format (str): (default=csv) Specify export format (default is CSV)

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("GET", f"/aggregator-settings/{aggregatorSettingsId}/exportcredentials", query=kwargs)
