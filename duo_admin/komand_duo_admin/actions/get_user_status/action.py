import komand
from .schema import GetUserStatusInput, GetUserStatusOutput, Input, Output, Component
# Custom imports below


class GetUserStatus(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_user_status',
            description=Component.DESCRIPTION,
            input=GetUserStatusInput(),
            output=GetUserStatusOutput())

    def run(self, params={}):
        username = params.get(Input.USER)
        users = (self.connection.admin_api.get_users())

        if not users:
            raise Exception("Error: No users exist!")

        for user in users:
            if user["username"] != username:
                continue

            return {Output.STATUS: user["status"], Output.USER_ID: user["user_id"]}
        else:
            raise Exception("Error: User not found!")  # For loop finished without early return, user not found
