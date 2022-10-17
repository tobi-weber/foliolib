# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import json
import logging

from foliolib.okapi.exceptions import OkapiRequestError
from foliolib.okapi.okapiClient import OkapiClient
from foliolib.okapi.okapiModule import (OkapiModule,
                                        sort_modules_by_requirements)

log = logging.getLogger("foliolib.helper.okapi")


def uninstall_tenant(tenantid, **kwargs):
    """Disable all modules of a tenant.

    Args:
        tenantid ([type]): tenant id.
    """
    okapi = OkapiClient()

    descriptors = okapi.get_tenant_modules(tenantid, full=True)
    modules = sort_modules_by_requirements(
        [OkapiModule(descriptor) for descriptor in descriptors]
    )
    modules.reverse()
    modIds = [module.get_id() for module in modules]

    for modId in modIds:
        print("Uninstall module %s" % modId)
        try:
            msg = okapi.disable_module(modId, tenantid, **kwargs)
            log.debug(json.dumps(msg, indent=2))
        except OkapiRequestError:
            if "purge" in kwargs and kwargs["purge"] == True:
                print("Purge for %s failed, try to uninstall without purge ..." % modId)
                _kwargs = kwargs.copy()
                del _kwargs["purge"]
                msg = okapi.disable_module(modId, tenantid, **_kwargs)
                log.debug(json.dumps(msg, indent=2))
            else:
                raise

    print("Remove tenat %s." % tenantid)
    OkapiClient().remove_tenant(tenantid)
