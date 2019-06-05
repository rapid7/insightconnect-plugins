import komand
from .schema import SaveImageVmInput, SaveImageVmOutput
# Custom imports below
import urllib2
import requests
import json


class SaveImageVm(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='save_image_vm',
                description='Save an image of a virtual machine',
                input=SaveImageVmInput(),
                output=SaveImageVmOutput())

    def run(self, params={}):
        try:
            server = self.connection.server
            token = self.connection.token
            apiVersion = self.connection.api_version

            data = {}       
            # Get request parameter
            vm = params.get("vm", "")
            subscriptionId = params.get("subscriptionId", "")
            resourceGroup = params.get("resourceGroup", "")

            vhdPrefix = params.get("vhdPrefix", "")
            destinationContainerName = params.get("destinationContainerName", "")
            overwriteVhds = params.get("overwriteVhds", "")

            data["vhdPrefix"] = vhdPrefix
            data["destinationContainerName"] = destinationContainerName
            data["overwriteVhds"] = overwriteVhds

            url = server + '/subscriptions/%s/resourceGroups/%s/providers/Microsoft.Compute/virtualMachines/%s/capture?api-version=%s'%(subscriptionId, resourceGroup, vm, apiVersion)
          
            # New Request Request   
            request = urllib2.Request(url, data=json.dumps(data), headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s'%token})   
          
            # Call API and response data
            resp = urllib2.urlopen(request)
            status_code = resp.getcode()

            return {'status_code': status_code}
          
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

        #  URL test authentication
        url = server + '/subscriptions?api-version=%s'%version
        
        # Call request test authentication
        response = requests.request(http_method, url,
                                    headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s'%token})

        if response.status_code == 401:
            raise Exception('Unauthorized: %s (HTTP status: %s)' % (response.text, response.status_code))
        if response.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (response.text, response.status_code))

        return {'status_code': response.status_code}
