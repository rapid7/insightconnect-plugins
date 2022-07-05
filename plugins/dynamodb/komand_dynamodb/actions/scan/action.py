# Custom imports below
import copy

import insightconnect_plugin_runtime
from .schema import ScanInput, ScanOutput, Output, Component, Input
from .extra_schema import exclusive_start_key_schema
from komand_dynamodb.util.constants import AWS_NONE_VALUE
from komand_dynamodb.util.validation import additional_argument_validator


class Scan(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="scan",
            description=Component.DESCRIPTION,
            input=ScanInput(),
            output=ScanOutput(),
        )

    @additional_argument_validator(Input.EXCLUSIVE_START_KEY, exclusive_start_key_schema)
    def run(self, params={}):
        mapped_params = copy.deepcopy(params)
        mapped_params[Input.RETURN_CONSUMED_CAPACITY] = params.get(Input.RETURN_CONSUMED_CAPACITY, AWS_NONE_VALUE)

        results = self.connection.client.scan_table(input_schema=self.input.schema, params=mapped_params)
        return {
            Output.COUNT: results.get("Count", 0),
            Output.ITEMS: results.get("Items", []),
            Output.RESPONSEMETADATA: results.get("ResponseMetadata"),
            Output.SCANNEDCOUNT: results.get("ScannedCount"),
        }
