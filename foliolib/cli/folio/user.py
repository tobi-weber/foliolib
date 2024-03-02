# -*- coding: utf-8 -*-
# Copyright (C) 2024 Tobias Weber <tobi-weber@gmx.de>

import json
import textwrap

import click
from foliolib.config import Config
from foliolib.folio.exceptions import GroupNotFound, UserNotFound
from foliolib.folio.permissionsImpl import PermissionsImpl
from foliolib.folio.usersImpl import (AddressTypesImpl, DepartmentsImpl,
                                      GroupsImpl, UserAddress, UsersImpl)
from foliolib.helper import jprint
from tabulate import tabulate

from ..confirm import confirm
from ..orderedGroup import OrderedGroup


@click.group(cls=OrderedGroup)
def user():
    """Commands related to user managment.
    """


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-q", "--query",
              help="CQL query string")
@click.option("-w", "--wide", is_flag=True,
              help="View verbosed user data")
@click.option("-a", "--active", is_flag=True,
              help="View only active users")
@click.option("-i", "--inactive", is_flag=True,
              help="View only inactive users")
@click.option("-u", "--user", help="Show data for given username or id.")
def users(**kwargs):
    """List users.
    """
    tenant = kwargs["tenant"]
    query = kwargs["query"]
    wide = kwargs["wide"]
    active = kwargs["active"]
    inactive = kwargs["inactive"]
    username = kwargs["user"]

    if username is not None:
        try:
            user = UsersImpl(tenant).get_user(username)
            del user["metadata"]
            jprint(user)
        except UserNotFound:
            print(f"User {username} not found!")
    else:
        if wide:
            headers = ["Username", "Name",
                       "EMail", "Barcode", "Active"]
        else:
            headers = ["Username", "Name", "Active"]
        body = []
        users = UsersImpl(tenant).get_users(query=query)
        if not (active and inactive):
            if active:
                users = [user for user in users if user["active"]]
            elif inactive:
                users = [user for user in users if not user["active"]]

        for u in users:
            username = u["username"]
            active = str(u["active"])
            try:
                firstname = u["personal"]["firstName"]
            except KeyError:
                firstname = ""
            try:
                lastname = u["personal"]["lastName"]
            except KeyError:
                lastname = ""
            if firstname:
                name = lastname + ", " + firstname
            else:
                name = lastname
            name = "\n".join(textwrap.wrap(name, width=25))
            try:
                email = u["personal"]["email"]
            except KeyError:
                email = ""
            try:
                barcode = u["barcode"]
            except KeyError:
                barcode = ""
            if wide:
                body.append([username, name, email, barcode, active])
            else:
                body.append([username, name, active])

        print(tabulate(body, headers, tablefmt="grid"))


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-q", "--query",
              help="CQL query string")
@click.option("-g", "--group", help="Show data for given groupname or id.")
def groups(**kwargs):
    """List groups.
    """
    tenant = kwargs["tenant"]
    query = kwargs["query"]
    group = kwargs["group"]
    if group is not None:
        try:
            group = GroupsImpl(tenant).get_group(group)
            del group["metadata"]
            jprint(group)
        except GroupNotFound:
            print(f"Group {group} not found!")
    else:
        groups = GroupsImpl(tenant).get_groups(query=query)
        headers = ["Id", "Group", "Description"]
        body = []
        for group in groups:
            gid = group["id"]
            name = group["group"]
            name = "\n".join(textwrap.wrap(name, width=25))
            desc = group["desc"] if "desc" in group else ""
            desc = "\n".join(textwrap.wrap(desc, width=25))
            body.append([gid, name, desc])

        print(tabulate(body, headers, tablefmt="grid"))


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-q", "--query",
              help="CQL query string")
@click.option("-n", "--name", help="Show data for given department name, code or id.")
def departments(**kwargs):
    """List departments.
    """
    tenant = kwargs["tenant"]
    query = kwargs["query"]
    name = kwargs["name"]
    if name is not None:
        try:
            department = DepartmentsImpl(tenant).get_department(name)
            del department["metadata"]
            jprint(department)
        except GroupNotFound:
            print(f"Department {name} not found!")
    else:
        departments = DepartmentsImpl(tenant).get_departments(query=query)
        headers = ["Id", "Department", "Code"]
        body = []
        for department in departments:
            gid = department["id"]
            name = department["name"]
            name = "\n".join(textwrap.wrap(name, width=25))
            code = department["code"]
            body.append([gid, name, code])

        print(tabulate(body, headers, tablefmt="grid"))


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-q", "--query",
              help="CQL query string")
