# -*- coding: utf-8 -*-
# Generated at 2024-03-01

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.mgrApplications")



class Am(FolioApi):
    """Manager Applications API

    Manager Applications API
    """

    def registerapplication(self, applicationDescriptor, **kwargs):
        """Register a new application.

        ``POST /applications``

        Args:
            applicationDescriptor (dict): See Schema below.

        Keyword Args:
            check (bool): Whether to run default validation of application descriptor or not
Default validation mode specified in the application properties
 (default: True)

        Returns:
            dict: See Schema below.

        Schema:

            .. literalinclude:: ../files/Am_registerapplication_request.schema
        """
        return self.call("POST", f"/applications", applicationDescriptor, query=kwargs)

		
    def getapplicationsbyquery(self, **kwargs):
        """Retrieve registered application by query.

        ``GET /applications``

        Keyword Args:
            query (str): A CQL query string with search conditions.
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, default: 0)
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 500, default: 10)
            full (bool): Show full information in the response including ModuleDescriptors (default: False)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Am_getapplicationsbyquery_response.schema
        """
        return self.call("GET", "/applications", query=kwargs)

    def getapplicationbyid(self, id_, **kwargs):
        """Retrieve registered application by id.

        ``GET /applications/{id}``

        Keyword Args:
            full (bool): Show full information in the response including ModuleDescriptors (default: False)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Am_getapplicationbyid_response.schema
        """
        return self.call("GET", f"/applications/{id_}", query=kwargs)

		
    def deregisterapplicationbyid(self, id_):
        """De-register (delete) application by id.

        ``DELETE /applications/{id}``

        Raises:
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.
        """
        return self.call("DELETE", f"/applications/{id_}")

    def validateapplicationdescriptor(self, applicationDescriptor, **kwargs):
        """Validate application descriptor.

        ``POST /applications/validate``

        Args:
            applicationDescriptor (dict): See Schema below.

        Keyword Args:
            mode (str): Validation mode to be applied

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Am_validateapplicationdescriptor_request.schema
        """
        return self.call("POST", f"/applications/validate", applicationDescriptor, query=kwargs)

    def getdiscovery(self, id_, **kwargs):
        """Retrieve module discovery info for application referenced by id.

        ``GET /applications/{id}/discovery``

        Keyword Args:
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, default: 0)
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 500, default: 10)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Am_getdiscovery_response.schema
        """
        return self.call("GET", f"/applications/{id_}/discovery", query=kwargs)

    def getmodulebootstrap(self, id_):
        """Retrieve bootstrap information for module referenced by id

        ``GET /modules/{id}``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Am_getmodulebootstrap_response.schema
        """
        return self.call("GET", f"/modules/{id_}")

    def searchmodulediscovery(self, **kwargs):
        """Retrieving module discovery information by CQL query and pagination parameters.

        ``GET /modules/discovery``

        Keyword Args:
            query (str): A CQL query string with search conditions.
            offset (int): Skip over a number of elements by specifying an offset value for the query. (minimum: 0, default: 0)
            limit (int): Limit the number of elements returned in the response. (minimum: 0, maximum: 500, default: 10)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Am_searchmodulediscovery_response.schema
        """
        return self.call("GET", "/modules/discovery", query=kwargs)

		
    def createmodulediscoveries(self, moduleDiscoveries):
        """Creates module discovery information in a batch

        ``POST /modules/discovery``

        Args:
            moduleDiscoveries (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Am_createmodulediscoveries_request.schema
        """
        return self.call("POST", f"/modules/discovery", moduleDiscoveries)

    def getmodulediscovery(self, id_):
        """Retrieving discovery for the module referenced by id.

        ``GET /modules/{id}/discovery``

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Am_getmodulediscovery_response.schema
        """
        return self.call("GET", f"/modules/{id_}/discovery")

		
    def createmodulediscovery(self, moduleDiscovery, id_):
        """Creates a discovery for the module referenced by id.

        ``POST /modules/{id}/discovery``

        Args:
            moduleDiscovery (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Am_createmodulediscovery_request.schema
        """
        return self.call("POST", f"/modules/{id_}/discovery", moduleDiscovery)

		
    def updatemodulediscovery(self, moduleDiscovery, id_):
        """Update discovery for the module referenced by id.

        ``PUT /modules/{id}/discovery``

        Args:
            moduleDiscovery (dict): See Schema below.

        Raises:
            OkapiRequestError: Error response if request body contains validation error (in json format)
            OkapiRequestNotFound: Error response if entity is not found by id (in json format)
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.

        Schema:

            .. literalinclude:: ../files/Am_updatemodulediscovery_request.schema
        """
        return self.call("PUT", f"/modules/{id_}/discovery", moduleDiscovery)

		
    def deletemodulediscovery(self, id_):
        """Delete discovery of the module referenced by id.

        ``DELETE /modules/{id}/discovery``

        Raises:
            OkapiRequestFatalError: Error response for unhandled or critical server exceptions, e.g. NullPointerException.
        """
        return self.call("DELETE", f"/modules/{id_}/discovery")
