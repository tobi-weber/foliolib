# -*- coding: utf-8 -*-
# Copyright (C) 2020 Tobias Weber <tobi-weber@gmx.de>

import logging

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from foliolib.config import Config

log = logging.getLogger("foliolib.okapi.database")


class Postgres:

    def __init__(self, user: str = None, password: str = None, database: str = "postgres",
                 host: str = None, port: str = "5432") -> None:
        host = host or Config().okapicfg().get("Postgres", "host")
        port = port or Config().okapicfg().get("Postgres", "port")
        user = user or Config().okapicfg().get("Postgres", "user")
        password = password or Config().okapicfg().get("Postgres", "password")
        log.debug("Open postgres %s:%s with database %s", host, port, database)
        self._con = psycopg2.connect(database=database, user=user,
                                     password=password, host=host,
                                     port=port)
        self._con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    def close(self):
        self._con.close()

    def get_databases(self):
        with self._con.cursor() as c:
            c.execute("SELECT datname FROM pg_database")
            dbs = c.fetchall()
            return [d[0] for d in dbs]

    def get_schemas(self):
        pg_schemas = ["pg_toast",
                      "pg_temp_1",
                      "pg_toast_temp_1",
                      "pg_catalog",
                      # "public",
                      "information_schema"]
        with self._con.cursor() as c:
            c.execute("select schema_name from information_schema.schemata;")
            schemas = c.fetchall()
            schemas = [s[0] for s in schemas if s[0] not in pg_schemas]
            return schemas

    def get_tables(self, schema: str):
        with self._con.cursor() as c:
            c.execute(f"select * from pg_tables where schemaname='{schema}';")
            tables = c.fetchall()
            tables = [t[1] for t in tables]

            return tables

    def get_table(self, table: str, schema: str = None):
        table = f"{schema}.{table}" if schema else table
        with self._con.cursor() as c:
            c.execute(f"SELECT * FROM {table};")
            r = c.fetchall()
            return r

    def get_users(self):
        with self._con.cursor() as c:
            c.execute("""select usesysid as user_id,
                        usename as username,
                        usesuper as is_superuser,
                        passwd as password_md5,
                        valuntil as password_expiration
                        from pg_shadow
                        order by usename;""")
            users = c.fetchall()
            return [u[1] for u in users]

    def create_database(self, dbname: str, user: str):
        with self._con.cursor() as c:
            c.execute(f"CREATE DATABASE {dbname} WITH OWNER {user};")
            # self._con.commit()

    def create_user(self, user: str, password: str, roles: list = []):
        with self._con.cursor() as c:
            c.execute(
                f"CREATE ROLE {user} WITH PASSWORD '{password}' {' '.join(roles)};")
            # self._con.commit()

    def drop_user(self, user: str):
        with self._con.cursor() as c:
            c.execute(f"""REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM {user};
                        REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public FROM {user};
                        REVOKE ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public FROM {user};
                        DROP USER {user};""")
            # self._con.commit()

    def drop_schema(self, schema: str):
        with self._con.cursor() as c:
            c.execute(f"drop schema {schema} cascade")
            self._con.commit()

    def drop_users_for_tenant(self, tenant: str):
        for user in self.get_users():
            if tenant in user:
                self.drop_user(user)

    def get_descriptors(self):
        with self._con.cursor() as c:
            c.execute("SELECT * FROM modules;")
            descriptors = {}
            for d in c.fetchall():
                descriptors[d[0]["id"]] = d[0]
            return descriptors

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            log.error("%s: %s", exc_type, exc_value)
        self.close()


def create_okapi_db(user: str = "okapi", password: str = "okapi25", database: str = "okapi"):
    with Postgres() as pg:
        pg.create_user(user, password, roles=["LOGIN", "CREATEDB"])
        pg.create_database(database, user)


def create_modules_db(user: str = "folio_admin", password: str = "folio_admin", database: str = "okapi_modules"):
    with Postgres() as pg:
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


def purge_modules_db(tenant: str, database: str = "okapis_module"):
    with Postgres(database=database) as pg:
        for s in pg.get_schemas():
            if s != "public":
                pg.drop_schema(s)
        for user in pg.get_users():
            if tenant in user:
                pg.drop_user(user)


def get_users():
    with Postgres() as pg:
        users = pg.get_users()
        return users


def get_databases():
    with Postgres() as pg:
        databases = pg.get_databases()
        return databases


def get_schemas(database: str):
    with Postgres(database=database) as pg:
        schemas = pg.get_schemas()
        return schemas


def get_tables(schema: str, database: str):
    with Postgres(database=database) as pg:
        tables = pg.get_tables(schema)
        return tables


def get_descriptors():
    with Postgres(database="okapi") as pg:
        descriptors = pg.get_descriptors()
        return descriptors


def get_descriptor(modId: str):
    descriptors = get_descriptors()
    if modId in descriptors:
        return descriptors[modId]
