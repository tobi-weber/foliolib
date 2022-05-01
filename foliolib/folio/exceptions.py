# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

from foliolib.exceptions import FoliolibError


class FolioException(FoliolibError):
    pass


class FolioTenantMissing(FolioException):
    pass


class UserNotFound(FolioException):
    pass


class PermissionUserNotFound(FolioException):
    pass


class ServicePointsUserNotFound(FolioException):
    pass


class UnknownFile(FolioException):
    pass
