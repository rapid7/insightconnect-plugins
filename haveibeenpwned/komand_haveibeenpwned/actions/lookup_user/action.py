import komand
from .schema import LookupUserInput, LookupUserOutput
# Custom imports below
from komand_haveibeenpwned.util.util import HaveIBeenPwned


class LookupUser(komand.Action):

    _BASE_URL = 'https://haveibeenpwned.com/api/breachedaccount/'

    def __init__(self):
        super(self.__class__, self).__init__(
            name='lookup_user',
            description='Check username or email for compromise',
            input=LookupUserInput(),
            output=LookupUserOutput())

    def run(self, params={}):
        hibp = HaveIBeenPwned(self.logger)
        user = params.get('user')
        breach = params.get('breach')
        include_unverified = params.get('include_unverified')

        querystring = dict()
        if breach:
            querystring["domain"] = breach
        if include_unverified:
            querystring["includeUnverified"] = include_unverified
        if querystring.keys():
            querystring = None

        url = self._BASE_URL + user

        results = hibp.get_request(url=url, params=querystring)
        if results:
            return {'found': True, 'breaches': results}
        return {'found': False}
