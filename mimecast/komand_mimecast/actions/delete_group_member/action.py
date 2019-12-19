import komand
from .schema import DeleteGroupMemberInput, DeleteGroupMemberOutput, Input, Component
# Custom imports below
from komand_mimecast.util import util
from komand.exceptions import PluginException


class DeleteGroupMember(komand.Action):

    _URI = '/api/directory/remove-group-member'

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_group_member',
                description=Component.DESCRIPTION,
                input=DeleteGroupMemberInput(),
                output=DeleteGroupMemberOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        access_key = self.connection.access_key
        secret_key = self.connection.secret_key
        app_id = self.connection.app_id
        app_key = self.connection.app_key

        group_id = params.get(Input.ID)
        email = params.get(Input.EMAIL_ADDRESS)
        domain = params.get(Input.DOMAIN)

        if not email and not domain:
            raise PluginException(cause='Invalid input.',
                                  assistance='Email Address and Domain inputs cannot both be blank.')
        if email and domain:
            raise PluginException(cause='Invalid input.',
                                  assistance='Both Email Address and Domain fields cannot be used. Choose either Email Address or Domain.')

        data = {}
        if email:
            data = {'id': group_id, 'emailAddress': email}
        else:
            data = {'id': group_id, 'domain': domain}

        # Mimecast request
        mimecast_request = util.MimecastRequests()
        _ = mimecast_request.mimecast_post(url=url, uri=DeleteGroupMember._URI,
                                           access_key=access_key, secret_key=secret_key,
                                           app_id=app_id, app_key=app_key, data=data)

        # if we get here and no mimecast_post() exception was thrown; we are good
        return {'success': True}
