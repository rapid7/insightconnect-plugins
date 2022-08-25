import insightconnect_plugin_runtime

from icon_manage_engine_service_desk.util.constants import ResponseStatus, Response, Request
from .schema import AddRequestInput, AddRequestOutput, Input, Output, Component


# Custom imports below


class AddRequest(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_request", description=Component.DESCRIPTION, input=AddRequestInput(), output=AddRequestOutput()
        )

    def run(self, params: dict = None) -> dict:
        response_json = self.connection.api_client.add_request(request_parameters=params)
        return {
            Output.REQUEST_ID: response_json.get(Response.REQUEST, {}).get(Request.ID),
            Output.STATUS: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS),
            Output.STATUS_CODE: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS_CODE),
        }
