# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

from foliolib.exceptions import FoliolibError


class RamlException(FoliolibError):
    pass


class RamlResourceTypeNotFound(RamlException):
    pass


class RamlTraitNotFound(RamlException):
    pass


class RamlTraitDataError(RamlException):
    pass


class RamlUnknownStatusCode(RamlException):
    pass


class RamlUnknownDataType(RamlException):
    pass


class CodeBuilderError(RamlException):
    pass


class RamlUnknownURLType(RamlException):
    pass
