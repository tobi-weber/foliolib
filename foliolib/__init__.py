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

log = logging.getLogger("foliolib")

RAISE = False


def set_logging():
    if "FOLIOLIB_LOGLEVEL" in os.environ:
        l = os.environ["FOLIOLIB_LOGLEVEL"]
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
    if "FOLIOLIB_FILTER" in os.environ:
        h.addFilter(logging.Filter(os.environ["FOLIOLIB_FILTER"]))
    h.setFormatter(formatter)
    log.addHandler(h)


set_logging()
