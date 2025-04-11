from io import BytesIO

import insightconnect_plugin_runtime
from .schema import SubmitCookbookInput, SubmitCookbookOutput, Input, Output, Component

# Custom imports below
from base64 import b64decode
import binascii
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException

import jbxapi


class SubmitCookbook(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_cookbook",
            description=Component.DESCRIPTION,
            input=SubmitCookbookInput(),
            output=SubmitCookbookOutput(),
        )

    def run(self, params={}):
        cookbook = params.get(Input.COOKBOOK)
        parameters = params.get(Input.PARAMETERS, {})
        additional_parameters = params.get(Input.ADDITIONAL_PARAMETERS, {})

        additional_parameters.update({"accept-tac": 1})

        try:
            cookbook_bytes = BytesIO(b64decode(cookbook)) if cookbook else None
        except binascii.Error:
            raise PluginException(
                cause='Unable to decode base64 input for "cookbook". ',
                assistance="Contents of the file must be encoded with base64!",
            )

        try:
            submission_id = self.connection.api.submit_cookbook(cookbook_bytes, parameters, additional_parameters)
        except jbxapi.MissingParameterError as error:
            raise ConnectionTestException(
                cause=f"An error occurred: {error}",
                assistance="If the issue persists please contact support.",
            )
        except jbxapi.InvalidParameterError as error:
            raise ConnectionTestException(cause=str(error), assistance="If the issue persists please contact support.")
        except jbxapi.ApiError as error:
            raise ConnectionTestException(
                cause=f"An error occurred: {error}",
                assistance="If the issue persists please contact support.",
            )

        return {Output.SUBMISSION_ID: submission_id.get("submission_id")}