@click.option("-n", "--name", help="Show data for given addresstype name or id.")
def addresstypes(**kwargs):
    """List addresstypes.
    """
    tenant = kwargs["tenant"]
    query = kwargs["query"]
    name = kwargs["name"]
    if name is not None:
        try:
            addresstype = AddressTypesImpl(tenant).get_addressType(name)
            del addresstype["metadata"]
            jprint(addresstype)
        except GroupNotFound:
            print(f"Addresstype {name} not found!")
    else:
        addresstypes = AddressTypesImpl(tenant).get_addressTypes(query=query)
        headers = ["Id", "Addresstype", "Description"]
        body = []
        for addresstype in addresstypes:
            gid = addresstype["id"]
            name = addresstype["addressType"]
            name = "\n".join(textwrap.wrap(name, width=25))
            desc = ""
            if "desc" in addresstype:
                desc = addresstype["desc"]
                desc = "\n".join(textwrap.wrap(desc, width=25))
            body.append([gid, name, desc])

        print(tabulate(body, headers, tablefmt="grid"))


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-a", "--api", is_flag=True, help="Show only api permissions.")
@click.option("-u", "--ui", is_flag=True, help="Show only ui permissions.")
def toplevelperms(**kwargs):
    """List available top level permissions
    """
    tenant = kwargs["tenant"]
    ui = kwargs["ui"]
    api = kwargs["api"]
    perms = PermissionsImpl(tenant).get_topLevelPermissions()
    headers = ["Name", "Description"]
    body = []
    if ui and not api:
        perms = [perm for perm in perms
                 if perm["permissionName"].startswith("ui-")]
    if api and not ui:
        perms = [perm for perm in perms
                 if not perm["permissionName"].startswith("ui-")]
    for perm in perms:
        desc = perm["displayName"] if "displayName" in perm else ""
        desc = "\n".join(textwrap.wrap(desc, width=50))
        body.append([perm["permissionName"], desc])
    print(tabulate(body, headers, tablefmt="grid"))


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-u", "--username", required=True,
              help="Username.")
@click.option("-p", "--password", required=True,
              help="Password.")
@confirm
def password(**kwargs):
    """Set new password to user.
    """
    tenant = kwargs.pop("tenant")
    username = kwargs.pop("username")
    password = kwargs.pop("password")
    UsersImpl(tenant).set_password(username, password)


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-u", "--username", required=True,
              help="Username.")
@click.option("-p", "--password", required=True,
              help="Password.")
@click.option("-i", "--inactive", is_flag=True,
              help="Set user inactive")
@click.option("-P", "--permission", 'permissions', multiple=True,
              help="Permission for the user. Can be repeated.")
@click.option("-s", "--noservicepoints", 'userServicePoints', is_flag=True,
              help="Do not bind servicepoints to the user")
@click.option("-b", "--barcode",
              help="Barcode")
@click.option("-g", "--group",
              help="Groupname or id")
@click.option("-d", "--department", 'departments', multiple=True,
              help="Department name, code or id. Can be repeated.")
@click.option("-f", "--firstName", 'firstName',
              help="First name.")
@click.option("-l", "--lastName", 'lastName',
              help="Last name.")
@click.option("-M", "--middleName", 'middleName',
              help="Middle name.")
@click.option("-F", "--preferredFirstName", 'preferredFirstName',
              help="Preferred name.")
@click.option("-e", "--email",
              help="EMail address.")
@click.option("-n", "--phone",
              help="The user's primary phone number.")
@click.option("-m", "--mobilePhone", 'mobilePhone',
              help="The user's mobile phone number.")
@click.option("-D", "--dateOfBirth", 'dateOfBirth',
              help="The user's birth date.")
@click.option("-y", "--type",
              help="The class of user like staff or patron; this is different from patronGroup.")
@click.option("-E", "--enrollmentDate", 'enrollmentDate',
              help="The date in which the user joined the organization (format: date-time).")
@click.option("-x", "--expirationDate", 'expirationDate',
              help="The date for when the user becomes inactive (format: date-time).")
