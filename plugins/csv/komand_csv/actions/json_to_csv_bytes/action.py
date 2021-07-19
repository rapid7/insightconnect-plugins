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
        encoded_string = json_to_csv(params.get(Input.JSON)).encode()
        encoded_bytes = base64.encodebytes(encoded_string)
        return {Output.CSV_BYTES: encoded_bytes.decode()}
