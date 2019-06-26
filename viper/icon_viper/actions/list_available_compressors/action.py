import komand
from .schema import ListAvailableCompressorsInput, ListAvailableCompressorsOutput, Input, Output, Component
from ...util import compressor


class ListAvailableCompressors(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_available_compressors',
                description=Component.DESCRIPTION,
                input=ListAvailableCompressorsInput(),
                output=ListAvailableCompressorsOutput())

    def run(self, params={}):
        return {
            Output.COMPRESSORS: compressor.Compressor.all(self.connection.config)
        }
