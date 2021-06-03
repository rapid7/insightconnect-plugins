import insightconnect_plugin_runtime
from .schema import HostInformationInput, HostInformationOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import shodan


class HostInformation(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="host_information",
            description="Return Services Found for the Given IP",
            input=HostInformationInput(),
            output=HostInformationOutput(),
        )

    def run(self, params={}):
        try:
            response = shodan.Shodan(self.connection.token).host(params.get(Input.IP))
        except shodan.exception.APIError as e:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=e)

        data = response["data"]
        data_list = []
        for item in data:
            data_list.append(item["data"])

        return insightconnect_plugin_runtime.helper.clean_dict(
            {
                Output.IP_STR: response.get("ip_str"),
                Output.ASN: response.get("asn"),
                Output.HOSTNAMES: response.get("hostnames"),
                Output.ORG: response.get("org"),
                Output.COUNTRY_NAME: response.get("country_name"),
                Output.COUNTRY_CODE: response.get("country_code"),
                Output.OS: response.get("os"),
                Output.PORTS: response.get("ports"),
                Output.DATA: data_list,
            }
        )
