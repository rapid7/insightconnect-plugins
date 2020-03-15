from domaintools import API
from domaintools.exceptions import NotAuthorizedException

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
        key = params.get(Input.API_KEY).get('secretKey')
        api = API(username, key)

        try:
            response = api.account_information()
            response.data()
        except NotAuthorizedException as e:
            self.logger.error(f'DomainTools: Connect: error {e}')
            raise ConnectionTestException(cause='DomainTools: Connect:',
                                          assistance='Authorization failed. Please try again')
        except Exception as e:
            self.logger.error(f'DomainTools: Connect: error {e}')
            raise ConnectionTestException(cause='DomainTools: Connect:',
                                          assistance=f'Failed to connect to server {e}')

        self.api = api
        phisheye_terms_list = Helper.make_request(api.phisheye_term_list)
        self.terms = []
        for term in phisheye_terms_list.response.terms:
            self.terms.append(term.term)
