import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from icon_threatcrowd.util.api import ThreadCrowdAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params={}):
        self.ssl_verification = params.get(Input.SSL_VERIFICATION, True)
        self.client = ThreadCrowdAPI(self.ssl_verification, self.logger)

    def test(self):
        try:
            if self.client.health_check():
                return {"success": True}
            else:
                raise ConnectionTestException(
                    cause="An unexpected error occurred during the API request.",
                    assistance="Check that https://threatcrowd.org is reachable or please contact support.",
                )
        except Exception:
            self.logger.error("An unexpected error occurred during the API request")
            raise ConnectionTestException(
                cause="An unexpected error occurred during the API request.",
                assistance="Check that https://threatcrowd.org is reachable or please contact support.",
            )
