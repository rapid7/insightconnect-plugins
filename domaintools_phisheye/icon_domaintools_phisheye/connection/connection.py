from domaintools import API
from domaintools.exceptions import NotAuthorizedException
from komand.exceptions import PluginException

import komand
from komand.exceptions import ConnectionTestException
from .schema import ConnectionSchema, Input
from icon_domaintools_phisheye.util.helper import Helper


class Connection(komand.Connection):
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
        except NotAuthorizedException as e:
            raise ConnectionTestException(cause="Authorization failed.",
                                          assistance="Double-check that your credentials configured in your connection are correct and try again.")
        except Exception as e:
            raise ConnectionTestException(cause="Unable to connect to DomainTools.",
                                          assistance=f"Exception was: {e}")

        phisheye_terms_list = Helper.make_request(self.api.phisheye_term_list, self.logger)
        self.terms = []
        for term in phisheye_terms_list.get("response").get("terms"):
            self.terms.append(term.get("term"))

    def test(self):
        try:
            Helper.make_request(self.api.phisheye_term_list, self.logger)
            return {}
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e.data)
