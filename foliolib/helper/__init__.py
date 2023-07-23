# -*- coding: utf-8 -*-
# Copyright (C) 2023 Tobias Weber <tobi-weber@gmx.de>

import base64
import re
import uuid

from foliolib.config import Config


def create_uuid():
    """Create uuid.

    Returns:
        str: uuid
    """
    return str(uuid.uuid4())


def is_valid_uuid(value):
    """Check if uuid is valid.

    Args:
        value (str): uuid

    Returns:
        bool: Wether uuid is valid.
    """
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False


def get_node():
    """Get first okapi node.

    Returns:
        str: node id
    """
    from foliolib.okapi.okapiClient import OkapiClient
    try:
        nodes = OkapiClient().get_nodes()
    except:
        nodes = []
    try:
        host = Config().servercfg().get("Okapi", "host")
    except:
        host = "localhost"
    try:
        port = Config().servercfg().get("Okapi", "port")
    except:
        port = "9130"
    # If Okapi role is clustered
    for node in nodes:
        if "nodeName" in node:
            if f"{host}:{port}" in node["url"]:
                return node["nodeName"]
    # If Okapi role is dev
    for node in nodes:
        if "nodeId" in node:
            return node["nodeId"]

    return host


def split_modid(modid: str):
    """Split Module id in name and version

    Args:
        modid (str): Module id

    Returns:
        tuple: Tuple with module name and id
    """
    m = re.search(r"-\d+.\d+.\d+", modid)
    if m is not None:
        version = m.group(0)
        modname = modid.replace(version, "")
        version = version[1:]
        return modname, version
    else:
        return modid, ""


def decode_base64(s):
    return base64.b64decode(s).decode("utf-8")


def encode_base64(s):
    return base64.b64encode(s.encode("utf-8"))
