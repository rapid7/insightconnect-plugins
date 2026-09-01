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

        # Add ConsistencyLevel header (required for $count, re-sent on each paged request)
        headers = self.connection.get_headers(self.connection.get_auth_token())
        headers["ConsistencyLevel"] = "eventual"

        url = Endpoint.MEMBERS.format(self.connection.tenant, group_id=group_id)

        # The API returns a maximum of 100 members per page. Follow @odata.nextLink to
        # collect every page. Bounded loop mirrors the search_device action to avoid
        # infinite loops (max 1,000 pages).
        members, member_count = [], None
        for _ in range(1_000):
            response = requests.request(method="GET", url=url, headers=headers)
            raise_for_status(response)

            try:
                result = response.json()
            except ValueError:
                raise PluginException(preset=PluginException.Preset.INVALID_JSON)

            members.extend(result.get("value", []))

            # @odata.count is only returned on the first page for directory resources
            if member_count is None:
                member_count = result.get("@odata.count")

            # nextLink already encodes every query param; switch to it and keep paging
            if not (url := result.get("@odata.nextLink")):
                break

        if member_count is None:  # Fallback to page count if @odata.count was missing
            member_count = len(members)

        return {Output.MEMBERS: clean(members), Output.COUNT: member_count}
