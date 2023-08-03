import komand
from .schema import SuspendUserInput, SuspendUserOutput, Input, Output, Component


# Custom imports below


class SuspendUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="suspend_user",
            description=Component.DESCRIPTION,
            input=SuspendUserInput(),
            output=SuspendUserOutput(),
        )

    def run(self, params={}):
        body = {"suspended": True}
        user = self.connection.service.users().update(userKey=params.get(Input.USER), body=body).execute()
        return {Output.USER: user}
