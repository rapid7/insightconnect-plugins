import komand
from .schema import DeleteManagedUrlInput, DeleteManagedUrlOutput, Input, Output, Component
# Custom imports below
from komand_mimecast.util import util


class DeleteManagedUrl(komand.Action):
    _URI = '/api/ttp/url/delete-managed-url'

    def __init__(self):
        super(self.__class__, self).__init__(
            name='delete_managed_url',
            description=Component.DESCRIPTION,
            input=DeleteManagedUrlInput(),
            output=DeleteManagedUrlOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        access_key = self.connection.access_key
        secret_key = self.connection.secret_key
        app_id = self.connection.app_id
        app_key = self.connection.app_key

        id_to_remove = params.get('id')
        if id_to_remove:
            # Mimecast request, only if there is an ID to remove
            mimecast_request = util.MimecastRequests()
            response = mimecast_request.mimecast_post(url=url, uri=DeleteManagedUrl._URI,
                                                      access_key=access_key, secret_key=secret_key,
                                                      app_id=app_id, app_key=app_key, data={'id': id_to_remove})


        return {'success': True}
