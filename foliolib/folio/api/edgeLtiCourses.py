# -*- coding: utf-8 -*-
# Generated at 2022-05-05

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.edgeLtiCourses")


class EdgeLtiCourses(FolioApi):
    """Edge API - Course Reserves LTI Tool

    Edge API to allow LTI platforms to fetch course reserves
    """

    def get_jwks_json(self):
        """Return the JWKS the tool uses to sign its JWTs

        ``GET /lti-courses/.well-known/jwks.json``
        """
        return self.call("GET", "/lti-courses/.well-known/jwks.json")

    def get_oidcLoginInit(self, apiKeyPath: str, **kwargs):
        """Begin a third-party OIDC login initiation flow

        ``GET /lti-courses/oidc-login-init/{apiKeyPath}``

        Args:
            apiKeyPath (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            iss (str):  The Issuer string of the Platform. This corresponds to a JWT's iss.
                    
                    Example:
                    
                     - https://my-lms.edu/
            login_hint (str):  Unused by this tool but required by the LTI Advantage spec.
            target_link_uri (str):  The actual end-point that should be executed at the end of the OpenID Connect authentication flow.
                    
                    Example:
                    
                     - https://folio-edge-apis.edu/lti-courses/launches/myApiKey

        Raises:
            OkapiRequestError: Bad Request
        """
        return self.call("GET", f"/lti-courses/oidc-login-init/{apiKeyPath}", query=kwargs)

    def set_launch(self, apiKeyPath: str):
        """

        ``POST /lti-courses/launches/{apiKeyPath}``

        Args:
            apiKeyPath (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("POST", f"/lti-courses/launches/{apiKeyPath}")

    def set_externalIdLaunch(self, apiKeyPath: str):
        """

        ``POST /lti-courses/externalIdLaunches/{apiKeyPath}``

        Args:
            apiKeyPath (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("POST", f"/lti-courses/externalIdLaunches/{apiKeyPath}")

    def set_registrarIdLaunch(self, apiKeyPath: str):
        """

        ``POST /lti-courses/registrarIdLaunches/{apiKeyPath}``

        Args:
            apiKeyPath (str)

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("POST", f"/lti-courses/registrarIdLaunches/{apiKeyPath}")

    def get_healths(self):
        """Health Check

        ``GET /admin/health``
        """
        return self.call("GET", "/admin/health")
