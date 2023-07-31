import insightconnect_plugin_runtime
from .schema import GetRecordInput, GetRecordOutput, Input, Output, Component

# Custom imports below
from komand_salesforce.util.helpers import clean, convert_to_camel_case


class GetRecord(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_record",
            description=Component.DESCRIPTION,
            input=GetRecordInput(),
            output=GetRecordOutput(),
        )

    def run(self, params={}):
        return {
            Output.RECORD: convert_to_camel_case(
                clean(
                    self.connection.api.get_record(
                        params.get(Input.RECORDID), params.get(Input.EXTERNALIDFIELDNAME), params.get(Input.OBJECTNAME)
                    )
                )
            )
        }
