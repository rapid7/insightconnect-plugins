class ApiException(Exception):
    def __init__(self, cause=None, assistance=None, data=None, status_code=None):
        self.cause = cause
        self.assistance = assistance
        self.status_code = status_code
        self.data = str(data) if data else ""

    def __str__(self):
        if self.data:
            return f"An error occurred during plugin execution!\n\n{self.cause} {self.assistance}\nResponse was: {self.data}"
        else:
            return f"An error occurred during plugin execution!\n\n{self.cause} {self.assistance}"
