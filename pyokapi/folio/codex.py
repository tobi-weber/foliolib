# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import logging

from pyokapi.folio import FolioServices

log = logging.getLogger("okapi.folio.codex")


class CodexServices(FolioServices):

    def get_codex_instances(self, **query):
        return self.call("GET", "codex-instances", query=query)

    def get_codex_instance(self, codexInstanceId):
        return self.call("GET", f"codex-instances/{codexInstanceId}")

    def get_codex_instances_sources(self, **query):
        return self.call("GET", "codex-instances-sources", query=query)

    def get_codex_packages(self, **query):
        return self.call("GET", "codex-packages", query=query)

    def get_codex_package(self, codexPackageId):
        return self.call("GET", f"codex-packages{codexPackageId}")

    def get_codex_packages_sources(self, **query):
        return self.call("GET", "codex-packages-sources", query=query)
