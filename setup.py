# # -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

from distutils.core import setup

setup(
    name="pyokapi",
    version="0.1",
    description="Okapi/Folio Manager",
    author="Tobias Weber",
    author_email="tobi-weber@gmx.de",
    url="",
    packages=["okapi",
              "okapi/folio"],
    scripts=["okapicli",
             "foliocli"],
    install_requires=[],
    long_description="""
    Manager and python Library for Okapi/Folio.
    https://www.folio.org/
    """
)
