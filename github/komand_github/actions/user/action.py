import komand
import json
import github
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
      g_user = github.Github()
      user_info = g_user.get_user(params.get('username'))
      user = {'avatar': user_info.avatar_url, 'bio': user_info.bio, 'email': user_info.email, 'name': user_info.name, 'url': user_info.html_url}
      return self.clean_json(user)
