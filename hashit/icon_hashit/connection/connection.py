import base64
import hashlib

import komand
from komand.exceptions import ConnectionTestException
from .schema import ConnectionSchema


# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        pass

    def test(self):
        return {"success": True}