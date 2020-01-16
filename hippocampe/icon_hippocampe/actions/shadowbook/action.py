import komand
from .schema import ShadowbookInput, ShadowbookOutput
# Custom imports below


class Shadowbook(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='shadowbook',
                description='Return the current job ID and status. If the service is indexing at the moment, this action will raise an error',
                input=ShadowbookInput(),
                output=ShadowbookOutput())

    def run(self, params={}):
        job = self.connection.api.shadowbook()
        return {
            'source': job['source'],
            'status': job['status']
        }
