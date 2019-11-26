import komand
from .schema import PermitOrBlockSenderInput, PermitOrBlockSenderOutput, Output
# Custom imports below
from komand_mimecast.util import util


class PermitOrBlockSender(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='permit_or_block_sender',
                description='Permits or blocks a sender',
                input=PermitOrBlockSenderInput(),
                output=PermitOrBlockSenderOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        uri = self.connection.PERMIT_OR_BLOCK_SENDER_URI
        access_key = self.connection.access_key
        secret_key = self.connection.secret_key
        app_id = self.connection.app_id
        app_key = self.connection.app_key

        # Generate payload dictionary
        data = {}
        for key, value in params.items():
            temp = util.normalize(key, value)
            data.update(temp)

        # Mimecast request
        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=url, uri=uri,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=data)

        return {Output.RESPONSE: response['data']}
