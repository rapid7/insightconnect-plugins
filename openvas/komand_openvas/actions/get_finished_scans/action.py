import komand
from .schema import GetFinishedScansInput, GetFinishedScansOutput
# Custom imports below


class GetFinishedScans(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_finished_scans',
                description='Get a list of all finished scans',
                input=GetFinishedScansInput(),
                output=GetFinishedScansOutput())

    def run(self, params={}):
        finishedScanDict = self.connection.scanner.get_finished_scans
        returnList = []
        for key, value in finishedScanDict.iteritems():
            scanDict = {key: value}
            returnList.append(scanDict)
        return {'list_scans': returnList, 'success': True, 'message': 'Successfully obtained list of finished scans'}

    def test(self):
        # TODO: Implement test function
        return {}
