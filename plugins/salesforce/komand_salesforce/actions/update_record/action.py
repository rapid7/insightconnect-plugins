import insightconnect_plugin_runtime
from .schema import UpdateRecordInput, UpdateRecordOutput, Input, Output


class UpdateRecord(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_record",
            description="Update a record",
            input=UpdateRecordInput(),
            output=UpdateRecordOutput(),
        )

    def run(self, params={}):
        return {
            Output.SUCCESS: self.connection.api.update_record(
                params.get(Input.RECORDID), params.get(Input.OBJECTNAME), params.get(Input.OBJECTDATA)
            )
        }
