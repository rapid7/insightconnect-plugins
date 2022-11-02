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
