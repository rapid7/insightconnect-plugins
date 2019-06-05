import komand
from .schema import InfoVmInput, InfoVmOutput
# Custom imports below
import urllib2
import requests


class InfoVm(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='info_vm',
                description='Get information about a virtual machine (model view and instance view)',
                input=InfoVmInput(),
                output=InfoVmOutput())

    def run(self, params={}):
        try:
          server  = self.connection.server
          token   = self.connection.token
          apiVersion = self.connection.api_version
               
          # Add request property
          vm = params.get("vm", "")
          mode = params.get("mode", "modelViewAndInstanceView")
          subscriptionId = params.get("subscriptionId", "")
          resourceGroup  = params.get("resourceGroup", "")

          url_dict = {}
          url_dict["modelViewAndInstanceView"] = '/subscriptions/%s/resourceGroups/%s/providers/Microsoft.Compute/virtualMachines/%s?$expand=instanceView&api-version=%s'%(subscriptionId, resourceGroup, vm, apiVersion)
          url_dict["instanceView"] = '/subscriptions/%s/resourceGroups/%s/providers/Microsoft.Compute/virtualMachines/%s/InstanceView?api-version=%s'%(subscriptionId, resourceGroup, vm, apiVersion)
          url_dict["modelView"] = '/subscriptions/%s/resourceGroups/%s/providers/Microsoft.Compute/virtualMachines/%s?api-version=%s'%(subscriptionId, resourceGroup, vm, apiVersion)

          url = server + url_dict[mode]
          
          # New Request Request   
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
          # return {"response":result_dic}
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
