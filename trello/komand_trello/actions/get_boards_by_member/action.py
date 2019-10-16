import komand
from .schema import GetBoardsByMemberInput, GetBoardsByMemberOutput
# Custom imports below
import json
import urllib
import urllib2
import requests_oauthlib
import requests

class GetBoardsByMember(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_boards_by_member',
                description='Get list of boards by member',
                input=GetBoardsByMemberInput(),
                output=GetBoardsByMemberOutput())

    def run(self, params={}):
        try:
          server  = self.connection.server
          api_key = self.connection.api_key
          token   = self.connection.token

          # Check and add parameter in dictionnary
          data = {}
          if params.get('filter', ""):
            data["filter"] = params.get('filter')

          if params.get('fields', ""):
            data["fields"] = params.get('fields')

          if params.get('actions', ""):
            data["actions"] = params.get('actions')

          if params.get('actions_entities', "") is not None:
            data["actions_entities"] = str(params.get('actions_entities')).lower()

          if params.get('actions_limit', "") and params.get('actions_limit') > 1000:
            data["actions_limit"] =  1000
          else:
            data["actions_limit"] = params.get('actions_limit')

          if params.get('actions_format', ""):
            data["actions_format"] = params.get('actions_format')

          if params.get('actions_since', ""):
            data["actions_since"] = params.get('actions_since')

          if params.get('action_fields', ""):
            data["action_fields"] = params.get('action_fields')

          if params.get('memberships', ""):
            data["memberships"] = params.get('memberships')

          if params.get('organization', "") is not None:
            data["organization"] = str(params.get('organization')).lower()

          if params.get('organization_fields', ""):
            data["organization_fields"] = params.get('organization_fields')

          if params.get('lists', ""):
            data["lists"] = params.get('lists')

          # add api key and token in query string
          data["key"] = api_key
          if token:
            data["token"] = token

          # encode data
          url_values = urllib.urlencode(data)
          url = server + '/member/' + params.get("id_or_name") + '/boards?' + url_values
          # api GetBoardsByMember response array board
          resp = urllib2.urlopen(url)
          # handle decoding json
          try:
            result_dic = json.loads(resp.read())
          except ValueError as e:
            self.logger.error('Decoding JSON Errors:  %s', e)
            raise('Decoding JSON Errors')
          
          return {'result' :result_dic}
        # handle exception
        except urllib2.HTTPError as e:
          self.logger.error('HTTPError: %s for %s', str(e.code), url)
        except urllib2.URLError as e:
          self.logger.error('URLError: %s for %s', str(e.reason), url)
        except Exception:
          import traceback
          self.logger.error('Generic Exception: %s', traceback.format_exc())
        raise Exception('URL Request Failed')

    def test(self):
        http_method = "GET"
        id_or_name = "586e017aed11e154f287d464"
        api_key = '35cc663206a549a44b12a196e8e17554'
        token = '8342ebeaf475ca337bae562abaf68582ebb18f469659440e4199020d108bd46d'

        #  url test authentication
        url = 'https://api.trello.com/1/organizations/' + id_or_name

        # OAuth1 authentication
        oauth = requests_oauthlib.OAuth1(api_key, client_secret=None,
                              resource_owner_key=token, resource_owner_secret=None)

        # perform the HTTP requests, if possible uses OAuth authentication
        response = requests.request(http_method, url,
                                    headers={
                                        'Content-Type': 'application/json'},
                                    auth=oauth)

        if response.status_code == 401:
            raise Exception('Unauthorized: %s (HTTP status: %s)' % (response.text, response.status_code))
        if response.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (response.text, response.status_code))

        return {'status_code': response.status_code}
