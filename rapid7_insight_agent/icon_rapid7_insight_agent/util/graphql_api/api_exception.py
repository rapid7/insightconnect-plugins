class APIException(Exception):
    def __init__(self, cause, assistance="", data=""):
        self.cause = cause
        self.assistance = assistance
        self.data = str(data) if data else None
        super().__init__(self.cause)

    def __str__(self):
        return f"\nAn error occurred with the Insight Agent API.\n" \
               f"{self.cause}\n{self.assistance}\nData: {self.data}"
