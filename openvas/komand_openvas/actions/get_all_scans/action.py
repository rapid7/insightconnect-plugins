import komand
from .schema import GetAllScansInput, GetAllScansOutput
# Custom imports below


class GetAllScans(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_all_scans',
                description='Get a list of all scans in the OpenVAS server',
                input=GetAllScansInput(),
                output=GetAllScansOutput())

    def run(self, params={}):
        allScanDict = self.connection.scanner.get_all_scans
        returnList = []
        for key, value in allScanDict.iteritems():
            scanDict = {key: value}
            returnList.append(scanDict)
        return {'list_scans': returnList, 'success': True, 'message': 'Successfully obtained list of all scans'}

    def test(self):
        # TODO: Implement test function
        return {}
