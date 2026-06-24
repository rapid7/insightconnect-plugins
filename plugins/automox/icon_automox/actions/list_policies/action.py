import insightconnect_plugin_runtime
from .schema import ListPoliciesInput, ListPoliciesOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

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
        # START INPUT BINDING - DO NOT REMOVE
        org_id = params.get(Input.ORG_ID, 0)
        # END INPUT BINDING - DO NOT REMOVE

        # Validation
        if org_id and org_id <= 0:
            raise PluginException(cause="Invalid input", assistance="Organization ID must be a positive integer")

        policies = self.connection.automox_api.get_policies(org_id)
        self.logger.info(f"Returned {len(policies)} policies")

        return {Output.POLICIES: policies}
