import komand
import requests
from .schema import DeleteRepoInput, DeleteRepoOutput


class DeleteRepo(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_repo',
                description='Delete a Repository',
                input=DeleteRepoInput(),
                output=DeleteRepoOutput())

    def run(self, params={}):
      try:
        api_call = self.connection.base_api + '/repositories/' + self.connection.username + '/' + params.get('title').lower()
        repo = self.connection.bucket_session.delete(api_call)  
        if repo.status_code == 204:
          self.logger.info('Run:Repo Successfully deleted')
          return {'status': 'Success'}
        else:
          repo_obj = repo.json()
          return {'status': repo_obj['error']['message']}

      except requests.exceptions.RequestException as e:
        raise e

    def test(self):
      try:
        api_call = self.connection.base_api + '/user'
        response = self.connection.bucket_session.get(api_call)
        if response.status_code == 200:
          return {'status': 'Success - api 2.0 still works'}
      except requests.exceptions.RequestException as e:
        return {'status': 'Error'}
