import komand
from .schema import ConnectionSchema, Input
# Custom imports below
from komand.exceptions import ConnectionTestException
from requests import Session
from requests.auth import HTTPBasicAuth
from json import JSONDecodeError


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.session, self.url = None, None

    def connect(self, params={}):
        username, password = params.get(Input.USERNAME_PASSWORD).get("username"), \
                             params.get(Input.USERNAME_PASSWORD).get("password")

        self.url = params.get(Input.URL)

        self.session: Session = Session()
        self.session.auth = HTTPBasicAuth(username=username,
                                          password=password)

    def test(self):
        test_url = f"{self.url}/hx/api/v3/version"
        response = self.session.get(url=test_url)

        if response.status_code == 200:
            return {"status": "success"}
        else:
            try:
                details = response.json()["details"][0]
                code, message = details["code"], details["message"]

                raise ConnectionTestException(cause=f"Reason: {message} (error code {code}")

            except JSONDecodeError as e:
                raise ConnectionTestException(cause=f"Malformed response received from FireEye HX appliance. "
                                                    f"Got: {response.text}") from e
            except (KeyError, IndexError) as e:
                raise ConnectionTestException(cause="Unknown error received from FireEye HX appliance "
                                                    "(no error cause reported).") from e
