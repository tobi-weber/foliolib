# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>

from datetime import date

API_PATH = "foliolib/folio/api"


def get_module_code(log_name):
    return f'''# -*- coding: utf-8 -*-
# Generated at {date.today()}

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("{log_name}")
'''
