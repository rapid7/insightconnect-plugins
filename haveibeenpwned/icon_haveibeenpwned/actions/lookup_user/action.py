import komand
from .schema import LookupUserInput, LookupUserOutput, Input, Output
# Custom imports below
from icon_haveibeenpwned.util.util import HaveIBeenPwned


class LookupUser(komand.Action):

    _BASE_URL = 'https://haveibeenpwned.com/api/v3/breachedaccount/'

    def __init__(self):
        super(self.__class__, self).__init__(
            name='lookup_user',
            description='Check username or email for compromise',
            input=LookupUserInput(),
            output=LookupUserOutput())

    def run(self, params={}):
        hibp = HaveIBeenPwned(self.logger)
        user = params.get(Input.USER)
        breach = params.get(Input.BREACH)
        include_unverified = params.get(Input.INCLUDE_UNVERIFIED)
        truncate_response = params.get(Input.TRUNCATE_RESPONSE)

        querystring = dict()
        if breach:
            querystring["domain"] = breach
        querystring["includeUnverified"] = include_unverified
        querystring["truncateResponse"] = truncate_response
        if not querystring.keys():
            querystring = None

        url = self._BASE_URL + user

        results = hibp.get_request(url=url, params=querystring, key=self.connection.api_key)
        if results:
            return {Output.FOUND: True, Output.BREACHES: results}
        return {Output.FOUND: False}
