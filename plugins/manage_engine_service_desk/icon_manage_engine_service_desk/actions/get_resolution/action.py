import insightconnect_plugin_runtime

# Custom imports below
from insightconnect_plugin_runtime.helper import clean

from icon_manage_engine_service_desk.util.constants import Response, ResponseStatus, Resolution
from .schema import GetResolutionInput, GetResolutionOutput, Input, Output, Component


class GetResolution(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_resolution",
            description=Component.DESCRIPTION,
            input=GetResolutionInput(),
            output=GetResolutionOutput(),
        )

    def run(self, params: dict = None) -> dict:
        request_id = params.get(Input.REQUEST_ID)
        response_json = self.connection.api_client.get_request_resolution(request_id=request_id)

        return clean(
            {
                Output.REQUEST_ID: request_id,
                Output.CONTENT: response_json.get(Response.RESOLUTION, {}).get(Resolution.CONTENT),
                Output.STATUS: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS),
                Output.STATUS_CODE: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS_CODE),
            }
        )
