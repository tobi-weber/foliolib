# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>

import os

import click
from foliolib import set_logging
from foliolib.apiBuilder.build_api import build_api


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option("-d", "--dir", required=True,
              help="Path to the directory of the module")
@click.option("-b", "--basepath", help="Base path", default=os.getcwd(),
              show_default=True)
@click.option("-t", "--type", help="Schema type, RAML or OAS",
              default="RAML", show_default=True)
@click.option("-p", "--path", help="Relative path to the schema dir")
@click.option("-o", "--output", help="Output path, relative to base path",
              default="foliolib/folio/api", show_default=True)
@click.option("-s", "--docpath", help="Sphinx doc source path, relative to base path",
              default="docs/source", show_default=True)
def cli(**kwargs):
    """[summary]
    """
    set_logging()
    module_dir = kwargs["dir"]
    base_path = kwargs["basepath"]
    api_path = os.path.join(base_path, kwargs["output"])
    sphinx_doc_src = os.path.join(base_path, kwargs["docpath"])
    schema_path = kwargs["path"]
    schema_type = kwargs["type"]
    if schema_path is None:
        if schema_type.lower() == "raml":
            schema_path = "ramls"
        elif schema_type.lower() == "oas":
            schema_path = "src/main/resources/swagger.api"
    build_api(module_dir, schema_path, schema_type,
              api_path=api_path,
              sphinx_doc_src=sphinx_doc_src)
