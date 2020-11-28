#!/usr/bin/env python3

import argparse
import json

parser = argparse.ArgumentParser()

parser.add_argument("src", help="okapi or stripes install file")
parser.add_argument("dest", help="template.json")
parser.add_argument("-l", "--latest", help="", action="store_true")
args = parser.parse_args()

with open(args.src) as f:
    data = json.load(f)
    mods = {}
    for m in data:
        p = m["id"].split("-")
        version = p.pop()
        if "SNAPSHOT" in version:
            version = "%s-%s" % (p.pop(), version)
        name = "-".join(p)
        if args.latest:
            version = None
        mods[name] = version

with open(args.dest, "w") as f:
    json.dump(mods, f, indent=2)
