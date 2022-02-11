import komand
from .schema import ConnectionSchema, Input


class Connection(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.username = None
        self.password = None
        self.auth_type = None
        self.port = None
        self.domain = None
        self.kdc = None

    def connect(self, params={}):
        self.username = params.get(Input.CREDENTIALS, {}).get("username")
        self.password = params.get(Input.CREDENTIALS, {}).get("password")
        self.auth_type = params.get(Input.AUTH, "None")
        self.port = params.get(Input.PORT, 5986)
        self.domain = params.get(Input.KERBEROS, {}).get("domain_name")
        self.kdc = params.get(Input.KERBEROS, {}).get("kdc")

        self.logger.info("Connect: Connecting..")
