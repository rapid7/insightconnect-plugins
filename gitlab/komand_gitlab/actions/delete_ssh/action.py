import komand
from .schema import DeleteSshInput, DeleteSshOutput
# Custom imports below
import requests


class DeleteSsh(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_ssh',
                description='Delete user SSH key',
                input=DeleteSshInput(),
                output=DeleteSshOutput())

    def run(self, params={}):
        r_url = '%s/users/%s/keys/%s' % (self.connection.url, params.get('id'), params.get('key_id'))
        try:
          r = requests.delete(r_url, headers={"PRIVATE-TOKEN": self.connection.token}, verify=False)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
          self.logger.error(e)
          raise Exception(e)
        return {"status": r.ok}

    def test(self):
        """TODO: Test action"""
        return {}
