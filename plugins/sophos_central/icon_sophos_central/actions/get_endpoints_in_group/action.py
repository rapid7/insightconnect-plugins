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
        fields = params.get(Input.FIELDS)
        parameters = {
            "sort": params.get(Input.SORT),
            "fields": fields if fields else default_fields,
            "pageFromKey": params.get(Input.PAGEFROMKEY),
            "pageSize": params.get(Input.PAGESIZE),
            "pageTotal": params.get(Input.PAGETOTAL),
            "search": params.get(Input.SEARCH),
            "searchFields": params.get(Input.SEARCHFIELDS),
        }
        response = self.connection.client.get_endpoints_in_group(params.get(Input.GROUPID), clean(parameters))
        return {Output.ITEMS: response.get("items", []), Output.PAGES: response.get("pages", {})}
