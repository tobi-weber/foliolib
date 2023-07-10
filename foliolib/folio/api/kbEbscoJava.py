# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.kbEbscoJava")


class KbCredentials(FolioApi):
    """mod-kb-ebsco-java

    Implements the eholdings interface using EBSCO KB as backend.
    """

    def get_kbCredentials(self):
        """Get a collection of KB credentials.

        ``GET /eholdings/kb-credentials``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/KbCredentials_get_kbCredentials_return.schema 
        """
        return self.call("GET", "/eholdings/kb-credentials")

    def set_kbCredential(self, kbCredential: dict):
        """Create KB credentials

        ``POST /eholdings/kb-credentials``

        Args:
            kbCredential (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/KbCredentials_set_kbCredential_request.schema
            .. literalinclude:: ../files/KbCredentials_set_kbCredential_return.schema 
        """
        return self.call("POST", "/eholdings/kb-credentials", data=kbCredential)

    def get_kbCredential(self, kbCredentialsId: str):
        """Get a specific KB credentials by id.

        ``GET /eholdings/kb-credentials/{kbCredentialsId}``

        Args:
            kbCredentialsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/KbCredentials_get_kbCredential_return.schema 
        """
        return self.call("GET", f"/eholdings/kb-credentials/{kbCredentialsId}")

    def modify_kbCredential(self, kbCredentialsId: str, kbCredential: dict):
        """Update KB credentials

        ``PUT /eholdings/kb-credentials/{kbCredentialsId}``

        Args:
            kbCredentialsId (str)
            kbCredential (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/KbCredentials_modify_kbCredential_request.schema
        """
        return self.call("PUT", f"/eholdings/kb-credentials/{kbCredentialsId}", data=kbCredential)

    def delete_kbCredential(self, kbCredentialsId: str):
        """Delete KB Credentials

        ``DELETE /eholdings/kb-credentials/{kbCredentialsId}``

        Args:
            kbCredentialsId (str)

        Raises:
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/eholdings/kb-credentials/{kbCredentialsId}")

    def get_key_by_kbCredential(self, kbCredentialsId: str):
        """Get a specific KB credentials key by id.

        ``GET /eholdings/kb-credentials/{kbCredentialsId}/key``

        Args:
            kbCredentialsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/KbCredentials_get_key_by_kbCredential_return.schema 
        """
        return self.call("GET", f"/eholdings/kb-credentials/{kbCredentialsId}/key")

    def get_userKbCredentials(self):
        """Retrieve KB credentials by given assigned user

        ``GET /eholdings/user-kb-credential``

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/KbCredentials_get_userKbCredentials_return.schema 
        """
        return self.call("GET", "/eholdings/user-kb-credential")


class Currencies(FolioApi):
    """mod-kb-ebsco-java

    Implements the eholdings interface using EBSCO KB as backend.
    """

    def get_currencies(self):
        """Retrieve a collection of currencies.

        ``GET /eholdings/currencies``

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/Currencies_get_currencies_return.schema 
        """
        return self.call("GET", "/eholdings/currencies")


class Export(FolioApi):
    """mod-kb-ebsco-java

    Implements the eholdings interface using EBSCO KB as backend.
    """

    def get_export_by_package(self, packageId: str, **kwargs):
        """Endpoint provides a cost-per-use information about the titles included into the package in csv format.

        ``GET /eholdings/packages/{packageId}/resources/costperuse/export``

        Args:
            packageId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            platform (str):  Include publisher, non-publisher or all platforms
                    Possible values are
                     - publisher
                     - nonPublisher
                     - all
                    
            fiscalYear (str):  Fiscal year of cost-per-use data

        Raises:
            OkapiFatalError: Server Error
        """
        return self.call("GET", f"/eholdings/packages/{packageId}/resources/costperuse/export", query=kwargs)


class Tags(FolioApi):
    """mod-kb-ebsco-java

    Implements the eholdings interface using EBSCO KB as backend.
    """

    def get_tags(self, **kwargs):
        """Retrieve a collection of tags associated with eholding records.

        ``GET /eholdings/tags``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            filter[rectype] (recordType[]):  Filter tags by one or more record types. Several types can be specified in form of `filter[rectype]=provider&filter[rectype]=package` Possible values are `provider`, `package`, `title`, `resource`
                    
                    Example:
                    
                     - ['provider', 'package']

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request

        Schema:

            .. literalinclude:: ../files/Tags_get_tags_return.schema 
        """
        return self.call("GET", "/eholdings/tags", query=kwargs)

    def get_summaries(self, **kwargs):
        """Retrieve a collection of unique tags associated with eholding records.

        ``GET /eholdings/tags/summary``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            filter[rectype] (recordType[]):  Filter tags by one or more record types. Several types can be specified in form of `filter[rectype]=provider&filter[rectype]=package` Possible values are `provider`, `package`, `title`, `resource`
                    
                    Example:
                    
                     - ['provider', 'package']

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request

        Schema:

            .. literalinclude:: ../files/Tags_get_summaries_return.schema 
        """
        return self.call("GET", "/eholdings/tags/summary", query=kwargs)


class Uc(FolioApi):
    """mod-kb-ebsco-java

    Implements the eholdings interface using EBSCO KB as backend.
    """

    def get_uc_by_kbCredential(self, kbCredentialsId: str, **kwargs):
        """Retrieve a Usage Consolidation settings.

        ``GET /eholdings/kb-credentials/{kbCredentialsId}/uc``

        Args:
            kbCredentialsId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            metrictype (bool): (default=False) Indicates that metric type should be included

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/Uc_get_uc_by_kbCredential_return.schema 
        """
        return self.call("GET", f"/eholdings/kb-credentials/{kbCredentialsId}/uc", query=kwargs)

    def set_uc(self, kbCredentialsId: str, uc: dict):
        """Create a new Usage Consolidation Settings

        ``POST /eholdings/kb-credentials/{kbCredentialsId}/uc``

        Args:
            kbCredentialsId (str)
            uc (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Uc_set_uc_request.schema
            .. literalinclude:: ../files/Uc_set_uc_return.schema 
        """
        return self.call("POST", f"/eholdings/kb-credentials/{kbCredentialsId}/uc", data=uc)

    def get_key_by_kbCredential(self, kbCredentialsId: str):
        """Retrieve a Usage Consolidation settings customer key.

        ``GET /eholdings/kb-credentials/{kbCredentialsId}/uc/key``

        Args:
            kbCredentialsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/Uc_get_key_by_kbCredential_return.schema 
        """
        return self.call("GET", f"/eholdings/kb-credentials/{kbCredentialsId}/uc/key")

    def get_ucs(self, **kwargs):
        """Retrieve a Usage Consolidation settings.

        ``GET /eholdings/uc``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            metrictype (bool): (default=False) Indicates that metric type should be included

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/Uc_get_ucs_return.schema 
        """
        return self.call("GET", "/eholdings/uc", query=kwargs)

    def get_ucCredentials(self):
        """Check if Usage Consolidation credentials exists.

        ``GET /eholdings/uc-credentials``

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/Uc_get_ucCredentials_return.schema 
        """
        return self.call("GET", "/eholdings/uc-credentials")

    def modify_ucCredential(self, ucCredential: dict):
        """Update Usage Consolidation credentials

        ``PUT /eholdings/uc-credentials``

        Args:
            ucCredential (dict): See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Uc_modify_ucCredential_request.schema
        """
        return self.call("PUT", "/eholdings/uc-credentials", data=ucCredential)

    def get_clientIds(self):
        """Get Usage Consolidation client id

        ``GET /eholdings/uc-credentials/clientId``

        Returns:
            str: See Schema below

        Schema:

            .. literalinclude:: ../files/Uc_get_clientIds_return.schema 
        """
        return self.call("GET", "/eholdings/uc-credentials/clientId")

    def get_clientSecrets(self):
        """Get Usage Consolidation client secret

        ``GET /eholdings/uc-credentials/clientSecret``

        Returns:
            str: See Schema below

        Schema:

            .. literalinclude:: ../files/Uc_get_clientSecrets_return.schema 
        """
        return self.call("GET", "/eholdings/uc-credentials/clientSecret")


class AccessTypes(FolioApi):
    """mod-kb-ebsco-java

    Implements the eholdings interface using EBSCO KB as backend.
    """

    def get_accessTypes(self):
        """Get a list of access types.

        ``GET /eholdings/access-types``

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/AccessTypes_get_accessTypes_return.schema 
        """
        return self.call("GET", "/eholdings/access-types")

    def get_accessType(self, accessTypesId: str):
        """Retrieve specific Access Types by Id

        ``GET /eholdings/access-types/{accessTypesId}``

        Args:
            accessTypesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/AccessTypes_get_accessType_return.schema 
        """
        return self.call("GET", f"/eholdings/access-types/{accessTypesId}")

    def get_accessTypes_by_kbCredential(self, kbCredentialsId: str):
        """Get a list of access types related to specific KB credentials.

        ``GET /eholdings/kb-credentials/{kbCredentialsId}/access-types``

        Args:
            kbCredentialsId (str)

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/AccessTypes_get_accessTypes_by_kbCredential_return.schema 
        """
        return self.call("GET", f"/eholdings/kb-credentials/{kbCredentialsId}/access-types")

    def set_accessType(self, kbCredentialsId: str, accessType: dict):
        """Create an access type in specific KB Credentials

        ``POST /eholdings/kb-credentials/{kbCredentialsId}/access-types``

        Args:
            kbCredentialsId (str)
            accessType (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AccessTypes_set_accessType_request.schema
            .. literalinclude:: ../files/AccessTypes_set_accessType_return.schema 
        """
        return self.call("POST", f"/eholdings/kb-credentials/{kbCredentialsId}/access-types", data=accessType)

    def get_accessType_for_kbCredential(self, kbCredentialsId: str, accessTypeId: str):
        """Retrieve specific Access Types by Id related to specific KB credentials

        ``GET /eholdings/kb-credentials/{kbCredentialsId}/access-types/{accessTypeId}``

        Args:
            kbCredentialsId (str)
            accessTypeId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/AccessTypes_get_accessType_for_kbCredential_return.schema 
        """
        return self.call("GET", f"/eholdings/kb-credentials/{kbCredentialsId}/access-types/{accessTypeId}")

    def modify_accessType(self, kbCredentialsId: str, accessTypeId: str, accessType: dict):
        """Update a Access Type by Id related to specific KB credentials

        ``PUT /eholdings/kb-credentials/{kbCredentialsId}/access-types/{accessTypeId}``

        Args:
            kbCredentialsId (str)
            accessTypeId (str)
            accessType (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AccessTypes_modify_accessType_request.schema
        """
        return self.call("PUT", f"/eholdings/kb-credentials/{kbCredentialsId}/access-types/{accessTypeId}", data=accessType)

    def delete_accessType(self, kbCredentialsId: str, accessTypeId: str):
        """Delete a Access Type by Id

        ``DELETE /eholdings/kb-credentials/{kbCredentialsId}/access-types/{accessTypeId}``

        Args:
            kbCredentialsId (str)
            accessTypeId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity
        """
        return self.call("DELETE", f"/eholdings/kb-credentials/{kbCredentialsId}/access-types/{accessTypeId}")


class Costperuse(FolioApi):
    """mod-kb-ebsco-java

    Implements the eholdings interface using EBSCO KB as backend.
    """

    def get_costperuse_by_resource(self, resourceId: str, **kwargs):
        """Retrieve cost-per-use information for a particular resource

        ``GET /eholdings/resources/{resourceId}/costperuse``

        Args:
            resourceId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            platform (str):  Include publisher, non-publisher or all platforms
                    Possible values are
                     - publisher
                     - nonPublisher
                     - all
                    
            fiscalYear (str):  Fiscal year of cost-per-use data

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Costperuse_get_costperuse_by_resource_return.schema 
        """
        return self.call("GET", f"/eholdings/resources/{resourceId}/costperuse", query=kwargs)

    def get_costperuse_by_title(self, titleId: str, **kwargs):
        """Retrieve cost-per-use information for a particular title

        ``GET /eholdings/titles/{titleId}/costperuse``

        Args:
            titleId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            platform (str):  Include publisher, non-publisher or all platforms
                    Possible values are
                     - publisher
                     - nonPublisher
                     - all
                    
            fiscalYear (str):  Fiscal year of cost-per-use data

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Costperuse_get_costperuse_by_title_return.schema 
        """
        return self.call("GET", f"/eholdings/titles/{titleId}/costperuse", query=kwargs)

    def get_costperuse_by_package_by_packageId(self, packageId: str, **kwargs):
        """Retrieve cost-per-use information for a particular package

        ``GET /eholdings/packages/{packageId}/costperuse``

        Args:
            packageId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            platform (str):  Include publisher, non-publisher or all platforms
                    Possible values are
                     - publisher
                     - nonPublisher
                     - all
                    
            fiscalYear (str):  Fiscal year of cost-per-use data

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Costperuse_get_costperuse_by_package_by_packageId_return.schema 
        """
        return self.call("GET", f"/eholdings/packages/{packageId}/costperuse", query=kwargs)

    def get_costperuse_by_package(self, packageId: str, **kwargs):
        """Retrieve cost-per-use information for package resources

        ``GET /eholdings/packages/{packageId}/resources/costperuse``

        Args:
            packageId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            platform (str):  Include publisher, non-publisher or all platforms
                    Possible values are
                     - publisher
                     - nonPublisher
                     - all
                    
            fiscalYear (str):  Fiscal year of cost-per-use data
            order (order): (default=asc) Order
            sort (str): (default=name) Option by which results are sorted. Possible values are name, type, cost, usage, costperuse, percent.
            page (int): (default=1) Page number
                    
                    Example:
                    
                     - 1
            count (int): (default=<<defaultCountValue>>) Page size
                    
                    Example:
                    
                     - 100

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Costperuse_get_costperuse_by_package_return.schema 
        """
        return self.call("GET", f"/eholdings/packages/{packageId}/resources/costperuse", query=kwargs)


class Proxies(FolioApi):
    """mod-kb-ebsco-java

    Implements the eholdings interface using EBSCO KB as backend.
    """

    def get_proxyTypes(self):
        """Get a list of supported proxy types.

        ``GET /eholdings/proxy-types``

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/Proxies_get_proxyTypes_return.schema 
        """
        return self.call("GET", "/eholdings/proxy-types")

    def get_proxyTypes_by_kbCredential(self, kbCredentialsId: str):
        """Get a list of supported proxy types for KB Credentials.

        ``GET /eholdings/kb-credentials/{kbCredentialsId}/proxy-types``

        Args:
            kbCredentialsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/Proxies_get_proxyTypes_by_kbCredential_return.schema 
        """
        return self.call("GET", f"/eholdings/kb-credentials/{kbCredentialsId}/proxy-types")

    def get_rootProxies(self):
        """Get the ID of root proxy that is currently selected from proxy-type list.

        ``GET /eholdings/root-proxy``

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/Proxies_get_rootProxies_return.schema 
        """
        return self.call("GET", "/eholdings/root-proxy")

    def get_rootProxy_by_kbCredential(self, kbCredentialsId: str):
        """Get the ID of root proxy that is currently selected from proxy-type list.

        ``GET /eholdings/kb-credentials/{kbCredentialsId}/root-proxy``

        Args:
            kbCredentialsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/Proxies_get_rootProxy_by_kbCredential_return.schema 
        """
        return self.call("GET", f"/eholdings/kb-credentials/{kbCredentialsId}/root-proxy")

    def modify_rootProxy(self, kbCredentialsId: str, rootProxy: dict):
        """Update root-proxy for a Kb Credentials.

        ``PUT /eholdings/kb-credentials/{kbCredentialsId}/root-proxy``

        Args:
            kbCredentialsId (str)
            rootProxy (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Proxies_modify_rootProxy_request.schema
            .. literalinclude:: ../files/Proxies_modify_rootProxy_return.schema 
        """
        return self.call("PUT", f"/eholdings/kb-credentials/{kbCredentialsId}/root-proxy", data=rootProxy)


class Packages(FolioApi):
    """mod-kb-ebsco-java

    Implements the eholdings interface using EBSCO KB as backend.
    """

    def get_packages(self, **kwargs):
        """Retrieve a collection of packages based on the search query.

        ``GET /eholdings/packages``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            filter[custom] (str):  Filter to get list of custom packages
                    Possible values are
                      - true
                    
                    
                    Example:
                    
                     - true
            q (str):  String used to search to retrieve a collection
                    
                    Example:
                    
                     - ABC-CLIO
            filter[selected] (str):  Filter to narrow down results based on selection status. Possible values are all, true, false, ebsco.
                    
                    Example:
                    
                     - all
            filter[type] (str): (default=all) Filter to narrow down results based on content type. Defaults to all.
                    Possible values are all, aggregatedfulltext, abstractandindex, ebook, ejournal, print, unknown, streamingmedia, mixedcontent, onlinereference.
                    
                    
                    Example:
                    
                     - ebook
            filter[tags] (list):  Filter to narrow down results based on assigned tags. Contains list of required tags.
            filter[access-type] (list):  Filter to narrow down results based on assigned access type.
            sort (str): (default=relevance) Option by which results are sorted. Possible values are name, relevance.
            page (int): (default=1) Page number
                    
                    Example:
                    
                     - 1
            count (int): (default=<<defaultCountValue>>) Page size
                    
                    Example:
                    
                     - 100

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request

        Schema:

            .. literalinclude:: ../files/Packages_get_packages_return.schema 
        """
        return self.call("GET", "/eholdings/packages", query=kwargs)

    def set_package(self, package: dict):
        """Create a custom package

        ``POST /eholdings/packages``

        Args:
            package (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Packages_set_package_request.schema
            .. literalinclude:: ../files/Packages_set_package_return.schema 
        """
        return self.call("POST", "/eholdings/packages", data=package)

    def get_package(self, packageId: str, **kwargs):
        """Retrieve a specific package given packageId.
        Note that packageId is providerId-packageId

        ``GET /eholdings/packages/{packageId}``

        Args:
            packageId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            include (str):  Include resources or provider in response
                    Possible values are
                      - resources
                      - provider
                    
                    
                    Example:
                    
                     - resources

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/Packages_get_package_return.schema 
        """
        return self.call("GET", f"/eholdings/packages/{packageId}", query=kwargs)

    def modify_package(self, packageId: str, package: dict):
        """Update a managed or custom package using packageId
        Note that packageId is providerId-packageId

        ``PUT /eholdings/packages/{packageId}``

        Args:
            packageId (str)
            package (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Packages_modify_package_request.schema
            .. literalinclude:: ../files/Packages_modify_package_return.schema 
        """
        return self.call("PUT", f"/eholdings/packages/{packageId}", data=package)

    def delete_package(self, packageId: str):
        """Delete a specific custom package using packageId.
        Note that packageId is providerId-packageId

        ``DELETE /eholdings/packages/{packageId}``

        Args:
            packageId (str)

        Raises:
            OkapiRequestError: Bad Request
        """
        return self.call("DELETE", f"/eholdings/packages/{packageId}")

    def get_resources_by_package(self, packageId: str, **kwargs):
        """Include all resources belonging to a specific package

        ``GET /eholdings/packages/{packageId}/resources``

        Args:
            packageId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            filter[tags] (list):  Filter to narrow down results based on assigned tags. Contains list of required tags.
            filter[access-type] (list):  Filter to narrow down results based on assigned access type.
            filter[selected] (str):  Filter to narrow down results based on selection status. Defaults to all. Possible values are all, true, false, ebsco.
                    
                    Example:
                    
                     - ebsco
            filter[type] (str):  Filter to narrow down results based on content type. 
                    Possible values are all, audiobook, book, bookseries, database, journal, newsletter, newspaper, proceedings, report, streamingaudio, streamingvideo,thesisdissertation, website, unspecified.
                    
            filter[name] (str):  String to search title name to get a collection of titles
                    
                    Example:
                    
                     - War and Peace
            filter[isxn] (str):  String to search ISSN and ISBN to get a collection of titles
                    
                    Example:
                    
                     - 1050-3331
            filter[subject] (str):  String to search subjects to get a collection of titles
                    
                    Example:
                    
                     - history
            filter[publisher] (str):  String to search publishers to get a collection of titles
                    
                    Example:
                    
                     - academic
            sort (str): (default=relevance) Option by which results are sorted. Possible values are name, relevance.
            page (int): (default=1) Page number
                    
                    Example:
                    
                     - 1
            count (int): (default=<<defaultCountValue>>) Page size
                    
                    Example:
                    
                     - 100

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/Packages_get_resources_by_package_return.schema 
        """
        return self.call("GET", f"/eholdings/packages/{packageId}/resources", query=kwargs)

    def modify_tag(self, packageId: str, tag: dict):
        """Update tags assigned to package

        ``PUT /eholdings/packages/{packageId}/tags``

        Args:
            packageId (str)
            tag (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Packages_modify_tag_request.schema
            .. literalinclude:: ../files/Packages_modify_tag_return.schema 
        """
        return self.call("PUT", f"/eholdings/packages/{packageId}/tags", data=tag)

    def set_fetch(self, fetch: dict):
        """

        ``POST /eholdings/packages/bulk/fetch``

        Args:
            fetch (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Packages_set_fetch_request.schema
            .. literalinclude:: ../files/Packages_set_fetch_return.schema 
        """
        return self.call("POST", "/eholdings/packages/bulk/fetch", data=fetch)


class AssignedUsers(FolioApi):
    """mod-kb-ebsco-java

    Implements the eholdings interface using EBSCO KB as backend.
    """

    def get_users_by_kbCredential(self, kbCredentialsId: str):
        """Retrieve users information assigned to a specific KB credentials.

        ``GET /eholdings/kb-credentials/{kbCredentialsId}/users``

        Args:
            kbCredentialsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request

        Schema:

            .. literalinclude:: ../files/AssignedUsers_get_users_by_kbCredential_return.schema 
        """
        return self.call("GET", f"/eholdings/kb-credentials/{kbCredentialsId}/users")

    def set_user(self, kbCredentialsId: str, user: dict):
        """Assign user to a specific KB credentials.

        ``POST /eholdings/kb-credentials/{kbCredentialsId}/users``

        Args:
            kbCredentialsId (str)
            user (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/AssignedUsers_set_user_request.schema
            .. literalinclude:: ../files/AssignedUsers_set_user_return.schema 
        """
        return self.call("POST", f"/eholdings/kb-credentials/{kbCredentialsId}/users", data=user)

    def delete_user(self, kbCredentialsId: str, userId: str):
        """Remove association between user and KB Credentials

        ``DELETE /eholdings/kb-credentials/{kbCredentialsId}/users/{userId}``

        Args:
            kbCredentialsId (str)
            userId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
        """
        return self.call("DELETE", f"/eholdings/kb-credentials/{kbCredentialsId}/users/{userId}")


class CustomLabels(FolioApi):
    """mod-kb-ebsco-java

    Implements the eholdings interface using EBSCO KB as backend.
    """

    def get_customLabels(self):
        """Get a list of custom labels.

        ``GET /eholdings/custom-labels``

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/CustomLabels_get_customLabels_return.schema 
        """
        return self.call("GET", "/eholdings/custom-labels")

    def get_customLabels_by_kbCredential(self, kbCredentialsId: str):
        """Get a custom labels related to specific KB credentials

        ``GET /eholdings/kb-credentials/{kbCredentialsId}/custom-labels``

        Args:
            kbCredentialsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/CustomLabels_get_customLabels_by_kbCredential_return.schema 
        """
        return self.call("GET", f"/eholdings/kb-credentials/{kbCredentialsId}/custom-labels")

    def modify_customLabel(self, kbCredentialsId: str, customLabel: dict):
        """Update a list of custom labels.

        ``PUT /eholdings/kb-credentials/{kbCredentialsId}/custom-labels``

        Args:
            kbCredentialsId (str)
            customLabel (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/CustomLabels_modify_customLabel_request.schema
            .. literalinclude:: ../files/CustomLabels_modify_customLabel_return.schema 
        """
        return self.call("PUT", f"/eholdings/kb-credentials/{kbCredentialsId}/custom-labels", data=customLabel)


class Providers(FolioApi):
    """mod-kb-ebsco-java

    Implements the eholdings interface using EBSCO KB as backend.
    """

    def get_providers(self, **kwargs):
        """Get a list of providers based on the search query.

        ``GET /eholdings/providers``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            q (str):  String used to search to retrieve a collection
                    
                    Example:
                    
                     - ABC-CLIO
            filter[tags] (list):  Filter to narrow down results based on assigned tags. Contains list of required tags.
            sort (str): (default=relevance) Option by which results are sorted. Possible values are name, relevance.
            page (int): (default=1) Page number
                    
                    Example:
                    
                     - 1
            count (int): (default=<<defaultCountValue>>) Page size
                    
                    Example:
                    
                     - 100

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/Providers_get_providers_return.schema 
        """
        return self.call("GET", "/eholdings/providers", query=kwargs)

    def get_provider(self, providerId: str, **kwargs):
        """Get provider given providerId

        ``GET /eholdings/providers/{providerId}``

        Args:
            providerId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            include (str):  Name of nested resource to include
                    
                    Example:
                    
                     - packages

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/Providers_get_provider_return.schema 
        """
        return self.call("GET", f"/eholdings/providers/{providerId}", query=kwargs)

    def modify_provider(self, providerId: str, provider: dict):
        """Update proxy and token information for a given provider Id.

        ``PUT /eholdings/providers/{providerId}``

        Args:
            providerId (str)
            provider (dict): See Schema below

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/Providers_modify_provider_request.schema
            .. literalinclude:: ../files/Providers_modify_provider_return.schema 
        """
        return self.call("PUT", f"/eholdings/providers/{providerId}", data=provider)

    def modify_tag(self, providerId: str, tag: dict):
        """Update tags assigned to provider

        ``PUT /eholdings/providers/{providerId}/tags``

        Args:
            providerId (str)
            tag (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Providers_modify_tag_request.schema
            .. literalinclude:: ../files/Providers_modify_tag_return.schema 
        """
        return self.call("PUT", f"/eholdings/providers/{providerId}/tags", data=tag)

    def get_packages_by_provider(self, providerId: str, **kwargs):
        """Search within a list of packages associated with a given provider.

        ``GET /eholdings/providers/{providerId}/packages``

        Args:
            providerId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            q (str):  String used to search to retrieve a collection
                    
                    Example:
                    
                     - ABC-CLIO
            filter[tags] (list):  Filter to narrow down results based on assigned tags. Contains list of required tags.
            filter[access-type] (list):  Filter to narrow down results based on assigned access type.
            filter[selected] (str):  Filter to narrow down results based on selection status. Possible values are all, true, false, ebsco.
                    
                    Example:
                    
                     - all
            filter[type] (str): (default=all) Filter to narrow down results based on content type. Defaults to all.
                    Possible values are all, aggregatedfulltext, abstractandindex, ebook, ejournal, print, unknown, streamingmedia, mixedcontent, onlinereference.
                    
                    
                    Example:
                    
                     - ebook
            sort (str): (default=relevance) Option by which results are sorted. Possible values are name, relevance.
            page (int): (default=1) Page number
                    
                    Example:
                    
                     - 1
            count (int): (default=<<defaultCountValue>>) Page size
                    
                    Example:
                    
                     - 100

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/Providers_get_packages_by_provider_return.schema 
        """
        return self.call("GET", f"/eholdings/providers/{providerId}/packages", query=kwargs)


class Resources(FolioApi):
    """mod-kb-ebsco-java

    Implements the eholdings interface using EBSCO KB as backend.
    """

    def set_resource(self, resource: dict):
        """Create a relation between an existing custom package and an existing custom/managed title.

        ``POST /eholdings/resources``

        Args:
            resource (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Resources_set_resource_request.schema
            .. literalinclude:: ../files/Resources_set_resource_return.schema 
        """
        return self.call("POST", "/eholdings/resources", data=resource)

    def get_resource(self, resourceId: str, **kwargs):
        """Retrieve a specific resource given resourceId.
        Note that a resource is a managed/custom title associated with a managed/custom package.
        resourceId is providerId-packageId-titleId

        ``GET /eholdings/resources/{resourceId}``

        Args:
            resourceId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            include (str):  Include provider, package or title in response
                    Possible values are
                     - provider
                     - package
                     - title
                    
                    
                    Example:
                    
                     - provider

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/Resources_get_resource_return.schema 
        """
        return self.call("GET", f"/eholdings/resources/{resourceId}", query=kwargs)

    def modify_resource(self, resourceId: str, resource: dict):
        """Update a managed or custom resource using resourceId
        Note that resourceId is providerId-packageId-titleId

        ``PUT /eholdings/resources/{resourceId}``

        Args:
            resourceId (str)
            resource (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Resources_modify_resource_request.schema
            .. literalinclude:: ../files/Resources_modify_resource_return.schema 
        """
        return self.call("PUT", f"/eholdings/resources/{resourceId}", data=resource)

    def delete_resource(self, resourceId: str):
        """Delete the association between a custom/managed title and a custom package using resourceId.
        Note that resourceId is providerId-packageId-titleId
        If the title is custom and is not associated with any other package, then the title will be deleted from the knowledge base.

        ``DELETE /eholdings/resources/{resourceId}``

        Args:
            resourceId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
        """
        return self.call("DELETE", f"/eholdings/resources/{resourceId}")

    def modify_tag(self, resourceId: str, tag: dict):
        """Update tags assigned to resource

        ``PUT /eholdings/resources/{resourceId}/tags``

        Args:
            resourceId (str)
            tag (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Resources_modify_tag_request.schema
            .. literalinclude:: ../files/Resources_modify_tag_return.schema 
        """
        return self.call("PUT", f"/eholdings/resources/{resourceId}/tags", data=tag)

    def set_fetch(self, fetch: dict):
        """

        ``POST /eholdings/resources/bulk/fetch``

        Args:
            fetch (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Resources_set_fetch_request.schema
            .. literalinclude:: ../files/Resources_set_fetch_return.schema 
        """
        return self.call("POST", "/eholdings/resources/bulk/fetch", data=fetch)


class Titles(FolioApi):
    """

    
    """

    def get_titles(self, **kwargs):
        """Get a set of titles matching the given search criteria.

        ``GET /eholdings/titles``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            filter[tags] (list):  Filter to narrow down results based on assigned tags. Contains list of required tags.
            filter[access-type] (list):  Filter to narrow down results based on assigned access type.
            filter[selected] (str):  Filter to narrow down results based on selection status. Defaults to all. Possible values are all, true, false, ebsco.
                    
                    Example:
                    
                     - ebsco
            filter[type] (str):  Filter to narrow down results based on content type. 
                    Possible values are all, audiobook, book, bookseries, database, journal, newsletter, newspaper, proceedings, report, streamingaudio, streamingvideo,thesisdissertation, website, unspecified.
                    
            filter[name] (str):  String to search title name to get a collection of titles
                    
                    Example:
                    
                     - War and Peace
            filter[isxn] (str):  String to search ISSN and ISBN to get a collection of titles
                    
                    Example:
                    
                     - 1050-3331
            filter[subject] (str):  String to search subjects to get a collection of titles
                    
                    Example:
                    
                     - history
            filter[publisher] (str):  String to search publishers to get a collection of titles
                    
                    Example:
                    
                     - academic
            filter[packageIds] (list):  Search by package ids.
            include (str):  Include related resource objects, each representing a partnering of this title with a package.
                    Any bogus value, like `include=deciduousTrees`, will be silently ignored.
                    
                    
                    Example:
                    
                     - resources
            sort (str): (default=relevance) Option by which results are sorted. Possible values are name, relevance.
            page (int): (default=1) Page number
                    
                    Example:
                    
                     - 1
            count (int): (default=<<defaultCountValue>>) Page size
                    
                    Example:
                    
                     - 100

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/Titles_get_titles_return.schema 
        """
        return self.call("GET", "/eholdings/titles", query=kwargs)

    def set_title(self, title: dict):
        """Create a new Custom Title.

        ``POST /eholdings/titles``

        Args:
            title (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Titles_set_title_request.schema
            .. literalinclude:: ../files/Titles_set_title_return.schema 
        """
        return self.call("POST", "/eholdings/titles", data=title)

    def get_title(self, titleId: str, **kwargs):
        """Get the title by its unique identifier.

        ``GET /eholdings/titles/{titleId}``

        Args:
            titleId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            include (str):  Include related resource objects, each representing a partnering of this title with a package.
                    Any bogus value, like `include=deciduousTrees`, will be silently ignored.
                    
                    
                    Example:
                    
                     - resources

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found

        Schema:

            .. literalinclude:: ../files/Titles_get_title_return.schema 
        """
        return self.call("GET", f"/eholdings/titles/{titleId}", query=kwargs)

    def modify_title(self, titleId: str, title: dict):
        """Update Custom Title.

        ``PUT /eholdings/titles/{titleId}``

        Args:
            titleId (str)
            title (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Titles_modify_title_request.schema
            .. literalinclude:: ../files/Titles_modify_title_return.schema 
        """
        return self.call("PUT", f"/eholdings/titles/{titleId}", data=title)


class Eholdings(FolioApi):
    """mod-kb-ebsco-java

    Implements the eholdings interface using EBSCO KB as backend.
    """

    def get_statuses(self):
        """Gives status of currently set KB configuration.

        ``GET /eholdings/status``

        Returns:
            dict: See Schema below

        Raises:
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Eholdings_get_statuses_return.schema 
        """
        return self.call("GET", "/eholdings/status")

    def delete_caches(self):
        """Invalidate configuration cache for tenant

        ``DELETE /eholdings/cache``
        """
        return self.call("DELETE", "/eholdings/cache")

    def set_kbCredential(self):
        """Run load holdings job.

        ``POST /eholdings/loading/kb-credentials``

        Raises:
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
        """
        return self.call("POST", "/eholdings/loading/kb-credentials")

    def set_kbCredential_by_kbCredentialsId(self, kbCredentialsId: str):
        """Run load holdings job by credentials id.

        ``POST /eholdings/loading/kb-credentials/{kbCredentialsId}``

        Args:
            kbCredentialsId (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestConflict: Conflict
            OkapiFatalError: Server Error
        """
        return self.call("POST", f"/eholdings/loading/kb-credentials/{kbCredentialsId}")

    def get_status_by_kbCredential(self, kbCredentialsId: str):
        """Get current status of load holdings job.

        ``GET /eholdings/loading/kb-credentials/{kbCredentialsId}/status``

        Args:
            kbCredentialsId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Eholdings_get_status_by_kbCredential_return.schema 
        """
        return self.call("GET", f"/eholdings/loading/kb-credentials/{kbCredentialsId}/status")
