import komand
from .schema import ConnectionSchema, Input

# Custom imports below
from komand.exceptions import ConnectionTestException, PluginException
from requests import Session
from requests.auth import HTTPBasicAuth
from icon_fireeye_hx.util.api import FireEyeAPI


class Connection(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.session, self.url = None, None
        self.api = None

    def connect(self, params={}):
        username, password = (
            params.get(Input.USERNAME_PASSWORD).get("username"),
            params.get(Input.USERNAME_PASSWORD).get("password"),
        )

        self.url = params.get(Input.URL)
        ssl_verify = params.get(Input.SSL_VERIFY)

        self.session: Session = Session()
        self.session.auth = HTTPBasicAuth(username=username, password=password)

        self.api = FireEyeAPI(self.url, username, password, ssl_verify, self.logger)

    def test(self):
        try:
            self.api.get_version()
        except PluginException:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.USERNAME_PASSWORD)
        return {"status": "success"}
