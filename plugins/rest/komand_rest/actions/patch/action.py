import json
import ast

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
        data = params.get(Input.BODY)
        for item in data:
            if isinstance(item, (dict, str)):
                # TODO
                return item
            else:
                raise PluginException(cause="Incorrect data type",
                                      assistance="Please enter a valid object or string")

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
