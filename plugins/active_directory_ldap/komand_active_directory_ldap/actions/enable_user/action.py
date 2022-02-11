import insightconnect_plugin_runtime

# Custom imports below
from .schema import EnableUserInput, EnableUserOutput, Input, Output


class EnableUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="enable_user",
            description="Enable a account",
            input=EnableUserInput(),
            output=EnableUserOutput(),
        )

    def run(self, params={}):
        return {Output.SUCCESS: self.connection.client.manage_user(params.get(Input.DISTINGUISHED_NAME), True)}
