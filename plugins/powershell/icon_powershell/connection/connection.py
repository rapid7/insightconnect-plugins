import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.username = None
        self.password = None
        self.auth_type = None
        self.port = None
        self.domain = None
        self.kdc = None
        self.script_credentials = None

    def connect(self, params={}):
        self.username = params.get(Input.CREDENTIALS, {}).get("username")
        self.password = params.get(Input.CREDENTIALS, {}).get("password")
        self.auth_type = params.get(Input.AUTH, "None")
        self.port = params.get(Input.PORT, 5986)
        self.domain = params.get(Input.KERBEROS, {}).get("domain_name")
        self.kdc = params.get(Input.KERBEROS, {}).get("kdc")
        self.script_credentials = {
            "username": params.get(Input.SCRIPT_USERNAME_AND_PASSWORD, {}).get("username"),
            "password": params.get(Input.SCRIPT_USERNAME_AND_PASSWORD, {}).get("password"),
            "secret_key": params.get(Input.SCRIPT_SECRET_KEY, {}).get("secretKey"),
        }
        self.logger.info("Connect: Connecting..")
