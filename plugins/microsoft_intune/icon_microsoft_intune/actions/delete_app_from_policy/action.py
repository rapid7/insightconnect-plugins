import insightconnect_plugin_runtime
from .schema import DeleteAppFromPolicyInput, DeleteAppFromPolicyOutput, Input, Output, Component
# Custom imports below


class DeleteAppFromPolicy(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_app_from_policy',
                description=Component.DESCRIPTION,
                input=DeleteAppFromPolicyInput(),
                output=DeleteAppFromPolicyOutput())

    def run(self, params={}):
        response = self.connection.api.delete_app_from_policy(
            params.get(Input.APPLICATION_NAME),
            params.get(Input.POLICY_NAME),
            params.get(Input.DEVICE_TYPE)
        )

        return {Output.SUCCESS: response}
