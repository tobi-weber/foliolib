# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>


class OkapiException(Exception):
    description = ""


class OkapiRedirect(OkapiException):
    description = "Moved temporarily"
    """
    Status code >= 300
    """


class OkapiMoved(OkapiRedirect):
    description = "Moved temporarily"
    """
    Status code = 302
    """


class OkapiRequestError(OkapiException):
    description = "Bad Request"
    """
    Status code >= 400
    """

    def __init__(self, response):
        self.status_code = response.status_code
        self.headers = response.headers
        try:
            obj = response.json()
            super().__init__(obj["errors"][0]["message"])
        except:
            super().__init__(response.text)


class OkapiRequestUnauthorized(OkapiRequestError):
    description = "Authentication is required"
    """
    Status code = 401
    """


class OkapiRequestForbidden(OkapiRequestError):
    description = "Forbidden"
    """
    Status code = 403
    """


class OkapiRequestNotFound(OkapiRequestError):
    description = "Not Found"
    """
    Status code = 404
    """


class OkapiRequestNotAcceptable(OkapiRequestError):
    description = "Not Acceptable"
    """
    Status code = 406
    """


class OkapiRequestTimeout(OkapiRequestError):
    description = "Request Timeout"
    """
    Status code = 408
    """


class OkapiRequestConflict(OkapiRequestError):
    description = "Conflict"
    """
    Status code = 409
    """


class OkapiRequestPayloadToLarge(OkapiRequestError):
    description = "Payload Too Large"
    """
    Status code = 413
    """


class OkapiRequestUnprocessableEntity(OkapiRequestError):
    description = "Unprocessable Entity"
    """
    Status code = 422
    """


class OkapiFatalError(OkapiRequestError):
    description = "Server Error"
