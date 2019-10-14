import komand
from .schema import RemoveUserFromGroupInput, RemoveUserFromGroupOutput, Input, Output, Component
# Custom imports below
from icon_azure_ad_admin.util.get_group import get_group
from icon_azure_ad_admin.util.get_user_info import get_user_info
from komand.exceptions import PluginException
import requests


class RemoveUserFromGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_user_from_group',
                description=Component.DESCRIPTION,
                input=RemoveUserFromGroupInput(),
                output=RemoveUserFromGroupOutput())

    def run(self, params={}):
        group_name = params.get(Input.GROUP_NAME)
        user_id = params.get(Input.USER_ID)

        self.logger.info(f"Getting group info: {group_name}")
        group = get_group(self.connection, group_name)
        group_id = group.get("id")

        self.logger.info(f"Getting user info: {user_id}")
        user_response = get_user_info(self.connection, user_id)
        user_object = user_response.json()
        user_id = user_object.get("id")

        headers = self.connection.get_headers(self.connection.get_auth_token())
        remove_from_group_endpoint = f"https://graph.microsoft.com/v1.0/{self.connection.tenant}/groups/{group_id}/members/{user_id}/$ref"
        result = requests.delete(remove_from_group_endpoint, headers=headers)

        if not result.status_code == 204:
            raise PluginException(cause=f"Delete User from Group call returned an unexpected response: {result.status_code}",
                                  assistance=f"Check that the group name {group_name} and user id {user_id} are correct.",
                                  data=result.text)

        return {Output.SUCCESS: True}
