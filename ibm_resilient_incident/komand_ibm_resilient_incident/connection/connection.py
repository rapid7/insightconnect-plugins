import komand
import json
import requests
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    API_BASE = None
    SESSION = None

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):

        email = params.get("creds").get("username")
        password = params.get("creds").get("password")

        hostname = params.get("hostname")
        self.API_BASE = hostname + "/rest"

        session_endpoint = self.API_BASE + "/session"

        self.SESSION = requests.Session()
        self.SESSION.headers.update({"content-type": "application/json"})
        self.SESSION.verify = False

        # Fill out payload with creds
        auth_payload = {
            "email": email,
            "password": password,
            "interactive": False
        }

        auth_payload = json.dumps(auth_payload)

        self.logger.info("Authenticating to %s..." % hostname)

        try:
            response = self.SESSION.post(url=session_endpoint, data=auth_payload, verify=False)
            csrf_token = response.json()["csrf_token"]
            self.SESSION.headers.update({"X-sess-id": csrf_token})
            self.logger.info("Authentication successful!")
        except BaseException as error:
            self.logger.error(error)
            raise
