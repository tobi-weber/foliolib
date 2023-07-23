# -*- coding: utf-8 -*-
# Copyright (C) 2022 Tobias Weber <tobi-weber@gmx.de>

import json
import logging
import os

import inflection
from foliolib.apiBuilder.raml.helper import pluralize, singularize
from foliolib.folio import FolioService
from foliolib.folio.api.inventoryStorage import (AlternativeTitleType,
                                                 AuthorityNoteType,
                                                 CallNumberType,
                                                 ClassificationType,
                                                 ContributorNameType,
                                                 ContributorType,
                                                 ElectronicAccessRelationship,
                                                 HoldingsNoteType,
                                                 HoldingsSources, HoldingsType,
                                                 IdentifierType, IllPolicy,
                                                 InstanceFormat,
                                                 InstanceNoteType,
                                                 InstanceRelationshipType,
                                                 InstanceStatus, InstanceType,
                                                 ItemDamagedStatuses,
                                                 ItemNoteType, LoanType,
                                                 Location, Locationunit,
                                                 MaterialType, ModeOfIssuance,
                                                 NatureOfContentTerm,
                                                 ServicePoint, StatisticalCode,
                                                 StatisticalCodeType)
from foliolib.helper import is_valid_uuid

log = logging.getLogger("foliolib.folio.inventoryReferenceData")


DIRS = [
    "alternative-title-types",
    "authority-note-types",
    "call-number-types",
    "classification-types",
    "contributor-name-types",
    "contributor-types",
    "electronic-access-relationships",
    "holdings-note-types",
    "holdings-sources",
    "holdings-types",
    "identifier-types",
    "ill-policies",
    "instance-formats",
    "instance-note-types",
    "instance-relationship-types",
    "instance-statuses",
    "instance-types",
    "item-damaged-statuses",
    "item-note-types",
    "loan-types",
    "location-units/institutions",
    "location-units/campuses",
    "location-units/libraries",
    "locations",
    "material-types",
    "modes-of-issuance",
    "nature-of-content-terms",
    "service-points",
    "statistical-codes",
    "statistical-code-types",
]


