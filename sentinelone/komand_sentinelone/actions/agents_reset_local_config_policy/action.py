import komand
from .schema import AgentsResetLocalConfigPolicyInput, AgentsResetLocalConfigPolicyOutput, Input, Output, Component
# Custom imports below


class AgentsResetLocalConfigPolicy(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_reset_local_config_policy',
                description=Component.DESCRIPTION,
                input=AgentsResetLocalConfigPolicyInput(),
                output=AgentsResetLocalConfigPolicyOutput())

    def run(self, params={}):
        return {
            Output.AFFECTED: self.connection.agents_action("reset-local-config", params.get(Input.FILTER, None)).get("affected", 0)
        }
