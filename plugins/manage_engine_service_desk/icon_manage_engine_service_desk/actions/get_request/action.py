import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from icon_manage_engine_service_desk.util.constants import (
    Response,
    Request,
    User,
    Priority,
    Status,
    Time,
    ResponseStatus,
)
from icon_manage_engine_service_desk.util.helpers import remove_other_keys
from .schema import GetRequestInput, GetRequestOutput, Input, Output, Component


# Custom imports below


class GetRequest(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_request", description=Component.DESCRIPTION, input=GetRequestInput(), output=GetRequestOutput()
        )

    def run(self, params: dict = None) -> dict:
        response_json = self.connection.api_client.get_request(request_id=params.get(Input.REQUEST_ID))
        request = response_json.get(Response.REQUEST)
        for user_type in [Request.TECHNICIAN, Request.CREATED_BY, Request.REQUESTER]:
            request[user_type] = remove_other_keys(request.get(user_type, {}), [User.ID, User.NAME, User.IS_VIPUSER])

        request[Request.PRIORITY] = remove_other_keys(request.get(Request.PRIORITY, {}), [Priority.NAME, Priority.ID])
        request[Request.STATUS] = remove_other_keys(request.get(Request.STATUS, {}), [Status.NAME, Status.ID])
        request[Request.CREATED_TIME] = request.get(Request.CREATED_TIME, {}).get(Time.DISPLAY_VALUE)
        request[Request.DUE_BY_TIME] = request.get(Request.DUE_BY_TIME, {}).get(Time.DISPLAY_VALUE)
        request = remove_other_keys(request, Request().get_all_attributes())

        return clean(
            {
                Output.REQUEST: request,
                Output.STATUS: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS),
            }
        )
