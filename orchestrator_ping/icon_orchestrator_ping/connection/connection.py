import komand
from .schema import ConnectionSchema, Input
from komand.exceptions import PluginException
# Custom imports below


class Connection(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.username, self.password = None, None

    def connect(self, params):
        self.username = params[Input.CREDENTIALS]["username"]
        self.password = params[Input.CREDENTIALS]["password"]

        if self.username == "bad-robot":
            raise PluginException(
                cause=f"The username {self.username} is not allowed to connect!",
                assistance="Try another username!",
            )

    def test(self):
        # Will execute connection code
        pass
