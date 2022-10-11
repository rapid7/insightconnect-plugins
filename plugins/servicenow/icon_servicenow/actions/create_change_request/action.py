import insightconnect_plugin_runtime
from .schema import CreateChangeRequestInput, CreateChangeRequestOutput, Input, Output, Component

# Custom imports below


class CreateChangeRequest(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_change_request",
            description=Component.DESCRIPTION,
            input=CreateChangeRequestInput(),
            output=CreateChangeRequestOutput(),
        )

    def run(self, params={}):
        additional_fields = params.get(Input.ADDITIONAL_FIELDS)
        self.connection.request.make_request(self.connection.change_request_url, "POST", payload=additional_fields)
        return {Output.SUCCESS: True}
