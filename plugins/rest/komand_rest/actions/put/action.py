import insightconnect_plugin_runtime
from .schema import PutInput, PutOutput, Component, Input, Output

# Custom imports below
from komand_rest.util.util import Common
from komand_rest.util.util import determine_body_type


class Put(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="put", description=Component.DESCRIPTION, input=PutInput(), output=PutOutput()
        )

    def run(self, params={}):
        body_non_array = params.get(Input.BODY, {})
        body_array = params.get(Input.BODY_AS_AN_ARRAY, [])

        data = determine_body_type(body_non_array, body_array)

        response = self.connection.api.call_api(
            method="PUT",
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
