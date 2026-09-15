import insightconnect_plugin_runtime
from .schema import GetCiInput, GetCiOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_servicenow.util.validators import validate_record_identifier, validate_table_name


class GetCi(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_ci",
            description=Component.DESCRIPTION,
            input=GetCiInput(),
            output=GetCiOutput(),
        )

    def run(self, params={}):
        table = validate_table_name(params.get(Input.TABLE))
        system_id = validate_record_identifier(params.get(Input.SYSTEM_ID), "system ID")
        url = f"{self.connection.table_url}{table}/{system_id}"
        method = "get"

        response = self.connection.request.make_request(url, method)

        try:
            result = response.get("resource", {}).get("result")
        except AttributeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

        return {Output.SERVICENOW_CI: result}
