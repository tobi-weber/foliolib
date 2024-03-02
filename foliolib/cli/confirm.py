# -*- coding: utf-8 -*-
# Copyright (C) 2024 Tobias Weber <tobi-weber@gmx.de>

import functools
import sys

from foliolib.config import Config


def __is_confirmed(name, kwargs):
    if not Config().servercfg().getboolean("Cli", "confirm", fallback=True):
        return True

    cmd = name + " " + " ".join(["%s=%s" % (k, v)
                                for k, v in kwargs.items() if v])
    # confirm = input(
    #     "== Do you want to continue [%s] on %s? [y/n/a] " % (cmd, Config().get_server()))
    confirm = input(
        "== Do you want to continue?\n== %s\n== on %s [y/n] " % (cmd, Config().get_server()))
    if confirm == "y":
        return True
    elif confirm == "n":
        return False
    # elif confirm == "a":
    #     Config().set_servercfg("Cli", "confirm", str(False))
    else:
        return False


def confirm(func, *args, **kwargs):
    @functools.wraps(func)
    def wrapper_confirm(*args, **kwargs):
        if __is_confirmed(func.__name__, kwargs):
            func(*args, **kwargs)
        else:
            sys.exit()
    return wrapper_confirm
