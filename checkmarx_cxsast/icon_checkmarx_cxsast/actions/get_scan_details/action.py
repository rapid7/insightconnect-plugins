import komand
from .schema import GetScanDetailsInput, GetScanDetailsOutput, Component
# Custom imports below


class GetScanDetails(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_scan_details',
                description=Component.DESCRIPTION,
                input=GetScanDetailsInput(),
                output=GetScanDetailsOutput())

    def run(self, params={}):
        scan = self.connection.client.get_scan_details(params.get("id"))
        return {"scan": komand.helper.clean(scan)}
