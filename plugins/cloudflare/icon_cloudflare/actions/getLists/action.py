import insightconnect_plugin_runtime
from .schema import GetListsInput, GetListsOutput, Input, Output, Component

# Custom imports below
from icon_cloudflare.util.helpers import convert_dict_keys_to_camel_case


class GetLists(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="getLists", description=Component.DESCRIPTION, input=GetListsInput(), output=GetListsOutput()
        )

    def run(self, params={}):
        return {
            Output.LISTS: convert_dict_keys_to_camel_case(
                self.connection.api_client.get_lists(params.get(Input.ACCOUNTID)).get("result", [])
            )
        }
