import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetEndpointsListInput, GetEndpointsListOutput, Input, Output, Component

# Custom imports below
from icon_bitdefender_gravityzone.util.helpers import to_endpoint_item

DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 30


class GetEndpointsList(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_endpoints_list",
            description=Component.DESCRIPTION,
            input=GetEndpointsListInput(),
            output=GetEndpointsListOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        filters = params.get(Input.FILTERS)
        is_managed = params.get(Input.IS_MANAGED)
        page = params.get(Input.PAGE)
        parent_id = params.get(Input.PARENT_ID)
        per_page = params.get(Input.PER_PAGE)
        # END INPUT BINDING - DO NOT REMOVE

        page = page or DEFAULT_PAGE
        per_page = per_page or DEFAULT_PER_PAGE
        result = self.connection.api.get_endpoints_list(
            parent_id=parent_id,
            is_managed=is_managed,
            page=page,
            per_page=per_page,
            filters=filters,
        )
        return {
            Output.ENDPOINTS: [to_endpoint_item(item) for item in result.get("items") or []],
            Output.TOTAL: result.get("total") or 0,
            Output.PAGES_COUNT: result.get("pagesCount") or 0,
            Output.PAGE: result.get("page") or page,
            Output.PER_PAGE: result.get("perPage") or per_page,
        }
