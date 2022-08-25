import insightconnect_plugin_runtime

from icon_manage_engine_service_desk.util.constants import Response, ResponseStatus
from .schema import AssignRequestInput, AssignRequestOutput, Input, Output, Component


# Custom imports below


class AssignRequest(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="assign_request",
            description=Component.DESCRIPTION,
            input=AssignRequestInput(),
            output=AssignRequestOutput(),
        )

    def run(self, params: dict = None) -> dict:
        request_id = params.get(Input.REQUEST_ID)
        response_json = self.connection.api_client.assign_request(
            request_id=request_id, technician=params.get(Input.TECHNICIAN), group=params.get(Input.GROUP)
        )

        return {
            Output.REQUEST_ID: request_id,
            Output.STATUS: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS),
            Output.STATUS_CODE: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS_CODE),
        }
