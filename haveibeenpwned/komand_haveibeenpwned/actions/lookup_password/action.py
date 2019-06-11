import komand
from .schema import LookupPasswordInput, LookupPasswordOutput
# Custom imports below
import hashlib
from komand_haveibeenpwned.util.util import HaveIBeenPwned


class LookupPassword(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='lookup_password',
            description='Check password for compromise',
            input=LookupPasswordInput(),
            output=LookupPasswordOutput())

    def run(self, params={}):
        hibp = HaveIBeenPwned(self.logger)
        password = params.get('password')
        password_is_hash = params.get('original_password_is_a_hash')

        if not password_is_hash:
            password = password.encode()
            password = hashlib.sha1(password).hexdigest()

        password = password.upper()
        hash_start = password[:5]

        result = hibp.get_password(hash_start=hash_start)

        if password in result:
            return {'found': True}
        return {'found': False}
