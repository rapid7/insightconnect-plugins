import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below
import requests
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        pass

    def test(self):
        url = "http://sitereview.bluecoat.com/sitereview.jsp"
        try:
            resp = requests.get(url)
            resp.raise_for_status()
        except Exception as error:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNKNOWN, data=error)
        return {"success": "http://sitereview.bluecoat.com/sitereview.jsp"}
