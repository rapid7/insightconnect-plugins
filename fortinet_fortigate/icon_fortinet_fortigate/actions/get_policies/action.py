import komand
from .schema import GetPoliciesInput, GetPoliciesOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class GetPolicies(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_policies',
                description=Component.DESCRIPTION,
                input=GetPoliciesInput(),
                output=GetPoliciesOutput())

    def run(self, params={}):
        endpoint = f"https://{self.connection.host}/api/v2/cmdb/firewall/policy"
        result = self.connection.session.get(endpoint, verify=self.connection.ssl_verify)

        try:
            result.raise_for_status()
        except Exception as e:
            raise PluginException(cause=f"Get policy failed for {endpoint}",
                                  assistance=result.text,
                                  data=e)

        return {Output.POLICIES: komand.helper.clean(result.json())}
