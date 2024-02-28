import insightconnect_plugin_runtime
from .schema import DeleteUserInput, DeleteUserOutput, Input, Output, Component

# Custom imports below
import requests


class DeleteUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_user",
            description=Component.DESCRIPTION,
            input=DeleteUserInput(),
            output=DeleteUserOutput(),
        )

    def run(self, params={}):
        r_url = "%s/users/%s" % (self.connection.url, params.get("id"))

        try:
            r = requests.delete(r_url, headers={"PRIVATE-TOKEN": self.connection.token}, verify=False)  # noqa: B501
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            self.logger.error(e)
            raise Exception(e)
        return {"status": False if r.ok else True}