class InventoryReferenceData(FolioService):

    def get_alternativeTitleType(self, name_or_id):
        return self.__get_reference_data(AlternativeTitleType, name_or_id)

    def get_alternativeTitleTypes(self, query=None):
        return self.__get_all_reference_data(AlternativeTitleType, query=query)

    def set_alternativeTitleType(self, data, replace=False):
        self.__set_reference_data(data, AlternativeTitleType, replace=replace)

    def delete_alternativeTitleType(self, name_or_id):
        return self.__delete_reference_data(AlternativeTitleType, name_or_id)

    def get_authorityNoteType(self, name_or_id):
        return self.__get_reference_data(AuthorityNoteType, name_or_id)

    def get_authorityNoteTypes(self, query=None):
        return self.__get_all_reference_data(AuthorityNoteType, query=query)

    def set_authorityNoteType(self, data, replace=False):
        self.__set_reference_data(data, AuthorityNoteType, replace=replace)

    def delete_authorityNoteType(self, name_or_id):
        return self.__delete_reference_data(AuthorityNoteType, name_or_id)

    def get_callNumberType(self, name_or_id):
        return self.__get_reference_data(CallNumberType, name_or_id)

    def get_callNumberTypes(self, query=None):
        return self.__get_all_reference_data(CallNumberType, query=query)

    def set_callNumberType(self, data, replace=False):
        self.__set_reference_data(data, CallNumberType, replace=replace)

    def delete_callNumberType(self, name_or_id):
        return self.__delete_reference_data(CallNumberType, name_or_id)

    def get_classificationType(self, name_or_id):
        return self.__get_reference_data(ClassificationType, name_or_id)

    def get_classificationTypes(self, query=None):
        return self.__get_all_reference_data(ClassificationType, query=query)

    def set_classificationType(self, data, replace=False):
        self.__set_reference_data(data, ClassificationType, replace=replace)

    def delete_classificationType(self, name_or_id):
        return self.__delete_reference_data(ClassificationType, name_or_id)

    def get_contributorNameType(self, name_or_id):
        return self.__get_reference_data(ContributorNameType, name_or_id)

    def get_contributorNameTypes(self, query=None):
        return self.__get_all_reference_data(ContributorNameType, query=query)

    def set_contributorNameType(self, data, replace=False):
        self.__set_reference_data(data, ContributorNameType, replace=replace)

    def delete_contributorNameType(self, name_or_id):
        return self.__delete_reference_data(ContributorNameType, name_or_id)

    def get_contributorType(self, name_or_id):
        return self.__get_reference_data(ContributorType, name_or_id)

    def get_contributorTypes(self, query=None):
        return self.__get_all_reference_data(ContributorType, query=query)

    def set_contributorType(self, data, replace=False):
        self.__set_reference_data(data, ContributorType, replace=replace)

    def delete_contributorType(self, name_or_id):
        return self.__delete_reference_data(ContributorType, name_or_id)

    def get_electronicAccessRelationship(self, name_or_id):
        return self.__get_reference_data(ElectronicAccessRelationship, name_or_id)

    def get_electronicAccessRelationships(self, query=None):
        return self.__get_all_reference_data(ElectronicAccessRelationship, query=query)

    def set_electronicAccessRelationship(self, data, replace=False):
        self.__set_reference_data(
            data, ElectronicAccessRelationship, replace=replace)

    def delete_electronicAccessRelationship(self, name_or_id):
        return self.__delete_reference_data(ElectronicAccessRelationship, name_or_id)

    def get_holdingsNoteType(self, name_or_id):
        return self.__get_reference_data(HoldingsNoteType, name_or_id)

    def get_holdingsNoteTypes(self, query=None):
        return self.__get_all_reference_data(HoldingsNoteType, query=query)

    def set_holdingsNoteType(self, data, replace=False):
        self.__set_reference_data(data, HoldingsNoteType, replace=replace)

    def delete_holdingsNoteType(self, name_or_id):
        return self.__delete_reference_data(HoldingsNoteType, name_or_id)

    def get_holdingsSource(self, name_or_id):
        return self.__get_reference_data(HoldingsSources, name_or_id,
                                         baseMethodName="holdingsSource")

    def get_holdingsSources(self, query=None):
        return self.__get_all_reference_data(HoldingsSources, query=query,
                                             baseMethodName="holdingsSource")

    def set_holdingsSource(self, data, replace=False):
        self.__set_reference_data(data, HoldingsSources, replace=replace,
                                  baseMethodName="holdingsSource")

    def delete_holdingsSource(self, name_or_id):
        return self.__delete_reference_data(HoldingsSources, name_or_id,
                                            baseMethodName="holdingsSource")

    def get_holdingsType(self, name_or_id):
        return self.__get_reference_data(HoldingsType, name_or_id)

    def get_holdingsTypes(self, query=None):
        return self.__get_all_reference_data(HoldingsType, query=query)

    def set_holdingsType(self, data, replace=False):
        self.__set_reference_data(data, HoldingsType, replace=replace)

    def delete_holdingsType(self, name_or_id):
        return self.__delete_reference_data(HoldingsType, name_or_id)

    def get_identifierType(self, name_or_id):
        return self.__get_reference_data(IdentifierType, name_or_id)

    def get_identifierTypes(self, query=None):
        return self.__get_all_reference_data(IdentifierType, query=query)

    def set_identifierType(self, data, replace=False):
        self.__set_reference_data(data, IdentifierType, replace=replace)

    def delete_identifierType(self, name_or_id):
        return self.__delete_reference_data(IdentifierType, name_or_id)

    def get_illPolicy(self, name_or_id):
        return self.__get_reference_data(IllPolicy, name_or_id)

    def get_illPolicies(self, query=None):
        return self.__get_all_reference_data(IllPolicy, query=query)

    def set_illPolicy(self, data, replace=False):
        self.__set_reference_data(data, IllPolicy, replace=replace)

    def delete_illPolicy(self, name_or_id):
        return self.__delete_reference_data(IllPolicy, name_or_id)

    def get_instanceFormat(self, name_or_id):
        return self.__get_reference_data(InstanceFormat, name_or_id)

    def get_instanceFormats(self, query=None):
        return self.__get_all_reference_data(InstanceFormat, query=query)

    def set_instanceFormat(self, data, replace=False):
        self.__set_reference_data(data, InstanceFormat, replace=replace)

    def delete_instanceFormat(self, name_or_id):
        return self.__delete_reference_data(InstanceFormat, name_or_id)

    def get_instanceNoteType(self, name_or_id):
        return self.__get_reference_data(InstanceNoteType, name_or_id)

    def get_instanceNoteTypes(self, query=None):
        return self.__get_all_reference_data(InstanceNoteType, query=query)

    def set_instanceNoteType(self, data, replace=False):
        self.__set_reference_data(data, InstanceNoteType, replace=replace)

    def delete_instanceNoteType(self, name_or_id):
        return self.__delete_reference_data(InstanceNoteType, name_or_id)

    def get_instanceRelationshipType(self, name_or_id):
        return self.__get_reference_data(InstanceRelationshipType, name_or_id)

    def get_instanceRelationshipTypes(self, query=None):
        return self.__get_all_reference_data(InstanceRelationshipType, query=query)

    def set_instanceRelationshipType(self, data, replace=False):
        self.__set_reference_data(
            data, InstanceRelationshipType, replace=replace)

    def delete_instanceRelationshipType(self, name_or_id):
        return self.__delete_reference_data(InstanceRelationshipType, name_or_id)

    def get_instanceStatus(self, name_or_id):
        return self.__get_reference_data(InstanceStatus, name_or_id)

    def get_instanceStatuses(self, query=None):
        return self.__get_all_reference_data(InstanceStatus, query=query)

    def set_instanceStatus(self, data, replace=False):
        self.__set_reference_data(data, InstanceStatus, replace=replace)

    def delete_instanceStatus(self, name_or_id):
        return self.__delete_reference_data(InstanceStatus, name_or_id)

    def get_instanceType(self, name_or_id):
        return self.__get_reference_data(InstanceType, name_or_id)

    def get_instanceTypes(self, query=None):
        return self.__get_all_reference_data(InstanceType, query=query)

    def set_instanceType(self, data, replace=False):
        self.__set_reference_data(data, InstanceType, replace=replace)

    def delete_instanceType(self, name_or_id):
        return self.__delete_reference_data(InstanceType, name_or_id)

    def get_itemDamagedStatus(self, name_or_id):
        return self.__get_reference_data(ItemDamagedStatuses, name_or_id,
                                         baseMethodName="itemDamagedStatus")

    def get_itemDamagedStatuses(self, query=None):
        return self.__get_all_reference_data(ItemDamagedStatuses, query=query,
                                             baseMethodName="itemDamagedStatus")

    def set_itemDamagedStatus(self, data, replace=False):
        self.__set_reference_data(data, ItemDamagedStatuses, replace=replace,
                                  baseMethodName="itemDamagedStatus")

    def delete_itemDamagedStatus(self, name_or_id):
        return self.__delete_reference_data(ItemDamagedStatuses, name_or_id,
                                            baseMethodName="itemDamagedStatus")

    def get_itemNoteType(self, name_or_id):
        return self.__get_reference_data(ItemNoteType, name_or_id)

    def get_itemNoteTypes(self, query=None):
        return self.__get_all_reference_data(ItemNoteType, query=query)

    def set_itemNoteType(self, data, replace=False):
        self.__set_reference_data(data, ItemNoteType, replace=replace)

    def delete_itemNoteType(self, name_or_id):
        return self.__delete_reference_data(ItemNoteType, name_or_id)

    def get_loanType(self, name_or_id):
        return self.__get_reference_data(LoanType, name_or_id)

    def get_loanTypes(self, query=None):
        return self.__get_all_reference_data(LoanType, query=query)

    def set_loanType(self, data, replace=False):
        self.__set_reference_data(data, LoanType, replace=replace)

    def delete_loanType(self, name_or_id):
        return self.__delete_reference_data(LoanType, name_or_id)

    def get_location(self, name_or_id):
        return self.__get_reference_data(Location, name_or_id)

    def get_locations(self, query=None):
        return self.__get_all_reference_data(Location, query=query)

    def set_location(self, data, replace=False):
        self.__set_reference_data(data, Location, replace=replace)

    def delete_location(self, name_or_id):
        return self.__delete_reference_data(Location, name_or_id)

    def get_institution(self, name_or_id):
        return self.__get_reference_data(Locationunit, name_or_id,
                                         baseMethodName="institution")

    def get_institutions(self, query=None):
        return self.__get_all_reference_data(Locationunit, query=query,
                                             baseMethodName="institution")

    def set_institution(self, data, replace=False):
        self.__set_reference_data(data, Locationunit, replace=replace,
                                  baseMethodName="institution")

    def delete_institution(self, name_or_id):
        return self.__delete_reference_data(Locationunit, name_or_id,
                                            baseMethodName="institution")

    def get_campuse(self, name_or_id):
        return self.__get_reference_data(Locationunit, name_or_id,
                                         baseMethodName="campuse")

    def get_campuses(self, query=None):
        return self.__get_all_reference_data(Locationunit, query=query,
                                             baseMethodName="campuse")

    def set_campuse(self, data, replace=False):
        self.__set_reference_data(data, Locationunit, replace=replace,
                                  baseMethodName="campuse")

    def delete_campuse(self, name_or_id):
        return self.__delete_reference_data(Locationunit, name_or_id,
                                            baseMethodName="campuse")

    def get_library(self, name_or_id):
        return self.__get_reference_data(Locationunit, name_or_id,
                                         baseMethodName="library")

    def get_libraries(self, query=None):
        return self.__get_all_reference_data(Locationunit, query=query,
                                             baseMethodName="library")

    def set_library(self, data, replace=False):
        self.__set_reference_data(data, Locationunit, replace=replace,
                                  baseMethodName="library")

    def delete_library(self, name_or_id):
        return self.__delete_reference_data(Locationunit, name_or_id,
                                            baseMethodName="library")

    def get_materialType(self, name_or_id):
        return self.__get_reference_data(MaterialType, name_or_id)

    def get_materialTypes(self, query=None):
        return self.__get_all_reference_data(MaterialType, query=query)

    def set_materialType(self, data, replace=False):
        self.__set_reference_data(data, MaterialType, replace=replace)

    def delete_materialType(self, name_or_id):
        return self.__delete_reference_data(MaterialType)

    def get_modeOfIssuance(self, name_or_id):
        return self.__get_reference_data(ModeOfIssuance, name_or_id)

    def get_modesOfIssuance(self, query=None):
        return self.__get_all_reference_data(ModeOfIssuance, query=query)

    def set_modeOfIssuance(self, data, replace=False):
        self.__set_reference_data(data, ModeOfIssuance, replace=replace)

    def delete_modeOfIssuance(self, name_or_id):
        return self.__delete_reference_data(ModeOfIssuance, name_or_id)

    def get_natureOfContentTerm(self, name_or_id):
        return self.__get_reference_data(NatureOfContentTerm, name_or_id)

    def get_natureOfContentTerms(self, query=None):
        return self.__get_all_reference_data(NatureOfContentTerm, query=query)

    def set_natureOfContentTerm(self, data, replace=False):
        self.__set_reference_data(data, NatureOfContentTerm, replace=replace)

    def delete_natureOfContentTerm(self, name_or_id):
        return self.__delete_reference_data(NatureOfContentTerm, name_or_id)

    def get_servicePoint(self, name_or_id):
        return self.__get_reference_data(ServicePoint, name_or_id)

    def get_servicePoints(self, query=None):
        return self.__get_all_reference_data(ServicePoint, query=query)

    def set_servicePoint(self, data, replace=False):
        self.__set_reference_data(data, ServicePoint, replace=replace)

    def delete_servicePoint(self, name_or_id):
        return self.__delete_reference_data(ServicePoint, name_or_id)

    def get_statisticalCode(self, name_or_id):
        return self.__get_reference_data(StatisticalCode, name_or_id)

    def get_statisticalCodes(self, query=None):
        return self.__get_all_reference_data(StatisticalCode, query=query)

    def set_statisticalCode(self, data, replace=False):
        self.__set_reference_data(data, StatisticalCode, replace=replace)

    def delete_statisticalCode(self, name_or_id):
        return self.__delete_reference_data(StatisticalCode, name_or_id)

    def get_statisticalCodeType(self, name_or_id):
        return self.__get_reference_data(StatisticalCodeType, name_or_id)

    def get_statisticalCodeTypes(self, query=None):
        return self.__get_all_reference_data(StatisticalCodeType, query=query)

    def set_statisticalCodeType(self, data, replace=False):
        self.__set_reference_data(data, StatisticalCodeType, replace=replace)

    def delete_statisticalCodeType(self, name_or_id):
        return self.__delete_reference_data(StatisticalCodeType, name_or_id)

    def load_reference_data(self, path, replace=False):
        count = 0
        for refpath in DIRS:
            lastPathName = refpath.split("/")[-1]
            baseMethodName = inflection.camelize(
                "".join([inflection.camelize(s)
                         for s in lastPathName.split("-")]),
                False)
            add = getattr(self, "set_%s" %
                          singularize(baseMethodName))
            fullpath = os.path.join(path, refpath)
            if os.path.exists(fullpath):
                for fname in os.listdir(fullpath):
                    if fname.endswith((".json")):
                        fpath = os.path.join(fullpath, fname)
                        log.info("Load json %s", fpath)
                        try:
                            with open(fpath, encoding="utf-8") as f:
                                data = json.load(f)
                        except:
                            with open(fpath, encoding="utf-8") as f:
                                log.error("Json error:\n%s", f.read())
                            raise
                        add(data, replace)
                        count += 1
        log.info("%i files processed", count)
        return count

    def dump_reference_data(self, path):
        for refpath in DIRS:
            lastPathName = refpath.split("/")[-1]
            baseMethodName = inflection.camelize(
                "".join([inflection.camelize(s)
                         for s in lastPathName.split("-")]),
                False)
            get = getattr(self, "get_%s" % baseMethodName)
            data = get()
            fullpath = os.path.join(path, refpath)
            if not os.path.exists(fullpath):
                os.makedirs(fullpath)
            for d in data:
                fname = d["name"].replace("/", "_") + ".json"
                fpath = os.path.join(fullpath, fname)
                with open(fpath, "w", encoding="utf-8") as f:
                    print("Write %s" % fpath)
                    json.dump(d, f, indent=2)

    def __delete_reference_data(self, klass, name_or_id, baseMethodName=None):
        api = klass(self._tenant)
        if baseMethodName is None:
            baseMethodName = inflection.camelize(klass.__name__, False)
        get = getattr(api, "get_" + pluralize(baseMethodName))
        delete = getattr(api, "delete_" + baseMethodName)
        if is_valid_uuid(name_or_id):
            id_ = name_or_id
        else:
            id_ = list(get(query=f"name=={name_or_id}").values())[0][0]["id"]
        log.info("Delete %s - %s" % (name_or_id, baseMethodName))
        delete(id_)

    def __get_reference_data(self, klass, name_or_id, baseMethodName=None):
        if baseMethodName is None:
            baseMethodName = inflection.camelize(klass.__name__, False)
        get = getattr(klass(self._tenant), "get_" +
                      pluralize(baseMethodName))
        if is_valid_uuid(name_or_id):
            query = f"id=={name_or_id}"
        else:
            query = f"name=={name_or_id}"
        try:
            res = list(get(query=query).values())[0][0]
            del res["metadata"]
        except IndexError:
            return None
        return res

    def __get_all_reference_data(self, klass, query=None, baseMethodName=None):
        api = klass(self._tenant)
        if baseMethodName is None:
            baseMethodName = inflection.camelize(klass.__name__, False)
        kwargs = {} if query is None else {"query": query}
        get = getattr(api, "get_" + pluralize(baseMethodName))
        limit = get(limit=1, **kwargs)["totalRecords"]
        res = list(get(limit=limit, **kwargs).values())[0]
        res = [{k: v for k, v in r.items() if k != "metadata"}
               for r in res]
        return res

    def __set_reference_data(self, data, klass, replace=False, baseMethodName=None):
        api = klass(self._tenant)
        if baseMethodName is None:
            baseMethodName = inflection.camelize(klass.__name__, False)
        get = getattr(api, "get_" + pluralize(baseMethodName))
        add = getattr(api, "set_" + baseMethodName)
        modify = getattr(api, "modify_" + baseMethodName)
        delete = getattr(api, "delete_" + baseMethodName)

        elements = list(get(limit=1000).values())[0]
        # print(json.dumps(elements, indent=2))
        ids = [element["id"] for element in elements]
        names = [element["name"] for element in elements]

        if "id" in data and data["id"] in ids:
            log.info("Modify %s - %s" % (data["name"], baseMethodName))
            res = modify(data["id"], data)
        elif data["name"] not in names:
            log.info("Add %s - %s" % (data["name"], baseMethodName))
            res = add(data)
        else:
            log.info("Name %s already exists" % data["name"])
            element = list(get(query="name==%s" % data["name"]).values())[0][0]
            if "id" in data and "id" != element["id"] and replace:
                log.info("Replace %s - %s" % (data["name"], baseMethodName))
                delete(element["id"])
                res = add(data)
            else:
                log.info("Modify %s - %s" % (data["name"], baseMethodName))
                res = modify(element["id"], data)

            return res

        return None
