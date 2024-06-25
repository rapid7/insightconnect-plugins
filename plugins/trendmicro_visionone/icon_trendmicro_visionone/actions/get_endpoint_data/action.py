import insightconnect_plugin_runtime
from .schema import (
    GetEndpointDataInput,
    GetEndpointDataOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1
import json


class GetEndpointData(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_endpoint_data",
            description=Component.DESCRIPTION,
            input=GetEndpointDataInput(),
            output=GetEndpointDataOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        fields = params.get(Input.FIELDS)
        query_op = params.get(Input.QUERY_OP)
        # Choose enum
        if "or" in query_op:
            query_op = pytmv1.QueryOp.OR
        elif "and" in query_op:
            query_op = pytmv1.QueryOp.AND
        new_endpoint_data = []
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.endpoint.consume_data(
            lambda endpoint_data: new_endpoint_data.append(json.loads(endpoint_data.model_dump_json())),
            pytmv1.QueryOp(query_op),
            **fields,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while getting endpoint data.",
                assistance="Please check your inputs and try again.",
                data=response.error,
            )
        self.logger.info("Returning Results...")
        return {Output.ENDPOINT_DATA: new_endpoint_data}
