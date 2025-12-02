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
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        email = params.get(Input.EMAIL, "")
        username = params.get(Input.USERNAME, "")
        password = params.get(Input.PASSWORD, "")
        notify = params.get(Input.NOTIFY, False)
        products = params.get(Input.PRODUCTS, [])
        # END INPUT BINDING - DO NOT REMOVE

        if not self.connection.is_cloud:
            success = self.connection.client.add_user(
                fullname=username,
                email=email,
                password=password,
                notify=notify,
                username=username,
            )
        else:
            success = self.connection.rest_client.add_user(username, email, password, products, notify)
        return {Output.SUCCESS: success}
