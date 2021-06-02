class Helper:
    @staticmethod
    def join_or_empty(joined_array):
        if joined_array:
            return ",".join(joined_array)
        else:
            return None
