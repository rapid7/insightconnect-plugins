import insightconnect_plugin_runtime
from .schema import ListUsersInput, ListUsersOutput

# Custom imports below


class ListUsers(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_users",
            description="List all users",
            input=ListUsersInput(),
            output=ListUsersOutput(),
        )

    def run(self, params={}):
        return {"users": self.connection.api.list_users()}
