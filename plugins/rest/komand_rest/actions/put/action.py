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
        headers = params.get(Input.HEADERS, {})
        path = params.get(Input.ROUTE, "")
        body_dict = params.get(Input.BODY_OBJECT, {})
        body_non_dict = params.get(Input.BODY_ANY, "")

        data = determine_body_type(body_dict, body_non_dict)

        response = self.connection.api.call_api(method="PUT", path=path, data=data, headers=headers)

        return {
            Output.BODY_OBJECT: Common.body_object(response),
            Output.BODY_STRING: response.text,
            Output.STATUS: response.status_code,
            Output.HEADERS: Common.copy_dict(response.headers),
        }
