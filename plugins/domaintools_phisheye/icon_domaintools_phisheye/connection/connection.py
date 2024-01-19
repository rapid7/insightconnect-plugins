from domaintools import API
from domaintools.exceptions import NotAuthorizedException

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException

from .schema import ConnectionSchema, Input
from icon_domaintools_phisheye.util.helper import Helper


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None
        self.terms = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        username = params.get(Input.USERNAME)
        key = params.get(Input.API_KEY).get("secretKey")
        self.api = API(username, key)

        try:
            response = self.api.account_information()
            response.data()
        except NotAuthorizedException:
            raise ConnectionTestException(
                cause="Authorization failed.",
                assistance="Double-check that your credentials configured in your connection are correct and try again.",
            )
        except Exception as error:
            raise ConnectionTestException(
                cause="Unable to connect to DomainTools.", assistance=f"Exception was: {error}"
            )

        phisheye_terms_list = Helper.make_request(self.api.phisheye_term_list, self.logger)
        self.terms = []
        for term in phisheye_terms_list.get("response").get("terms"):
            self.terms.append(term.get("term"))

    def test(self):
        try:
            Helper.make_request(self.api.phisheye_term_list, self.logger)
            return {}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
