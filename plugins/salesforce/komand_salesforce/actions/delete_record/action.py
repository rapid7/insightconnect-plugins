import insightconnect_plugin_runtime
from .schema import DeleteRecordInput, DeleteRecordOutput, Input, Output


class DeleteRecord(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_record",
            description="Delete a record",
            input=DeleteRecordInput(),
            output=DeleteRecordOutput(),
        )

    def run(self, params={}):
        return {
            Output.SUCCESS: self.connection.api.delete_record(params.get(Input.RECORDID), params.get(Input.OBJECTNAME))
        }
