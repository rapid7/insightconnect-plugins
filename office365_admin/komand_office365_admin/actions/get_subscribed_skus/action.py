import komand
from .schema import GetSubscribedSkusInput, GetSubscribedSkusOutput, Input, Output, Component
# Custom imports below
import requests
from komand.exceptions import PluginException


class GetSubscribedSkus(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="get_subscribed_skus",
                description=Component.DESCRIPTION,
                input=GetSubscribedSkusInput(),
                output=GetSubscribedSkusOutput())

    def run(self, params={}):
        token = self.connection.access_token

        base_url = "https://graph.microsoft.com/v1.0/subscribedSkus/"
        headers = {"Authorization": "Bearer %s" % token}

        try:
            response = requests.get(base_url, headers=headers)
        except requests.HTTPError:
            raise PluginException(cause=f"There was an issue with the Get Subscribed SKUs user request. Double-check the username: {user_principal_name}",
                        data=response.text)
        if response.status_code == 200:
            return {Output.SKU_ITEM: response.json()["value"]}
        else:
             PluginException(cause=f"The response from Office365 indicated something went wrong: {response.status_code}",
                              data=response.text)

