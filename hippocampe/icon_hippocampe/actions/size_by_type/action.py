import komand
from .schema import SizeByTypeInput, SizeByTypeOutput
# Custom imports below


class SizeByType(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='size_by_type',
                description='Return the size (number of elements) for every type',
                input=SizeByTypeInput(),
                output=SizeByTypeOutput())

    def run(self, params={}):
        sizes = self.connection.api.size_by_type()
        return {'sizes': sizes}
