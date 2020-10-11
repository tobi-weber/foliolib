# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import logging

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from okapi.config import CONFIG

log = logging.getLogger("okapi.database")


class Postgres:

    def __init__(self, user: str = None, password: str = None, database: str = "postgres",
                 host: str = None, port: str = "5432") -> None:
        host = host or CONFIG.okapicfg().get("Postgres", "host")
        port = port or CONFIG.okapicfg().get("Postgres", "port")
        user = user or CONFIG.okapicfg().get("Postgres", "user")
        password = password or CONFIG.okapicfg().get("Postgres", "password")
        log.debug("Open postgres %s:%s with database %s", host, port, database)
        self._con = psycopg2.connect(database=database, user=user,
                                     password=password, host=host,
                                     port=port)
        self._con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    def close(self):
        self._con.close()

    def get_databases(self):
        c = self._con.cursor()
        c.execute("SELECT datname FROM pg_database")
        dbs = c.fetchall()
        c.close()

        return [d[0] for d in dbs]

    def get_schemas(self):
        pg_schemas = ["pg_toast",
                      "pg_temp_1",
                      "pg_toast_temp_1",
                      "pg_catalog",
                      # "public",
                      "information_schema"]
        c = self._con.cursor()
        c.execute("select schema_name from information_schema.schemata;")
        schemas = c.fetchall()
        schemas = [s[0] for s in schemas if s[0] not in pg_schemas]

        return schemas

    def get_tables(self, schema: str):
        c = self._con.cursor()
        c.execute(f"select * from pg_tables where schemaname='{schema}';")
        tables = c.fetchall()
        tables = [t[1] for t in tables]
        c.close()

        return tables

    def get_users(self):
        c = self._con.cursor()
        c.execute("""select usesysid as user_id,
                     usename as username,
                     usesuper as is_superuser,
                     passwd as password_md5,
                     valuntil as password_expiration
                     from pg_shadow
                     order by usename;""")
        users = c.fetchall()
        c.close()
        return [u[1] for u in users]

    def create_database(self, dbname: str, user: str):
        c = self._con.cursor()
        c.execute(f"CREATE DATABASE {dbname} WITH OWNER {user};")
        self._con.commit()
        c.close()

    def create_user(self, user: str, password: str, roles: list = []):
        c = self._con.cursor()
        c.execute(
            f"CREATE ROLE {user} WITH PASSWORD '{password}' {' '.join(roles)};")
        self._con.commit()
        c.close()

    def drop_user(self, user: str):
        c = self._con.cursor()
        c.execute(f"""REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM {user};
                    REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public FROM {user};
                    REVOKE ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public FROM {user};
                    DROP USER {user};""")
        self._con.commit()
        c.close()

    def drop_schema(self, schema: str):
        c = self._con.cursor()
        c.execute(f"drop schema {schema} cascade")
        self._con.commit()
        c.close()

    def drop_users_for_tenant(self, tenant: str):
        for user in self.get_users():
            if tenant in user:
                self.drop_user(user)

    def get_descriptors(self):
        c = self._con.cursor()
        c.execute("SELECT * FROM modules;")
        descriptors = {}
        for d in c.fetchall():
            descriptors[d[0]["id"]] = d[0]
        c.close()
        return descriptors


def create_okapi_db(user: str = "okapi", password: str = "okapi25", database: str = "okapi"):
    pg = Postgres()
    try:
        pg.create_user(user, password, roles=["LOGIN", "CREATEDB"])
    except Exception as err:
        log.error(err)
    try:
        pg.create_database(database, user)
    except Exception as err:
        log.error(err)
    pg.close()


def create_modules_db(user: str = "folio_admin", password: str = "folio_admin", database: str = "okapi_modules"):
    pg = Postgres()
    try:
        # pg.create_user(user, password, roles=[
        #               "LOGIN", "SUPERUSER", "CREATEROLE", "CREATEDB"])
        pg.create_user(user, password, roles=[
                       "LOGIN", "SUPERUSER"])
    except Exception as err:
        log.error(err)
    try:
        pg.create_database(database, user)
    except Exception as err:
        log.error(err)
    pg.close()


def purge_modules_db(tenant: str, database: str = "okapis_module"):
    pg = Postgres(database=database)
    for s in pg.get_schemas():
        if s != "public":
            pg.drop_schema(s)
    for user in pg.get_users():
        if tenant in user:
            pg.drop_user(user)
    pg.close()


def get_users():
    pg = Postgres()
    users = pg.get_users()
    pg.close()
    return users


def get_databases():
    pg = Postgres()
    databases = pg.get_databases()
    pg.close()
    return databases


def get_schemas(database: str):
    pg = Postgres(database=database)
    schemas = pg.get_schemas()
    pg.close()
    return schemas


def get_tables(schema: str, database: str):
    pg = Postgres(database=database)
    tables = pg.get_tables(schema)
    pg.close()
    return tables


def get_descriptors():
    pg = Postgres(database="okapi")
    descriptors = pg.get_descriptors()
    pg.close()

    return descriptors


def get_descriptor(modId: str):
    descriptors = get_descriptors()
    if modId in descriptors:
        return descriptors[modId]
