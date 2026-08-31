import insightconnect_plugin_runtime
from .schema import GetEndpointsInGroupInput, GetEndpointsInGroupOutput, Input, Output, Component

# Custom imports below
from icon_sophos_central.util.helpers import clean


class GetEndpointsInGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_endpoints_in_group",
            description=Component.DESCRIPTION,
            input=GetEndpointsInGroupInput(),
            output=GetEndpointsInGroupOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        group_id = params.get(Input.GROUPID)
        fields = params.get(Input.FIELDS)
        sort = params.get(Input.SORT)
        page_from_key = params.get(Input.PAGEFROMKEY)
        page_size = params.get(Input.PAGESIZE)
        page_total = params.get(Input.PAGETOTAL)
        search = params.get(Input.SEARCH)
        search_fields = params.get(Input.SEARCHFIELDS)
        # END INPUT BINDING - DO NOT REMOVE

        default_fields = [
            "associatedPerson",
            "cloud",
            "encryption",
            "group",
            "health",
            "hostname",
            "id",
            "ipv4Addresses",
            "ipv6Addresses",
            "isolation",
            "lastSeenAt",
            "lockdown",
            "macAddresses",
            "online",
            "os",
            "tamperProtectionEnabled",
            "tenant",
            "type",
        ]
        parameters = {
            "sort": sort,
            "fields": fields if fields else default_fields,
            "pageFromKey": page_from_key,
            "pageSize": page_size,
            "pageTotal": page_total,
            "search": search,
            "searchFields": search_fields,
        }
        response = self.connection.client.get_endpoints_in_group(group_id, clean(parameters))
        return {Output.ITEMS: response.get("items", []), Output.PAGES: response.get("pages", {})}
