import insightconnect_plugin_runtime
from .schema import JsonToCsvBytesInput, JsonToCsvBytesOutput, Input, Output, Component

# Custom imports below
import base64
from komand_csv.util.utils import json_to_csv


class JsonToCsvBytes(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="json_to_csv_bytes",
            description=Component.DESCRIPTION,
            input=JsonToCsvBytesInput(),
            output=JsonToCsvBytesOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        json_object = params.get(Input.JSON, {})
        # END INPUT BINDING - DO NOT REMOVE

        csv_string = json_to_csv(json_object)  # str
        csv_bytes = csv_string.encode("utf-8")  # explicit UTF-8
        csv_b64 = base64.b64encode(csv_bytes).decode("ascii")  # NO line wraps
        return {Output.CSV_BYTES: csv_b64}
