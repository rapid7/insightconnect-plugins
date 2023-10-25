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
        endpoints = params.get(Input.ENDPOINTS)
        query_op = params.get(Input.QUERY_OP)
        # Choose enum
        if "or" in query_op:
            query_op = pytmv1.QueryOp.OR
        elif "and" in query_op:
            query_op = pytmv1.QueryOp.AND
        new_endpoint_data = []
        # Make Action API Call
        self.logger.info("Making API Call...")
        try:
            client.consume_endpoint_data(
                lambda endpoint_data: new_endpoint_data.append(endpoint_data.json()),
                pytmv1.QueryOp(query_op),
                *endpoints,
            )
        except Exception as error:
            raise PluginException(
                cause="An error occurred while getting endpoint data.",
                assistance="Please check your inputs and try again.",
                data=error,
            )
        # Load json objects to list
        endpoint_data_resp = []
        for data in new_endpoint_data:
            endpoint_data_resp.append(json.loads(data))
        self.logger.info("Returning Results...")
        return {Output.ENDPOINT_DATA: endpoint_data_resp}
