# -*- coding: utf-8 -*-
# Generated at 2024-03-01

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.ldp")


class Ldp(FolioApi):
    """Library Data Platform API

    API calls to obtain information generated by the LDP
    """

    def get_configs(self):
        """Return a list of configuration items

        ``GET /ldp/config``

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/Ldp_get_configs_return.schema 
        """
        return self.call("GET", "/ldp/config")

    def get_config(self, key: str):
        """Retrieve a single configuration by key

        ``GET /ldp/config/{key}``

        Args:
            key (str)

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/Ldp_get_config_return.schema 
        """
        return self.call("GET", f"/ldp/config/{key}")

    def modify_config(self, key: str, config: dict):
        """Modify or add a configuration by key

        ``PUT /ldp/config/{key}``

        Args:
            key (str)
            config (dict): See Schema below

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/Ldp_modify_config_request.schema
        """
        return self.call("PUT", f"/ldp/config/{key}", data=config)

    def get_tables(self):
        """Return a list of all tables in all schemas

        ``GET /ldp/db/tables``

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/Ldp_get_tables_return.schema 
        """
        return self.call("GET", "/ldp/db/tables")

    def get_columns(self, **kwargs):
        """Return a list of all columns in a table. Example: /ldp/db/columns?schema=public&table=user_users

        ``GET /ldp/db/columns``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            schema (str):  The name of the schema containing the specified table
                    
                    Example:
                    
                     - public
            table (str):  The name of the table within the specified schema
                    
                    Example:
                    
                     - user_users

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/Ldp_get_columns_return.schema 
        """
        return self.call("GET", "/ldp/db/columns", query=kwargs)

    def set_query(self, query: dict):
        """Send a query to the LDP server and obtain results

        ``POST /ldp/db/query``

        Args:
            query (dict): See Schema below

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/Ldp_set_query_request.schema
            .. literalinclude:: ../files/Ldp_set_query_return.schema 
        """
        return self.call("POST", "/ldp/db/query", data=query)

    def set_report(self, report: dict):
        """

        ``POST /ldp/db/reports``

        Args:
            report (dict): See Schema below

        Returns:
            dict: See Schema below

        Schema:

            .. literalinclude:: ../files/Ldp_set_report_request.schema
            .. literalinclude:: ../files/Ldp_set_report_return.schema 
        """
        return self.call("POST", "/ldp/db/reports", data=report)
