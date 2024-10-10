import insightconnect_plugin_runtime

from .schema import GetResourceIdInput, GetResourceIdOutput, Input, Output, Component


# Custom imports below


class GetResourceId(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_resource_id",
            description=Component.DESCRIPTION,
            input=GetResourceIdInput(),
            output=GetResourceIdOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        limit = params.get(Input.LIMIT)
        offset = params.get(Input.OFFSET)
        search_string = params.get(Input.SEARCH_STRING)
        # END INPUT BINDING - DO NOT REMOVE

        response = self.connection.api.get_resource_id(
            {
                "limit": limit,
                "offset": offset,
                "search_string": search_string,
            }
        )

        return {
            Output.RESOURCES: response.get("resources", []),
            Output.TOTALCOUNT: response.get("totalCount", 0),
        }
