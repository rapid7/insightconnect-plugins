import komand
from .schema import CreateUserInput, CreateUserOutput, Input, Output, Component
# Custom imports below


class CreateUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='create_user',
            description=Component.DESCRIPTION,
            input=CreateUserInput(),
            output=CreateUserOutput())

    def run(self, params={}):
        """Run action"""

        username = ""
        if not self.connection.is_cloud:
            username = params[Input.USERNAME]

        success = self.connection.client.add_user(
            fullname=params[Input.USERNAME],
            email=params[Input.EMAIL],
            password=params.get(Input.PASSWORD, None),
            notify=params.get(Input.NOTIFY, False),
            username=username
        )
        return {Output.SUCCESS: success}
