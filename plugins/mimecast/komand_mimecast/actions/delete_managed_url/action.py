import insightconnect_plugin_runtime
from .schema import DeleteManagedUrlInput, DeleteManagedUrlOutput, Input, Output, Component
from komand_mimecast.util.constants import ID_FIELD

class DeleteManagedUrl(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_managed_url",
            description=Component.DESCRIPTION,
            input=DeleteManagedUrlInput(),
            output=DeleteManagedUrlOutput(),
        )

    def run(self, params={}):
        self.connection.client.delete_managed_url(data={ID_FIELD: params.get(Input.ID)})
        return {Output.SUCCESS: True}
