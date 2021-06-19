import insightconnect_plugin_runtime
from .schema import AddAppToPolicyInput, AddAppToPolicyOutput, Input, Output, Component
# Custom imports below


class AddAppToPolicy(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_app_to_policy',
                description=Component.DESCRIPTION,
                input=AddAppToPolicyInput(),
                output=AddAppToPolicyOutput())

    def run(self, params={}):
        response = self.connection.api.delete_app_from_policy(
            params.get(Input.APPLICATION_NAME),
            params.get(Input.POLICY_NAME),
            params.get(Input.DEVICE_TYPE)
        )

        return {Output.SUCCESS: response}
