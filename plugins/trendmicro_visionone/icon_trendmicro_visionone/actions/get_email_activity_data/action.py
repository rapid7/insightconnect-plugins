import insightconnect_plugin_runtime
from .schema import (
    GetEmailActivityDataInput,
    GetEmailActivityDataOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1


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
        # Make sure response contains < 5K entries
        self.logger.info("Checking Response Size...")
        count = client.email.get_activity_count(
            start_time=start_date_time,
            end_time=end_date_time,
            select=select,
            top=top,
            op=pytmv1.QueryOp(query_op),
            **fields,
        )
        if "error" in count.result_code.lower():
            raise PluginException(
                cause="An error occurred while getting email activity data count.",
                assistance="Please check your inputs and try again.",
                data=count.error,
            )
        total_count = count.response.total_count
        if total_count >= 5000:
            raise PluginException(
                cause="Attempted query is over-sized (more than 5K results).",
                assistance="Please refine your inputs to reduce search size and try again.",
            )
        # Get Email Activity
        new_email_activity_data = []
        self.logger.info("Getting Email Activity...")
        response = client.email.consume_activity(
            lambda email_activity_data: new_email_activity_data.append(email_activity_data.model_dump()),
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
