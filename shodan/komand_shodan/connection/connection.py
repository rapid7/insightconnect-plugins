import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
import shodan


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.token = None

    def connect(self, params={}):
        self.token = params[Input.TOKEN]["secretKey"]

    def test(self):
        try:
            shodan.Shodan(self.token).host("8.8.8.8")
            return {"Success": True}
        except shodan.exception.APIError as e:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVER_ERROR, data=e)
