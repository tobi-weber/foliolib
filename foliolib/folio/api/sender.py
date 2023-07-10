# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.sender")


class Sender(FolioApi):
    """

    
    """

    def set_messageDelivery(self, messageDelivery: dict):
        """Send prepered notification to delivery channels

        ``POST /message-delivery``

        Args:
            messageDelivery (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Sender_set_messageDelivery_request.schema
        """
        return self.call("POST", "/message-delivery", data=messageDelivery)
