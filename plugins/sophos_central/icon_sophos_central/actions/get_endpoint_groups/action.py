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
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        group_type = params.get(Input.GROUPTYPE)
        sort = params.get(Input.SORT)
        fields = params.get(Input.FIELDS)
        page = params.get(Input.PAGE)
        page_total = params.get(Input.PAGETOTAL)
        page_size = params.get(Input.PAGESIZE)
        ids = params.get(Input.IDS)
        search = params.get(Input.SEARCH)
        search_fields = params.get(Input.SEARCHFIELDS)
        endpoint_ids = params.get(Input.ENDPOINTIDS)
        # END INPUT BINDING - DO NOT REMOVE

        query_params = {
            "groupType": group_type if group_type != "all" else None,
            "sort": sort,
            "fields": fields,
            "page": page,
            "pageTotal": page_total,
            "pageSize": page_size,
            "ids": ids,
            "search": "+".join(search.split(" ")) if search else None,
            "searchFields": search_fields,
            "endpointIds": endpoint_ids,
        }

        response = self.connection.client.get_endpoint_groups(params=clean(query_params))

        return {Output.ENDPOINTGROUPS: response.get("items", []), Output.PAGES: response.get("pages", {})}
