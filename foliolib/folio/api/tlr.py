# -*- coding: utf-8 -*-
# Generated at 2024-03-23

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("foliolib.folio.api.tlr")



class Ecstlr(FolioApi):
    """ECS TLR API

    
    """

    def postecstlr(self, ecs_tlr):
        """Create ECS TLR

        ``POST /tlr/ecs-tlr``

        Args:
            ecs-tlr (dict): See Schema below.

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiRequestFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Ecstlr_postecstlr_request.schema
        """
        return self.call("POST", f"/tlr/ecs-tlr", ecs_tlr)

    def getecstlrbyid(self, requestId):
        """Retrieve ECS TLR by ID

        ``GET /tlr/ecs-tlr/{requestId}``

        Args:
            requestId (str):  (format: uuid)

        Returns:
            dict: See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiRequestNotFound: Not found
            OkapiRequestFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Ecstlr_getecstlrbyid_response.schema
        """
        return self.call("GET", f"/tlr/ecs-tlr/{requestId}")

		
    def putecstlrbyid(self, requestId, ecs_tlr):
        """Update ECS TLR by ID

        ``PUT /tlr/ecs-tlr/{requestId}``

        Args:
            requestId (str):  (format: uuid)
            ecs-tlr (dict): See Schema below.

        Raises:
            OkapiRequestError: Validation errors
            OkapiRequestNotFound: Not found
            OkapiRequestFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException

        Schema:

            .. literalinclude:: ../files/Ecstlr_putecstlrbyid_request.schema
        """
        return self.call("PUT", f"/tlr/ecs-tlr/{requestId}", ecs_tlr)

		
    def deleteecstlrbyid(self, requestId):
        """Remove ECS TLR by ID

        ``DELETE /tlr/ecs-tlr/{requestId}``

        Args:
            requestId (str):  (format: uuid)

        Raises:
            OkapiRequestError: Validation errors
            OkapiRequestNotFound: Not found
            OkapiRequestFatalError: When unhandled exception occurred during code execution, e.g. NullPointerException
        """
        return self.call("DELETE", f"/tlr/ecs-tlr/{requestId}")
