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

        filter_ = params.get(Input.NAME_FILTER, "")
        get_params = {}
        if filter_:
            get_params = {
                "filter": f"name=@{filter_}"
            }

        result = self.connection.session.get(endpoint, params=get_params, verify=self.connection.ssl_verify)

        try:
            result.raise_for_status()
        except Exception as e:
            raise PluginException(cause=f"Get policy failed for {endpoint}\n",
                                  assistance=result.text,
                                  data=e)

        policies = result.json().get("results")

        return {Output.POLICIES: komand.helper.clean(policies)}
