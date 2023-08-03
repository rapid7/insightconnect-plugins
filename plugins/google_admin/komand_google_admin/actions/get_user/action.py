import komand
from .schema import GetUserInput, GetUserOutput, Input, Output, Component


# Custom imports below


class GetUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user",
            description=Component.DESCRIPTION,
            input=GetUserInput(),
            output=GetUserOutput()
        )

    def run(self, params={}):
        user = self.connection.service.users().get(userKey=params.get(Input.USER)).execute()
        return {Output.USER: user, Output.FOUND: (not not user)}
