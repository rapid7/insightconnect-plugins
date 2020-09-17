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
        try:
            ip_address(address)
            return "ip-netmask"
        except:
            pass
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
                self.logger.info(f" Whitelist matched\n{address} was found in whitelist")
                return True
            else:
                return False

        # if 1.1.1.1/32 - remove /32
        trimmed_address = re.sub(r"/32$", "", address)

        # if contains / we compare explicit matches, but not subnets in subnets
        if '/' in trimmed_address:
            return address in whitelist

        # IP is in CIDR - Give the user a log message
        for object in whitelist:
            type = self.determine_address_type(object)
            if type == "ip-netmask":
                net = ip_network(object, False) # False means ignore the masked bits, otherwise they need to be 0
                ip = ip_address(trimmed_address)
                if ip in net:
                    self.logger.info(f" Whitelist matched\nIP {address} was found in {object}")
                    return True

        return False

    def check_if_private(self, address):
        if re.search('/', address): # CIDR
            return ip_network(address, False).is_private
        elif re.search('-', address): # IP Range
            split_ = address.split("-")
            if len(split_) == 2: # If this isn't 2, I'm not sure what the input was
                return (ip_address(split_[0]).is_private and ip_address(split_[1]).is_private)
        try: # Other
            if ip_address(address).is_private:
                return True
        except Exception: # This was a domain name
            pass

        return False

    def run(self, params={}):
        address = params.get(Input.ADDRESS)
        # object_type = params.get(Input.TYPE)
        name = params.get(Input.ADDRESS_OBJECT)
        description = params.get(Input.DESCRIPTION)
        tag_list = params.get(Input.TAGS)
        whitelist = params.get(Input.WHITELIST)
        skip_private = params.get(Input.SKIP_RFC1918)

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
        if skip_private:
            if object_type != "fqdn":
               if self.check_if_private(address):
                   return {
                       Output.MESSAGE: "Address object was RFC 1918 (private).",
                       Output.CODE: "",
                       Output.STATUS: "error"
                   }


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
