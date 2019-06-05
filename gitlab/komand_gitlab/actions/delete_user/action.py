import komand
from .schema import DeleteUserInput, DeleteUserOutput
# Custom imports below
import requests


class DeleteUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_user',
                description='Delete Gitlab user',
                input=DeleteUserInput(),
                output=DeleteUserOutput())

    def run(self, params={}):
        r_url = '%s/users/%s' % (self.connection.url, params.get('id'))

        try:
          r = requests.delete(r_url, headers={'PRIVATE-TOKEN': self.connection.token}, verify=False)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
          self.logger.error(e)
          raise Exception(e)
        return {"status": False if r.ok else True}

    def test(self):
        """TODO: Test action"""
        return {}
