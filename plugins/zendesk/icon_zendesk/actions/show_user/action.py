import insightconnect_plugin_runtime
from .schema import ShowUserInput, ShowUserOutput, Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
from zenpy.lib.exception import APIException
from icon_zendesk.util.objects import Objects


class ShowUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="show_user",
            description="Retrieve user information",
            input=ShowUserInput(),
            output=ShowUserOutput(),
        )

    def run(self, params={}):
        identifier = params.get(Input.USER_ID)

        try:
            user = self.connection.client.users(id=identifier)
        except APIException as error:
            self.logger.debug(error)
            raise PluginException(
                cause=f"User ID {params.get(Input.USER_ID)} not found in Zendesk.",
                assistance="Make sure the input user ID is correct.",
            )

        user_object = Objects.create_user_object(user)
        return {Output.USER: user_object}
