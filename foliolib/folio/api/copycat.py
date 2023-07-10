# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.copycat")


class Copycat(FolioApi):
    """

    
    """

    def set_import(self, import_: dict):
        """Import record from external system

        ``POST /copycat/imports``

        Args:
            import_ (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Copycat_set_import_request.schema
        """
        return self.call("POST", "/copycat/imports", data=import_)

    def set_profile(self, profile: dict):
        """Create profile

        ``POST /copycat/profiles``

        Args:
            profile (dict): See Schema below

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Headers:
            - **Location** - URI of profile

        Schema:

            .. literalinclude:: ../files/Copycat_set_profile_request.schema
        """
        return self.call("POST", "/copycat/profiles", data=profile)

    def get_profiles(self, **kwargs):
        """Get profiles

        ``GET /copycat/profiles``

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
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    search profiles
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name = loc

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Copycat_get_profiles_return.schema 
        """
        return self.call("GET", "/copycat/profiles", query=kwargs)

    def get_profile(self, profilesId: str):
        """Get profile

        ``GET /copycat/profiles/{profilesId}``

        Args:
            profilesId (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Copycat_get_profile_return.schema 
        """
        return self.call("GET", f"/copycat/profiles/{profilesId}")

    def modify_profile(self, profilesId: str, profile: dict):
        """Update target profile

        ``PUT /copycat/profiles/{profilesId}``

        Args:
            profilesId (str)
            profile (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Copycat_modify_profile_request.schema
        """
        return self.call("PUT", f"/copycat/profiles/{profilesId}", data=profile)

    def delete_profile(self, profilesId: str):
        """Delete target profile

        ``DELETE /copycat/profiles/{profilesId}``

        Args:
            profilesId (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/copycat/profiles/{profilesId}")
