import komand
from .schema import DeleteUserInput, DeleteUserOutput, Input, Output, Component
# Custom imports below
import requests
from komand.exceptions import PluginException


class DeleteUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_user',
                description=Component.DESCRIPTION,
                input=DeleteUserInput(),
                output=DeleteUserOutput())

    def run(self, params={}):
        user_principal_name = params.get(Input.USER_PRINCIPAL_NAME)
        token = self.connection.access_token

        base_url = 'https://graph.microsoft.com/beta/users/%s' % user_principal_name
        headers = {'Authorization': 'Bearer %s' % token}

        try:
            response = requests.delete(base_url, headers=headers)
        except requests.HTTPError:
            raise PluginException(cause=f"There was an issue with the Delete User request. Double-check the username: {user_principal_name}",
                                  data=response.text)
        if response.status_code == 204:
            success = True
            return {Output.SUCCESS: success}
        else:
            raise PluginException(cause="The response from Office365 indicated something went wrong: {response.status_code}",
                                  data=response.text)
