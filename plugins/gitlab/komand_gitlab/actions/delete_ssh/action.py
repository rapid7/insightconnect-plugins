import insightconnect_plugin_runtime
from .schema import DeleteSshInput, DeleteSshOutput, Input, Output, Component

# Custom imports below
import requests


class DeleteSsh(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_ssh",
            description=Component.DESCRIPTION,
            input=DeleteSshInput(),
            output=DeleteSshOutput(),
        )

    def run(self, params={}):
        request_url = "%s/users/%s/keys/%s" % (
            self.connection.url,
            params.get(Input.ID),
            params.get(Input.KEY_ID),
        )
        try:
            response= requests.delete(request_url, headers={"PRIVATE-TOKEN": self.connection.token}, verify=False)  # noqa: B501
        except requests.exceptions.RequestException as error:  # This is the correct syntax
            self.logger.error(error)
            raise Exception(error)
        return {Output.STATUS: response.ok}
