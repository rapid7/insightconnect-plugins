import insightconnect_plugin_runtime
from .schema import PatchInput, PatchOutput, Component, Input, Output

# Custom imports below
from komand_rest.util.util import Common, determine_body_type


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

        data = determine_body_type(body_non_array, body_array)

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
