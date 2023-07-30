# -*- coding: utf-8 -*-
# Copyright (C) 2023 Tobias Weber <tobi-weber@gmx.de>

import json
import os

import click
from foliolib.folio.api.inventoryStorage import (
    AuthoritiesReindex, BoundWithPart, HoldingsStorage,
    InstancePrecedingSucceedingTitles, InstanceReindex, InstanceStorage,
    ItemStorage)
from foliolib.folio.api.search import Search
from foliolib.folio.inventoryReferenceData import InventoryReferenceData
from foliolib.helper import jprint
from foliolib.okapi.exceptions import OkapiRequestError

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
def dumpref(**kwargs):
    """Write referencedata to filesystem path.
    """
    tenant = kwargs["tenant"]
    path = kwargs["path"]
    InventoryReferenceData(tenant).dump_reference_data(path)


@inventory.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
def reindex(**kwargs):
    """Create indicies if needed and reindex.
    """
    tenant = kwargs["tenant"]
    print("\n## Reindex")
    search = Search(tenant)
    try:
        res = search.createindices({"resourceName": "instance"})
        print("Instance index created.")
    except OkapiRequestError as e:
        pass
    try:
        res = search.createindices({"resourceName": "instance_subject"})
        print("Instance subject index created.")
    except OkapiRequestError as e:
        pass
    try:
        res = search.createindices({"resourceName": "authority"})
        print("Authority index created.")
    except OkapiRequestError as e:
        pass
    print("Reindex Inventory")
    res = search.reindexinventoryrecords({"recreateIndex": True})
    print(res)
    print("Reindex Instance")
    res = InstanceReindex(tenant).set_reindex()
    print(res)
    print("Reindex Authorities")
    res = AuthoritiesReindex(tenant).set_reindex()
    print(res)


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
