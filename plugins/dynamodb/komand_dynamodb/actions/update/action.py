import copy

import insightconnect_plugin_runtime
from .schema import UpdateInput, UpdateOutput, Component, Input, Output
from komand_dynamodb.util.constants import AWS_NONE_VALUE

# Custom imports below
from ...util.utils import Utils


class Update(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update",
            description=Component.DESCRIPTION,
            input=UpdateInput(),
            output=UpdateOutput(),
        )

    def run(self, params={}):
        mapped_params = copy.deepcopy(params)
        mapped_params[Input.RETURN_ITEM_COLLECTION_METRICS] = Utils.map_return_item_collection_metrics(
            params.get(Input.RETURN_ITEM_COLLECTION_METRICS, False)
        )
        mapped_params[Input.RETURN_CONSUMED_CAPACITY] = params.get(Input.RETURN_CONSUMED_CAPACITY, AWS_NONE_VALUE)
        mapped_params[Input.RETURN_VALUES] = params.get(Input.RETURN_VALUES, AWS_NONE_VALUE)
        self.connection.client.update_data(input_schema=self.input.schema, params=mapped_params)
        return {Output.SUCCESS: True}
