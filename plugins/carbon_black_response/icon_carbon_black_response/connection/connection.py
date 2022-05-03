import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below
import os
import contextlib
from cbapi.response import CbEnterpriseResponseAPI
from cbapi.errors import ApiError, UnauthorizedError
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


@contextlib.contextmanager
def temp_umask(umask):
    oldmask = os.umask(umask)
    try:
        yield
    finally:
        os.umask(oldmask)


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.carbon_black = None
        self.connection_test_passed = False

    def connect(self, params={}):
        """Connect uses the carbon black credentials to get the latest api token for the user"""
        url = params.get("url")
        token = params.get("api_key").get("secretKey")
        ssl_verify = params.get("ssl_verify")

        try:
            self.carbon_black = CbEnterpriseResponseAPI(
                url=url, token=token, ssl_verify=ssl_verify, max_retries=2
            )  # Two retries to speed up a likely failure
        except UnauthorizedError as e:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY) from e
        except ApiError as e:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.NOT_FOUND) from e
        else:
            self.connection_test_passed = True

    def test(self):
        return self.connection_test_passed
