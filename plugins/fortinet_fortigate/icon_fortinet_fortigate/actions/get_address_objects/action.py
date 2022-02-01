import insightconnect_plugin_runtime
from .schema import GetAddressObjectsInput, GetAddressObjectsOutput, Input, Output, Component

# Custom imports below
from icon_fortinet_fortigate.util.util import Helpers


class GetAddressObjects(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_address_objects",
            description=Component.DESCRIPTION,
            input=GetAddressObjectsInput(),
            output=GetAddressObjectsOutput(),
        )

    def run(self, params={}):
        name_filter = params.get(Input.NAME_FILTER, "")
        fqdn_filter = params.get(Input.FQDN_FILTER, "")
        subnet_filter = params.get(Input.SUBNET_FILTER, "")
        ipv6_subnet_filter = params.get(Input.IPV6_SUBNET_FILTER, "")
        helper = Helpers(self.logger)

        filters = []
        ipv6_filters = []

        if name_filter:
            filters.append(f"name=@{name_filter}")
            ipv6_filters.append(f"name=@{name_filter}")
        if subnet_filter:
            subnet_filter = helper.ipmask_converter(subnet_filter)
            subnet_filter = helper.netmask_converter(subnet_filter)
            filters.append(f"subnet=@{subnet_filter}")
        if fqdn_filter:
            filters.append(f"fqdn=@{fqdn_filter}")
        if ipv6_subnet_filter:
            ipv6_filters.append(f"ip6=@{ipv6_subnet_filter}")

        params = {"filter": filters}
        endpoint = "firewall/address"
        results = self.connection.api.get_address_objects(endpoint, params).get("results", [])

        for i, result in enumerate(results):
            subnet = result.get("subnet")
            if subnet:
                subnet = helper.ipmask_converter(subnet)
                results[i]["subnet"] = subnet

        ipv6_params = {"filter": ipv6_filters}
        endpoint = "firewall/address6"
        ipv6_results = self.connection.api.get_address_objects(endpoint, ipv6_params).get("results")

        return {
            Output.ADDRESS_OBJECTS: insightconnect_plugin_runtime.helper.clean(results),
            Output.IPV6_ADDRESS_OBJECTS: insightconnect_plugin_runtime.helper.clean(ipv6_results),
        }
