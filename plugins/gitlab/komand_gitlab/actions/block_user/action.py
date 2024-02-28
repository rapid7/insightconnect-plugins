import insightconnect_plugin_runtime
from .schema import BlockUserInput, BlockUserOutput, Input, Output, Component

# Custom imports below
import requests


class BlockUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="block_user",
            description=Component.DESCRIPTION,
            input=BlockUserInput(),
            output=BlockUserOutput(),
        )

    def run(self, params={}):
        request_url = f"{self.connection.url}/users/{params.get(Input.ID)}/block"

        try:
            response = requests.post(request_url, headers={"PRIVATE-TOKEN": self.connection.token}, verify=False)  # noqa: B501
        except requests.exceptions.RequestException as error:  # This is the correct syntax
            self.logger.error(error)
            raise Exception(error)

        return {Output.STATUS: response.ok}

