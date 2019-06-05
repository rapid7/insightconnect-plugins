import komand
import requests
from .schema import DeprovisionUserInput, DeprovisionUserOutput


class DeprovisionUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='deprovision_user',
                description='remove user',
                input=DeprovisionUserInput(),
                output=DeprovisionUserOutput())

    def run(self, params={}):
        cid = self.connection.cid
        provhash = self.connection.provhash
        user_name = params.get('user_name')
        delete_action = params.get('delete_action')
        
        # Use the deluser command
        cmd = "deluser"

        # API URL
        url = "https://lastpass.com/enterpriseapi.php"

        # Set headers
        headers = {'content-type': 'application/json'}

        # Initialize data dic
        data = {}

        # Add username
        data['username'] = user_name

        # Add deleteaction
        if delete_action == "deactivate":
          delete_action = 0
        elif delete_action == "remove":
          delete_action = 1
        else:
          delete_action = 2

        data['deleteaction'] = delete_action

        # Set POST data
        post = {'provhash': provhash, 'cid': cid, 'cmd': cmd, 'data': data}

        # Generate request
        response = requests.post(url, json=post, headers=headers)

        try:
            status = response.json().get('status')
        except Exception as e:
            self.logger.error(f"Deprovision user failed.\n"
                              f"Exception was: {e}"
                              f"Response was: {response.text}")
            raise e

        # Check status
        if status != "OK":
            self.logger.error(f"Deprovision user failed.\n"                              
                              f"Response was: {response.text}")
            raise Exception('Deprovision user failed.')

        return {'status': status}