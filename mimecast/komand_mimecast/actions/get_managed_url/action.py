import komand
from .schema import GetManagedUrlInput, GetManagedUrlOutput
# Custom imports below
from komand_mimecast.util import util


class GetManagedUrl(komand.Action):
    # URI for create managed url
    _URI = "/api/ttp/url/get-all-managed-urls"

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_managed_url',
                description='Get information on a managed URL',
                input=GetManagedUrlInput(),
                output=GetManagedUrlOutput())

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

        # Mimecast request
        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=url, uri=GetManagedUrl._URI, username=username,
                                                  password=password, auth_type=auth_type,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=None)

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
                'An unhandled error response was received from the Mimecast server. Response: {}'.format(logout_result))

        # Create filter dictionary
        filter_ = {}
        for key, value in params.items():
            temp = util.normalize(key, value)
            filter_.update(temp)

        data = response['data']
        # Create filtered list
        for item in filter_:
            data[:] = [d for d in data if d.get(item) == filter_[item]]

        return {'response': data}
