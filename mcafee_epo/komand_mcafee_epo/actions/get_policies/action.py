import insightconnect_plugin_runtime
from .schema import GetPoliciesInput, GetPoliciesOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class GetPolicies(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_policies',
                description=Component.DESCRIPTION,
                input=GetPoliciesInput(),
                output=GetPoliciesOutput())

    def run(self, params={}):
        try:
            return {
                Output.POLICIES_RETURNED: self.connection.client(
                    'policy.find',
                    params.get(Input.SEARCH_TEXT)
                )
            }
        except Exception as e:
            raise PluginException(
                cause="Error",
                assistance=f"Policies that match to the given search text and user are not found. Error: {e}"
            )

