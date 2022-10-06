import insightconnect_plugin_runtime
from .schema import GetItemInput, GetItemOutput, Input, Output, Component

# Custom imports below

import copy
from komand_dynamodb.util.validation import additional_argument_validator
from komand_dynamodb.util.extra_schemas.get_item import key_schema


class GetItem(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_item", description=Component.DESCRIPTION, input=GetItemInput(), output=GetItemOutput()
        )

    @additional_argument_validator(Input.KEY, key_schema)
    def run(self, params={}):
        mapped_params = copy.deepcopy(params)
        results = self.connection.client.get_item(input_schema=self.input.schema, params=mapped_params)
        return {Output.ITEM: results}
