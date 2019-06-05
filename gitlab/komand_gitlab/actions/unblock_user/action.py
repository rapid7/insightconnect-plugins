import komand
from .schema import UnblockUserInput, UnblockUserOutput
# Custom imports below
import requests


class UnblockUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='unblock_user',
                description='Unlock Gitlab user',
                input=UnblockUserInput(),
                output=UnblockUserOutput())

    def run(self, params={}):
        r_url = '%s/users/%s/unblock' % (self.connection.url, params.get('id'))

        try:
          r = requests.post(r_url, headers={'PRIVATE-TOKEN': self.connection.token}, verify=False)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
          self.logger.error(e)
          raise Exception(e)

        return {"status": r.ok}

    def test(self):
        """TODO: Test action"""
        return {}
