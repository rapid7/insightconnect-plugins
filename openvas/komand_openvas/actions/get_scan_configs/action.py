import komand
from .schema import GetScanConfigsInput, GetScanConfigsOutput
# Custom imports below


class GetScanConfigs(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_scan_configs',
                description='Get a list of all scan configurations in the OpenVAS server',
                input=GetScanConfigsInput(),
                output=GetScanConfigsOutput())

    def run(self, params={}):
        scanProfileDict = self.connection.scanner.get_profiles
        returnList = []
        for key, value in scanProfileDict.iteritems():
            jsonObjectTranslation = {key: value}
            returnList.append(jsonObjectTranslation)
        return {'list_scans': returnList, 'success': True,
                'message': 'Successfully obtained list of scan configurations'}

    def test(self):
        # TODO: Implement test function
        return {}
