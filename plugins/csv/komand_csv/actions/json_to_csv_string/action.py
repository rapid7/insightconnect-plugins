import insightconnect_plugin_runtime
from .schema import JsonToCsvStringInput, JsonToCsvStringOutput, Input, Output, Component

# Custom imports below
from komand_csv.util.utils import json_to_csv


class JsonToCsvString(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="json_to_csv_string",
            description=Component.DESCRIPTION,
            input=JsonToCsvStringInput(),
            output=JsonToCsvStringOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        json_object = params.get(Input.JSON, {})
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.CSV_STRING: json_to_csv(json_object)}
