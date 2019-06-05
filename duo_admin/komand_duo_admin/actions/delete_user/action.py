import komand
from .schema import DeleteUserInput, DeleteUserOutput, Input, Output, Component
# Custom imports below


class DeleteUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='delete_user',
            description=Component.DESCRIPTION,
            input=DeleteUserInput(),
            output=DeleteUserOutput())

    def run(self, params={}):
        resp = self.connection.admin_api.delete_user(params.get(Input.USER_ID))
        return {Output.RESPONSE: resp}
