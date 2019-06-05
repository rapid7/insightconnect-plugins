import komand
import json
import requests
from .schema import UserInput, UserOutput


class User(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='user',
                description='Get user information',
                input=UserInput(),
                output=UserOutput())

    def clean_json(self, obj):
      new_json = []
      for key, value in obj.items():
        if value is None: 
          value = ''
        new_json.append((key, value))
      output = json.dumps(dict(new_json))
      return json.loads(output)

    def run(self, params={}):
      try:
        user_info = {}
        self.connection.bucket_session.headers.update({'Content-Type': 'application/json'})
        user = self.connection.bucket_session.get(self.connection.base_api + '/users/' + params.get('username'))
        user_obj = user.json()
        if user.status_code == 200:
          user_info = self.clean_json({
              'username': user_obj['username'],
              'url': 'https://bitbucket.org/' + params.get('username'),
              'display name': user_obj['display_name'],
              'website': user_obj['website'],
              'location': user_obj['location']
              })
          return {'user': user_info}
        return {'status': user_obj['error']['message']}
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
