import insightconnect_plugin_runtime
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

from .schema import GetUserMembershipsInput, GetUserMembershipsOutput, Input, Output, Component

# Custom imports below
from ...util.api_utils import raise_for_status
from ...util.constants import Endpoint


class GetUserMemberships(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user_memberships",
            description=Component.DESCRIPTION,
            input=GetUserMembershipsInput(),
            output=GetUserMembershipsOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        user_id = params.get(Input.USER_ID)
        next_link = params.get(Input.NEXT_LINK, "")
        # END INPUT BINDING - DO NOT REMOVE

        headers = self.connection.get_headers(self.connection.get_auth_token())
        headers["ConsistencyLevel"] = "eventual"

        if next_link:
            self.logger.info(f"Using provided next_link for pagination: {next_link}")
            url = next_link
        else:
            url = Endpoint.USER_MEMBER_OF.format(self.connection.tenant, user_id=user_id)

        response = requests.request(
            method="GET",
            url=url,
            headers=headers,
        )
        raise_for_status(response)

        try:
            result = response.json()
        except ValueError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)

        total_count = result.get("@odata.count")
        if total_count:
            self.logger.info(f"Total memberships reported by API: {total_count}")

        memberships = result.get("value")
        member_count = len(memberships) if memberships else 0
        self.logger.info(f"Found {member_count} memberships for user {user_id} in this page.")

        if output_next_link := result.get("@odata.nextLink"):
            self.logger.info("Additional pages available via next_link.")

        return clean(
            {
                Output.MEMBERSHIPS: memberships,
                Output.COUNT: member_count,
                Output.NEXT_LINK: output_next_link,
            }
        )
