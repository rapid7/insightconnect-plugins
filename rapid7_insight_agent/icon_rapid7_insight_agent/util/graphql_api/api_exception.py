class APIException(Exception):
    def __init__(self, cause, assistance="", data=""):
        self.cause = cause
        self.assistance = assistance
        self.data = data
        super().__init__(self.cause)
