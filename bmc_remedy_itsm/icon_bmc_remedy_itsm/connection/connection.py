import komand
from komand.exceptions import ConnectionTestException, PluginException
from .schema import ConnectionSchema, Input
# Custom imports below
import requests
import maya


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.last_jwt_time = maya.now()
        self.url = f'{params.get(Input.URL)}:{params.get(Input.PORT)}'
        self.auth_payload = {
            'username': params.get(Input.CREDENTIALS).get("username"),
            'password': params.get(Input.CREDENTIALS).get("password")
        }

        self.get_auth_token()

    def get_auth_token(self):
        login_endpoint = f'{self.url}/api/jwt/login'

        self.session = requests.session()
        self.logger.info(f"Logging into URL: {self.url}")

        try:
            response = self.session.post(login_endpoint, data=self.auth_payload, verify=Input.SSL_VERIFY)
        except requests.exceptions.ConnectionError as e:
            # These if statements will ensure that the args variables have a length of 1 or more. I do not know how they would not but just in case
            if len(e.args) < 1:
                raise PluginException(cause="An unknown connection error occurred.",
                                      assistance="Contact support for help.",
                                      data=e)
            if len(e.args[0].reason.args) < 1:
                raise PluginException(cause="An unknown connection error occurred.",
                                      assistance="Contact support for help.",
                                      data=e)
            # checks for a urllib3 error number 61 which is caused by a ConnectionRefused base exception
            if "[Errno 61]" in e.args[0].reason.args[0]:
                raise PluginException(cause="A connection refused error occurred.",
                                      assistance=f"This error is normally caused by an incorrect port number. The port number used was {Input.PORT}.",
                                      data=e)
            # checks for a urllib3 error number 60 which is caused by a TimeOut base exception
            if "[Errno 60]" in e.args[0].reason.args[0]:
                raise PluginException(cause="A timeout error occurred.",
                                      assistance=f"This error is normally caused by an incorrect URL. The URL used was {Input.URL}."
                                                 f" The error may also indicate other connection issues such as the BMC server being down,"
                                                 f" or a firewall blocking the connection.",
                                      data=e)
        self.logger.info(f"Result of authentication request: ****************************{response.text[-5:]}")
        self.jwt = response.text

    def make_headers_and_refresh_token(self):
        now = maya.now()

        interval = now.epoch - self.last_jwt_time.epoch
        if interval > 3500: # default is 3600. Give ourselves some room if we hit this at 3599
            self.last_jwt_time = now
            self.get_auth_token()

        return {
            "Authorization": f"AR-JWT {self.jwt}"
        }

    def test(self):
        if not self.jwt:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
