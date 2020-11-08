# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>


def merge_dict(destination: dict, source: dict):
    for key, value in source.items():
        if value is None:
            continue
        if isinstance(value, dict):
            node = destination.setdefault(key, {})
            merge_dict(node, value)
        else:
            destination[key] = value
    return destination
