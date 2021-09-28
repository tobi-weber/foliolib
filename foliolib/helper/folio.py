
import logging
from distutils.version import StrictVersion

from foliolib.folio.api.permissions import Permissions
from foliolib.folio.users import UserService
from foliolib.okapi.okapiClient import OkapiClient

log = logging.getLogger("foliolib.helper.okapi")


def create_superuser(tenant: str, username: str = "admin",
                     password: str = "folio"):
    """Create a superuser for a tenant.

    Args:
        tenant (str): tenant id.
        username (str, optional): username. Defaults to "admin".
        password (str, optional): password. Defaults to "folio".

    Returns:
        [type]: [description]
    """
    okapi = OkapiClient()

    log.info("Disable authtoken for tenant.")
    try:
        mod_authtoken = okapi.get_tenant_interface("authtoken", tenant)[0]
        disabled_mods = okapi.disable_module(mod_authtoken["id"], tenant)
    except:
        disabled_mods = None

    userService = UserService(tenant)

    log.info("Create user record.")
    user = userService.create_user(
        username, password,
        permissions=["perms.all",
                     "users.collection.get"],
        personal={"lastName": "Superuser"})

    log.info("Create service points for user record.")
    servicepoints = userService.get_servicePoints()
    servicepointsIds = [sp["id"] for sp in servicepoints["servicepoints"]]
    if servicepointsIds:
        log.debug(servicepoints)
        userService.set_servicePoints(username, servicepointsIds,
                                      servicepointsIds[0])

    log.info("Enable mod-authtoken.")
    okapi.enable_modules([m["id"] for m in disabled_mods], tenant)

    log.info("Login as superuser")
    userService.login(username, password)

    log.info("Generate list of permissions")
    perms = Permissions(tenant).get_permissions(
        query="cql.allRecords=1 not permissionName==okapi.* not permissionName==modperms.* not permissionName==SYS#*",
        length="5000")
    topLevelPermissions = []
    for permission in perms["permissions"]:
        mods_perms = 0
        for s in permission["childOf"]:
            if s.startswith("SYS#") or s.startswith("modperms"):
                mods_perms += 1
        if len(permission["childOf"]) == mods_perms:
            topLevelPermissions.append(permission["permissionName"])

    # topLevelPermissions.extend(
    #    ["codex.collection.get",
    #     "codex-mux.instances.collection.get"])
    if StrictVersion(okapi.version()) >= StrictVersion("4.0"):
        topLevelPermissions.extend(["okapi.proxy.modules.get"])
    userService.set_permissions(username, topLevelPermissions)

    log.info("Superuser %s created.", username)

    return user
