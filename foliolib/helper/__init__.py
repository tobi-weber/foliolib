# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import base64
import re

from foliolib.config import Config


def get_node():
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


def split_modid(modid):
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
