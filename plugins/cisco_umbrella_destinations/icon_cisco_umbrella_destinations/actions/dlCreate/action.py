import insightconnect_plugin_runtime
from .schema import DlCreateInput, DlCreateOutput, Input, Output, Component

# Custom imports below


class DlCreate(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="dlCreate",
            description=Component.DESCRIPTION,
            input=DlCreateInput(),
            output=DlCreateOutput(),
        )

    def run(self, params={}):
        data = {
            "access": params.get(Input.ACCESS),
            "isGlobal": params.get(Input.ISGLOBAL),
            "name": params.get(Input.LABEL),
            "destinations": [
                {
                    "destination": params.get(Input.DESTINATION),
                    "type": params.get(Input.TYPE),
                    "comment": params.get(Input.COMMENT),
                }
            ],
        }
        result = self.connection.client.create_destination_list(data=data)
        newResult = {k: v for k, v in result.items() if v is not None}

        return {Output.SUCCESS: newResult}
