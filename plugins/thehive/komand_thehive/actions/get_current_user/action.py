import insightconnect_plugin_runtime
from .schema import GetCurrentUserInput, GetCurrentUserOutput, Output, Component

# Custom imports below


class GetCurrentUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_current_user",
            description=Component.DESCRIPTION,
            input=GetCurrentUserInput(),
            output=GetCurrentUserOutput(),
        )

    def run(self, params={}):  # pylint: disable=unused-argument

        response = self.connection.client.get_current_user()

        return {Output.SUCCESS: response}
