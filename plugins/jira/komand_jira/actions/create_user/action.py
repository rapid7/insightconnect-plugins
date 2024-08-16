import insightconnect_plugin_runtime
from .schema import CreateUserInput, CreateUserOutput, Input, Output, Component

# Custom imports below


class CreateUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_user",
            description=Component.DESCRIPTION,
            input=CreateUserInput(),
            output=CreateUserOutput(),
        )

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
                username=username,
            )

        else:
            params = {
                "displayName": params[Input.USERNAME],
                "emailAddress": params[Input.EMAIL],
                "password": params.get(Input.PASSWORD, None),
                "notification": params.get(Input.NOTIFY, False),
                "name": username,
                "products": params.get(Input.PRODUCTS, []),
            }
            success = self.connection.rest_client.add_user(params)

        return {Output.SUCCESS: success}
