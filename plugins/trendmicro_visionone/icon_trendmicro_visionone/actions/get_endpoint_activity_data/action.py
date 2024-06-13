import insightconnect_plugin_runtime
from .schema import (
    GetEndpointActivityDataInput,
    GetEndpointActivityDataOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1
import json


class GetEndpointActivityData(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_endpoint_activity_data",
            description=Component.DESCRIPTION,
            input=GetEndpointActivityDataInput(),
            output=GetEndpointActivityDataOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        top = params.get(Input.TOP)
        start_date_time = params.get(Input.START_DATE_TIME)
        end_date_time = params.get(Input.END_DATE_TIME)
        select = params.get(Input.SELECT)
        query_op = params.get(Input.QUERY_OP)
        fields = params.get(Input.FIELDS)
        # Choose enum
        if "or" in query_op:
            query_op = pytmv1.QueryOp.OR
        elif "and" in query_op:
            query_op = pytmv1.QueryOp.AND
        # Make sure response contains < 5K entries
        self.logger.info("Checking Response Size...")
        count = client.endpoint.get_activity_count(
            start_time=start_date_time,
            end_time=end_date_time,
            select=select,
            top=top,
            op=pytmv1.QueryOp(query_op),
            **fields,
        )
        if "error" in count.result_code.lower():
            raise PluginException(
                cause="An error occurred while getting endpoint activity data count.",
                assistance="Please check your inputs and try again.",
                data=count.error,
            )
        total_count = count.response.total_count
        if total_count > 5000:
            raise PluginException(
                cause="Attempted query is over-sized (more than 5K results).",
                assistance="Please refine your inputs to reduce search size and try again.",
            )
        # Get Endpoint Activity
        new_endpoint_activity_data = []
        self.logger.info("Getting Endpoint Activity...")
        response = client.endpoint.consume_activity(
            lambda endpoint_activity_data: new_endpoint_activity_data.append(endpoint_activity_data.model_dump()),
            start_time=start_date_time,
            end_time=end_date_time,
            select=select,
            top=top,
            op=pytmv1.QueryOp(query_op),
            **fields,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while getting endpoint activity data.",
                assistance="Please check your inputs and try again.",
                data=response.error,
            )
        # Default values for keys that may be null
        default_values = {
            "dpt": 0,
            "logonUser": [],
            "objectPort": 0,
            "objectSigner": [],
            "objectSignerValid": [],
            "spt": 0,
            "tags": [],
        }
        # Handling null values or missing keys
        for data in new_endpoint_activity_data:
            for key, default_value in default_values.items():
                try:
                    if data[key] is None:
                        data[key] = default_value
                except KeyError:
                    data[key] = default_value
        # Return results
        self.logger.info("Returning Results...")
        return {Output.ENDPOINT_ACTIVITY_DATA_RESP: new_endpoint_activity_data}
