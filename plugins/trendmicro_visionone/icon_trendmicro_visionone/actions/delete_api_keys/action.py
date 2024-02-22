import insightconnect_plugin_runtime
from .schema import DeleteApiKeysInput, DeleteApiKeysOutput, Input, Output, Component
# Custom imports below


class DeleteApiKeys(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="delete_api_keys",
                description=Component.DESCRIPTION,
                input=DeleteApiKeysInput(),
                output=DeleteApiKeysOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE
        # TODO - If input bindings for connection can be done check to same if it you can do the same here
        return {}
