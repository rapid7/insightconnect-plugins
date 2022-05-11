import copy

import insightconnect_plugin_runtime
from komand_dynamodb.util.constants import AWS_NONE_VALUE
from .schema import InsertOutput, InsertInput, Component, Input, Output

# Custom imports below
from ...util.utils import Utils


class Insert(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="insert",
            description=Component.DESCRIPTION,
            input=InsertInput(),
            output=InsertOutput(),
        )

    def run(self, params={}):
        mapped_params = copy.deepcopy(params)
        mapped_params[Input.RETURN_ITEM_COLLECTION_METRICS] = Utils.map_return_item_collection_metrics(
            params.get(Input.RETURN_ITEM_COLLECTION_METRICS, False)
        )
        mapped_params[Input.RETURN_VALUES] = Utils.map_return_values(params.get(Input.RETURN_VALUES, False))
        mapped_params[Input.RETURN_CONSUMED_CAPACITY] = params.get(Input.RETURN_CONSUMED_CAPACITY, AWS_NONE_VALUE)
        self.connection.client.insert_data(input_schema=self.input.schema, params=mapped_params)
        return {Output.SUCCESS: True}
