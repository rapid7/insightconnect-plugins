import insightconnect_plugin_runtime
from .schema import DetachPolicyInput, DetachPolicyOutput, Input, Output, Component

# Custom imports below


class DetachPolicy(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="detach_policy",
            description=Component.DESCRIPTION,
            input=DetachPolicyInput(),
            output=DetachPolicyOutput(),
        )

    def run(self, params={}):
        return {
            Output.SUCCESS: self.connection.api.detach_policy(
                params.get(Input.RESOURCEID), params.get(Input.POLICYRESOURCEID)
            )
        }
