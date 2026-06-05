import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetEndpointsListInput, GetEndpointsListOutput, Input, Output, Component

# Custom imports below


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
        is_managed = params.get(Input.IS_MANAGED)
        name_filter = params.get(Input.NAME_FILTER)
        page = params.get(Input.PAGE, 1)
        parent_id = params.get(Input.PARENT_ID)
        per_page = params.get(Input.PER_PAGE, 30)
        # END INPUT BINDING - DO NOT REMOVE

        result = self.connection.api.get_endpoints_list(
            parent_id=parent_id,
            is_managed=is_managed,
            page=page,
            per_page=per_page,
            name_filter=name_filter,
        )

        # Map API response fields to our output schema
        raw_items = result.get("items", [])
        endpoints = []
        for item in raw_items:
            endpoints.append(
                {
                    "id": item.get("id", ""),
                    "name": item.get("name", ""),
                    "label": item.get("label", ""),
                    "fqdn": item.get("fqdn", ""),
                    "group_id": item.get("groupId", ""),
                    "is_managed": item.get("isManaged", False),
                    "machine_type": item.get("machineType", 0),
                    "operating_system_version": item.get("operatingSystemVersion", ""),
                    "ip": item.get("ip", ""),
                    "macs": item.get("macs", []),
                    "managed_with_best": item.get("managedWithBest", False),
                }
            )

        return {
            Output.ENDPOINTS: endpoints,
            Output.TOTAL: result.get("total", 0),
            Output.PAGES_COUNT: result.get("pagesCount"),
            Output.PAGE: result.get("page", page),
            Output.PER_PAGE: result.get("perPage", per_page),
        }
