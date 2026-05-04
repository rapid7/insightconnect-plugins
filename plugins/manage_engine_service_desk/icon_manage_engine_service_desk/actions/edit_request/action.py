import insightconnect_plugin_runtime

from icon_manage_engine_service_desk.util.constants import Response, ResponseStatus, Request
from .schema import EditRequestInput, EditRequestOutput, Input, Output, Component

# Custom imports below


class EditRequest(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="edit_request", description=Component.DESCRIPTION, input=EditRequestInput(), output=EditRequestOutput()
        )

    def run(self, params: dict = None) -> dict:
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        request_id = params.get(Input.REQUEST_ID, "")
        # END INPUT BINDING - DO NOT REMOVE
        request_parameters = {key: value for key, value in params.items() if key != Input.REQUEST_ID}
        response_json = self.connection.api_client.edit_request(
            request_id=request_id, request_parameters=request_parameters
        )

        return {
            Output.REQUEST_ID: response_json.get(Response.REQUEST, {}).get(Request.ID),
            Output.STATUS: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS),
            Output.STATUS_CODE: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS_CODE),
        }
