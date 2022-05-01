# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>


def print_curl(url, method, headers, data=None):
    method = method.upper()
    s = "curl -w '\\n'"
    s += " -D -"
    s += f" -X {method}"
    for k, v in headers.items():
        if k.startswith("X-Okapi"):
            if v:
                s += f" -H \"{k}: {v}\""
    if method in ["POST", "PUT"]:
        s += f" -H \"Content-type: application/json\" -d '{data}'"

    s += f" {url}"

    print(f"\n### CURL {url}")
    print(s)
    print("### /CURL\n")
