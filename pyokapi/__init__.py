# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>
import configparser
import logging
import os
import pathlib
import socket
import sys

VERSION = (0, 0, 1)


path = os.path.abspath(__file__)
MODPATH = os.path.dirname(path)
SRCPATH = os.path.dirname(MODPATH)

log = logging.getLogger("pyokapi")

RAISE = False


def set_logging():
    if "PYOKAPI_LOGLEVEL" in os.environ:
        l = os.environ["PYOKAPI_LOGLEVEL"]
        if l == "RAISE":
            global RAISE
            RAISE = True
            l = "DEBUG"
        elif l == "NONE":
            return
        try:
            level = getattr(logging, l)
        except:
            level = logging.DEBUG
        formatter = logging.Formatter("[%(name)s] %(levelname)s %(message)s")
    else:
        level = logging.INFO
        formatter = logging.Formatter("%(message)s")
        sys.tracebacklimit = 0
    log.setLevel(level)
    h = logging.StreamHandler()
    if "PYOKAPI_FILTER" in os.environ:
        h.addFilter(logging.Filter(os.environ["PYOKAPI_FILTER"]))
    h.setFormatter(formatter)
    log.addHandler(h)


set_logging()
