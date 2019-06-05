import komand
from .schema import GetUsersInput, GetUsersOutput, Output, Component
# Custom imports below


class GetUsers(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_users',
            description=Component.DESCRIPTION,
            input=GetUsersInput(),
            output=GetUsersOutput())

    def run(self, params={}):
        result = self.connection.admin_api.get_users()
        users = komand.helper.clean(result)

        return {Output.USERS: users}
