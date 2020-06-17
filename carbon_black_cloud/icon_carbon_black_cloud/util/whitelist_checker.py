import re
from ipaddress import ip_network, ip_address

HOST = "host"
IP_NETMASK = "ip-netmask"
IP_RANGE = "ip-range"
DEVICE_ID = "device-id"


def determine_agent_type(agent):
    if re.search('[a-zA-Z]', agent):
        return HOST
    if re.search('/', agent):
        return IP_NETMASK
    if re.search('-', agent):
        return IP_RANGE

    try:
        int(agent)
        return DEVICE_ID
    except Exception:
        pass

    return IP_NETMASK


def match_whitelist(agent, whitelist, logger):
    object_type = determine_agent_type(agent)

    if object_type == HOST or object_type == DEVICE_ID:
        if agent in whitelist:
            logger.info(f" Whitelist matched\n{agent} was found in whitelist")
            return True
        else:
            return False

    # if 1.1.1.1/32 - remove /32
    trimmed_address = re.sub(r"/32$", "", agent)

    # if contains / we compare explicit matches, but not subnets in subnets
    if '/' in trimmed_address:
        return agent in whitelist

    # IP is in CIDR - Give the user a log message
    for object in whitelist:
        type = determine_agent_type(object)
        if type == IP_NETMASK:
            net = ip_network(object, False)  # False means ignore the masked bits, otherwise they need to be 0
            ip = ip_address(trimmed_address)
            if ip in net:
                logger.info(f" Whitelist matched\nIP {agent} was found in {object}")
                return True

    return False
