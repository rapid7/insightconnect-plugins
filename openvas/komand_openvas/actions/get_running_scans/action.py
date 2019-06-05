import komand
from .schema import GetRunningScansInput, GetRunningScansOutput
# Custom imports below


class GetRunningScans(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_running_scans',
                description='Get a list of all currently running scans',
                input=GetRunningScansInput(),
                output=GetRunningScansOutput())

    def run(self, params={}):
        runningScanDict = self.connection.scanner.get_running_scans
        returnList = []
        for key, value in runningScanDict.iteritems():
            scanDict = {key: value}
            returnList.append(scanDict)
        return {'list_scans': returnList, 'success': True, 'message': 'Successfully obtained list of running scans'}

    def test(self):
        # TODO: Implement test function
        return {}
