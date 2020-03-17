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

        filter = params.get(Input.NAME_FILTER, "")
        if filter:
            get_params = {
                "filter": f"name=@{filter}"
            }

        result = self.connection.session.get(endpoint, params=params, verify=self.connection.ssl_verify)

        try:
            result.raise_for_status()
        except Exception as e:
            raise PluginException(cause=f"Get policy failed for {endpoint}",
                                  assistance=result.text,
                                  data=e)

        policies = result.json().get("results")

        return {Output.POLICIES: komand.helper.clean(policies)}
