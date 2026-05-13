import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from icon_manage_engine_service_desk.util.constants import Response, ResponseStatus
from icon_manage_engine_service_desk.util.helpers import transform_request, safe_get
from .schema import GetRequestInput, GetRequestOutput, Input, Output, Component

# Custom imports below


class GetRequest(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_request", description=Component.DESCRIPTION, input=GetRequestInput(), output=GetRequestOutput()
        )

    def run(self, params: dict = None) -> dict:
        response_json = self.connection.api_client.get_request(request_id=params.get(Input.REQUEST_ID))
        request = transform_request(response_json.get(Response.REQUEST))

        return clean(
            {
                Output.REQUEST: request,
                Output.STATUS: safe_get(response_json, Response.RESPONSE_STATUS, ResponseStatus.STATUS),
            }
        )
