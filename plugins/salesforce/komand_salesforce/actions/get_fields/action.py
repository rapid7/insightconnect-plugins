import insightconnect_plugin_runtime
from .schema import GetFieldsInput, GetFieldsOutput, Input, Output, Component

# Custom imports below
from komand_salesforce.util.helpers import clean, convert_to_camel_case


class GetFields(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_fields",
            description=Component.DESCRIPTION,
            input=GetFieldsInput(),
            output=GetFieldsOutput(),
        )

    def run(self, params={}):
        fields = params.get(Input.FIELDS)
        response = self.connection.api.get_fields(
            params.get(Input.RECORDID), params.get(Input.OBJECTNAME), {"fields": ",".join(fields)} if fields else {}
        )
        response.pop("attributes", None)
        return {Output.FIELDS: convert_to_camel_case(clean(response))}
