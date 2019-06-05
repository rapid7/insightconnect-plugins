import komand
from .schema import PromoteInput, PromoteOutput
# Custom imports below
import requests

class Promote(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='promote',
                description='Promote ordinary user to admin',
                input=PromoteInput(),
                output=PromoteOutput())

    def run(self, params={}):
        # init variables
        api_call = self.connection.api_prefix + '/users/' + params.get('user') + '/site_admin'
        try:
          # Promote user
          response = requests.put(api_call, 
            verify=False, 
            auth = (self.connection.username, self.connection.secret), 
            headers= {'Content-Length': 0})
          if response.headers['Status'].startswith('2'):
            self.logger.info('Promotion successful')
          else:
            self.logger.info('Error occured during promotion: ' + response.headers['Status'])
          return {"status": response.headers['Status']}
        except requests.exceptions.RequestException as e:
          raise e

    def test(self):
      try:
        api_call = self.connection.api_prefix + '/user'
        response = requests.get(api_call, auth = (self.connection.username, self.connection.secret), verify=False)
        if response.status_code == 200:
          return {'status': 'Success'}
      except requests.exceptions.RequestException as e:
        return {'status': 'Error'}
