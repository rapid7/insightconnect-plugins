class APIException(Exception):
    def __init__(self, cause, assistance="", data=""):
        self.cause = cause
        self.assistance = assistance
        self.data = data
        super().__init__(self.cause)

    def __str__(self):
        return "An error occurred connecting to the Insight Agent API!\n\n{cause}\n{assistance}\nResponse was: {data}".format(
            cause=self.cause, assistance=self.assistance, data=self.data
        )
