import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from icon_manage_engine_service_desk.util.constants import (
    Response,
    ResponseStatus,
    Request,
    Priority,
    Status,
    User,
    Time,
)
from icon_manage_engine_service_desk.util.helpers import remove_other_keys
from .schema import GetListRequestInput, GetListRequestOutput, Input, Output, Component


# Custom imports below


class GetListRequest(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_list_request",
            description=Component.DESCRIPTION,
            input=GetListRequestInput(),
            output=GetListRequestOutput(),
        )

    def run(self, params: dict = None) -> dict:
        sort_order = None if params.get(Input.SORT_ORDER) == "None" else params.get(Input.SORT_ORDER)
        response_json = self.connection.api_client.get_requests_list(
            start_index=params.get(Input.START_INDEX),
            page_size=params.get(Input.PAGE_SIZE),
            search_fields=params.get(Input.SEARCH_FIELDS),
            sort_order=sort_order,
            sort_field=params.get(Input.SORT_FIELD),
            filter_name=params.get(Input.FILTER_NAME),
        )

        requests = []
        for request in clean(response_json.get(Response.REQUESTS)):
            for user_type in [Request.TECHNICIAN, Request.CREATED_BY, Request.REQUESTER]:
                request[user_type] = remove_other_keys(
                    request.get(user_type, {}), [User.ID, User.NAME, User.IS_VIPUSER]
                )

            request[Request.PRIORITY] = remove_other_keys(
                request.get(Request.PRIORITY, {}), [Priority.NAME, Priority.ID]
            )
            request[Request.STATUS] = remove_other_keys(request.get(Request.STATUS, {}), [Status.NAME, Status.ID])
            request[Request.CREATED_TIME] = request.get(Request.CREATED_TIME, {}).get(Time.DISPLAY_VALUE)
            request[Request.DUE_BY_TIME] = request.get(Request.DUE_BY_TIME, {}).get(Time.DISPLAY_VALUE)
            request = remove_other_keys(request, Request().get_all_attributes())
            requests.append(request)

        return clean(
            {
                Output.REQUESTS: requests,
                Output.STATUS: response_json.get(Response.RESPONSE_STATUS, [{}])[0].get(ResponseStatus.STATUS),
            }
        )
