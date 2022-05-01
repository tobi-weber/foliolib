# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import click
from foliolib.config import Config
from foliolib.helper.okapi import (clean_okapi, secure_supertenant, set_env_db,
                                   set_env_elastic, set_env_kafka,
                                   unsecure_supertenant)
from foliolib.okapi.okapiClient import OkapiClient
from tabulate import tabulate

from.orderedGroup import OrderedGroup


@click.group(cls=OrderedGroup)
def okapi():
    """Commands to manage Okapi.
    """


@okapi.command()
def version():
    """Get Okapi version.
    """
    print(OkapiClient().version())


@okapi.command()
@click.option("-s", "--serviceId", help="")
@click.option("-i", "--instanceId", help="requires serviceId")
def health(**kwargs):
    """Get health.
    """
    res = OkapiClient().health(kwargs["serviceid"], kwargs["instanceid"])
    if isinstance(res, dict):
        res = [res]

    headers = ["Service ID", "Message", "Install ID", "Status"]
    body = [[e["srvcId"], e["healthMessage"], e["instId"], e["healthStatus"]]
            for e in sorted(res, key=lambda x: x["srvcId"])]
    print(tabulate(body, headers=headers))


@okapi.command()
def nodes():
    """List Nodes.
    """
    headers = ["Node id", "URL"]
    body = []
    for e in OkapiClient().get_nodes():
        l = [e["nodeId"], e["url"]]
        if "nodeName" in e:
            l.append(e["nodeName"])
        body.append(l)
    print(tabulate(body, headers=headers))


@okapi.command()
def env():
    """List Okapi enviroment variables.
    """
    ev = OkapiClient().get_env()
    if not ev:
        print("No entries in okapi enviroment!")
    headers = ["Name", "Value", "Description"]
    body = []
    for e in ev:
        l = [e["name"], e["value"]]
        if "description" in e:
            l.append(e["description"])
        else:
            l.append("")
        body.append(l)
    print(tabulate(body, headers=headers))


@okapi.command()
@click.option("-n", "--name", help="")
@click.option("-v", "--value", help="")
@click.option("-d", "--description", help="")
def add_env(**kwargs):
    """Add enviroment variable to Okapi.
    """
    OkapiClient().set_env(kwargs["name"], kwargs["value"],
                          description=kwargs["description"])
    print("Added enviroment variable to Okapi:")
    print(f"\tname: {kwargs['name']}")
    print(f"\tname: {kwargs['value']}")
    print(f"\tname: {kwargs['description']}")


@okapi.command()
@click.option("-u", "--user",
              default="folio_admin", help=" ", show_default=True)
@click.option("-p", "--password",
              default="folio_admin", help=" ", show_default=True)
@click.option("-d", "--database",
              default="okapi_modules", help=" ", show_default=True)
def set_dbenv(**kwargs):
    """Set global database settings to Okapi.
    """
    server = Config().okapicfg().get("Postgres", "host")
    port = Config().okapicfg().get("Postgres", "port")
    print("Set db parameters:")
    print(f"\tdb host: \t{server}")
    print(f"\tdb port: \t{port}")
    print(f"\tdatabase \t{kwargs['database']}")
    print(f"\tusername: \t{kwargs['user']}")
    print(f"\tpassword: \t{kwargs['password']}")
    set_env_db(server, port, kwargs["user"],
               kwargs["password"], kwargs["database"])


@okapi.command()
@click.option("-k", "--host", required=True, help="Kafka host")
@click.option("-p", "--port",
              default="9092", help="Kafka port", show_default=True)
def set_kafkaenv(**kwargs):
    """Set global Kafka settings to Okapi.
    """
    print("Set kafka parameters:")
    print(f"\tkafka host: \t{kwargs['host']}")
    print(f"\tkafka port: \t{kwargs['port']}")
    set_env_kafka(kwargs["host"], kwargs["port"])


@okapi.command()
@click.option("-e", "--host", required=True, help="Elasticsearch host")
@click.option("-p", "--port",
              default="9200", help="Elasticsearch port", show_default=True)
@click.option("-u", "--user",
              default="elastic", help="Elasticsearch username",
              show_default=True)
@click.option("-p", "--password", default="", help="Elasticsearch password",
              show_default=True)
@click.option("-l", "--language", multiple=True,
              help="Elasticsearch initial language. Can be repeated. (default: eng)", show_default=True)
def set_elasticenv(**kwargs):
    """Set global Elasticsearch settings to Okapi.
    """
    langs = kwargs["language"]
    if not langs:
        langs = ("eng",)
    print("Set Elasticsearch parameters:")
    print(f"\telasticsearch host: \t{kwargs['host']}")
    print(f"\telasticsearch port: \t{kwargs['port']}")
    print(f"\telasticsearch user: \t{kwargs['user']}")
    print(f"\telasticsearch password: \t{kwargs['password']}")
    print("\tinitial languages: \t%s" % (",".join(langs)))
    set_env_elastic(kwargs["host"], elastic_port=kwargs["port"], elastic_user=kwargs["user"],
                    elastic_password=kwargs["password"], languages=langs)


@okapi.command()
@click.option("-u", "--user", default="okapi_admin", help=" ", show_default=True)
@click.option("-p", "--password", default="admin", help=" ", show_default=True)
def secure(**kwargs):
    """Secure Okapi installation.
    """
    print(f"Create supertenant user {kwargs['user']}:{kwargs['password']}")
    secure_supertenant(kwargs["user"], kwargs["password"])


@okapi.command()
def unsecure():
    """Unsecure Okapi installation.
    """
    print("Remove supertenant user")
    unsecure_supertenant()


@okapi.command()
def clean():
    """Undeploy and remove not enabled modules in a tenant.
    """
    clean_okapi()
