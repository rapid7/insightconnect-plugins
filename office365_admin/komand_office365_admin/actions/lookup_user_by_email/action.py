import komand
from .schema import LookupUserByEmailInput, LookupUserByEmailOutput, Input, Output, Component
# Custom imports below
import requests


class LookupUserByEmail(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup_user_by_email',
                description=Component.DESCRIPTION,
                input=LookupUserByEmailInput(),
                output=LookupUserByEmailOutput())

    def run(self, params={}):
        #required param, so we can assume it exists
        email_address = params.get(Input.EMAIL_ADDRESS)
        token = self.connection.access_token

        headers = {"Authorization": "Bearer %s" % token, "Content-Type": "application/json"}
        base_url = f"https://graph.microsoft.com/v1.0/{self.connection.tenant_id}/users?$filter=userPrincipalName eq '{email_address}'"

        try:
            response = requests.get(base_url, headers=headers)
        except requests.HTTPError as e:
            raise PluginException("Error with the Lookup User by Email request.", data=str(e))

        try:
            #this will throw any 4xx error
            response.raise_for_status()
        except Exception as e:
            raise PluginException(f"The response from Office365 indicated something went wrong: {response.status_code}",
                                  data=response.text)
        return {Output.USER: response.json()}
