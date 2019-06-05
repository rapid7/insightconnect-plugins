import komand
from .schema import ListSshInput, ListSshOutput
# Custom imports below
import json
import requests


class ListSsh(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_ssh',
                description='List user SSH keys',
                input=ListSshInput(),
                output=ListSshOutput())

    def run(self, params={}):
        r_url = '%s/users/%s/keys' % (self.connection.url, params.get('id'))
        ssh_keys = []

        try:
          r = requests.get(r_url, headers={"PRIVATE-TOKEN": self.connection.token}, verify=False)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
          self.logger.error(e)
          raise Exception(e)
        if r.ok:
          for key in json.loads(json.dumps(r.json())):
            key_obj = {
                "created_at": key['created_at'],
                "id": key['id'],
                "key": key['key'],
                "title": key['title']
            }
            ssh_keys.append(key_obj)

          return {"ssh_keys": ssh_keys}
        raise Exception(r.text)

    def test(self):
        """TODO: Test action"""
        return {}
