import komand
import json
from .schema import CreateRepoInput, CreateRepoOutput


class CreateRepo(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_repo',
                description='Create a Repository',
                input=CreateRepoInput(),
                output=CreateRepoOutput())

    def clean_json(self, obj):
      new_json = []
      for key, value in obj.items():
        if value is None: 
          value = ''
        new_json.append((key, value))
      output = json.dumps(dict(new_json))
      return json.loads(output)

    def run(self, params={}):
      repo_name = params.get('title').lower()
      try:
        repository = {
            'has_issues': params.get('has_issues'), # default False
            'is_private': params.get('is_private'), # default False
            'scm': params.get('type').lower(), # hg or git default git 
            'description': params.get('description'),
            'has_wiki': params.get('has_wiki')
        }
        self.connection.bucket_session.headers.update({'Content-Type': 'application/json'})
        api_call = self.connection.base_api + '/repositories/' + self.connection.username + '/' + repo_name
        repo = self.connection.bucket_session.post(api_call, data = json.dumps(repository))
        repo_obj = repo.json()
        try:
          repo_info = self.clean_json({
              'name': repo_obj['name'],
              'git clone': repo_obj['links']['clone'][0]['href'],
              'url': repo_obj['links']['html']['href']        
              })
          return {'repository': repo_info}
        except:
          return {"status": repo_obj['error']['message']}

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
