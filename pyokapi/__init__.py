# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>


import configparser
import logging
import os
import pathlib
import socket
import sys

path = os.path.abspath(__file__)
MODPATH = os.path.dirname(path)
SRCPATH = os.path.dirname(MODPATH)

log = logging.getLogger("okapi")


def set_logging(level=logging.INFO):
    if "PYOKAPI_DEBUG" in os.environ:
        level = logging.DEBUG
    else:
        sys.tracebacklimit = 0
    log.setLevel(level)
    if level == logging.INFO:
        formatter = logging.Formatter("%(message)s")
    else:
        formatter = logging.Formatter("[%(name)s] %(levelname)s %(message)s")
    h = logging.StreamHandler()
    h.setFormatter(formatter)
    log.addHandler(h)
