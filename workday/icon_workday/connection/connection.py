import komand
from .schema import ConnectionSchema, Input
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.username = None
        self.password = None
        self.tenant = None
        self.environment = None

    def connect(self, params):
        self.username = params[Input.USERNAME]
        self.password = params[Input.PASSWORD]
        self.tenant = params[Input.TENANT]

        self.environment = params.get(Input.ENVIRONMENT)

    def test(self):
        pass
