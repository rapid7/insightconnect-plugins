import komand
from .schema import CreateScanInput, CreateScanOutput, Component
# Custom imports below


class CreateScan(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_scan',
                description=Component.DESCRIPTION,
                input=CreateScanInput(),
                output=CreateScanOutput())

    def run(self, params={}):
        return self.connection.client.create_scan(params)
