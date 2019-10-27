import komand
from .schema import AddUserToGroupInput, AddUserToGroupOutput, Input, Output, Component
# Custom imports below
from icon_azure_ad_admin.util.get_group import get_group
from icon_azure_ad_admin.util.get_user_info import get_user_info
from komand.exceptions import PluginException
import requests


class AddUserToGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_user_to_group',
                description=Component.DESCRIPTION,
                input=AddUserToGroupInput(),
                output=AddUserToGroupOutput())

    def run(self, params={}):
        group_name = params.get(Input.GROUP_NAME)
        user_id = params.get(Input.USER_ID)

        self.logger.info(f"Getting group info: {group_name}")
        group = get_group(self.connection, group_name)
        group_id = group.get("id")

        self.logger.info(f"Getting user info: {user_id}")
        user_response = get_user_info(self.connection, user_id)
        user_object = user_response.json()
        user = {
            "@odata.id": f"https://graph.microsoft.com/v1.0/{self.connection.tenant}/users/{user_object.get('id')}"
        }

        headers = self.connection.get_headers(self.connection.get_auth_token())
        add_to_group_endpoint = f"https://graph.microsoft.com/v1.0/{self.connection.tenant}/groups/{group_id}/members/$ref"
        result = requests.post(add_to_group_endpoint, json=user, headers=headers)

        if not result.status_code == 204:
            raise PluginException(cause=f"Add User to Group call returned an unexpected response: {result.status_code}",
                                  assistance=f"Check that the group name {group_name} and user id {user_id} are correct.",
                                  data=result.text)

        return {Output.SUCCESS: True}
