DEFAULT_TASK_TYPE = "CMEF"


class UserType:
    @staticmethod
    def value_of(user_type: str) -> int:
        return {"Basic": 1, "Licensed": 2}.get(user_type)
