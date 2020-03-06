import komand
from .schema import ConnectionSchema
from komand.exceptions import ConnectionTestException
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        result = requests.get("https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/info")
        if (result.status_code == requests.codes.ok) is True:
            return {"success": True}
        else:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
