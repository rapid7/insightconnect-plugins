import komand
import requests
from .schema import AddUserInput, AddUserOutput


class AddUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_user',
                description='Add Cloud Node user',
                input=AddUserInput(),
                output=AddUserOutput())

    def run(self, params={}):
        url  = self.connection.url + '/admin/add-user'
        data = self.connection.data
        data['user_email'] = params.get('user_email')
        data['user_name'] = params.get('user_name')
        data['user_role'] = params.get('user_role')
        try:
            resp = requests.post(headers=self.connection.headers, json=data, url=url)
            if resp.status_code == 200:
                r = resp.json()
                r['success'] = True
                if 'message' not in r.keys():
                    r['message'] = 'User created'
                return r
            else:
                return { 'message': resp.json()['message'], 'success': False }
        except: 
            self.logger.error('An error occurred during the API request')
            raise

    def test(self):
        url  = self.connection.url + '/get-indicators'
        try:
            resp = requests.get(headers=self.connection.headers, url=url)
            if resp.status_code == 200:
                return { 'message': 'Testing API request', 'success': True }
        except: 
            self.logger.error('An error occurred during the API request')
            raise
