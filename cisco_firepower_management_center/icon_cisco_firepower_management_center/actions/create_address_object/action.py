import komand
from .schema import CreateAddressObjectInput, CreateAddressObjectOutput, Input, Output, Component
# Custom imports below
import re
import validators
from ipaddress import ip_network, ip_address, IPv4Network, IPv6Network
from komand.exceptions import PluginException
import fmcapi


class CreateAddressObject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_address_object',
                description=Component.DESCRIPTION,
                input=CreateAddressObjectInput(),
                output=CreateAddressObjectOutput())

    def run(self, params={}):
        name = params.get(Input.ADDRESS_OBJECT, params.get(Input.ADDRESS))
        address = params.get(Input.ADDRESS)
        address_type = self._determine_address_type(address)
        whitelist = params.get(Input.WHITELIST)

        if params.get(Input.SKIP_PRIVATE_ADDRESS) and address_type != "fqdn" and self._check_if_private(address,
                                                                                                        address_type):
            raise PluginException(cause="Private address provided to be blocked.",
                                    assistance="Skip Private Address set to true but private IP: "
                                                f"{address} provided to be blocked.")

        if whitelist:
            self._match_whitelist(address, whitelist)

        try:
            with fmcapi.FMC(
                host=self.connection.host,
                username=self.connection.username,
                password=self.connection.password,
                autodeploy=True,
                limit=10
            ) as fmc1:
                return {
                    Output.ADDRESS_OBJECT: self.create_address_object(
                        fmc=fmc1,
                        name=name,
                        value=address,
                        object_type=address_type
                    )
                }
        except TypeError:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)

    def create_address_object(self, fmc: fmcapi.FMC, name: str, value: str, object_type: str) -> dict:
        if object_type == 'ipv4' or object_type == 'ipv6':
            address_object = fmcapi.Hosts(fmc=fmc)
        elif object_type == 'cidr':
            address_object = fmcapi.Networks(fmc=fmc)
        elif object_type == 'fqdn':
            address_object = fmcapi.FQDNS(fmc=fmc)

        address_object.name = name
        address_object.value = value
        if address_object.post():
            return address_object
        
        raise PluginException(
            cause=f"Address Object - {name}, already exists.",
            assistance=f"Please provide a different name for the address object and try again.")
    

    # def create_host_object(self, fmc: fmcapi.FMC, name: str, value: str) -> dict:
    #     host = fmcapi.Hosts(fmc=fmc)
    #     host.name = name
    #     host.value = value
    #     host.post()
    #     return host.get()

    # def create_network_object(self, fmc: fmcapi.FMC, name: str, value: str) -> dict:
    #     network = fmcapi.Networks(fmc=fmc)
    #     network.name = name
    #     network.value = value
    #     network.post()
    #     return network.get()

    # def create_fqdn_object(self, fmc: fmcapi.FMC, name: str, value: str) -> dict:
    #     fqdn = fmcapi.FQDNS(fmc=fmc)
    #     fqdn.name = name
    #     fqdn.value = value
    #     fqdn.post()
    #     return fqdn.get()

    def _match_whitelist(self, address: str, whitelist: str) -> bool:
        trimmed_address = re.sub(r"/32$", "", address)
        if address in whitelist:
            raise PluginException(
                cause=f"Address Object not created because the host {address} was found in the whitelist as {address}.",
                assistance=f"If you would like to block this host, remove {address} from the whitelist and try again.")
        elif '/' not in trimmed_address:
            pass

        for address_object in whitelist:
            if self._determine_address_type(address_object) == "cidr":
                net = ip_network(address_object, False)
                ip = ip_address(trimmed_address)
                if ip in net:
                    raise PluginException(
                        cause=f"Address Object not created because the host {address}"
                              f" was found in the whitelist as {address_object}.",
                        assistance="If you would like to block this host,"
                                   f" remove {address_object} from the whitelist and try again.")

        return False

    @staticmethod
    def _check_if_private(address: str, address_type: str) -> bool:
        if address_type == "ipv6":
            ip_list = [str(ip) for ip in IPv6Network(address)]
        else:
            ip_list = [str(ip) for ip in IPv4Network(address)]

        if ip_address(ip_list[0]).is_private and ip_address(ip_list[-1]).is_private:
            return True
        return False

    @staticmethod
    def _determine_address_type(address: str) -> str:
        if validators.ipv4(address):
            return "ipv4"
        if validators.ipv6(address):
            return "ipv6"
        if validators.domain(address):
            return "fqdn"
        if re.search('/', address):
            return "cidr"
        raise PluginException(cause="Unknown address type provided.",
                              assistance=f"{address} is not one of the following: IPv4, IPv6, CIDR or domain name.")
