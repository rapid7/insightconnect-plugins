import komand
from .schema import GetAddressObjectsInput, GetAddressObjectsOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
from icon_fortinet_fortigate.util.util import Helpers


class GetAddressObjects(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_address_objects',
                description=Component.DESCRIPTION,
                input=GetAddressObjectsInput(),
                output=GetAddressObjectsOutput())

    def run(self, params={}):
        endpoint = f"https://{self.connection.host}/api/v2/cmdb/firewall/address"
        filter_ = params.get(Input.NAME_FILTER, "")
        helper = Helpers(self.logger)

        params = None
        if filter_:
            params = {
                "filter": f"name=@{filter_}"
            }

        response = self.connection.session.get(endpoint, verify=self.connection.ssl_verify, params=params)

        try:
            json_response = response.json()
        except ValueError:
            raise PluginException(cause="Data sent by FortiGate was not in JSON format.\n",
                                  assistance="Contact support for help.",
                                  data=response.text)
        helper.http_errors(json_response, response.status_code)

        results = response.json().get("results")
        return {Output.ADDRESS_OBJECTS: komand.helper.clean(results)}
