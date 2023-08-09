import insightconnect_plugin_runtime
from .schema import GetUserGroupsInput, GetUserGroupsOutput, Input, Output, Component

# Custom imports below


class GetUserGroups(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user_groups",
            description=Component.DESCRIPTION,
            input=GetUserGroupsInput(),
            output=GetUserGroupsOutput(),
        )

    def run(self, params={}):
        response = self.connection.api_client.get_user_groups(params.get(Input.ID))
        if response:
            # Normalize data for easier UX
            for group in response:
                keys = group.pop("profile")
                group["name"] = keys.get("name", "Unknown")
                group["description"] = keys.get("description", "Unknown")
                group["links"] = group.pop("_links")
        return {
            Output.USERGROUPS: response,
        }
