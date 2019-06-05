import komand
from .schema import BlockUserInput, BlockUserOutput
# Custom imports below
import requests
import urllib.parse


class BlockUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='block_user',
                description='Block a user',
                input=BlockUserInput(),
                output=BlockUserOutput())

    def run(self, params={}):
        url = requests.compat.urljoin(self.connection.api_prefix, '/user/blocks/' + urllib.parse.quote(params.get('username')))
        headers = {
            'Accept': 'application/vnd.github.giant-sentry-fist-preview+json',
            'Content-Type': 'application/json',
        }

        response = requests.put(url, headers=headers, auth=(self.connection.username, self.connection.secret))

        try:
            data = response.json()
        except ValueError:
            if response.status_code == 204:
                self.logger.info('Successfully blocked user')
                return { 'success': True }

        return { 'success': False }
