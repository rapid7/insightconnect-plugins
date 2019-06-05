import komand
from .schema import VmInSubscriptionInput, VmInSubscriptionOutput
# Custom imports below
import urllib2
import requests


class VmInSubscription(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='vm_in_subscription',
                description='Lists the virtual machines in a subscription',
                input=VmInSubscriptionInput(),
                output=VmInSubscriptionOutput())

    def run(self, params={}):
        try:
          server  = self.connection.server
          token   = self.connection.token
          apiVersion = self.connection.api_version

          # Add request property
          subscriptionId  = params.get("subscriptionId", "")

          url = server + '/subscriptions/%s/providers/Microsoft.Compute/virtualmachines?api-version=%s'%(subscriptionId, apiVersion)

          # New Request   
          request = urllib2.Request(url, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s'%token})   
          
          # Call API and response data    
          resp = urllib2.urlopen(request)
          
          # Handle decoding json
          try:
            result_dic = json.loads(resp.read())
          except ValueError as e:
            self.logger.error('Decoding JSON Errors:  %s', e)
            raise('Decoding JSON Errors')

          return result_dic
        # Handle exception
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
        version = "2017-03-01"

        # URL test authentication
        url = server + '/subscriptions?api-version=%s'%version
        
        # Call request test authentication
        response = requests.request(http_method, url,
                                    headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s'%token})

        if response.status_code == 401:
            raise Exception('Unauthorized: %s (HTTP status: %s)' % (response.text, response.status_code))
        if response.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (response.text, response.status_code))

        return {'status_code': response.status_code}
