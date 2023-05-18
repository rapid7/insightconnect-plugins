class ApiException(Exception):
    def __init__(self, cause=None, assistance=None, data=None, status_code=None):
        self.cause = cause
        self.assistance = assistance
        self.status_code = status_code
        self.data = str(data) if data else ""

    def __str__(self):
        if self.data:
            return "An error occurred during plugin execution!\n\n{cause} {assistance}\nResponse was: {data}".format(
                cause=self.cause, assistance=self.assistance, data=self.data
            )
        else:
            return "An error occurred during plugin execution!\n\n{cause} {assistance}".format(
                cause=self.cause, assistance=self.assistance
            )
