
import logging

from foliolib.okapi.okapiClient import OkapiClient
from foliolib.okapi.okapiModule import (OkapiModule,
                                        sort_modules_by_requirements)

log = logging.getLogger("foliolib.helper.okapi")


def uninstall_tenant(tenantid):
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
    okapi.disable_modules([module.get_modId()
                           for module in modules],
                          tenantid)
