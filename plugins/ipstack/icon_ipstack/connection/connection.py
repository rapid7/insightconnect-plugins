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
        self.token = params.get(Input.CRED_TOKEN, {}).get("secretKey", "").strip()

    def test(self):
        # Sending a request using the secretKey to test if it is valid
        url = f"http://api.ipstack.com/" + "example.com" + "?access_key=" + self.token + "&output=json"

        try:
            response = insightconnect_plugin_runtime.helper.open_url(url)
            parsed_response = json.loads(response.read())
        except Exception:
            raise PluginException(PluginException.Preset.SERVER_ERROR)

        # All requests are returned as a 200 from IPStack. To find out if successful or not, we need to look in the parsed response to find if any error messages are returned or not
        success = parsed_response.get("success", True)
        if success:
            return {"success": True}
        raise PluginException(
            data=parsed_response,
            assistance="Please check your credentials and try again. If the issue persists, please contact support.",
            cause="An error has occurred. Please check your credentials are correct and that you have not exceeded the lookup limits.",
        )