@click.option("-T", "--tags", multiple=True,
              help="List of tags (str).")
@click.option("-c", "--customField", 'customFields',
              help="JSON-Object that contains custom fields.")
#@confirm
def adduser(**kwargs):
    """Add a user.
    """
    tenant = kwargs.pop("tenant")
    username = kwargs.pop("username")
    password = kwargs.pop("password")
    inactive = kwargs.pop("inactive")
    kwargs = {k: v for k, v in kwargs.items() if v is not None}
    kwargs["active"] = False if inactive else True
    if "customFields" in kwargs:
        kwargs["customFields"] = json.loads(kwargs["customFields"])
    user = UsersImpl(tenant).add_user(username, password, **kwargs)
    del user["metadata"]
    jprint(user)


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-u", "--username", required=True,
              help="Username or id.")
@click.option("-i", "--inactive", is_flag=True,
              help="Set user inactive")
@click.option("-P", "--permission", 'permissions', multiple=True,
              help="Permission for the user. Can be repeated.")
@click.option("-b", "--barcode",
              help="Barcode")
@click.option("-g", "--group",
              help="Groupname or id")
@click.option("-d", "--department", 'departments', multiple=True,
              help="Department name, code or id. Can be repeated.")
@click.option("-f", "--firstName", 'firstName',
              help="First name.")
@click.option("-l", "--lastName", 'lastName',
              help="Last name.")
@click.option("-M", "--middleName", 'middleName',
              help="Middle name.")
@click.option("-F", "--preferredFirstName", 'preferredFirstName',
              help="Preferred name.")
@click.option("-e", "--email",
              help="EMail address.")
@click.option("-n", "--phone",
              help="The user's primary phone number.")
@click.option("-m", "--mobilePhone", 'mobilePhone',
              help="The user's mobile phone number.")
@click.option("-D", "--dateOfBirth", 'dateOfBirth',
              help="The user's birth date.")
@click.option("-y", "--type",
              help="The class of user like staff or patron; this is different from patronGroup.")
@click.option("-E", "--enrollmentDate", 'enrollmentDate',
              help="The date in which the user joined the organization (format: date-time).")
@click.option("-x", "--expirationDate", 'expirationDate',
              help="The date for when the user becomes inactive (format: date-time).")
@click.option("-T", "--tags", multiple=True,
              help="List of tags (str).")
@click.option("-c", "--customFields", 'customFields',
              help="JSON-Object that contains custom fields.")
@confirm
def modifyuser(**kwargs):
    """Modify a user.

    To delete an entry, you can set the value to null. Example:
    'foliolib folio user modifyuser -m null'
    will remove the entry middleName from the user object.
    """
    tenant = kwargs.pop("tenant")
    username = kwargs.pop("username")
    inactive = kwargs.pop("inactive")

    kwargs["active"] = False if inactive else True
    kwargs = {k: v for k, v in kwargs.items() if v is not None}
    for k, v in kwargs.items():
        if v == "null" or v == ("null",):
            kwargs[k] = None

    if "customFields" in kwargs and \
            kwargs["customFields"] is not None:
        kwargs["customFields"] = json.loads(kwargs["customFields"])
    user = UsersImpl(tenant).modify_user(username, **kwargs)
    del user["metadata"]
    jprint(user)


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-u", "--username", required=True,
              help="Username or id.")
@confirm
def deluser(**kwargs):
    """Delete a user.
    """
    tenant = kwargs.pop("tenant")
    username = kwargs.pop("username")
    UsersImpl(tenant).delete_user(username)


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-u", "--username", required=True,
              help="Username or id.")
@click.option("-T", "--addressType", required=True,
              help="Name or UUID of the addressType")
@click.option("-P", "--primary", "primaryAddress", is_flag=True,
              help="Wether address is the primary address")
@click.option("-c", "--country", "countryId", help="The country code for this address")
@click.option("-a", "--addressline1", "addressLine1", help="Address, Line 1.")
@click.option("-A", "--addressline2", "addressLine2", help="Address, Line 2.")
@click.option("-c", "--city", help="City name.")
@click.option("-r", "--region", help="Region.")
@click.option("-p", "--postalcode", "postalCode", help="Postal Code.")
@click.option("-R", "--replace", is_flag=True, help="Wether to replace adresses.")
@confirm
def adduseraddress(**kwargs):
    """Add address to a user.
    """
    tenant = kwargs.pop("tenant")
    username = kwargs.pop("username")
    addressType = kwargs.pop("addresstype")
    replace = kwargs.pop("replace")
    kwargs = {k:v for k,v in kwargs.items() if v is not None}
    address = UserAddress(addressType, **kwargs)
    if replace:
        address = [address]
    user = UsersImpl(tenant).modify_user(username, addresses=address)
    del user["metadata"]
    jprint(user)

