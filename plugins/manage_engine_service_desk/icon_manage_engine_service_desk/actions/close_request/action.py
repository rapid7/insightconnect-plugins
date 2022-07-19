import insightconnect_plugin_runtime

from icon_manage_engine_service_desk.util.constants import ResponseStatus, Response
from .schema import CloseRequestInput, CloseRequestOutput, Input, Output, Component


# Custom imports below


class CloseRequest(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="close_request",
            description=Component.DESCRIPTION,
            input=CloseRequestInput(),
            output=CloseRequestOutput(),
        )

    def run(self, params: dict = None) -> dict:
        closure_parameters = params.copy()
        request_id = closure_parameters.pop(Input.REQUEST_ID)
        response_json = self.connection.api_client.close_request(
            request_id=request_id, closure_parameters=closure_parameters
        )

        return {
            Output.REQUEST_ID: request_id,
            Output.STATUS: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS),
            Output.STATUS_CODE: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS_CODE),
        }
