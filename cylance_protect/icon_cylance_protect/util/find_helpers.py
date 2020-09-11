from insightconnect_plugin_runtime.exceptions import PluginException

def find_in_whitelist(device_obj: dict, whitelist: list) -> list:
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
