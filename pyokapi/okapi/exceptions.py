# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>


class OkapiException(Exception):
    pass


class OkapiNotFound(OkapiException):
    pass


class OkapiForbidden(OkapiException):
    pass


class OkapiUnauthorized(OkapiException):
    pass


class OkapiInvalid(OkapiException):

    def __init__(self, response):
        try:
            obj = response.json()
            super().__init__(obj["errors"][0]["message"])
            self.errorobj = obj
        except:
            super().__init__(response.text)
            self.errorobj = None

    def get_error(self):
        return self.errorobj
