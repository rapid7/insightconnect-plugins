from io import BytesIO

import insightconnect_plugin_runtime
from .schema import SubmitSampleInput, SubmitSampleOutput, Input, Output, Component

# Custom imports below
from base64 import b64decode
import binascii
from insightconnect_plugin_runtime.exceptions import PluginException


class SubmitSample(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_sample",
            description=Component.DESCRIPTION,
            input=SubmitSampleInput(),
            output=SubmitSampleOutput(),
        )

    def run(self, params={}):
        sample = params.get(Input.SAMPLE)
        cookbook = params.get(Input.COOKBOOK)
        parameters = params.get(Input.PARAMETERS, {})
        additional_parameters = params.get(Input.ADDITIONAL_PARAMETERS, {})
        filename = params.get(Input.FILENAME, "")

        additional_parameters.update({"accept-tac": 1})
        # The default seemed to have changed in the API...this matched the online documentation (default of false, 0)
        if "hybrid-decompilation" not in additional_parameters:
            additional_parameters.update({"hybrid-decompilation": 0})
        try:
            sample_bytes = BytesIO(b64decode(sample))
        except binascii.Error:
            raise PluginException(
                cause='Unable to decode base64 input for "sample". ',
                assistance="Contents of the file must be encoded with base64!",
            )

        try:
            cookbook_bytes = BytesIO(b64decode(cookbook)) if cookbook else None
        except binascii.Error:
            raise PluginException(
                cause='Unable to decode base64 input for "cookbook". ',
                assistance="Contents of the file must be encoded with base64!",
            )

        if filename:
            sample_tuple = (filename, sample_bytes)
            submission_id = self.connection.api.submit_sample(
                sample_tuple, cookbook_bytes, parameters, additional_parameters
            )
        else:
            submission_id = self.connection.api.submit_sample(
                sample_bytes, cookbook_bytes, parameters, additional_parameters
            )

        submission_id_object = submission_id.get("submission_id")
        self.logger.info(f"submission_id {submission_id_object}")

        return {Output.SUBMISSION_ID: submission_id_object}
