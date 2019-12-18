import komand
from .schema import SourcesInput, SourcesOutput
# Custom imports below


class Sources(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='sources',
                description='Return all the known sources with their metadata',
                input=SourcesInput(),
                output=SourcesOutput())

    def run(self, params={}):
        sources = self.connection.api.sources()
        return {'sources': sources}
