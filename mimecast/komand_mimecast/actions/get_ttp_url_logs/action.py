import komand
from .schema import GetTtpUrlLogsInput, GetTtpUrlLogsOutput, Input, Output, Component
# Custom imports below
from komand_mimecast.util import util


class GetTtpUrlLogs(komand.Action):

    _URI = '/api/ttp/url/get-logs'

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_ttp_url_logs',
                description=Component.DESCRIPTION,
                input=GetTtpUrlLogsInput(),
                output=GetTtpUrlLogsOutput())

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

        from_ = params.get(Input.FROM)
        to_ = params.get(Input.TO)
        route = params.get(Input.ROUTE)
        scan_result = params.get(Input.SCAN_RESULT)

        data = {'route': route, 'scanResult': scan_result}
        if to_:
            data['to'] = to_
        if from_:
            data['from'] = from_

        # Mimecast request
        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=url, uri=GetTtpUrlLogs._URI, username=username,
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
            output = response['data'][0]['clickLogs']
        except KeyError:
            self.logger.error(response)
            raise Exception('The output from Mimecast was not in the expected format. Please contact support for help')
        return {Output.CLICK_LOGS: output}
