import komand
from .schema import FindGroupsInput, FindGroupsOutput, Input, Output, Component
# Custom imports below
from komand_mimecast.util import util


class FindGroups(komand.Action):

    _URI = '/api/directory/find-groups'

    def __init__(self):
        super(self.__class__, self).__init__(
                name='find_groups',
                description=Component.DESCRIPTION,
                input=FindGroupsInput(),
                output=FindGroupsOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        username = self.connection.username
        password = self.connection.password
        access_key = self.connection.access_key
        secret_key = self.connection.secret_key
        app_id = self.connection.app_id
        app_key = self.connection.app_key
        auth_type = self.connection.auth_type

        query = params.get(Input.QUERY)
        source = params.get(Input.SOURCE)
        if query:
            data = {'query': query, 'source': source}
        else:
            data = {'source': source}

        # Mimecast request
        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=url, uri=FindGroups._URI, username=username,
                                                  password=password, auth_type=auth_type,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=data)

        # Logout
        logout = util.Authentication()
        logout_result = logout.logout(url=url, username=username, password=password,
                                      auth_type=auth_type, access_key=access_key,
                                      secret_key=secret_key, app_id=app_id, app_key=app_key)

        try:
            # Test for logout fail
            if logout_result['fail']:
                self.logger.error(logout_result['fail'])
                try:
                    raise Exception(
                        'Could not log out. Contact support for help. Status code is {}, see log for details'.format(
                            response['meta']['status']))
                except KeyError:
                    self.logger.error(response)
                    raise Exception(
                        'Unknown error. The Mimecast server did not respond correctly, see log for details.')

        except KeyError:
            # Unknown key error
            self.logger.error(logout_result)
            raise Exception(
                'Unknown error. The Mimecast server did not respond correctly, see log for details.')
        try:
            output = response['data'][0]['folders']
        except KeyError:
            self.logger.error(response)
            raise Exception('The output from Mimecast was not in the expected format. Please contact support for help')

        return {Output.GROUPS: output}
