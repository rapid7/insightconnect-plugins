import komand
import requests
from komand_bitbucket.util import helpers
from .schema import UserInput, UserOutput, Input, Output, Component
from komand.exceptions import PluginException


class User(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='user',
            description=Component.DESCRIPTION,
            input=UserInput(),
            output=UserOutput())

    def run(self, params={}):
        try:
            self.connection.bucket_session.headers.update({'Content-Type': 'application/json'})
            user = self.connection.bucket_session.get(f'{self.connection.base_api}/users/{params.get(Input.USERNAME)}')
            user_obj = user.json()
            if user.status_code == 200:
                user_info = helpers.clean_json({
                    'username': user_obj['username'] if 'username' in user_obj else params.get(Input.USERNAME),
                    'url': 'https://bitbucket.org/' + params.get(Input.USERNAME),
                    'display name': user_obj['display_name'] if 'display_name' in user_obj else '',
                    'website': user_obj['website'] if 'website' in user_obj else '',
                    'location': user_obj['location'] if 'location' in user_obj else ''
                })
                return {Output.USER: user_info}

            return {'error': user_obj['error']['message']}
        except requests.exceptions.RequestException as e:
            raise PluginException(
                cause='User repository error',
                data=e
            )
