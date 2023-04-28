import insightconnect_plugin_runtime
from .schema import ListGroupsInput, ListGroupsOutput, Input, Output, Component

# Custom imports below
from komand_okta.util.helpers import clean


class ListGroups(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_groups",
            description=Component.DESCRIPTION,
            input=ListGroupsInput(),
            output=ListGroupsOutput(),
        )

    def run(self, params={}):
        response = self.connection.api_client.list_groups(clean({"q": params.get(Input.QUERY)}))
        if response:
            # Normalize data for easier UX
            for group in response:
                keys = group.pop("profile")
                group["name"] = keys.get("name", "Unknown")
                group["description"] = keys.get("description", "Unknown")
                group["links"] = group.pop("_links")

        return {Output.GROUPS: response, Output.SUCCESS: True if response else False}
