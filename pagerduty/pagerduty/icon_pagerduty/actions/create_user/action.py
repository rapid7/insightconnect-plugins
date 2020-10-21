import insightconnect_plugin_runtime
from .schema import CreateUserInput, CreateUserOutput, Input, Output, Component
# Custom imports below


class CreateUser(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_user',
                description=Component.DESCRIPTION,
                input=CreateUserInput(),
                output=CreateUserOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
