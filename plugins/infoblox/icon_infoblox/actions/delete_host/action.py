import insightconnect_plugin_runtime
from .schema import DeleteHostInput, DeleteHostOutput, Input, Output, Component

# Custom imports below


class DeleteHost(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_host",
            description=Component.DESCRIPTION,
            input=DeleteHostInput(),
            output=DeleteHostOutput(),
        )

    def run(self, params={}):
        ref = params.get(Input.REF)

        ref = self.connection.infoblox_connection.delete_host(ref)

        return {Output.REF: ref}
