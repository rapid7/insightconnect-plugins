import insightconnect_plugin_runtime

# Custom imports below
from .schema import DisableUserInput, DisableUserOutput, Input, Output


class DisableUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="disable_user",
            description="Disable a account",
            input=DisableUserInput(),
            output=DisableUserOutput(),
        )

    def run(self, params={}):
        return {Output.SUCCESS: self.connection.client.manage_user(params.get(Input.DISTINGUISHED_NAME), False)}
