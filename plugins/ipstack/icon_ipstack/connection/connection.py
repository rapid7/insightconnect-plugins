import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException

# Custom imports below
import json


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.token = None

    def connect(self, params):
        self.token = params.get(Input.CRED_TOKEN).get("secretKey")

    def test(self):
        url = "http://api.ipstack.com/" + "check" + "?access_key=" + self.token + "&output=json"
        resp = insightconnect_plugin_runtime.helper.open_url(url)
        dic = json.loads(resp.read())
        if "error" in dic:
            code = dic["error"].get("code")
            if code != 200:
                raise ConnectionTestException(
                    cause="Connection test failed", assistance="Check the API key and try again"
                )
        else:
            return {"success": True}
