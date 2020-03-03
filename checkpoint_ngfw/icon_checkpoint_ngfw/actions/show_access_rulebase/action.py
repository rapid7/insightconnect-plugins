import komand
from .schema import ShowAccessRulebaseInput, ShowAccessRulebaseOutput, Input, Output, Component
# Custom imports below
import requests
from komand.exceptions import PluginException


class ShowAccessRulebase(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='show_access_rulebase',
                description=Component.DESCRIPTION,
                input=ShowAccessRulebaseInput(),
                output=ShowAccessRulebaseOutput())

    def run(self, params={}):
        url = f"https://{self.connection.server_ip}:{self.connection.server_port}/web_api/show-access-rulebase"
        headers = self.connection.get_headers()
        paylaod = {
            "offset": 0,
            "limit": params.get(Input.LIMIT, 1),
            "name": params.get(Input.LAYER_NAME),
            "details-level": "full",
            "use-object-dictionary": True
        }

        result = requests.post(url, headers=headers, json=paylaod, verify=self.connection.ssl_verify)

        try:
            result.raise_for_status()
        except Exception as e:
            raise PluginException(cause=f"Show Access Rules from {url} failed.\n",
                                  assistance=result.text + "\n",
                                  data=e)

        return {Output.ACCESS_RULES: komand.helper.clean(result.json())}
