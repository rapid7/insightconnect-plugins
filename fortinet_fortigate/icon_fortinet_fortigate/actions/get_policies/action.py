import komand
from .schema import GetPoliciesInput, GetPoliciesOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
from icon_fortinet_fortigate.util.util import Helpers


class GetPolicies(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_policies',
                description=Component.DESCRIPTION,
                input=GetPoliciesInput(),
                output=GetPoliciesOutput())

    def run(self, params={}):
        endpoint = f"https://{self.connection.host}/api/v2/cmdb/firewall/policy"
        helper = Helpers(self.logger)

        filter_ = params.get(Input.NAME_FILTER, "")
        get_params = {}
        if filter_:
            get_params = {
                "filter": f"name=@{filter_}"
            }

        response = self.connection.session.get(endpoint, params=get_params, verify=self.connection.ssl_verify)

        try:
            json_response = response.json()
        except ValueError:
            raise PluginException(cause="Data sent by FortiGate was not in JSON format.\n",
                                  assistance="Contact support for help.",
                                  data=response.text)
        helper.http_errors(json_response, response.status_code)

        policies = response.json().get("results")

        return {Output.POLICIES: komand.helper.clean(policies)}
