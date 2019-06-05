import komand
from .schema import DeleteFirewallInput, DeleteFirewallOutput
# Custom imports below
import json
import urllib2


class DeleteFirewall(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_firewall',
                description='Deletes the specified firewall',
                input=DeleteFirewallInput(),
                output=DeleteFirewallOutput())

    def run(self, params={}):
        try:
          server  = self.connection.server
          token   = self.connection.token
          
          # add request path parameter
          project_id = self.connection.project_id
          firewall = params.get("firewall", "")

          url = server + '/projects/{0}/global/firewalls/{1}'.format(project_id, firewall)

          # new Request Request   
          request = urllib2.Request(url, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s'%token})   
          request.get_method = lambda: "DELETE"
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
