# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>


class FolioException(BaseException):
    pass


class OkapiException(FolioException):
    pass


class OkapiNotFound(OkapiException):
    pass


class OkapiForbidden(OkapiException):
    pass
