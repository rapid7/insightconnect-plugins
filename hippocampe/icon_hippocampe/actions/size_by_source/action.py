import komand
from .schema import SizeBySourceInput, SizeBySourceOutput
# Custom imports below


class SizeBySource(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='size_by_source',
                description='Return the size (number of elements) for every source',
                input=SizeBySourceInput(),
                output=SizeBySourceOutput())

    def run(self, params={}):
        sizes = self.connection.api.size_by_source()
        return {'sizes': sizes}
