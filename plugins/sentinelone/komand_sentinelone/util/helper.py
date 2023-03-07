from komand_sentinelone.util.constants import MIN_PASSWORD_LENGTH


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


def check_password_meets_requirements(password):
    if password:
        if len(password) <= 10 or " " in password:
            raise PluginException(
                cause="Invalid password.",
                assistance="Password must have more than 10 characters and cannot contain whitespace.",
            )
