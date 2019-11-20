import komand
from .schema import AddGroupMemberInput, AddGroupMemberOutput, Input, Output
# Custom imports below
from komand_mimecast.util import util
from komand.exceptions import PluginException


class AddGroupMember(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_group_member',
                description='Add an email address or domain to a group',
                input=AddGroupMemberInput(),
                output=AddGroupMemberOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        uri = self.connection.ADD_GROUP_MEMBER_URI
        access_key = self.connection.access_key
        secret_key = self.connection.secret_key
        app_id = self.connection.app_id
        app_key = self.connection.app_key

        id_ = params.get(Input.ID)
        email = params.get(Input.EMAIL_ADDRESS)
        domain = params.get(Input.DOMAIN)

        if not email and not domain:
            raise PluginException(cause='Invalid input.',
                                  assistance='Email Address and Domain inputs cannot both be blank.')
        if email and domain:
            raise PluginException(cause='Invalid input.',
                                  assistance='Both Email Address and Domain fields cannot be used. Choose either Email Address or Domain.')

        if email:
            data = {'id': id_, 'emailAddress': email}
        else:
            data = {'id': id_, 'domain': domain}

        # Mimecast request
        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=url, uri=uri,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=data)
        output = response['data'][0]

        return {Output.ID: output['id'], Output.FOLDER_ID: output['folderId'],
                Output.EMAIL_ADDRESS: output['emailAddress'], Output.INTERNAL: output['internal']}
