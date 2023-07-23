# -*- coding: utf-8 -*-
# Copyright (C) 2023 Tobias Weber <tobi-weber@gmx.de>


import click
from foliolib.folio.api.email import Email, SmtpConfiguration
from foliolib.folio.config import Config
from tabulate import tabulate

from ..orderedGroup import OrderedGroup


@click.group(cls=OrderedGroup)
def config():
    """Commands related to config.
    """


@config.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
def lst(**kwargs):
    """List config entries.
    """
    entries = Config(kwargs["tenant"]).get_entries()
    for entry in entries:
        body = [[k, v]
                for k, v in entry.items() if not k == "metadata"]
        print("\n" + tabulate(body, tablefmt="plain"))


@click.group(cls=OrderedGroup)
def email():
    """Commands related to email config.
    """


config.add_command(email)


@email.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-d", "--deprecated", is_flag=True,
              help="For older Folio versions, the config module is used.")
def get(**kwargs):
    """Get EMail config.
    """
    tenant = kwargs["tenant"]
    deprecated = kwargs["deprecated"]
    print(f"\nEmail config for {tenant}:")
    if deprecated:
        entries = Config(tenant).get_entries("SMTP_SERVER")
        for entry in entries:
            print("\t%s: %s" % (entry["description"], entry["value"]))
    else:
        smtpConfigs = SmtpConfiguration(tenant).get_smtpConfigurations()
        for smtpConfig in smtpConfigs["smtpConfigurations"]:
            del smtpConfig["id"]
            del smtpConfig["metadata"]
            print("")
            for k, v in smtpConfig.items():
                print(f"\t{k}: {v}")


@email.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-d", "--deprecated", is_flag=True,
              help="For older Folio versions, the config module is used.")
@click.option("-H", "--host", required=True,
              help="SMTP server host")
@click.option("-p", "--port", required=True,
              help="SMTP server port")
@click.option("-f", "--emailfrom", required=True,
              help="Email address to send emails from")
@click.option("-u", "--username", required=True,
              help="Username (credentials to access the SMTP server)")
@click.option("-x", "--password", required=True,
              help="Password (credentials to access the SMTP server)")
@click.option("-s", "--ssl", is_flag=True,
              help="Connect to SMTP server using SSL")
@click.option("-T", "--trustall", is_flag=True,
              help="Trust all certificates when establishing an SSL connection")
@click.option("-l", "--loginoption",
              help="Login mode")
@click.option("-S", "--starttls",
              help="Start TLS options. Values are DISABLED, OPTIONAL or REQUIRED")
@click.option("-a", "--authmethods",
              help="Authentication methods")
def set(**kwargs):
    """Set EMail config.
    """
    tenant = kwargs["tenant"]
    deprecated = kwargs["deprecated"]
    host = kwargs["host"]
    port = kwargs["port"]
    email_from = kwargs["emailfrom"]
    username = kwargs["username"]
    password = kwargs["password"]
    ssl = kwargs["ssl"]
    trustall = kwargs["trustall"]
    loginoption = kwargs["loginoption"]
    starttls = kwargs["starttls"]
    authmethods = kwargs["authmethods"]
    print(f"\Set Email config for {tenant}")
    if deprecated:
        Config(tenant).set_email(host, port, email_from,
                                 username, password,
                                 ssl=ssl, loginoption=loginoption,
                                 starttls=starttls, trustall=trustall,
                                 authmethods=authmethods)
    else:
        smtpConfig = {"host": host,
                      "port": port,
                      "from": email_from,
                      "username": username,
                      "password": password,
                      "ssl": ssl,
                      "trustAll": trustall,
                      "loginOption": loginoption,
                      "startTlsOptions": starttls,
                      "authMethods": authmethods}
        smtpConfigs = SmtpConfiguration(tenant).get_smtpConfigurations()[
            "smtpConfigurations"]
        if len(smtpConfigs):

            SmtpConfiguration(tenant).modify_smtpConfiguration(
                smtpConfigs[0]["id"], smtpConfig)
        else:
            SmtpConfiguration(tenant).set_smtpConfiguration(smtpConfig)


@email.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-d", "--deprecated", is_flag=True,
              help="For older Folio versions, the config module is used.")
def delete(**kwargs):
    """Delete EMail config.
    """
    tenant = kwargs["tenant"]
    deprecated = kwargs["deprecated"]
    print(f"\nDelete Email config for {tenant}")
    if deprecated:
        Config(tenant).delete_email()
    else:
        smtpConfigs = SmtpConfiguration(tenant).get_smtpConfigurations()[
            "smtpConfigurations"]
        if len(smtpConfigs):
            SmtpConfiguration(tenant).delete_smtpConfiguration(
                smtpConfigs[0]["id"])


@click.group(cls=OrderedGroup)
def foliohost():
    """Commands related to Folio UI application host config.
    """


config.add_command(foliohost)


@foliohost.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
def get(**kwargs):
    """Get Folio UI application host.
    """
    tenant = kwargs["tenant"]
    entries = Config(tenant).get_entries("USERSBL")
    for entry in entries:
        print("\n%s: %s" % (entry["description"], entry["value"]))


@foliohost.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
@click.option("-f", "--foliohost", required=True,
              help="Folio UI application host")
def set(**kwargs):
    """Set Folio UI application host.
    """
    tenant = kwargs["tenant"]
    foliohost = kwargs["foliohost"]
    print(f"Set Folio UI application host: {foliohost}")
    # if not foliohost.startswith("http"):
    #     foliohost = "https://%s" % foliohost
    Config(tenant).set_folio_host(foliohost)


@foliohost.command()
@click.option("-t", "--tenant", required=True,
              help="Tenant id")
def delete(**kwargs):
    """Delete Folio UI application host.
    """
    tenant = kwargs["tenant"]
    print("Delete Folio UI application host")
    Config(tenant).delete_folio_host()
