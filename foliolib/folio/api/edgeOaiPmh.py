# -*- coding: utf-8 -*-
# Generated at 2022-04-08

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.edgeOaiPmh")


class EdgeOaiPmh(FolioApi):
    """Edge API - OAI-PMH

    Edge API to interface with FOLIO for 3rd party harvesters to harvest metadta via OAI-PMH
    """

    def get_oais(self, **kwargs):
        """Run OAI-PMH request

        ``GET /oai``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            verb (str):  One of the defined OAI-PMH verbs
            identifier (str):  The unique identifier of the item in the repository from which the record must be disseminated
            metadataPrefix (str):  The metadataPrefix of the format that should be included in the metadata part of the returned record
            from (datetime):  UTC datetime value, which specifies a lower bound for datestamp-based selective harvesting
                    
                    Example:
                    
                     - 2018-11-25 16:17:18+00:00
            until (datetime):  UTC datetime value, which specifies a upper bound for datestamp-based selective harvesting
                    
                    Example:
                    
                     - 2018-11-28 14:15:16+00:00
            set (str):  SetSpec value, which specifies set criteria for selective harvesting
            resumptionToken (str):  The flow control token returned by a ListIdentifiers request that issued an incomplete list
            apikey (str):  API Key

        Returns:
            str: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiRequestNotAcceptable: Not Acceptable
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/EdgeOaiPmh_get_oais_return.schema 
        """
        return self.call("GET", "/oai", query=kwargs)

    def set_oai(self, **kwargs):
        """Run OAI-PMH request

        ``POST /oai``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            verb (str):  One of the defined OAI-PMH verbs
            identifier (str):  The unique identifier of the item in the repository from which the record must be disseminated
            metadataPrefix (str):  The metadataPrefix of the format that should be included in the metadata part of the returned record
            from (datetime):  UTC datetime value, which specifies a lower bound for datestamp-based selective harvesting
                    
                    Example:
                    
                     - 2018-11-25 16:17:18+00:00
            until (datetime):  UTC datetime value, which specifies a upper bound for datestamp-based selective harvesting
                    
                    Example:
                    
                     - 2018-11-28 14:15:16+00:00
            set (str):  SetSpec value, which specifies set criteria for selective harvesting
            resumptionToken (str):  The flow control token returned by a ListIdentifiers request that issued an incomplete list
            apikey (str):  API Key

        Returns:
            str: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiRequestNotAcceptable: Not Acceptable
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/EdgeOaiPmh_set_oai_return.schema 
        """
        return self.call("POST", "/oai", query=kwargs)

    def get_oai(self, apiKeyPath: str, **kwargs):
        """Run OAI-PMH request

        ``GET /oai/{apiKeyPath}``

        Args:
            apiKeyPath (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            verb (str):  One of the defined OAI-PMH verbs
            identifier (str):  The unique identifier of the item in the repository from which the record must be disseminated
            metadataPrefix (str):  The metadataPrefix of the format that should be included in the metadata part of the returned record
            from (datetime):  UTC datetime value, which specifies a lower bound for datestamp-based selective harvesting
                    
                    Example:
                    
                     - 2018-11-25 16:17:18+00:00
            until (datetime):  UTC datetime value, which specifies a upper bound for datestamp-based selective harvesting
                    
                    Example:
                    
                     - 2018-11-28 14:15:16+00:00
            set (str):  SetSpec value, which specifies set criteria for selective harvesting
            resumptionToken (str):  The flow control token returned by a ListIdentifiers request that issued an incomplete list

        Returns:
            str: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiRequestNotAcceptable: Not Acceptable
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/EdgeOaiPmh_get_oai_return.schema 
        """
        return self.call("GET", f"/oai/{apiKeyPath}", query=kwargs)

    def set_oai_for_apiKeyPath(self, apiKeyPath: str, **kwargs):
        """Run OAI-PMH request

        ``POST /oai/{apiKeyPath}``

        Args:
            apiKeyPath (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            verb (str):  One of the defined OAI-PMH verbs
            identifier (str):  The unique identifier of the item in the repository from which the record must be disseminated
            metadataPrefix (str):  The metadataPrefix of the format that should be included in the metadata part of the returned record
            from (datetime):  UTC datetime value, which specifies a lower bound for datestamp-based selective harvesting
                    
                    Example:
                    
                     - 2018-11-25 16:17:18+00:00
            until (datetime):  UTC datetime value, which specifies a upper bound for datestamp-based selective harvesting
                    
                    Example:
                    
                     - 2018-11-28 14:15:16+00:00
            set (str):  SetSpec value, which specifies set criteria for selective harvesting
            resumptionToken (str):  The flow control token returned by a ListIdentifiers request that issued an incomplete list

        Returns:
            str: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiRequestNotFound: Not Found
            OkapiRequestNotAcceptable: Not Acceptable
            OkapiRequestUnprocessableEntity: Unprocessable Entity
            OkapiFatalError: Server Error
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/EdgeOaiPmh_set_oai_for_apiKeyPath_return.schema 
        """
        return self.call("POST", f"/oai/{apiKeyPath}", query=kwargs)

    def get_healths(self):
        """Health Check

        ``GET /admin/health``
        """
        return self.call("GET", "/admin/health")
