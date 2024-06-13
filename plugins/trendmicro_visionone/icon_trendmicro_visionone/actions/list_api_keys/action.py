import insightconnect_plugin_runtime
from .schema import ListApiKeysInput, ListApiKeysOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1
import json


class ListApiKeys(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_api_keys",
            description=Component.DESCRIPTION,
            input=ListApiKeysInput(),
            output=ListApiKeysOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        top = params.get(Input.TOP, 50)
        query_op = params.get(Input.QUERY_OP)
        fields = params.get(Input.FIELDS)
        # Choose enum
        if "or" in query_op:
            query_op = pytmv1.QueryOp.OR
        elif "and" in query_op:
            query_op = pytmv1.QueryOp.AND
        api_keys_list = []
        # Make Action API Call
        self.logger.info("Creating API key list...")
        try:
            client.api_key.consume(
                lambda api_key: api_keys_list.append(json.loads(api_key.model_dump_json())),
                top=top,
                op=query_op,
                **fields,
            )
        except Exception as error:
            raise PluginException(
                cause="An error occurred while trying to get the API key list.",
                assistance="Please check the provided parameters and try again.",
                data=error,
            )
        # Return results
        self.logger.info("Returning Results...")
        return {Output.TOTAL_COUNT: len(api_keys_list), Output.ITEMS: api_keys_list}
