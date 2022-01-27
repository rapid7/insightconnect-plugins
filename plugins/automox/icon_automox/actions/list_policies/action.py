import insightconnect_plugin_runtime
from .schema import ListPoliciesInput, ListPoliciesOutput, Input, Output, Component

# Custom imports below


class ListPolicies(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_policies",
            description=Component.DESCRIPTION,
            input=ListPoliciesInput(),
            output=ListPoliciesOutput(),
        )

    def run(self, params={}):
        policies = self.connection.automox_api.get_policies(params.get(Input.ORG_ID))
        self.logger.info(f"Returned {len(policies)} policies")

        return {Output.POLICIES: policies}
