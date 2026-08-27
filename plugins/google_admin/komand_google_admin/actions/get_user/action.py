import insightconnect_plugin_runtime
from .schema import GetUserInput, GetUserOutput

# Custom imports below


class GetUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user", description="Get a User", input=GetUserInput(), output=GetUserOutput()
        )

    def run(self, params={}):
        user = self.connection.service.users().get(userKey=params["user"]).execute()
        return {"user": user, "found": bool(user)}
