import komand
from .schema import GetUserInput, GetUserOutput
# Custom imports below
import json
import requests


class GetUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_user',
                description='Get Gitlab user',
                input=GetUserInput(),
                output=GetUserOutput())

    def run(self, params={}):
        r_url = '%s/users/%s' % (self.connection.url, params.get('id'))

        try:
          r = requests.get(r_url, headers={"PRIVATE-TOKEN": self.connection.token}, verify=False)
          if not r.ok:
            self.logger.error("Run: Error: ID Does not exist")
            raise Exception("Run: Error: ID Does not exist")
            return
          u = json.loads(json.dumps(r.json()))
          user_obj = {
            "avatar_url": u['avatar_url'] or "None",
            "bio": u['bio'] or "None",
            "created_at": u['created_at'] or "None",
            "id": u['id'] or -1,
            "linkedin": u['linkedin'] or "None",
            "location": u['location'] or "None",
            "name": u['name'] or "None",
            "organization": u['organization'] or "None",
            "skype": u['skype'] or "None",
            "state": u['state'] or "None",
            "twitter": u['twitter'] or "None",
            "username": u['username'] or "None",
            "web_url": u['web_url'] or "None",
            "website_url": u['website_url'] or "None"
          }
        except requests.exceptions.RequestException as e:  # This is the correct syntax
          self.logger.error(e)
          raise Exception(e)
          
        return user_obj

    def test(self):
        """TODO: Test action"""
        return {}
