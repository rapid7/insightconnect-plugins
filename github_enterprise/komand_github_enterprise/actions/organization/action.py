import komand
from .schema import OrganizationInput, OrganizationOutput
# Custom imports below
import requests


class Organization(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='organization',
                description='Create organization in enterprise',
                input=OrganizationInput(),
                output=OrganizationOutput())

    def run(self, params={}):
        # init variables
        api_call = self.connection.api_prefix + '/admin/organizations'
        try:
          # Create organization
          response = requests.post(api_call, 
            verify=False, 
            auth = (self.connection.username, self.connection.secret),
            json = {
                'login': params.get('name'), 
                'admin': params.get('admin'),
                'profile_name': params.get('profile_name')
                }
            )
          if response.status_code == 404:
            self.logger.info('Must be admin to create Organization')
          if response.status_code == 422:
            self.logger.info('Organization already exsist')
          if str(response.status_code).startswith('2') :
            self.logger.info('Organization created: ')
          else:
            self.logger.info('Error occured during Creation: ' + response.headers['Status'])
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
