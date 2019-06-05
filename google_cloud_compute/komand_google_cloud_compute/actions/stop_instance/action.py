import komand
from .schema import StopInstanceInput, StopInstanceOutput
# Custom imports below
import json
import urllib2


class StopInstance(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='stop_instance',
                description='Stops a running instance, shutting it down cleanly, and allows you to restart the instance at a later time',
                input=StopInstanceInput(),
                output=StopInstanceOutput())

    def run(self, params={}):
        try:
          server  = self.connection.server
          token   = self.connection.token

          # get path parameter
          project_id = self.connection.project_id
          instance = params.get("instance")
          zone = params.get("zone")

          url = server + '/projects/{0}/zones/{1}/instances/{2}/stop'.format(project_id, zone, instance)
          
          # Call API
          request = urllib2.Request(url, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s'%token})   
          request.get_method = lambda: "POST"

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
        except urllib2.URLError, e:
          self.logger.error('URLError: %s for %s', str(e.reason), url)
        except Exception:
          import traceback
          self.logger.error('Generic Exception: %s', traceback.format_exc())
        raise Exception('URL Request Failed')

    def test(self):
        try:
          token   = self.connection.token
          #  url test authentication
          url = "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={0}".format(token)
          
          # call request test authentication
          request = urllib2.Request(url, headers={'Content-Type': 'application/json'})   
          response = urllib2.urlopen(request)
          
        except urllib2.HTTPError, e:
          message = json.loads(e.read())
          raise Exception('%s (HTTP status: %s)' % (message, str(e.code)))

        return {'status_code': response.getcode()}
