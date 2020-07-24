class APIException(Exception):
    def __init__(self, cause, assistance="", data=""):
        self.cause = cause
        self.assistance = assistance
        self.data = data
        super().__init__(self.cause)

    def __str__(self):
        return f"An error occurred connecting to the Insight Agent API!\n\n" \
               f"{self.cause}\n{self.assistance}\nResponse was: {self.data}"
