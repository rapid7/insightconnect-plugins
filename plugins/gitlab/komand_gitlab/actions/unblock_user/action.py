import insightconnect_plugin_runtime
from .schema import UnblockUserInput, UnblockUserOutput, Input, Output, Component

# Custom imports below
import requests


class UnblockUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="unblock_user",
            description=Component.DESCRIPTION,
            input=UnblockUserInput(),
            output=UnblockUserOutput(),
        )

    def run(self, params={}):
        request_url = "%s/users/%s/unblock" % (self.connection.url, params.get("id"))

        try:
            r = requests.post(request_url, headers={"PRIVATE-TOKEN": self.connection.token}, verify=False)  # noqa: B501
        except requests.exceptions.RequestException as error:  # This is the correct syntax
            self.logger.error(error)
            raise Exception(error)

        return {Output.STATUS: r.ok}