@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-u", "--username", required=True,
              help="Username or id.")
@click.option("-T", "--addresstype", required=True,
              help="Name or UUID of the addressType")
@confirm
def deluseraddress(**kwargs):
    """Delete a address of a user by addresstype.
    """
    tenant = kwargs.pop("tenant")
    username = kwargs.pop("username")
    addressType = kwargs.pop("addresstype")
    user = UsersImpl(tenant).get_user(username)
    addressTypeId = AddressTypesImpl(tenant).get_addressType(addressType)["id"]
    addresses = [a for a in user["personal"]["addresses"]
                 if not a["addressTypeId"] == addressTypeId]
    user = UsersImpl(tenant).modify_user(username, addresses=addresses)
    del user["metadata"]
    jprint(user)


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-g", "--name", required=True,
              help="Groupname.")
@click.option("-d", "--desc", help="Description")
@click.option("-e", "--expiredays", help="ExpirationOffset in days")
@confirm
def addgroup(**kwargs):
    """Add a group.
    """
    tenant = kwargs.pop("tenant")
    name = kwargs.pop("name")
    desc = kwargs.pop("desc")
    expiredays = kwargs.pop("expiredays")
    if expiredays is None:
        expiredays = 0
    group = GroupsImpl(tenant).add_group(name, desc=desc,
                                            expirationOffsetInDays=expiredays)
    del group["metadata"]
    jprint(group)


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-g", "--name", required=True,
              help="Groupname.")
@click.option("-i", "--id", help="Group uuid.")
@click.option("-d", "--desc", help="Description")
@click.option("-e", "--expiredays", help="ExpirationOffset in days")
@confirm
def modifygroup(**kwargs):
    """Modify a group.
    In order to change the name of the group, the uuid of the group must be given.
    """
    tenant = kwargs.pop("tenant")
    name = kwargs.pop("name")
    uuid = kwargs.pop("id")
    desc = kwargs.pop("desc")
    expiredays = kwargs.pop("expiredays")
    if expiredays is None:
        expiredays = 0
    group = GroupsImpl(tenant).modify_group(name, uuid=uuid, desc=desc,
                                            expirationOffsetInDays=expiredays)
    del group["metadata"]
    jprint(group)



@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-g", "--group", required=True,
              help="Groupname or id.")
@confirm
def delgroup(**kwargs):
    """Delete a group.
    """
    tenant = kwargs.pop("tenant")
    group = kwargs.pop("group")
    GroupsImpl(tenant).delete_group(group)


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-n", "--name", required=True,
              help="Department name.")
@click.option("-c", "--code", required=True,
              help="Department code")
@confirm
def adddepartment(**kwargs):
    """Add a department.
    """
    tenant = kwargs.pop("tenant")
    name = kwargs.pop("name")
    code = kwargs.pop("code")
    department = DepartmentsImpl(tenant).add_department(name, code)
    del department["metadata"]
    jprint(department)

@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-n", "--name", required=True,
              help="Department name.")
@click.option("-c", "--code", required=True,
              help="Department code")
@click.option("-i", "--id", help="Group uuid.")
@confirm
def modifydepartment(**kwargs):
    """Modify a department.
    In order to change the name of a department, the uuid or the code of the departemnt
    must be given.
    """
    tenant = kwargs.pop("tenant")
    name = kwargs.pop("name")
    code = kwargs.pop("code")
    uuid = kwargs.pop("id")
    department = DepartmentsImpl(tenant).modify_department(name, code=code, uuid=uuid)
    del department["metadata"]
    jprint(department)


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-n", "--name", required=True,
              help="Department name, code or id.")
@confirm
def deldepartment(**kwargs):
    """Delete a department.
    """
    tenant = kwargs.pop("tenant")
    name = kwargs.pop("name")
    DepartmentsImpl(tenant).delete_department(name)


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-n", "--name", required=True,
              help="Addresstype name.")
