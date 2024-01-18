import insightconnect_plugin_runtime
from .schema import GetEmailActivityDataInput, GetEmailActivityDataOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1
import json


class GetEmailActivityData(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_email_activity_data",
            description=Component.DESCRIPTION,
            input=GetEmailActivityDataInput(),
            output=GetEmailActivityDataOutput(),
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
        new_email_activity_data = []
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.consume_email_activity_data(
            lambda email_activity_data: new_email_activity_data.append(email_activity_data.json()),
            start_time=start_date_time,
            end_time=end_date_time,
            select=select,
            top=top,
            op=pytmv1.QueryOp(query_op),
            **fields,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while getting email activity data.",
                assistance="Please check your inputs and try again.",
                data=response.error,
            )
        # Return results
        self.logger.info("Returning Results...")
        return {Output.EMAIL_ACTIVITY_DATA_RESP: new_email_activity_data}
