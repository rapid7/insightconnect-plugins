import insightconnect_plugin_runtime
from .schema import ListGroupMembersInput, ListGroupMembersOutput, Input, Output, Component

# Custom imports below
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from icon_azure_ad_admin.util.api_utils import raise_for_status
from icon_azure_ad_admin.util.constants import Endpoint


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

        # Add ConsistencyLevel header for counting
        headers = self.connection.get_headers(self.connection.get_auth_token())
        headers["ConsistencyLevel"] = "eventual"

        response = requests.request(
            method="GET",
            url=Endpoint.MEMBERS.format(self.connection.tenant, group_id=group_id),
            headers=headers,
        )

        raise_for_status(response)

        try:
            result = response.json()
            members = result.get("value", [])
            member_count = result.get(
                "@odata.count", len(members)
            )  # Fallback to len(members) if @odata.count is missing

        except ValueError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)

        return {Output.MEMBERS: clean(members), Output.COUNT: member_count}
