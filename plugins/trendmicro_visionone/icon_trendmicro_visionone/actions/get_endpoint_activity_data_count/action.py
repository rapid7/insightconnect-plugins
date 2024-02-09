import insightconnect_plugin_runtime
from .schema import (
    GetEndpointActivityDataCountInput,
    GetEndpointActivityDataCountOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1
import json


class GetEndpointActivityDataCount(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_endpoint_activity_data_count",
            description=Component.DESCRIPTION,
            input=GetEndpointActivityDataCountInput(),
            output=GetEndpointActivityDataCountOutput(),
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
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.endpoint.get_activity_count(
            start_time=start_date_time,
            end_time=end_date_time,
            select=select,
            top=top,
            op=pytmv1.QueryOp(query_op),
            **fields,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while getting endpoint activity data count.",
                assistance="Please check your inputs and try again.",
                data=response.error,
            )
        # Return results
        self.logger.info("Returning Results...")
        return {Output.TOTAL_COUNT: response.response.total_count}
