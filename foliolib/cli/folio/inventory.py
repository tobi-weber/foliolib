# -*- coding: utf-8 -*-
# Copyright (C) 2024 Tobias Weber <tobi-weber@gmx.de>

import textwrap

import click
from foliolib.config import Config
from foliolib.folio.api.inventoryStorage import (
    BoundWithPart, HoldingsStorage, InstancePrecedingSucceedingTitles,
    InstanceStorage, ItemStorage)
from foliolib.folio.inventoryImpl import InventoryImpl, InventoryReferenceData
from foliolib.helper import jprint
from tabulate import tabulate

from ..confirm import confirm
from ..orderedGroup import OrderedGroup


@click.group(cls=OrderedGroup)
def inventory():
    """Commands related to inventory.
    """


@inventory.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-p", "--path", required=True,
              help="Filesystem path")
@click.option("-r", "--replace", is_flag=True,
              default=False, help="Replace, if name exists with different id")
@confirm
def loadref(**kwargs):
    """Load referencedata from filesystem path.
    """
    tenant = kwargs["tenant"]
    path = kwargs["path"]
    replace = kwargs["replace"]
    InventoryReferenceData(tenant).load_reference_data(path, replace=replace)


@inventory.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-p", "--path", required=True,
              help="Filesystem path")
@confirm
def dumpref(**kwargs):
    """Write referencedata to filesystem path.
    """
    tenant = kwargs["tenant"]
    path = kwargs["path"]
    InventoryReferenceData(tenant).dump_reference_data(path)


@inventory.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@confirm
def reindex(**kwargs):
    """Create indicies if needed and reindex.
    """
    tenant = kwargs["tenant"]
    InventoryImpl(tenant).reindex()


@inventory.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
def totals(**kwargs):
    """Show total records in inventory.
    """
    tenant = kwargs["tenant"]

    count = ItemStorage(tenant).get_items()["totalRecords"]
    print("Items: %d records" % count)

    count = HoldingsStorage(tenant).get_holdings()["totalRecords"]
    print("Holdings: %d records" % count)

    count = InstanceStorage(tenant).get_instances()["totalRecords"]
    print("Instances: %d records" % count)

    count = InstanceStorage(tenant).get_instanceRelationships()["totalRecords"]
    print("Instance relationships: %d records" % count)

    count = BoundWithPart(tenant).get_boundWithParts()["totalRecords"]
    print("Bound with parts: %d records" % count)

    count = InstancePrecedingSucceedingTitles(
        tenant).get_precedingSucceedingTitles()["totalRecords"]
    print("Preceding succeeding titles: %d records" % count)


@inventory.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-b", "--barcode", required=True,
              help="barcode")
def barcode(**kwargs):
    """View Item, HodingsRecord and Instance by given barcode.
    """
    tenant = kwargs["tenant"]
    barcode = kwargs["barcode"]
    try:
        item = ItemStorage(tenant).get_items(
            query=f"barcode={barcode}")["items"][0]
        holdingsRecordId = item["holdingsRecordId"]
        print("\nItem:\n")
        del item["metadata"]
        jprint(item)
        holdingRecord = HoldingsStorage(tenant).get_holdings(
            query=f"id={holdingsRecordId}")["holdingsRecords"][0]
        instanceId = holdingRecord["instanceId"]
        print("\n---")
        print("\nHoldingRecord:\n")
        del holdingRecord["metadata"]
        jprint(holdingRecord)
        instance = InstanceStorage(tenant).get_instances(
            query=f"id={instanceId}")["instances"][0]
        print("\n---")
        print("\nInstance:\n")
        del instance["metadata"]
        jprint(instance)
    except IndexError:
        print("Title for barcode %s not found" % barcode)


@inventory.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-q", "--query",
              help="Query string")
@click.option("-i", "--id", help="Get instance by id")
@click.option("-f", "--full", is_flag=True, help="Wether output complete record.")
def instances(**kwargs):
    """List Instances by query.
    """
    tenant = kwargs["tenant"]
    query = kwargs["query"] or "id=* sortby title"
    full = kwargs["full"]
    uuid = kwargs["id"]
    if uuid is not None:
        full = True
        query = "id=%s" % uuid

    count = InstanceStorage(tenant).get_instances(
        query=query)["totalRecords"]
    instances = []
    for i in range(0, count, 1000):
        instances += InstanceStorage(tenant).get_instances(query=query,
                                                           offset=i,
                                                           limit=1000)["instances"]
        
    if full:
        for instance in instances:
            jprint(instance)
            print("\n---\n")
    else:
        headers = ["id", "hrid", "title"]
        body = [[i["id"], i["hrid"], "\n".join(textwrap.wrap(i["title"], width=70))]
                for i in instances]
        print(tabulate(body, headers, tablefmt="grid"))


@inventory.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-q", "--query",
              help="Query string")
@click.option("-i", "--id", help="Get holding by id")
@click.option("-f", "--full", is_flag=True, help="Wether output complete record.")
def holdings(**kwargs):
    """List Holdings by query.
    """
    tenant = kwargs["tenant"]
    query = kwargs["query"] or "id=* sortby id"
    full = kwargs["full"]
    uuid = kwargs["id"]
    if uuid is not None:
        full = True
        query = "id=%s" % uuid

    count = HoldingsStorage(tenant).get_holdings(
        query=query)["totalRecords"]
    holdings = []
    for i in range(0, count, 1000):
        holdings += HoldingsStorage(tenant).get_holdings(query=query,
                                                           offset=i,
                                                           limit=1000)["holdingsRecords"]
        
    if full:
        for holding in holdings:
            jprint(holding)
            print("\n---\n")
    else:
        headers = ["id", "hrid", "instanceId"]
        body = [[h["id"], h["hrid"], h["instanceId"]]
                for h in holdings]
        print(tabulate(body, headers, tablefmt="grid"))


