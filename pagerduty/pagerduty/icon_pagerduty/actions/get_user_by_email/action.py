import insightconnect_plugin_runtime
from .schema import GetUserByEmailInput, GetUserByEmailOutput, Input, Output, Component
# Custom imports below


class GetUserByEmail(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_user_by_email',
                description=Component.DESCRIPTION,
                input=GetUserByEmailInput(),
                output=GetUserByEmailOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
