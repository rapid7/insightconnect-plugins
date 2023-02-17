import insightconnect_plugin_runtime
from .schema import CreateUserInput, CreateUserOutput

# Custom imports below


class CreateUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_user",
            description="Create a new user",
            input=CreateUserInput(),
            output=CreateUserOutput(),
        )

    def run(self, params={}):
        email = params.get("email")
        name = params.get("name")
        phone = params.get("phone")
        mobile_phone = params.get("mobile_phone")
        role = params.get("role")
        department = params.get("department")

        user = self.connection.api.create_user(email, name, phone, mobile_phone, role, department)

        return {"user": user}
