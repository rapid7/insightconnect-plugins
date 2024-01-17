import insightconnect_plugin_runtime
from .schema import (
    GetCustomScriptListInput,
    GetCustomScriptListOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1
import json


class GetCustomScriptList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_custom_script_list",
            description=Component.DESCRIPTION,
            input=GetCustomScriptListInput(),
            output=GetCustomScriptListOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        query_op = params.get(Input.QUERY_OP)
        fields = params.get(Input.FIELDS)
        # Choose enum
        if "or" in query_op:
            query_op = pytmv1.QueryOp.OR
        elif "and" in query_op:
            query_op = pytmv1.QueryOp.AND
        new_script_list_data = []
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.consume_custom_script_list(
            lambda script_list_data: new_script_list_data.append(script_list_data.json()),
            pytmv1.QueryOp(query_op),
            **fields,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while getting custom script list.",
                assistance="Please check your inputs and try again.",
                data=response.error,
            )
        # Json load suspicious list objects
        custom_script_list_resp = []
        for item in response.response.dict().get("items"):
            custom_script_list_resp.append(json.loads(json.dumps(item)))
        # Return results
        self.logger.info("Returning Results...")
        print(response)
        return custom_script_list_resp
        # return {Output.SANDBOX_SUSPICIOUS_LIST_RESP: sandbox_suspicious_list_resp}
