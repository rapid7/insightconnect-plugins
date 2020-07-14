import insightconnect_plugin_runtime
from .schema import QuarantineInput, QuarantineOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below
import validators

class Quarantine(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='quarantine',
                description=Component.DESCRIPTION,
                input=QuarantineInput(),
                output=QuarantineOutput())

    def run(self, params={}):
        whitelist = params.get(Input.WHITELIST, None)
        agent = params.get(Input.AGENT)

        if validators.ipv4(agent):
            agent = self.find_agent_by_ip(agent)

        device_obj = self.connection.client.get_agent_details(agent)

        if whitelist:
            matches = self._find_in_whitelist(device_obj, whitelist)
            if matches:
                raise PluginException(
                    cause="Agent found in the whitelist.",
                    assistance=f"If you would like to block this host, remove {str(matches)[1:-1]} from the whitelist."
                )
        
        return {
            Output.LOCKDOWN_DETAILS: self.connection.client.device_lockdown(device_obj.get('id'))
        }

    @staticmethod
    def _find_in_whitelist(device_obj: dict, whitelist: list) -> list:
        whitelist_values = []
        for key, value in device_obj.items():
            if key in ['id', 'host_name']:
                if value in whitelist:
                    whitelist_values.append(value)

        for ip_address in device_obj.get('ip_addresses'):
            if ip_address in whitelist:
                whitelist_values.append(ip_address)

        return whitelist_values

    def find_agent_by_ip(self, ip_address: str) -> str:
        i = 1
        total_pages = self.connection.client.get_agents(i, "20").get('total_pages')
        while i <= total_pages:
            response = self.connection.client.get_agents(i, "20")
            device_list = response.get('page_items')
            for device in device_list:
                for ip in device.get('ip_addresses'):
                    if ip_address == ip:
                        return device.get('id')
            i += 1

        raise PluginException(
            cause="Agent not found.",
            assistance=f"Unable to find an agent with IP: {ip_address}, please ensure that the IP address is correct."
        )
