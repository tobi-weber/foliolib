# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>
import logging
import os
import sys

from .config import server

path = os.path.abspath(__file__)
MODPATH = os.path.dirname(path)
SRCPATH = os.path.dirname(MODPATH)

log = logging.getLogger("foliolib")

RAISE = False


def set_logging(level="INFO", traceback=True):
    _log = logging.getLogger()
    _log.handlers = []
    if traceback or level == "DEBUG":
        formatter = logging.Formatter("[%(name)s] %(levelname)s %(message)s")
    else:
        formatter = logging.Formatter("%(message)s")
        sys.tracebacklimit = 0
    _log.setLevel(getattr(logging, level))
    h = logging.StreamHandler()
    if "FOLIOLIB_FILTER" in os.environ:
        h.addFilter(logging.Filter(os.environ["FOLIOLIB_FILTER"]))
    h.setFormatter(formatter)
    _log.addHandler(h)
