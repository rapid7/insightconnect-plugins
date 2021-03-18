import komand
from .schema import GetAddressesFromGroupInput, GetAddressesFromGroupOutput, Input, Output, Component

# Custom imports below
from komand.exceptions import PluginException
import validators


class GetAddressesFromGroup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_addresses_from_group",
            description=Component.DESCRIPTION,
            input=GetAddressesFromGroupInput(),
            output=GetAddressesFromGroupOutput(),
        )

    def run(self, params={}):
        group_name = params.get(Input.GROUP)
        device_name = params.get(Input.DEVICE_NAME)
        virtual_system = params.get(Input.VIRTUAL_SYSTEM)

        response = self.connection.request.get_address_group(
            device_name=device_name, virtual_system=virtual_system, group_name=group_name
        )

        try:
            address_objects = response.get("response").get("result").get("entry").get("static").get("member")
        except AttributeError:
            raise PluginException(
                cause="PAN OS returned an unexpected response.",
                assistance=f"Could not find group '{group_name}', or group was empty. Check the name, virtual system "
                f"name, and device name.\nDevice name: {device_name}\nVirtual system: {virtual_system}\n",
                data=response,
            )

        fqdn_addresses = []
        ipv4_addresses = []
        ipv6_addresses = []
        all_addresses = []

        for name in address_objects:
            object_name = self.get_name(name)
            response = self.connection.request.get_address_object(
                device_name=device_name, virtual_system=virtual_system, object_name=object_name
            )
            try:
                address_object = response.get("response").get("result").get("entry")
            except AttributeError:
                raise PluginException(
                    cause="PAN OS returned an unexpected response.",
                    assistance=f"Could not find address object '{name}'. Check the name, virtual system name, and "
                    f"device name.\nDevice name: {device_name}\nVirtual system: {virtual_system}\n",
                    data=response,
                )
            address = ""
            if address_object.get("fqdn"):
                address = self.get_name(address_object.get("fqdn"))
                if address in fqdn_addresses:
                    continue
                else:
                    fqdn_addresses.append(address)
            elif address_object.get("ip-netmask"):
                address = self.get_name(address_object.get("ip-netmask"))
                if validators.ipv4(address) or validators.ipv4_cidr(address):
                    if address in ipv4_addresses:
                        continue
                    else:
                        ipv4_addresses.append(address)
                if validators.ipv6(address) or validators.ipv6_cidr(address):
                    if address in ipv6_addresses:
                        continue
                    else:
                        ipv6_addresses.append(address)
            if address in all_addresses:
                continue
            else:
                all_addresses.append(address)

        return {
            Output.SUCCESS: True,
            Output.FQDN_ADDRESSES: fqdn_addresses,
            Output.IPV4_ADDRESSES: ipv4_addresses,
            Output.IPV6_ADDRESSES: ipv6_addresses,
            Output.ALL_ADDRESSES: all_addresses,
        }

    @staticmethod
    def get_name(address_object):
        if type(address_object) == str:
            name = address_object
        else:
            name = address_object.get("#text")
        return name
