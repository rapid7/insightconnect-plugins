import komand
from .schema import CreateManagedUrlInput, CreateManagedUrlOutput
# Custom imports below
from komand_mimecast.util import util


class CreateManagedUrl(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_managed_url',
                description='Create a managed URL',
                input=CreateManagedUrlInput(),
                output=CreateManagedUrlOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        uri = self.connection.CREATE_MANAGED_URL_URI
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

        return {'response': response['data']}
