# -*- coding: utf-8 -*-
# Copyright (C) 2023 Tobias Weber <tobi-weber@gmx.de>

import json
import os
import textwrap

import click
from foliolib.folio.exceptions import GroupNotFound, UserNotFound
from foliolib.folio.users import Users
from foliolib.helper import jprint
from tabulate import tabulate

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
@click.option("-u", "--user", help="Show data for given username.")
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
            user = Users(tenant).get_user(username)
            del user["metadata"]
            jprint(user)
        except UserNotFound:
            print(f"User {username} not found!")
    else:
        if wide:
            headers = ["Username", "Name",
                       "EMail", "Barcode", "Active"]
        else:
            headers = ["Username", "Active"]
        body = []
        users = Users(tenant).get_users(query=query)
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
                body.append([username, active])

        print(tabulate(body, headers, tablefmt="grid"))


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-q", "--query",
              help="CQL query string")
@click.option("-g", "--group", help="Show data for given groupname.")
def groups(**kwargs):
    """List groups.
    """
    tenant = kwargs["tenant"]
    query = kwargs["query"]
    group = kwargs["group"]
    if group is not None:
        try:
            group = Users(tenant).get_group(group)
            del group["metadata"]
            jprint(group)
        except GroupNotFound:
            print(f"Group {group} not found!")
    else:
        groups = Users(tenant).get_groups(query=query)
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
@click.option("-n", "--name", help="Show data for given department name or code.")
def departments(**kwargs):
    """List departments.
    """
    tenant = kwargs["tenant"]
    query = kwargs["query"]
    name = kwargs["name"]
    if name is not None:
        try:
            department = Users(tenant).get_department(name)
            del department["metadata"]
            jprint(department)
        except GroupNotFound:
            print(f"Department {name} not found!")
    else:
        departments = Users(tenant).get_departments(query=query)
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
def toplevelperms(**kwargs):
    """List available top level permissions
    """
    tenant = kwargs["tenant"]
    perms = Users(tenant).get_topLevelPermissions()
    headers = ["Name", "Description"]
    body = []
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
def password(**kwargs):
    """Set new password to user.
    """
    tenant = kwargs.pop("tenant")
    username = kwargs.pop("username")
    password = kwargs.pop("password")
    Users(tenant).set_password(username, password)


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-u", "--username", required=True,
              help="Username.")
@click.option("-p", "--password", required=True,
              help="Password.")
@click.option("-f", "--firstname", help="First name.")
@click.option("-l", "--lastname", help="Last name.")
@click.option("-e", "--email", help="EMail address.")
@click.option("-b", "--barcode", help="Barcode")
@click.option("-g", "--group", help="Groupname or id")
@click.option("-d", "--department", multiple=True,
              help="Department name, code or id. Can be repeated.")
@click.option("-i", "--inactive", is_flag=True,
              help="Set user inactive")
@click.option("-P", "--permission", multiple=True,
              help="Permission for the user. Can be repeated.")
@click.option("-s", "--noservicepoints", is_flag=True,
              help="Do not bind servicepoints to the user")
@click.option("-j", "--json",
              help="Data for the user as a json string or path to a json file. This data will be merged into the user instance.")
def adduser(**kwargs):
    """Add a user.
    """
    tenant = kwargs.pop("tenant")
    username = kwargs.pop("username")
    password = kwargs.pop("password")
    permissions = kwargs.pop("permission")
    departments = kwargs.pop("department")
    userJson = kwargs.pop("json")
    if userJson is not None:
        if os.path.exists(userJson):
            with open(userJson) as f:
                userData = json.load(f)
        else:
            userData = json.loads(userJson)
    else:
        userData = None
    print(userData)
    userServicePoints = False if kwargs.pop("noservicepoints") else True
    user = Users(tenant).create_user(username, password,
                                     permissions=permissions,
                                     departments=departments,
                                     userServicePoints=userServicePoints,
                                     userData=userData,
                                     **kwargs)
    del user["metadata"]
    jprint(user)


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-u", "--username", required=True,
              help="Username or id.")
def deluser(**kwargs):
    """Delete a user.
    """
    tenant = kwargs.pop("tenant")
    username = kwargs.pop("username")
    Users(tenant).delete_user(username)


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-n", "--name", required=True,
              help="Groupname.")
@click.option("-d", "--desc", help="Description")
@click.option("-e", "--expiredays", help="ExpirationOffset in days")
def addgroup(**kwargs):
    """Add a group.
    """
    tenant = kwargs.pop("tenant")
    name = kwargs.pop("name")
    desc = kwargs.pop("desc")
    expiredays = kwargs.pop("expiredays")
    if expiredays is None:
        expiredays = 0
    group = Users(tenant).create_group(name, desc=desc,
                                       expirationOffsetInDays=expiredays)
    del group["metadata"]
    jprint(group)


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-g", "--group", required=True,
              help="Groupname or id.")
def delgroup(**kwargs):
    """Delete a group.
    """
    tenant = kwargs.pop("tenant")
    group = kwargs.pop("group")
    Users(tenant).delete_group(group)


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-n", "--name", required=True,
              help="Department name.")
@click.option("-c", "--code", required=True,
              help="Department code")
def adddepartment(**kwargs):
    """Add a department.
    """
    tenant = kwargs.pop("tenant")
    name = kwargs.pop("name")
    code = kwargs.pop("code")
    department = Users(tenant).create_department(name, code)
    del department["metadata"]
    jprint(department)


@user.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-n", "--name", required=True,
              help="Department name, code or id.")
def deldepartment(**kwargs):
    """Delete a department.
    """
    tenant = kwargs.pop("tenant")
    name = kwargs.pop("name")
    Users(tenant).delete_department(name)