@inventory.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-q", "--query",
              help="Query string")
@click.option("-i", "--id", help="Get item by id")
@click.option("-f", "--full", is_flag=True, help="Wether output complete record.")
def items(**kwargs):
    """List Items by query.
    """
    tenant = kwargs["tenant"]
    query = kwargs["query"] or "id=* sortby id"
    full = kwargs["full"]
    uuid = kwargs["id"]
    if uuid is not None:
        full = True
        query = "id=%s" % uuid

    count = ItemStorage(tenant).get_items(
        query=query)["totalRecords"]
    items = []
    for i in range(0, count, 1000):
        items += ItemStorage(tenant).get_items(query=query,
                                                           offset=i,
                                                           limit=1000)["items"]
        
    if full:
        for item in items:
            jprint(item)
            print("\n---\n")
    else:
        headers = ["id", "hrid", "holdingsRecordId"]
        body = [[i["id"], i["hrid"], i["holdingsRecordId"]]
                for i in items]
        print(tabulate(body, headers, tablefmt="grid"))


@inventory.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-q", "--query",
              help="Query string")
@click.option("-i", "--id", help="Get servicepoint by id")
@click.option("-f", "--full", is_flag=True, help="Wether output complete record.")
def servicepoints(**kwargs):
    """List Servicepoints by query.
    """
    tenant = kwargs["tenant"]
    query = kwargs["query"] or "id=* sortby id"
    full = kwargs["full"]
    uuid = kwargs["id"]
    if uuid is not None:
        full = True
        query = "id=%s" % uuid

    refData = InventoryReferenceData(tenant)
    sps = refData.get_servicePoints(query=query)

    if full:
        for sp in sps:
            jprint(sp)
            print("\n---\n")
    else:
        headers = ["id", "name", "code", "description"]
        body = [[s["id"], s["name"], s["code"],
                 "\n".join(textwrap.wrap(s["discoveryDisplayName"], width=40))]
                for s in sps]
        print(tabulate(body, headers, tablefmt="grid"))


if Config().servercfg().getboolean("Cli", "dev", fallback=False):
    @inventory.command()
    @click.option("-t", "--tenant", required=True,
                help="Tenant id")
    @click.option("-q", "--query",
                help="Query string")
    @click.option("-i", "--id", help="Get library by id")
    @click.option("-f", "--full", is_flag=True, help="Wether output complete record.")
    def libraries(**kwargs):
        """List Libraries by query.
        """
        tenant = kwargs["tenant"]
        query = kwargs["query"] or "id=* sortby id"
        full = kwargs["full"]
        uuid = kwargs["id"]
        if uuid is not None:
            full = True
            query = "id=%s" % uuid

        refData = InventoryReferenceData(tenant)
        libraries = refData.get_libraries(query=query)

        if full:
            for l in libraries:
                jprint(l)
                print("\n---\n")
        else:
            headers = ["id", "name", "code", "campusId"]
            body = [[l["id"], l["name"], l["code"], l["campusId"]]
                    for l in libraries]
            print(tabulate(body, headers, tablefmt="grid"))


    @inventory.command()
    @click.option("-t", "--tenant", required=True,
                help="Tenant id")
    @click.option("-q", "--query",
                help="Query string")
    @click.option("-i", "--id", help="Get campus by id")
    @click.option("-f", "--full", is_flag=True, help="Wether output complete record.")
    def campuses(**kwargs):
        """List Campuses by query.
        """
        tenant = kwargs["tenant"]
        query = kwargs["query"] or "id=* sortby id"
        full = kwargs["full"]
        uuid = kwargs["id"]
        if uuid is not None:
            full = True
            query = "id=%s" % uuid

        refData = InventoryReferenceData(tenant)
        campuses = refData.get_campuses(query=query)

        if full:
            for c in campuses:
                jprint(c)
                print("\n---\n")
        else:
            headers = ["id", "name", "code", "institutionId"]
            body = [[c["id"], c["name"], c["code"], c["institutionId"]]
                    for c in campuses]
            print(tabulate(body, headers, tablefmt="grid"))


    @inventory.command()
    @click.option("-t", "--tenant", required=True,
                help="Tenant id")
    @click.option("-q", "--query",
                help="Query string")
    @click.option("-i", "--id", help="Get campus by id")
    @click.option("-f", "--full", is_flag=True, help="Wether output complete record.")
    def institutions(**kwargs):
        """List Institutions by query.
        """
        tenant = kwargs["tenant"]
        query = kwargs["query"] or "id=* sortby id"
        full = kwargs["full"]
        uuid = kwargs["id"]
        if uuid is not None:
            full = True
            query = "id=%s" % uuid

        refData = InventoryReferenceData(tenant)
        institutions = refData.get_institutions(query=query)

        if full:
            for i in institutions:
                jprint(i)
                print("\n---\n")
        else:
            headers = ["id", "name", "code"]
            body = [[i["id"], i["name"], i["code"]]
                    for i in institutions]
            print(tabulate(body, headers, tablefmt="grid"))

