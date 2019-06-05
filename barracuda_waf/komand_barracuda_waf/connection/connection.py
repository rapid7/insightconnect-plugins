import komand
from .schema import ConnectionSchema

from komand_barracuda_waf.util.connector import Connector


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        url = params.get("address")
        login = params.get("credentials").get("username")
        password = params.get("credentials").get("password")

        self.connector = Connector(url, self)

        if not url:
            self.connector.raise_error("Empty url")
        if not login:
            self.connector.raise_error("Empty login")
        if not password:
            self.connector.raise_error("Empty password")

        json_ret = self.connector.post("login", {
            "username": login,
            "password": password
        })

        if self.connector.get_code() != 200:
            self.connector.raise_error("Wrong credentials")

        token = json_ret['token']
        self.connector.set_token(token)
        self.logger.info("Connect: Connecting..")