@click.option("-d", "--desc", required=True,
              help="Addresstype description")
@confirm
def addaddresstype(**kwargs):
    """Add a addresstype.
    """
    tenant = kwargs.pop("tenant")
    name = kwargs.pop("name")
    desc = kwargs.pop("desc")
    addresstype = AddressTypesImpl(tenant).add_addressType(name, desc=desc)
    del addresstype["metadata"]
    jprint(addresstype)


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-n", "--name", required=True,
              help="Addresstype name.")
@click.option("-d", "--desc", required=True,
              help="Addresstype description")
@click.option("-i", "--id", help="Group uuid.")
@confirm
def modifyaddresstype(**kwargs):
    """Modify a addresstype.

    In order to change the name of a addressType, the uuid of the addressType
    must be given.
    """
    tenant = kwargs.pop("tenant")
    name = kwargs.pop("name")
    desc = kwargs.pop("desc")
    uuid = kwargs.pop("id")
    addresstype = AddressTypesImpl(tenant).modify_addressType(name, desc=desc, uuid=uuid)
    del addresstype["metadata"]
    jprint(addresstype)


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-n", "--name", required=True,
              help="Addresstype name or id.")
@confirm
def deladdresstype(**kwargs):
    """Delete a addresstype.
    """
    tenant = kwargs.pop("tenant")
    name = kwargs.pop("name")
    AddressTypesImpl(tenant).delete_addressType(name)


@user.command()
@click.option("-t", "--tenant", required=True,
            help="Tenant id")
@click.option("-u", "--user", required=True,
            help="username or id")
def permissions(**kwargs):
    """List permissions of a user
    """
    tenant = kwargs.pop("tenant")
    username = kwargs.pop("user")
    user = UsersImpl(tenant).get_user(username)
    permissions = PermissionsImpl(tenant).get_permissions_for_user(user["id"])
    jprint(permissions)

@user.command()
@click.option("-t", "--tenant", required=True,
            help="Tenant id")
@click.option("-u", "--user", required=True,
            help="name or id")
@click.option("-p", "--permission", multiple=True, required=True)
@confirm
def addpermission(**kwargs):
    """Add permissions to a user
    """
    tenant = kwargs.pop("tenant")
    username = kwargs.pop("user")
    permissions = kwargs.pop("permission")
    user = UsersImpl(tenant).get_user(username)
    for perm in permissions:
        print("Set permission %s to %s" % (perm, user["username"]))
        PermissionsImpl(tenant).set_permission_for_user(user["id"], perm)

@user.command()
@click.option("-t", "--tenant", required=True,
            help="Tenant id")
@click.option("-u", "--user", required=True,
            help="name or id")
@click.option("-p", "--permission", multiple=True, required=True)
@confirm
def delpermission(**kwargs):
    """Delete permissions of a user
    """
    tenant = kwargs.pop("tenant")
    username = kwargs.pop("user")
    permissions = kwargs.pop("permission")
    user = UsersImpl(tenant).get_user(username)
    for perm in permissions:
        print("Delete permission %s to %s" % (perm, user["username"]))
        PermissionsImpl(tenant).delete_permission_for_user(user["id"], perm)




if Config().servercfg().getboolean("Cli", "dev", fallback=False):
    @user.command()
    @click.option("-t", "--tenant", required=True,
                help="Tenant id")
    @click.option("-u", "--user", required=True,
                help="username or id")
    def permissionuser(**kwargs):
        """Get a PermissionUser.
        """
        tenant = kwargs.pop("tenant")
        username = kwargs.pop("user")
        user = UsersImpl(tenant).get_user(username)
        permsUser = PermissionsImpl(tenant).get_user(user["id"])
        print("PermissionUser:")
        jprint(permsUser)
        print("\nUser:")
        user = UsersImpl(tenant).get_user(permsUser["userId"])
        jprint(user)

    @user.command()
    @click.option("-t", "--tenant", required=True,
                help="Tenant id")
    @click.option("-p", "--permission", required=True)
    def getpermission(**kwargs):
        """Get a permission
        """
        tenant = kwargs.pop("tenant")
        name = kwargs.pop("permission")
        permission = PermissionsImpl(tenant).get_permission(name)
        jprint(permission)

