import insightconnect_plugin_runtime
from .schema import GetUserInput, GetUserOutput, Input, Output, Component

# Custom imports below


class GetUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user",
            description=Component.DESCRIPTION,
            input=GetUserInput(),
            output=GetUserOutput(),
        )

    def run(self, params={}):
        user_id = params.get(Input.ID)
        response = self.connection.client.get_user(user_id=user_id)

        return {Output.USER: response}
