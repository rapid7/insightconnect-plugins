import komand
from .schema import DemoteInput, DemoteOutput
# Custom imports below
import requests


class Demote(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='demote',
                description='Demote admin to ordinary user',
                input=DemoteInput(),
                output=DemoteOutput())

    def run(self, params={}):
        # init variables
        api_call = self.connection.api_prefix + '/users/' + params.get('user') + '/site_admin'
        try:
          # Promote user
          response = requests.delete(api_call, 
            verify=False, 
            auth = (self.connection.username, self.connection.secret),
            headers= {'Content-Length': 0})
          if response.headers['Status'].startswith('2'):
            self.logger.info('Demotion successful')
          else:
            self.logger.info('Error occured during demotion: ' + response.headers['Status'])
          return {"status": str(response.headers['Status'])}
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
