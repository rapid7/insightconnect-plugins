import insightconnect_plugin_runtime
from .schema import CreateRecordInput, CreateRecordOutput, Input, Output

# Custom imports below


class CreateRecord(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_record",
            description="Create a new SObject record",
            input=CreateRecordInput(),
            output=CreateRecordOutput(),
        )

    def run(self, params={}):
        return {
            Output.ID: self.connection.api.create_record(
                params.get(Input.OBJECTNAME), params.get(Input.OBJECTDATA)
            ).get("id", "")
        }
