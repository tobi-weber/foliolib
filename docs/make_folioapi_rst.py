#!/usr/bin/env python3

import os

FOLIOAPI = os.path.join("..", "foliolib", "folio", "api")
FOLIOAPI_RST = os.path.join("source", "foliolib.folio.api.rst")

RST_TPL = """
foliolib.folio.api package
==========================

Modules
-------

.. autosummary::
\t:toctree: generated
\t:template: module2.rst
\t:recursive:

\t{}
"""


def main():
    mods = []
    for mod in os.listdir(FOLIOAPI):
        if not mod.startswith("__"):
            mod_name = os.path.splitext(mod)[0]
            mods.append(f"foliolib.folio.api.{mod_name}")
            mods.sort()

    rst = RST_TPL.format("\n\t".join(mods))
    print(rst)
    with open(FOLIOAPI_RST, "w") as f:
        f.write(rst)


if __name__ == "__main__":
    main()
