import komand
from .schema import DiskSnapshotInput, DiskSnapshotOutput
# Custom imports below
import json
import urllib2


class DiskSnapshot(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='disk_snapshot',
                description='Creates a snapshot of a specified persistent disk',
                input=DiskSnapshotInput(),
                output=DiskSnapshotOutput())

    def run(self, params={}):
        try:
          server  = self.connection.server
          token   = self.connection.token
          
          # add request path parameter
          project_id = self.connection.project_id
          zone = params.get("zone", "")
          disk = params.get("disk", "")

          # add request body parameter
          data = {}
          data['kind'] = params.get("kind", "")
          data['name'] = params.get("name", "")

          if params.get("id", ""):
            data["id"] = params.get("id", "")
          if params.get("description", ""):
            data["description"] = params.get("description", "")
          if params.get("status", ""):
            data["status"] = params.get("status", "")
          if params.get("creationTimestamp", ""):
            data["creationTimestamp"] = params.get("creationTimestamp", "")
          if params.get("diskSizeGb", ""):
            data["diskSizeGb"] = params.get("diskSizeGb", "")
          if params.get("licenses", ""):
            data["licenses"] = params.get("licenses", "")
          if params.get("selfLink", ""):
            data["selfLink"] = params.get("selfLink", "")

          snapshotEncryptionKey = params.get("snapshotEncryptionKey")
          if any(snapshotEncryptionKey.values()):
            data["snapshotEncryptionKey"] = snapshotEncryptionKey
          
          sourceDiskEncryptionKey = params.get("sourceDiskEncryptionKey")
          if any(sourceDiskEncryptionKey.values()):
            data["sourceDiskEncryptionKey"] = sourceDiskEncryptionKey

          url = server + '/projects/{0}/zones/{1}/disks/{2}/createSnapshot'.format(project_id, zone, disk)

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
