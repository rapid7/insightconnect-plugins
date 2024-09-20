import json

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import ConnectionSchema, Input

# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.token = None

    def connect(self, params):
        self.token = params.get(Input.CRED_TOKEN).get("secretKey")

    def test(self):
        # Sending a request using the secretKey to test if it is valid
        url = "http://api.ipstack.com/" + "rapid7.com" + "?access_key=" + self.token + "&output=json"

        invalid_status_codes = ["404", "101", "102", "104", "106"]

        resp = insightconnect_plugin_runtime.helper.open_url(url)
        dic = json.loads(resp.read())
        if any(invalid_status_codes) in dic or "error" in dic:
            raise PluginException(
                data=dic,
                assistance="Please check your credentials and try again. If the issue persists, please contact support.",
                cause="An error has occurred. Please check your credentials are correct and that you have not exceeded the lookup limits.",
            )
        else:
            return {"success": True}
