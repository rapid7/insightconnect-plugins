import komand
from .schema import GetManagedUrlInput, GetManagedUrlOutput
# Custom imports below
from komand_mimecast.util import util


class GetManagedUrl(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_managed_url',
                description='Get information on a managed URL',
                input=GetManagedUrlInput(),
                output=GetManagedUrlOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        uri = self.connection.GET_MANAGED_URL_URI
        access_key = self.connection.access_key
        secret_key = self.connection.secret_key
        app_id = self.connection.app_id
        app_key = self.connection.app_key

        # Mimecast request
        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=url, uri=uri,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=None)

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
