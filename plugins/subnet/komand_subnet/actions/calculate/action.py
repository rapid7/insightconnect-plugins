import insightconnect_plugin_runtime
from .schema import CalculateInput, CalculateOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import ipcalc
import validators


class Calculate(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="calculate",
            description=Component.DESCRIPTION,
            input=CalculateInput(),
            output=CalculateOutput(),
        )

    def run(self, params={}):
        cidr = params.get(Input.CIDR)

        # Test for correct input
        if validators.ipv4_cidr(cidr):
            subnet = ipcalc.Network(cidr)
        else:
            raise PluginException(
                cause=f"Provided network {cidr} is not in CIDR notation.",
                assistance="Please check that the provided network is correct and try again.",
            )

        # Extract first octet from input
        address = cidr.split("/", 1)
        separate = cidr.split(".", 1)
        octet = int(separate[0])

        # Test if IP is is within class A, B, or C
        if octet < 128:
            bits = 8
            ip_class = "A"
        elif octet < 192:
            bits = 16
            ip_class = "B"
        elif octet < 224:
            bits = 24
            ip_class = "C"
        else:
            raise PluginException(
                cause=f"IP address {address[0]} resides in reserved range.",
                assistance="Please provide an IP address outside the reserved range.",
            )
        # Error if an invalid mask is provided for the network class
        if int(subnet.subnet()) < bits:
            raise PluginException(
                cause="Invalid mask for network class.",
                assistance="Please provide a valid mask for the network class.",
            )

        hosts = max(int(subnet.size() - 2), 0)
        host_range = "" if not hosts else f"{str(subnet.host_first())} - {str(subnet.host_last())}"
        netmask = str(subnet.netmask())
        netmask_split = netmask.split(".", 4)

        # Calculate wildcard mask
        wildcard = []
        for i in netmask_split:
            wildcard.append(str(255 - int(i)))
        wildcard = ".".join(wildcard)

        # Calculate number of subnets
        borrowed = int(subnet.subnet()) - bits
        subnets = 2**borrowed

        # Subnets should never return zero
        if subnets == 0:
            subnets = 1

        return {
            Output.IP: address[0],
            Output.NETMASK: netmask,
            Output.WILDCARD: wildcard,
            Output.CIDR: f"/{address[1]}",
            Output.BINARY_NETMASK: subnet.netmask().bin(),
            Output.IP_CLASS: ip_class,
            Output.SUBNETS: subnets,
            Output.HOSTS: hosts,
            Output.SUBNET_ID: str(subnet.network()),
            Output.HOST_RANGE: host_range,
            Output.BROADCAST: str(subnet.broadcast()),
        }
