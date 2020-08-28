import insightconnect_plugin_runtime
from .schema import ConnectionSchema
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
# Custom imports below
import requests


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        result = requests.get("https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/info")
        if result.status_code == requests.codes.ok:
            return {"success": True}
        else:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
