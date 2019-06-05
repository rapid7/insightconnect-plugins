import komand
import json
import requests
from .schema import ProvisionUserInput, ProvisionUserOutput


class ProvisionUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='provision_user',
                description='Provision new user or change exisiting user',
                input=ProvisionUserInput(),
                output=ProvisionUserOutput())

    def run(self, params={}):
        cid = self.connection.cid
        provhash = self.connection.provhash
        user_name = params.get('user_name')
        full_name = params.get('full_name')
        groups = params.get('groups')
        password = params.get('password')
        password_reset_required = params.get('password_reset_required')

        #Use the batchadd command
        cmd = "batchadd"

        # API URL
        url = "https://lastpass.com/enterpriseapi.php"

        # Set headers
        headers = {'content-type': 'application/json'}

        # Initialize data dic
        data = {}

        # Create group list
        if groups:
          data['groups'] = groups
    
        # Add username
        data['username'] = user_name

        # Add fullname
        if full_name:
          data['fullname'] = full_name
  
        # Add password
        if password:
          data['password'] = password
          data['password_reset_required'] = password_reset_required

        # Data should be a list
        data = [data]

        # Set POST data
        post = {
            'provhash': provhash,
            'cid': cid,
            'cmd': cmd,
            'data': data
        }

        self.logger.info(post)

        # Generate request
        response = requests.post(url, json=post, headers=headers)

        # Get status
        try:
            status = response.json().get('status')
        except Exception as e:
            self.logger.error(f"Provision user failed.\n"
                              f"Exception was: {e}\n"
                              f"Response was: {response.text}")
            raise e

        # Check status
        if status != "OK":
            self.logger.error(f"Provision user failed.\n"                              
                              f"Response was: {response.text}")
            raise Exception('Provision user failed.')

        return {'status': status}