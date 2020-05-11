import komand
from .schema import SetAddressObjectInput, SetAddressObjectOutput, Input, Output
from komand.exceptions import PluginException
# Custom imports below
import re
from ipaddress import ip_network, ip_address

class SetAddressObject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='set_address_object',
                description='Create a new address object',
                input=SetAddressObjectInput(),
                output=SetAddressObjectOutput())

    def determine_address_type(self, address):
        if re.search('[a-zA-Z]', address):
            return "fqdn"
        if re.search('/', address):
            return "ip-netmask"
        if re.search('-', address):
            return "ip-range"
        return "ip-netmask"

    def match_whitelist(self, address, whitelist, object_type):
        if object_type == "fqdn":
            if address in whitelist:
                self.logger.info(f" Whitelist matched\nIP {address} was found in whitelist")
                return True
            else:
                return False

        # if 1.1.1.1/32 - remove /32
        trimmed_address = re.sub(r"/32$", "", address)

        # if contains / skip - Can't compare CIDR to CIDR
        if '/' in trimmed_address:
            self.logger.info(f"{address} appears to be CIDR, skipping whitelist check.")
            return False

        # IP is in CIDR - Give the user a log message
        for object in whitelist:
            type = self.determine_address_type(object)
            if type == "ip-netmask":
                net = ip_network(object)
                ip = ip_address(trimmed_address)
                if ip in net:
                    self.logger.info(f" Whitelist matched\nIP {address} was found in {object}")
                    return True

        return False

    def run(self, params={}):
        address = params.get(Input.ADDRESS_OBJECT)
        # object_type = params.get(Input.TYPE)
        name = params.get(Input.OBJECT_NAME)
        description = params.get(Input.OBJECT_DESCRIPTION)
        tag_list = params.get(Input.TAGS)
        whitelist = params.get(Input.WHITELIST)

        object_type = self.determine_address_type(address)

        # create tags XML
        tag = ''
        if tag_list:
            tag_list = tag_list.split(',')
            for item in tag_list:
                tag = tag + f'<member>{item}</member>'

        """
        create object type XML
        
        supported types: 

        - ip-netmask
        - ip-range
        - fqdn        
        """
        # object_type = object_type.lower()

        if object_type != "ip-range":
            if whitelist:
                if self.match_whitelist(address, whitelist, object_type):
                    return {
                        Output.MESSAGE: "Address object matched whitelist.",
                        Output.CODE: "",
                        Output.STATUS: "error"
                    }


        address = f'<{object_type}>{address}</{object_type}>'

        # xpath = f"/config/devices/entry/vsys/entry/address/entry[@name='test{name}']"
        xpath = f"/config/devices/entry/vsys/entry/address/entry[@name='{name}']"
        element = address
        if description:
            element = f'{element}<description>{description}</description>'
        if tag:
            element = f'{element}<tag>{tag}</tag>'

        output = self.connection.request.set_(xpath=xpath, element=element)
        try:
            return {Output.MESSAGE: output['response']['msg'],
                    Output.STATUS: output['response']['@status'],
                    Output.CODE: output['response']['@code']}
        except KeyError:
            raise PluginException(cause='The output did not contain expected keys.',
                                  assistance='Contact support for help.',
                                  data=output)
