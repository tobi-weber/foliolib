# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>

import inflection

SINGULARIZE = {"mods": "mods"}
PLURALIZE = {}


def merge_dict(destination: dict, source: dict):
    if not destination:
        return source
    if not isinstance(destination, dict):
        print("ERROR destination is not type dict")
        print(destination)
        raise Exception()
    if not isinstance(source, dict):
        print("ERROR source is not type dict")
        print(source)
        raise Exception()
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
            try:
                print(1)
                destination[key] = value
            except:
                print(2)
                print(value)
                print(destination)
                raise
    return destination


def singularize(name: str):
    if name in SINGULARIZE:
        return SINGULARIZE[name]
    return inflection.singularize(name)


def pluralize(name: str):
    if name in PLURALIZE:
        return PLURALIZE[name]
    return inflection.pluralize(name)
