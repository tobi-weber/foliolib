# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import json
import logging

import inflection

SINGULARIZE = {"mods": "mods",
               "ModesOfIssuance": "ModeOfIssuance",
               "modesOfIssuance": "modeOfIssuance",
               "ModeOfIssuance": "ModeOfIssuance",
               "modeOfIssuance": "modeOfIssuance"}
PLURALIZE = {"ModeOfIssuance": "ModesOfIssuance",
             "ModesOfIssuance": "ModesOfIssuance",
             "modeOfIssuance": "modesOfIssuance",
             "modesOfIssuance": "modesOfIssuance"}

log = logging.getLogger("foliolib.apiBuilder.raml.helper")

def merge_dict(destination: dict, source: dict):
    #print("### merge dict ###")
    #print(json.dumps(destination, indent=2))
    #print(json.dumps(source, indent=2))
    if not destination:
        return source
    if not isinstance(destination, dict):
        log.error("ERROR destination is not type dict")
        print(destination)
        raise Exception()
    if not isinstance(source, dict):
        log.error("ERROR source is not type dict")
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
            #merge_dict(node, value)
            try:
                merge_dict(node, value)
            except:
                destination[key] = {}
                merge_dict(destination[key], value)
        else:
            try:
                destination[key] = value
            except:
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
