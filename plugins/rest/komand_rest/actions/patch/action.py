import json
import ast

import insightconnect_plugin_runtime
from .schema import PatchInput, PatchOutput, Component, Input, Output

# Custom imports below
from komand_rest.util.util import Common


class Patch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="patch",
            description=Component.DESCRIPTION,
            input=PatchInput(),
            output=PatchOutput(),
        )

    def run(self, params={}):
        response = self.connection.api.call_api(
            method="PATCH",
            path=params.get(Input.ROUTE),
            json_data=ast.literal_eval(params.get(Input.BODY)),
            headers=params.get(Input.HEADERS, {}),
        )

        return {
            Output.BODY_OBJECT: Common.body_object(response),
            Output.BODY_STRING: response.text,
            Output.STATUS: response.status_code,
            Output.HEADERS: Common.copy_dict(response.headers),
        }
