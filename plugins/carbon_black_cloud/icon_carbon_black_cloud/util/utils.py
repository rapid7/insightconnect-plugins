from typing import List
from ipaddress import ip_network, ip_address
from logging import Logger
import re


HOST = "host"
IP_NETMASK = "ip-netmask"
IP_RANGE = "ip-range"
DEVICE_ID = "device-id"

REGEX_HOST = "[a-zA-Z]"
REGEX_IP_NETMASK = "/"
REGEX_IP_RANGE = "-"


class Util:
    @staticmethod
    def determine_agent_type(agent: str) -> str:
        """
        determine_agent_type. Determine the type of agent based on its name.

        :param agent: A string representing the name of the agent to classify.
        :type: str

        :return: The type of agent.
        :rtype: str
        """

        if re.search(REGEX_HOST, agent):
            return HOST
        if re.search(REGEX_IP_NETMASK, agent):
            return IP_NETMASK
        if re.search(REGEX_IP_RANGE, agent):
            return IP_RANGE
        try:
            int(agent)
            return DEVICE_ID
        except Exception:  # noqa: B110
            pass
        return IP_NETMASK

    @staticmethod
    def match_whitelist(agent: str, whitelist: List[str], logger: Logger) -> bool:
        """
        match_whitelist. Check if the given agent string matches any of the whitelist strings.

        :param agent: The agent string to be checked.
        :type: str

        :param whitelist: A list of strings to be compared against the agent string.
        :type: List[str]

        :param logger: A logger object.
        :type: Logger

        :return: True if the agent string matches any of the whitelist strings, False otherwise.
        :rtype: bool
        """

        object_type = Util.determine_agent_type(agent)
        if object_type in (HOST, DEVICE_ID):
            if agent in whitelist:
                logger.info(f" Whitelist matched\n{agent} was found in whitelist")
                return True
            else:
                return False

        # if 1.1.1.1/32 - remove /32
        trimmed_address = re.sub(r"/32$", "", agent)

        # if contains / we compare explicit matches, but not subnets in subnets
        if "/" in trimmed_address:
            return agent in whitelist

        # IP is in CIDR - Give the user a log message
        for object_ in whitelist:
            type_ = Util.determine_agent_type(object_)
            if type_ == IP_NETMASK:
                net = ip_network(object_, False)  # False means ignore the masked bits, otherwise they need to be 0
                ip = ip_address(trimmed_address)
                if ip in net:
                    logger.info(f" Whitelist matched\nIP {agent} was found in {object_}")
                    return True
        return False
