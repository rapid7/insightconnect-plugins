import insightconnect_plugin_runtime
from .schema import DeleteUserByIdInput, DeleteUserByIdOutput, Input, Output, Component
# Custom imports below


class DeleteUserById(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_user_by_id',
                description=Component.DESCRIPTION,
                input=DeleteUserByIdInput(),
                output=DeleteUserByIdOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
