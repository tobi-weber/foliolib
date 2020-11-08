#!/usr/bin/env python3

import os

FOLIOAPI = os.path.join("..", "pyokapi", "folio", "api")
FOLIOAPI_RST = os.path.join("source", "pyokapi.folio.api.rst")

RST_TPL = """
pyokapi.folio.api package
=========================

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
            mods.append(f"pyokapi.folio.api.{mod_name}")
            mods.sort()

    rst = RST_TPL.format("\n\t".join(mods))
    print(rst)
    with open(FOLIOAPI_RST, "w") as f:
        f.write(rst)


if __name__ == "__main__":
    main()
