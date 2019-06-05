import komand
from .schema import ListUsersInput, ListUsersOutput
# Custom imports below
from newrelic_api import users


class ListUsers(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_users',
                description='Show a paginated list of all users. Users can be filtered by their IDs or email',
                input=ListUsersInput(),
                output=ListUsersOutput())

    def run(self, params={}):
        api_key = self.connection.api_key
        email = params.get('email')
        user_id = params.get('user_id')

        if user_id is not None:
            user_list = [int(x) for x in user_id.split(',')]
            request = users.Users(api_key=api_key)
            response = request.list(filter_email=email, filter_ids=user_list)
            return {'message': response}

        request = users.Users(api_key=api_key)

        response = request.list(filter_email=email)

        return {'user_list': response['users']}

    def test(self):
        try:
            request = users.Users(api_key=self.connection.api_key)
            response = request.list()
            temp = response['users']
        except KeyError:
            raise Exception(response)
        return {}
