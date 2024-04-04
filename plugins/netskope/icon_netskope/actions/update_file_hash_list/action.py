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
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        name = params.get(Input.NAME, "")
        input_list = params.get(Input.LIST, [])
        # END INPUT BINDING - DO NOT REMOVE

        response = self.connection.client.update_file_hash_list(name, input_list)
        return {Output.STATUS: response.get("status"), Output.MESSAGE: response.get("msg")}
