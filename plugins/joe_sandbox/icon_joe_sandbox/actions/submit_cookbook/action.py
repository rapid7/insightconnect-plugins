import insightconnect_plugin_runtime
from .schema import SubmitCookbookInput, SubmitCookbookOutput, Input, Output, Component

# Custom imports below
import jbxapi
from base64 import b64decode
import binascii

class SubmitCookbook(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="submit_cookbook",
                description=Component.DESCRIPTION,
                input=SubmitCookbookInput(),
                output=SubmitCookbookOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE
        # TODO - If input bindings for connection can be done check to same if it you can do the same here

        cookbook = params.get("cookbook")
        parameters = params.get("parameters", {})
        additional_parameters = params.get("additional_parameters", {})

        additional_parameters.update({"accept-tac": 1})

        try:
            cookbook_bytes = b64decode(cookbook) if cookbook else None
        except binascii.Error:
            raise PluginException('Unable to decode base64 input for "cookbook". ' "Contents of the file must be encoded with base64!")

        try:
            webids = self.connection.api.submit_cookbook(cookbook_types, parameters, additional_parameters)
        except jbxapi.MissingParameterError as e:
            raise ConnectionTestException(
                cause = f"An error occurd: {e}",
                assistance = f"If the issue persists please contact support.",
            )
        except jbxapi.InvalidParameterError as e:
            raise ConnectionTestException(cause=str(e), assistance="If the issue persists please contact support.")
        except jbxapi.ApiError as e:
            raise ConnectionTestException(
                cause = f"An error occurd: {e}",
                assistance = f"If the issue persists please contact support.",
            )
        
        return webids
