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
            device_obj = self.find_agent_by_ip(agent)

        device_obj = self.connection.client.get_agent_details(agent)

        if whitelist:
            self._find_in_whitelist(device_obj, whitelist)
        
        return {
            Output.LOCKDOWN_DETAILS: self.connection.client.device_lockdown(device_obj.get('id'))
        }

    @staticmethod
    def _find_in_whitelist(device_obj: dict, whitelist: list):
        for key, value in device_obj.items():
            if key in ['id', 'host_name', 'ip_addresses']:
                if value in whitelist:
                    raise PluginException(
                        cause="Agent found in the whitelist.",
                        assistance=f"If you would like to block this host, remove {value} from the whitelist and try again."
                    )
        return

    def find_agent_by_ip(self, ip_address: str) -> str:
        i = 1
        response = self.connection.client.device_lockdown(i, "20")
        device_list = response.get('page_items')
        #TODO: To be finished. Think about pagination of the results. 
        for page in range(2, response.get('total_pages')+1):
            for device in device_list:
                for ip in device.get('ip_addresses'):
                    if ip_address == ip:
                        return device.get('id')