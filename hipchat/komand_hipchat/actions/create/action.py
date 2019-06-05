import komand
from .schema import CreateInput, CreateOutput
# Custom imports below
import json
import urllib2
import requests


class Create(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='create',
                description='Creates a new user',
                input=CreateInput(),
                output=CreateOutput())

    def run(self, params={}):
        try:
          server  = self.connection.server
          token   = self.connection.token
          data = {}       
          # add request property
          name  = params.get("name", "")
          email = params.get("email", "")
          roles = params.get("roles", "")
          title = params.get("title", "")
          timezone = params.get("timezone", "")
          password = params.get("password", "")
          mention_name   = params.get("mention_name", "")
          is_group_admin = params.get("is_group_admin", "")

          data["name"] = name
          data["email"] = email
          data["is_group_admin"] = is_group_admin

          if roles:
            data["roles"] = roles
          if title:
            data["title"] = title
          if timezone:
            data["timezone"] = timezone
          if password:
            data["password"] = password
          if mention_name:
            data["mention_name"] = mention_name

          url = server + '/user'

          # new Request Request   
          request = urllib2.Request(url, data=json.dumps(data), headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s'%token})   
          
          # Call api and response data    
          resp = urllib2.urlopen(request)
          
          # handle decoding json
          try:
            result_dic = json.loads(resp.read())
          except ValueError as e:
            self.logger.error('Decoding JSON Errors:  %s', e)
            raise('Decoding JSON Errors')

          return result_dic
        # handle exception
        except urllib2.HTTPError, e:
          self.logger.error('HTTPError: %s for %s', str(e.code), url)
          message = json.loads(e.read())["error"]["message"]
          self.logger.error('HTTPError Reason: %s'%message)
          raise Exception(message)
        except urllib2.URLError, e:
          self.logger.error('URLError: %s for %s', str(e.reason), url)
        except Exception:
          import traceback
          self.logger.error('Generic Exception: %s', traceback.format_exc())
        raise Exception('URL Request Failed')

    def test(self):
        http_method = "GET"
        server  = self.connection.server
        token   = self.connection.token

        #  url test authentication
        url = server + '/room'
        
        # call request test authentication
        response = requests.request(http_method, url,
                                    headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s'%token})

        if response.status_code == 401:
            raise Exception('Unauthorized: %s (HTTP status: %s)' % (response.text, response.status_code))
        if response.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (response.text, response.status_code))

        return {'status_code': response.status_code}
