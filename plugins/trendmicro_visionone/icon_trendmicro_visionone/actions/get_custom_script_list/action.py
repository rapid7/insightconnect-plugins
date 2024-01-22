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
        response = client.script.consume(
            lambda script_list_data: new_script_list_data.append(script_list_data.dict()),
            pytmv1.QueryOp(query_op),
            **fields,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while getting custom script list.",
                assistance="Please check your inputs and try again.",
                data=response.error,
            )
        # Return results
        self.logger.info("Returning Results...")
        return {Output.CUSTOM_SCRIPTS_LIST_RESP: new_script_list_data}
