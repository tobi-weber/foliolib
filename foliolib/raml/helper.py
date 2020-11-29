# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import inflection

SINGULARIZE = {"mods": "mods"}
PLURALIZE = {}


def merge_dict(destination: dict, source: dict):
    for key, value in source.items():
        if value is None:
            continue
        if isinstance(value, dict):
            try:
                node = destination.setdefault(key, {})
            except:
                continue
            merge_dict(node, value)
        else:
            destination[key] = value
    return destination


def singularize(name: str):
    if name in SINGULARIZE:
        return SINGULARIZE[name]
    return inflection.singularize(name)


def pluralize(name: str):
    if name in PLURALIZE:
        return PLURALIZE[name]
    return inflection.pluralize(name)
