# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>
import json
import os
import pprint
import tarfile
from distutils.version import LooseVersion
from json.decoder import JSONDecodeError

import requests
from github import Github
from lxml import etree

import okapi
from okapi.exceptions import OkapiException


class OkapiModule:

    def __init__(self, descriptor: str) -> None:
        self._descriptor = descriptor
        self.__set_modules_parameters()
        self.__fix_permission_required_missing()

    def get_modId(self):
        return self._descriptor["id"]

    def get_descriptor(self):
        return self._descriptor

    def get_requires(self):
        if "requires" in self._descriptor:
            return [r["id"] for r in self._descriptor["requires"]]
        else:
            return []

    def get_provides(self):
        if "provides" in self._descriptor:
            return [r["id"] for r in self._descriptor["provides"]]
        else:
            return []

    def get_docker_image(self):
        return self._descriptor["launchDescriptor"]["dockerImage"]

    def __set_modules_parameters(self):

        def remove_entry(l, name):
            for e in l:
                if e["name"].lower() == name.lower():
                    l.remove(e)

        config = okapi.get_modules_config(self.get_modId())
        if config is not None:
            if "Docker" in config:
                if "Memory" in config["Docker"]:
                    self._descriptor["launchDescriptor"]["dockerArgs"]["HostConfig"]["Memory"] = config.getint(
                        "Docker", "Memory")
            if "Env" in config:
                env = self._descriptor["launchDescriptor"]["env"]
                for k, v in config["Env"].items():
                    remove_entry(env, k)
                    env.append({"name": k.upper(), "value": v})

    def __fix_permission_required_missing(self):
        if "provides" in self._descriptor:
            for p in self._descriptor["provides"]:
                for handler in p["handlers"]:
                    if not "permissionsRequired" in handler:
                        handler["permissionsRequired"] = []


def request_release(name: str, version: str = None, download_dir: str = "pkgs"):
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)
    access_token = okapi.PYOKAPI_CONFIG.get("GitHub", "access-token")
    g = Github(access_token)
    repo = g.get_repo(f"folio-org/{name}")
    if version is None:
        release = repo.get_latest_release()
        version = release.tag_name.replace("v", "")

    fname = os.path.join(download_dir, f"{name}-{version}.tar.gz")
    if os.path.exists(fname):
        print(f"{fname} already downloaded")
        return {"name": name,
                "version": version,
                "fname": fname}
    else:
        releases = repo.get_releases()
        for r in releases:
            if version in r.tag_name:
                release = r
                break
        tarball_url = release.tarball_url
        with open(fname, "wb") as f:
            f.write(requests.get(tarball_url).content)

        return {"name": name,
                "version": version,
                "fname": fname}


def request_docker_tag(name: str, version: str = None, repository: str = "folioorg"):
    url = f"https://registry.hub.docker.com/v1/repositories/{repository}/{name}/tags"
    # print(url)
    response = requests.get(url)
    tags = response.json()
    if not tags:
        raise OkapiException(f"Docker Image for {name} not found")
    if version is not None:
        tags = [tag["name"]
                for tag in tags if version in tag["name"]]
    if version is None or len(tags) == 0:
        tags = response.json()
        tags = [tag["name"].replace("v", "")
                for tag in tags if not "latest" in tag["name"]]
    try:
        tags = sorted(tags, key=LooseVersion)
    except:
        tags = sorted(tags)

    tag = tags.pop()

    return tag


def makeOkapiModule(name: str, version: str = None, docker_image: str = None,
                    descriptor: str = None, docker_repository: str = "folioorg"):

    def request_descriptor(name):
        url = f"https://raw.githubusercontent.com/folio-org/{name}/master/descriptors/ModuleDescriptor-template.json"
        response = requests.get(url)
        try:
            return response.json()
        except JSONDecodeError:
            print(url)
            raise OkapiException(response.text)

    def request_version(name):
        url = f"https://raw.githubusercontent.com/folio-org/{name}/master/pom.xml"
        response = requests.get(url)
        root = etree.fromstring(response.text.encode("utf-8"))
        e = root.find('version', root.nsmap)

        return e.text

    if descriptor is None:
        descriptor = request_descriptor(name)
    # Remove db config
    if "env" in descriptor["launchDescriptor"]:
        env = [item for item in descriptor["launchDescriptor"]["env"]
               if not item["name"].startswith("DB_")]
        descriptor["launchDescriptor"]["env"] = env
    if docker_image is None:
        tag = request_docker_tag(name, version, docker_repository)
        docker_image = f"{docker_repository}/{name}:{tag}"
        if version is None:
            if "SNAPSHOT" in tag:
                # Mit regex machen!!!
                version = request_version(name)
            else:
                version = tag
    print(version)

    descriptor["id"] = f"{name}-{version}"
    descriptor["launchDescriptor"]["dockerImage"] = docker_image
    descriptor["launchDescriptor"]["dockerPull"] = True

    return OkapiModule(descriptor)


def makeOkapiModule_with_pkg(name: str, version: str = None, pkg_dir: str = "pkgs"):
    pkg = request_release(name, version=version, download_dir=pkg_dir)
    descriptor = None
    with tarfile.open(pkg["fname"]) as tar:
        members = tar.getmembers()
        for member in members:
            if "ModuleDescriptor" in member.name:
                print(member.name)
                f = tar.extractfile(member)
                descriptor = json.load(f)
    if descriptor is not None:
        return makeOkapiModule(name, pkg["version"], descriptor=descriptor, docker_repository="folioorg")
    else:
        return None


def main():
    pp = pprint.PrettyPrinter(indent=2)
    for name in ["mod-users", "mod-pubsub"]:
        print("\n")
        print("####################")
        print(f"#### MOD {name} #####")
        print("####################")
        print("\n")
        m = makeOkapiModule(name, docker_repository="folioorg")
        # m = makeOkapiModule(name, docker_repository="folioci")
        pp.pprint(m.get_descriptor())
        print("\n")
        print("####################")
        print("\n")


if __name__ == "__main__":
    main()
