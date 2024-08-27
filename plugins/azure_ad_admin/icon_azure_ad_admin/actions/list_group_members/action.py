import insightconnect_plugin_runtime
from .schema import ListGroupMembersInput, ListGroupMembersOutput, Input, Output, Component

# Custom imports below
import requests
from insightconnect_plugin_runtime.exceptions import PluginException


class ListGroupMembers(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_group_members",
            description=Component.DESCRIPTION,
            input=ListGroupMembersInput(),
            output=ListGroupMembersOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        group_id = params.get(Input.GROUP_ID)
        # END INPUT BINDING - DO NOT REMOVE
        url = f"https://graph.microsoft.com/v1.0/groups/{group_id}/members?$count=true"

        # Add ConsistencyLevel header for counting
        headers = self.connection.get_headers(self.connection.get_auth_token())
        headers["ConsistencyLevel"] = "eventual"

        response = requests.request(
            method="GET",
            url=url,
            headers=headers,
        )

        if response.status_code == 404:
            raise PluginException(
                cause="Group not found.",
                assistance=f"Group ID {group_id} was not found.",
                data=response.text,
            )
        if not response.status_code == 200:
            raise PluginException(
                cause="Unexpected response from Azure AD.",
                assistance=f"Received an unexpected response with status code {response.status_code}.",
                data=response.text,
            )

        try:
            result = response.json()
            members = result.get("value", [])
            member_count = result.get(
                "@odata.count", len(members)
            )  # Fallback to len(members) if @odata.count is missing
        except ValueError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)

        return {Output.MEMBERS: members, Output.COUNT: member_count}
