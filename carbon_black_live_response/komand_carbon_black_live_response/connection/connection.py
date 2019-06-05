import komand
from .schema import ConnectionSchema
# Custom imports below
import os
import contextlib
from cbapi.six.moves.configparser import RawConfigParser
from cbapi.response import CbEnterpriseResponseAPI
import cbapi.six as six
if six.PY3:
    from io import StringIO as StringIO
else:
    from cStringIO import StringIO

@contextlib.contextmanager
def temp_umask(umask):
    oldmask = os.umask(umask)
    try:
        yield
    finally:
        os.umask(oldmask)

class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        url = params.get('url')
        token = params.get('api_key').get('secretKey')
        ssl_verify = False

        self.logger.info("Connect: Connecting...")
        self.carbon_black = CbEnterpriseResponseAPI(url=url, token=token, ssl_verify=ssl_verify)
