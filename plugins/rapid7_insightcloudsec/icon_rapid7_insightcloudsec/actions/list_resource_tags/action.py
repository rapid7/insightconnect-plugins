import insightconnect_plugin_runtime
from .schema import ListResourceTagsInput, ListResourceTagsOutput, Input, Output, Component

# Custom imports below


class ListResourceTags(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_resource_tags",
            description=Component.DESCRIPTION,
            input=ListResourceTagsInput(),
            output=ListResourceTagsOutput(),
        )

    def run(self, params={}):
        return {
            Output.RESOURCETAGS: self.connection.api.list_resource_tags(params.get(Input.RESOURCEID)).get(
                "resource_tags", []
            )
        }
