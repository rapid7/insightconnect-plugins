import insightconnect_plugin_runtime
from .schema import DeleteInput, DeleteOutput, Component, Input, Output

# Custom imports below
from komand_rest.util.util import Common


class Delete(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete",
            description=Component.DESCRIPTION,
            input=DeleteInput(),
            output=DeleteOutput(),
        )

    def run(self, params={}):
        response = self.connection.api.call_api(
            method="DELETE",
            path=params.get(Input.ROUTE),
            data=params.get(Input.BODY, {}),
            headers=params.get(Input.HEADERS, {}),
        )

        return {
            Output.BODY_OBJECT: Common.body_object(response),
            Output.BODY_STRING: response.text,
            Output.STATUS: response.status_code,
            Output.HEADERS: Common.copy_dict(response.headers),
        }
