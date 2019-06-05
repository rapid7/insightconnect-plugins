import komand
from .schema import AddGroupMemberInput, AddGroupMemberOutput, Input, Output
# Custom imports below
from komand_mimecast.util import util


class AddGroupMember(komand.Action):

    _URI = '/api/directory/add-group-member'

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_group_member',
                description='Add an email address or domain to a group',
                input=AddGroupMemberInput(),
                output=AddGroupMemberOutput())

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

        id_ = params.get(Input.ID)
        email = params.get(Input.EMAIL_ADDRESS)
        domain = params.get(Input.DOMAIN)

        if not email and not domain:
            raise Exception('Email Address and Domain inputs can not both be blank')
        if email and domain:
            raise Exception('Both Email Address and Domain fields can not be used. Choose one Email Address or Domain')

        if email:
            data = {'id': id_, 'emailAddress': email}
        else:
            data = {'id': id_, 'domain': domain}

        # Mimecast request
        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=url, uri=AddGroupMember._URI, username=username,
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

        output = response['data'][0]

        return {Output.ID: output['id'], Output.FOLDER_ID: output['folderId'],
                Output.EMAIL_ADDRESS: output['emailAddress'], Output.INTERNAL: output['internal']}
