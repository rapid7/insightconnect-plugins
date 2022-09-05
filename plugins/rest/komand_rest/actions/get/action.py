import insightconnect_plugin_runtime
from .schema import GetInput, GetOutput, Component, Input, Output

# Custom imports below
from komand_rest.util.util import Common


class Get(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get", description=Component.DESCRIPTION, input=GetInput(), output=GetOutput()
        )

    def run(self, params={}):
        response = self.connection.api.call_api(
            method="GET",
            path=params.get(Input.ROUTE),
            headers=params.get(Input.HEADERS, {}),
            data=params.get(Input.BODY)
        )

        return {
            Output.BODY_OBJECT: Common.body_object(response),
            Output.BODY_STRING: response.text,
            Output.STATUS: response.status_code,
            Output.HEADERS: Common.copy_dict(response.headers),
        }
