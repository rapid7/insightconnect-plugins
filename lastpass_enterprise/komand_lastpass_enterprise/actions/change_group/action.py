import komand
import requests
from .schema import ChangeGroupInput, ChangeGroupOutput


class ChangeGroup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='change_group',
                description='Add or remove a users group',
                input=ChangeGroupInput(),
                output=ChangeGroupOutput())

    def run(self, params={}):
        cid = self.connection.cid
        provhash = self.connection.provhash
        user_name = params.get('user_name')
        groups = params.get('groups')
        action = params.get('action')

        # Use the batchchangegrp command
        cmd = "batchchangegrp"

        # API URL
        url = "https://lastpass.com/enterpriseapi.php"

        # Set headers
        headers = {'content-type': 'application/json'}

        # Initialize data dic
        data = {}

        # Create group list
        if action == "add":
          data['add'] = groups
        else:
          data['del'] = groups
    
        # Add username
        data['username'] = user_name

        # Data should be a list
        data = [data]

        # Set POST data
        post = {'provhash': provhash, 'cid': cid, 'cmd': cmd, 'data': data}

        # Generate request
        response = requests.post(url, json=post, headers=headers)

        try:
            status = response.json().get('status')
        except Exception as e:
            self.logger.error(f"Change group failed.\n"
                              f"Exception was: {e}\n"
                              f"Response was: {response.text}")
            raise e

        # Check status
        if status != "OK":
            self.logger.error(f"Change group failed.\n"                              
                              f"Response was: {response.text}")
            raise Exception('Change group failed.')


        return {'status': status}
