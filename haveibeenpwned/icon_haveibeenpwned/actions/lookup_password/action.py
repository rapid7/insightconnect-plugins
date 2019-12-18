import komand
from .schema import LookupPasswordInput, LookupPasswordOutput, Input, Output
# Custom imports below
import hashlib
from icon_haveibeenpwned.util.util import HaveIBeenPwned


class LookupPassword(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='lookup_password',
            description='Check password for compromise',
            input=LookupPasswordInput(),
            output=LookupPasswordOutput())

    def run(self, params={}):
        hibp = HaveIBeenPwned(self.logger)
        password = params.get(Input.PASSWORD)
        password_is_hash = params.get(Input.ORIGINAL_PASSWORD_IS_A_HASH)

        # The API only needs the first 5 characters of the hash and returns a list of the matching prefixed hashes
        # which this action then reviews for inclusion of the original hash
        if not password_is_hash:
            password = password.encode()
            password = hashlib.sha1(password).hexdigest()  # nosec

        password = password.upper()
        hash_start = password[:5]

        result = hibp.get_password(hash_start=hash_start)

        if password in result:
            return {Output.FOUND: True}
        return {Output.FOUND: False}
