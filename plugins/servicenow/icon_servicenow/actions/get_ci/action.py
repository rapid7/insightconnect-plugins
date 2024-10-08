import insightconnect_plugin_runtime
from .schema import GetCiInput, GetCiOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class GetCi(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_ci",
            description=Component.DESCRIPTION,
            input=GetCiInput(),
            output=GetCiOutput(),
        )

    def run(self, params={}):
        url = f"{self.connection.table_url}{params.get(Input.TABLE)}/{params.get(Input.SYSTEM_ID)}"
        method = "get"

        response = self.connection.request.make_request(url, method)

        try:
            result = response.get("resource", {}).get("result")
        except AttributeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

        return {Output.SERVICENOW_CI: result}
