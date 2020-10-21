import insightconnect_plugin_runtime
from .schema import GetUserByIdInput, GetUserByIdOutput, Input, Output, Component
# Custom imports below


class GetUserById(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_user_by_id',
                description=Component.DESCRIPTION,
                input=GetUserByIdInput(),
                output=GetUserByIdOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
