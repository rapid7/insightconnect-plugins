import komand
from .schema import GetUserInput, GetUserOutput, Component
# Custom imports below
import requests

class GetUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_user',
                description=Component.DESCRIPTION,
                input=GetUserInput(),
                output=GetUserOutput())

    def run(self, params={}):
        client = self.connection.client
        user_id = params.get('id')

        if user_id:
            url = '{}/api/user/{}'.format(client.url, user_id)
        else:
            url = '{}/api/user/current'.format(client.url)

        try:
            user = requests.get(url, auth=(self.connection.username, self.connection.password), verify=self.connection.verify)
            user.raise_for_status()
        except requests.exceptions.HTTPError:
            self.logger.error(user.json())
            raise
        except:
            self.logger.error('Failed to get user')
            raise

        return user.json()
