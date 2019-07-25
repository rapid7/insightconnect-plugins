import komand
from .schema import ListAvailableExtractorsInput, ListAvailableExtractorsOutput, Input, Output, Component
from ...util import extractor


class ListAvailableExtractors(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_available_extractors',
                description=Component.DESCRIPTION,
                input=ListAvailableExtractorsInput(),
                output=ListAvailableExtractorsOutput())

    def run(self, params={}):
        return {
            Output.EXTRACTORS: extractor.Extractor.all(self.connection.config)
        }
