from komand_sentinelone.util.constants import MIN_PASSWORD_LENGTH
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import Union, Dict, Any, List


class Helper:
    @staticmethod
    def join_or_empty(joined_array):
        if joined_array:
            return ",".join(joined_array)
        else:
            return None

    @staticmethod
    def check_agents_found(agents: list) -> bool:
        if len(agents) > 1:
            raise PluginException(
                cause="Multiple agents found.",
                assistance="Please provide a unique identifier for the agent to be quarantined.",
            )
        if not agents:
            return False
        return True

    @staticmethod
    def check_disconnected(agent_obj: dict) -> bool:
        if agent_obj["networkStatus"] in ("disconnected", "disconnecting"):
            return True
        return False

    @staticmethod
    def find_in_whitelist(agent_obj: dict, whitelist: list):
        for key, value in agent_obj.items():
            if key in ["externalIp", "computerName", "id", "uuid"]:
                Helper.raise_when_value_in_whitelist(value, whitelist)
            if key == "networkInterfaces":
                network_dict = value[0]
                for network_key, network_val in network_dict.items():
                    if network_key in ["inet", "inet6"]:
                        for ip_address in network_val:
                            Helper.raise_when_value_in_whitelist(ip_address, whitelist)

    @staticmethod
    def raise_when_value_in_whitelist(value: str, whitelist: List[str]):
        if value in whitelist:
            raise PluginException(
                cause="Agent found in the whitelist.",
                assistance=f"If you would like to block this host, remove {value} from the whitelist and try again.",
            )

    @staticmethod
    def return_failure_details(agent: str, error: str) -> Dict[str, Any]:
        return {"input_key": agent, "error": error}


class BlacklistMessage:
    blocked = "The given hash has been blocked"
    unblocked = "The given hash has been unlocked"
    not_exists = "The given hash does not exist"


def check_password_meets_requirements(password: str) -> Union[None, PluginException]:
    """
    A method to determine if password meets required format (minimum length and no whitespace)
    :param password: The password to check
    """
    if len(password) <= MIN_PASSWORD_LENGTH or " " in password:
        raise PluginException(
            cause="Invalid password.",
            assistance=f"Password must have more than {MIN_PASSWORD_LENGTH} characters and cannot contain whitespace.",
        )
