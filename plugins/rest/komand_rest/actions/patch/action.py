import insightconnect_plugin_runtime
from .schema import PatchInput, PatchOutput, Component, Input, Output

# Custom imports below
from komand_rest.util.util import Common
from insightconnect_plugin_runtime.exceptions import PluginException


class Patch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="patch",
            description=Component.DESCRIPTION,
            input=PatchInput(),
            output=PatchOutput(),
        )

    def run(self, params={}):
        """
        If both inputs exist throw pluginException
        Otherwise determine which one is empty
        Send non-empty data
        """
        body_non_array = params.get(Input.BODY, {})
        body_array = params.get(Input.BODY_AS_AN_ARRAY, [])

        if body_array and body_non_array:
            raise PluginException(
                cause="You cannot send both inputs",
                assistance="Try sending data either as an array OR an object, not both.",
            )
        elif body_array:
            data = body_array
        elif body_non_array:
            data = body_non_array
        else:
            data = None

        response = self.connection.api.call_api(
            method="PATCH",
            path=params.get(Input.ROUTE),
            json_data=data,
            headers=params.get(Input.HEADERS, {}),
        )

        return {
            Output.BODY_OBJECT: Common.body_object(response),
            Output.BODY_STRING: response.text,
            Output.STATUS: response.status_code,
            Output.HEADERS: Common.copy_dict(response.headers),
        }
