import komand
from komand.exceptions import PluginException

from .schema import GetUserGroupsInput, GetUserGroupsOutput, Input, Output, Component
# Custom imports below
import json


class GetUserGroups(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_user_groups',
                description=Component.DESCRIPTION,
                input=GetUserGroupsInput(),
                output=GetUserGroupsOutput())

    def run(self, params={}):
        client = self.connection.box_connection
        user_id = params.get(Input.USER_ID)

        self.logger.info(f"Looking for user groups with user ID: {user_id}")
        # The API method for memberships didn't work, thus doing it manually
        box_response = client.make_request("get", f"https://api.box.com/2.0/users/{user_id}/memberships")

        if not box_response or not box_response.ok:
            raise PluginException(cause="User ID was not found.",
                                  assistance=f"The user with ID {user_id} can not be found.")

        try:
            response_json = json.loads(box_response.content.decode())
            group_entries = response_json.get('entries')
        except Exception as e:
            raise PluginException(PluginException.Preset.INVALID_JSON) from e

        groups = []
        for entry in group_entries:
            group = {
                "user_id": entry.get("user", {}).get("id"),
                "group_id": entry.get("group", {}).get("id"),
                "role": entry.get("role"),
                "type": entry.get("type"),
                "name": entry.get("group", {}).get("name")
            }
            groups.append(group)

        return {Output.GROUPS: groups}
