# -*- coding: utf-8 -*-
# Generated at 2022-04-08

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.edgeRtac")


class EdgeRtac(FolioApi):
    """Edge API - Real Time Availability Check

    Edge API to interface with FOLIO for 3rd party discovery services to determine holdings availability
    """

    def get_rtacs(self, **kwargs):
        """Batch RTAC for the specified ids

        ``GET /rtac``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            instanceIds (str):  List of Folio instance identifiers
            fullPeriodicals (bool):  Flag for including items data
            apikey (str):  API Key

        Returns:
            str: See Schema below

        Schema:

            .. literalinclude:: ../files/EdgeRtac_get_rtacs_return.schema 
        """
        return self.call("GET", "/rtac", query=kwargs)

    def get_rtac(self, instanceId: str, **kwargs):
        """RTAC for the specified holding id

        ``GET /rtac/{instanceId}``

        Args:
            instanceId (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            fullPeriodicals (bool):  Flag for including items data
            apikey (str):  API Key

        Returns:
            str: See Schema below

        Schema:

            .. literalinclude:: ../files/EdgeRtac_get_rtac_return.schema 
        """
        return self.call("GET", f"/rtac/{instanceId}", query=kwargs)

    def get_folioRTACs(self, **kwargs):
        """<Deprecated> RTAC for the specified holding id

        ``GET /prod/rtac/folioRTAC``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            mms_id (str):  The UUID of a FOLIO instance
            apikey (str):  API Key

        Returns:
            str: See Schema below

        Schema:

            .. literalinclude:: ../files/EdgeRtac_get_folioRTACs_return.schema 
        """
        return self.call("GET", "/prod/rtac/folioRTAC", query=kwargs)

    def get_healths(self):
        """Health Check

        ``GET /admin/health``
        """
        return self.call("GET", "/admin/health")
