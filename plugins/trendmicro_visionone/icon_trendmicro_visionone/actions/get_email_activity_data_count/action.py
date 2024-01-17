import insightconnect_plugin_runtime
from .schema import GetEmailActivityDataCountInput, GetEmailActivityDataCountOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1
import json


class GetEmailActivityDataCount(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_email_activity_data_count",
            description=Component.DESCRIPTION,
            input=GetEmailActivityDataCountInput(),
            output=GetEmailActivityDataCountOutput(),
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
        response = client.get_email_activity_data_count(
            start_time=start_date_time,
            end_time=end_date_time,
            select=select,
            top=top,
            op=pytmv1.QueryOp(query_op),
            **fields,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while getting email activity data count.",
                assistance="Please check your inputs and try again.",
                data=response.error,
            )
        # Json load suspicious list objects
        email_activity_data_count_resp = []
        for item in response.response.dict().get("items"):
            email_activity_data_count_resp.append(json.loads(json.dumps(item)))
        # Return results
        self.logger.info("Returning Results...")
        print(response)
        return email_activity_data_count_resp
        # return {Output.SANDBOX_SUSPICIOUS_LIST_RESP: sandbox_suspicious_list_resp}
