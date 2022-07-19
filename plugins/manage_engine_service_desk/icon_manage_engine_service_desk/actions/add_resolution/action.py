import insightconnect_plugin_runtime

from icon_manage_engine_service_desk.util.constants import Response, ResponseStatus
from .schema import AddResolutionInput, AddResolutionOutput, Input, Output, Component


# Custom imports below


class AddResolution(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_resolution",
            description=Component.DESCRIPTION,
            input=AddResolutionInput(),
            output=AddResolutionOutput(),
        )

    def run(self, params: dict = None) -> dict:
        request_id = params.get(Input.REQUEST_ID)
        response_json = self.connection.api_client.add_request_resolution(
            request_id=request_id,
            content=params.get(Input.CONTENT),
            add_to_linked_requests=params.get(Input.ADD_TO_LINKED_REQUESTS),
        )

        return {
            Output.REQUEST_ID: request_id,
            Output.STATUS: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS),
            Output.STATUS_CODE: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS_CODE),
        }
