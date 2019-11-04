import komand
from .schema import UpdateUsageLocationInput, UpdateUsageLocationOutput, Input, Output, Component
# Custom imports below
import requests
from komand.exceptions import PluginException


class UpdateUsageLocation(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_usage_location',
                description=Component.DESCRIPTION,
                input=UpdateUsageLocationInput(),
                output=UpdateUsageLocationOutput())

    def run(self, params={}):
        user_principal_name = params.get(Input.USER_PRINCIPAL_NAME)
        location = params.get(Input.LOCATION)
        token = self.connection.access_token

        base_url = "https://graph.microsoft.com/v1.0/users/%s" % user_principal_name
        headers = {"Authorization": "Bearer %s" % token, "Content-Type": "application/json",}
        
        body = {
            "usageLocation": location
        }
        
        try:
            response = requests.patch(base_url, json=body, headers=headers)
        except requests.HTTPError:
            raise PluginException(cause=f"There was an issue updating the user's location. Double-check the user name: {user_principal_name}",
                        data=response.text)
        if response.status_code == 204:
            return {Output.SUCCESS: True}
        else:
            raise PluginException(f"The response from Office365 indicated something went wrong: {response.status_code}",
                              data=response.text)

