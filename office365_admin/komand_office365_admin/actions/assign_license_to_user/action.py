import komand
from .schema import AssignLicenseToUserInput, AssignLicenseToUserOutput, Input, Output, Component
# Custom imports below
import requests
from komand.exceptions import PluginException


class AssignLicenseToUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="assign_license_to_user",
                description=Component.DESCRIPTION,
                input=AssignLicenseToUserInput(),
                output=AssignLicenseToUserOutput())

    def run(self, params={}):
        user_principal_name = params.get(Input.USER_PRINCIPAL_NAME)
        sku_id = params.get(Input.SKU_ID)
        token = self.connection.access_token

        base_url = "https://graph.microsoft.com/v1.0/users/%s/assignLicense" % user_principal_name
        headers = {"Authorization": "Bearer %s" % token, "Content-Type": "application/json",}
        
        body = {
            "addLicenses": [{
                "disabledPlans": [],
                "skuId": sku_id
            }],
            "removeLicenses": []
        }
        
        try:
            response = requests.post(base_url, json=body, headers=headers)
        except requests.HTTPError:
            raise PluginException(cause=f"There was an issue with the Assign License request. Double-check the user name: {user_principal_name}",
                        data=response.text)
        if response.status_code == 200:
            return {Output.SUCCESS: True}
        else:
            raise PluginException(f"The response from Office365 indicated something went wrong: {response.status_code}",
                              data=response.text)
