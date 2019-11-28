import komand
from .schema import AddUserInput, AddUserOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
import requests
import json


class AddUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="add_user",
                description=Component.DESCRIPTION,
                input=AddUserInput(),
                output=AddUserOutput())

    def run(self, params={}):
        account_enabled = params.get(Input.ACCOUNT_ENABLED)
        display_name = params.get(Input.DISPLAY_NAME)
        mail_nickname = params.get(Input.MAIL_NICKNAME)
        user_principal_name = params.get(Input.USER_PRINCIPAL_NAME)
        force_change_password = params.get(Input.FORCE_CHANGE_PASSWORD)
        location = params.get(Input.OFFICE_LOCATION, None)
        password = params.get(Input.PASSWORD)
        token = self.connection.access_token

        password_profile = {"forceChangePasswordNextSignIn": force_change_password, "password": password}

        base_url = "https://graph.microsoft.com/beta/users"
        headers = {"Authorization": "Bearer %s" % token, "Content-Type": "application/json"}
        body = {"accountEnabled": account_enabled, "displayName": display_name, "mailNickname": mail_nickname,
                "userPrincipalName": user_principal_name, "passwordProfile": password_profile, "officeLocation":location}

        body = json.dumps(body)

        try:
            response = requests.post(base_url, headers=headers, data=body)
        except requests.HTTPError:
            raise PluginException("There was an issue with the Add User request. Double-check the request body:", data=body)
            
        if response.status_code == 201:
            return {Output.USER: response.json()}
        else:
            raise PluginException(f"The response from Office365 indicated something went wrong: {response.status_code}",
                              data=response.text)
                              
