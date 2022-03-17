import insightconnect_plugin_runtime

from .schema import Component, Input, Output, UpdateFileHashListInput, UpdateFileHashListOutput

# Custom imports below


class UpdateFileHashList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_file_hash_list",
            description=Component.DESCRIPTION,
            input=UpdateFileHashListInput(),
            output=UpdateFileHashListOutput(),
        )

    def run(self, params={}):
        response = self.connection.client.update_file_hash_list(params.get(Input.NAME), params.get(Input.LIST))
        return {Output.STATUS: response.get(Output.STATUS), Output.MESSAGE: response.get("msg")}
