import insightconnect_plugin_runtime
from .schema import DeleteGroupInput, DeleteGroupOutput, Input, Output, Component

# Custom imports below


class DeleteGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_group", description=Component.DESCRIPTION, input=DeleteGroupInput(), output=DeleteGroupOutput()
        )

    def run(self, params={}):
        self.connection.automox_api.delete_group(params.get(Input.ORG_ID), params.get(Input.GROUP_ID))

        return {Output.SUCCESS: True}
