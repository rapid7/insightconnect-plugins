import komand
from .schema import ShowUserInput, ShowUserOutput
# Custom imports below
from newrelic_api import users


class ShowUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='show_user',
                description='Returns a single user, identified by ID',
                input=ShowUserInput(),
                output=ShowUserOutput())

    def run(self, params={}):
        api_key = self.connection.api_key
        user_id = params.get('id')
        user_found = True

        try:
            request = users.Users(api_key=api_key)
            response = request.show(user_id)
            temp = response['user']
        except KeyError:
            if 'error' in response:
                user_found = False
                self.logger.error(response)
                return {'user_found': user_found}
            raise Exception('something went wrong')

        return {'user_found': user_found, 'user_information': response}

    def test(self):
        try:
            request = users.Users(api_key=self.connection.api_key)
            response = request.list()
            temp = response['users']
        except KeyError:
            raise Exception(response)
        return {}
