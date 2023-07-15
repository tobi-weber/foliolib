# -*- coding: utf-8 -*-
# Copyright (C) 2023 Tobias Weber <tobi-weber@gmx.de>

import logging

from foliolib.config import Config

log = logging.getLogger("foliolib.helper.database")


try:
    import psycopg2
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
except:
    log.debug("Cannot import postgres client. You have to install psycopg2.")


class Postgres:
    """
    Postgres config can be defined in $HOME/.foliolib/[SERVERNAME]/server.conf:

    .. code-block:: cfg

        [Postgres]
        host = localhost
        port = 5432
        user = postgres
        password = password


    Example:

    .. code-block:: python

        with Postgres(database="okapi_modules") as pg:
            print(pg.get_schemas())
            pg.cursor.execute("SELECT * FROM TABLENAME;")
            print(pg.cursor.fetchall())

    """

    def __init__(self, user: str = None, password: str = None, database: str = "postgres",
                 host: str = None, port: str = None) -> None:
        self._host = host or Config().servercfg().get(
            "Postgres", "host", fallback="localhost")
        self._port = port or Config().servercfg().get(
            "Postgres", "port", fallback="5432")
        self._user = user or Config().servercfg().get(
            "Postgres", "user", fallback="postgres")
        self._password = password or Config().servercfg().get(
            "Postgres", "password", fallback="postgres")
        self._database = database
        self._con = None
        self.cursor = None

    def open(self):
        try:
            log.debug("Open postgres database %s on %s:%s with user %s:%s",
                      self._database, self._host, self._port, self._user, self._password)
            self._con = psycopg2.connect(database=self._database, user=self._user,
                                         password=self._password, host=self._host,
                                         port=self._port)
            self._con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            self.cursor = self._con.cursor()
        except psycopg2.OperationalError as err:
            log.error("Postgresql: %s", err)

    def close(self):
        if self._con is not None:
            self._con.close()

    def is_open(self):
        return False if self._con is None else True

    def get_databases(self):
        self.cursor.execute("SELECT datname FROM pg_database")
        dbs = self.cursor.fetchall()
        return [d[0] for d in dbs]

    def create_database(self, dbname: str, user: str):
        self.cursor.execute(f"CREATE DATABASE {dbname} WITH OWNER {user};")

    def drop_database(self, dbname: str, force=False):
        self.cursor.execute(f"DROP DATABASE {dbname};")

    def get_schemas(self):
        pg_schemas = ["pg_toast",
                      "pg_temp_1",
                      "pg_toast_temp_1",
                      "pg_catalog",
                      # "public",
                      "information_schema"]
        self.cursor.execute(
            "select schema_name from information_schema.schemata;")
        schemas = self.cursor.fetchall()
        schemas = [s[0] for s in schemas if s[0] not in pg_schemas]
        return schemas

    def create_schema(self, schema: str, user: str = None):
        if user is None:
            log.info("Create Schema %s", schema)
            self.cursor.execute(f"CREATE SCHEMA {schema};")
        else:
            log.info("Create Schema %s for user %s", schema, user)
            self.cursor.execute(
                f"CREATE SCHEMA {schema} AUTHORIZATION {user};")

    def drop_schema(self, schema: str):
        self.cursor.execute(f"drop schema {schema} cascade")

    def get_tables(self, schema: str):
        self.cursor.execute(
            f"select * from pg_tables where schemaname='{schema}';")
        tables = c.fetchall()
        tables = [t[1] for t in tables]

        return tables

    def get_table_column_names(self, table: str, schema: str = None):
        table = f"{schema}.{table}" if schema else table
        log.debug("Get column names from table %s", table)
        s = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE "
        s += f"table_name = '{table}';"
        self.cursor.execute(s)
        r = self.cursor.fetchall()
        return r

    def get_table_data(self, table: str, schema: str = None, id_=None):
        table = f"{schema}.{table}" if schema else table
        log.debug("Get data from table %s", table)
        s = f"SELECT * FROM {table}"
        if id_ is not None:
            s += f" WHERE id={id_}"
        self.cursor.execute(s + ";")
        r = self.cursor.fetchall()
        return r

    def get_table_row_count(self, table: str, schema: str = None):
        table = f"{schema}.{table}" if schema else table
        log.debug("Get row count from table %s", table)
        self.cursor.execute(f"SELECT count(*) FROM {table};")
        r = self.cursor.fetchall()[0][0]
        return r

    def delete_rows_from_table(self, table: str, schema: str = None,
                               ids=[]):
        table = f"{schema}.{table}" if schema else table
        for id_ in ids:
            log.debug("Delete %s in table %s", (id_, table))
            self.cursor.execute(f"DELETE FROM {table} WHERE id={id_};")

    def clear_table(self, table: str, schema: str = None):
        table = f"{schema}.{table}" if schema else table
        log.debug("Clear table %s", table)
        self.cursor.execute(
            f"TRUNCATE TABLE {table} CONTINUE IDENTITY CASCADE;")

    def drop_table(self, table: str, schema: str = None):
        table = f"{schema}.{table}" if schema else table
        log.debug("Drop table %s", table)
        self.cursor.execute(f"DROP TABLE {table};")

    def get_users(self):
        self.cursor.execute("""select usesysid as user_id,
                    usename as username,
                    usesuper as is_superuser,
                    passwd as password_md5,
                    valuntil as password_expiration
                    from pg_shadow
                    order by usename;""")
        users = self.cursor.fetchall()
        return [u[1] for u in users]

    def create_user(self, user: str, password: str, roles: list = []):
        self.cursor.execute(
            f"CREATE ROLE {user} WITH PASSWORD '{password}' {' '.join(roles)};")

    def drop_user(self, user: str):
        self.cursor.execute(f"""REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM {user};
                    REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public FROM {user};
                    REVOKE ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public FROM {user};
                    DROP USER {user};""")

    def drop_schema(self, schema: str):
        self.cursor.execute(f"drop schema {schema} cascade")
        self._con.commit()

    def drop_users_for_tenant(self, tenant: str):
        for user in self.get_users():
            if tenant in user:
                self.drop_user(user)

    def get_descriptors(self):
        self.cursor.execute("SELECT * FROM modules;")
        descriptors = {}
        for d in self.cursor.fetchall():
            descriptors[d[0]["id"]] = d[0]
        return descriptors

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            log.error("%s: %s", exc_type, exc_value)
        if not self.cursor.closed:
            self.cursor.close()
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


def purge_modules(tenant: str, database: str = "okapi_modules"):
    with Postgres(database=database) as pg:
        for s in pg.get_schemas():
            if s != "public" and s.startswith(tenant):
                pg.drop_schema(s)
        for user in pg.get_users():
            if user.startswith(tenant):
                pg.drop_user(user)
