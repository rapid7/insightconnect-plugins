import insightconnect_plugin_runtime
from .schema import GetEndpointGroupsInput, GetEndpointGroupsOutput, Input, Output, Component

# Custom imports below

from icon_sophos_central.util.helpers import clean


class GetEndpointGroups(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_endpoint_groups",
            description=Component.DESCRIPTION,
            input=GetEndpointGroupsInput(),
            output=GetEndpointGroupsOutput(),
        )

    def run(self, params={}):
        group_type = params.get(Input.GROUPTYPE)
        params = {
            "groupType": group_type if group_type != "all" else None,
            "sort": params.get(Input.SORT),
            "fields": params.get(Input.FIELDS),
            "page": params.get(Input.PAGE),
            "pageTotal": params.get(Input.PAGETOTAL),
            "pageSize": params.get(Input.PAGESIZE),
            "ids": params.get(Input.IDS),
            "search": "+".join(params.get(Input.SEARCH).split(" ")),
            "searchFields": params.get(Input.SEARCHFIELDS),
            "endpointIds": params.get(Input.ENDPOINTIDS),
        }

        response = self.connection.client.get_endpoint_groups(params=clean(params))

        return {Output.ENDPOINTGROUPS: response.get("items", []), Output.PAGES: response.get("pages", {})}
