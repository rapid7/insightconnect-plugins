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

        invalid_status_codes = {
            "404": "The requested resource does not exist, Error 404",
            "101": "The access key is blank or invalid",
            "102": "The access key was recognized but the user account is not active",
            "104": "The maximum monthly ip lookups has been hit",
            "106": "The supplied host address/domain is invalid"
        }

        resp = insightconnect_plugin_runtime.helper.open_url(url)
        dic = json.loads(resp.read())
        if "error" not in dic:
            return {"success": True}
        else:
            for error, cause in invalid_status_codes.items():
                self.logger.info(f"Error: {error} . {cause}")
                raise PluginException(cause=cause, data=dic)
                break
