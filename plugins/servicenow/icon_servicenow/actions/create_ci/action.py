import insightconnect_plugin_runtime
from .schema import CreateCiInput, CreateCiOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class CreateCi(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_ci",
            description=Component.DESCRIPTION,
            input=CreateCiInput(),
            output=CreateCiOutput(),
        )

    def run(self, params={}):
        url = f"{self.connection.table_url}{params.get(Input.TABLE)}"
        payload = params.get(Input.CREATE_DATA)
        method = "post"

        response = self.connection.request.make_request(url, method, payload=payload)

        try:
            result = response.get("resource", {}).get("result")
        except AttributeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

        sys_id = result.get("sys_id")

        if sys_id is None:
            raise PluginException(
                cause="Error: create_ci failed - no system_id returned.",
                assistance=f"Response: {response.text}",
            )

        return {Output.SYSTEM_ID: sys_id}
