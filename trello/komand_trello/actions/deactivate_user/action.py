import komand
from .schema import DeactivateUserInput, DeactivateUserOutput
# Custom imports below
import json
import urllib2
import requests_oauthlib
import requests


class DeactivateUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='deactivate_user',
                description='Deactivate user',
                input=DeactivateUserInput(),
                output=DeactivateUserOutput())

    def run(self, params={}):
        try:
          """ Get api_key and token from connection """
          server  = self.connection.server
          api_key = self.connection.api_key
          token   = self.connection.token

          data = {}       
          # add id member in data   
          id_member = params.get("id_member", "")   
          data["idMember"] = id_member    

          # add api key and token in dictionary
          data["key"] = api_key   
          if token:   
            data["token"] = token

          data["value"] = params.get("value")

          url = server + '/organizations/' + params.get("id_or_name") + '/members/' + id_member + "/deactivated"

          # new Request Request   
          request = urllib2.Request(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})   
          request.get_method = lambda: "PUT"

          # Call api and response data    
          resp = urllib2.urlopen(request)
          status_code = resp.getcode()

          return {'status_code': status_code}
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
