from komand_sentinelone.util.constants import MIN_PASSWORD_LENGTH
from insightconnect_plugin_runtime.exceptions import PluginException


class Helper:
    @staticmethod
    def join_or_empty(joined_array):
        if joined_array:
            return ",".join(joined_array)
        else:
            return None


class BlacklistMessage:
    blocked = "The given hash has been blocked"
    unblocked = "The given hash has been unlocked"
    not_exists = "The given hash does not exist"


def check_password_meets_requirements(password: str) -> Union[None, PluginException]:
    """
    A method to determine if password meets required format (minimum length and no whitespace)
    :param password: The password to check
    """
    if len(password) <= 10 or " " in password:
        raise PluginException(
            cause="Invalid password.",
            assistance="Password must have more than 10 characters and cannot contain whitespace.",
        )
