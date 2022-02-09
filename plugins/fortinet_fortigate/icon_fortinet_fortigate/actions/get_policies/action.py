import insightconnect_plugin_runtime
from .schema import GetPoliciesInput, GetPoliciesOutput, Input, Output, Component

# Custom imports below


class GetPolicies(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_policies",
            description=Component.DESCRIPTION,
            input=GetPoliciesInput(),
            output=GetPoliciesOutput(),
        )

    def run(self, params={}):
        name_filter = params.get(Input.NAME_FILTER)
        get_params = {}
        if name_filter:
            get_params = {"filter": f"name=@{name_filter}"}

        return {
            Output.POLICIES: insightconnect_plugin_runtime.helper.clean(
                self.connection.api.get_policies(get_params).get("results")
            )
        }
