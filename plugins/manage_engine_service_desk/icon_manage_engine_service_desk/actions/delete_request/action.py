import insightconnect_plugin_runtime

from icon_manage_engine_service_desk.util.constants import Response, ResponseStatus
from .schema import DeleteRequestInput, DeleteRequestOutput, Input, Output, Component


# Custom imports below


class DeleteRequest(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_request",
            description=Component.DESCRIPTION,
            input=DeleteRequestInput(),
            output=DeleteRequestOutput(),
        )

    def run(self, params: dict = None) -> dict:
        request_id = params.get(Input.REQUEST_ID)
        response_json = self.connection.api_client.delete_request(request_id=request_id)

        return {
            Output.REQUEST_ID: request_id,
            Output.STATUS: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS),
            Output.STATUS_CODE: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS_CODE),
        }
