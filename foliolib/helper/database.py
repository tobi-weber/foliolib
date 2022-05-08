# -*- coding: utf-8 -*-
# Copyright (C) 2021 Tobias Weber <tobi-weber@gmx.de>

import logging

import psycopg2
from foliolib.config import Config
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

log = logging.getLogger("foliolib.helper.database")


class Postgres:
    """Example:

    with Postgres(databas="okapi_modules") as pg:
        print(pg.get_schemas)
    """

    def __init__(self, user: str = None, password: str = None, database: str = "postgres",
                 host: str = None, port: str = "5432") -> None:
        self._host = host or Config().okapicfg().get(
            "Postgres", "host", fallback="localhost")
        self._port = port or Config().okapicfg().get(
            "Postgres", "port", fallback="5432")
        self._user = user or Config().okapicfg().get(
            "Postgres", "user", fallback="postgres")
        self._password = password or Config().okapicfg().get(
            "Postgres", "password", fallback="postgres")
        self._database = database
        self._con = None

    def open(self):
        try:
            log.debug("Open postgres database %s on %s:%s with user %s:%s",
                      self._database, self._host, self._port, self._user, self._password)
            self._con = psycopg2.connect(database=self._database, user=self._user,
                                         password=self._password, host=self._host,
                                         port=self._port)
            self._con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        except psycopg2.OperationalError as err:
            log.error("Postgresql: %s", err)

    def close(self):
        if self._con is not None:
            self._con.close()

    def is_open(self):
        return False if self._con is None else True

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

    def get_table_column_names(self, table: str, schema: str = None):
        table = f"{schema}.{table}" if schema else table
        log.debug("Get column names from table %s", table)
        with self._con.cursor() as c:
            s = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE "
            s += f"table_name = '{table}';"
            c.execute(s)
            r = c.fetchall()
            return r

    def get_table_data(self, table: str, schema: str = None, id_=None):
        table = f"{schema}.{table}" if schema else table
        log.debug("Get data from table %s", table)
        with self._con.cursor() as c:
            s = f"SELECT * FROM {table}"
            if id_ is not None:
                s += f" WHERE id={id_}"
            c.execute(s + ";")
            r = c.fetchall()
            return r

    def delete_rows_from_table(self, table: str, schema: str = None,
                               ids=[]):
        table = f"{schema}.{table}" if schema else table
        with self._con.cursor() as c:
            for id_ in ids:
                log.debug("Delete %s in table %s", (id_, table))
                c.execute(f"DELETE FROM {table} WHERE id={id_};")

    def clear_table(self, table: str, schema: str = None):
        table = f"{schema}.{table}" if schema else table
        log.debug("Clear table %s", table)
        with self._con.cursor() as c:
            c.execute(f"DELETE FROM {table};")

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
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            log.error("%s: %s", exc_type, exc_value)
        self.close()


def create_okapi_db(user: str = "okapi", password: str = "okapi25",
                    database: str = "okapi"):
    # pylint: disable=no-member
    with Postgres() as pg:
        log.info("Create okapi database %s with user %s:%s",
                 database, user, password)
        try:
            pg.create_user(user, password, roles=["LOGIN", "CREATEDB"])
        except psycopg2.errors.DuplicateObject as err:
            log.error(err)
        try:
            pg.create_database(database, user)
        except psycopg2.errors.DuplicateDatabase as err:
            log.error(err)


def create_modules_db(user: str = "folio_admin", password: str = "folio_admin",
                      database: str = "okapi_modules"):
    # pylint: disable=no-member
    with Postgres() as pg:
        log.info("Create module database %s with user %s:%s",
                 database, user, password)
        try:
            # pg.create_user(user, password, roles=[
            #               "LOGIN", "SUPERUSER", "CREATEROLE", "CREATEDB"])
            pg.create_user(user, password, roles=[
                "LOGIN", "SUPERUSER"])
        except psycopg2.errors.DuplicateObject as err:
            log.error(err)
        try:
            pg.create_database(database, user)
        except psycopg2.errors.DuplicateDatabase as err:
            log.error(err)


def purge_modules_db(tenant: str, database: str = "okapi_modules"):
    with Postgres(database=database) as pg:
        for s in pg.get_schemas():
            if s != "public" and s.startswith(tenant):
                pg.drop_schema(s)
        for user in pg.get_users():
            if user.startswith(tenant):
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
