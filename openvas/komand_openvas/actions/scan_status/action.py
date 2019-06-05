import komand
from .schema import ScanStatusInput, ScanStatusOutput
# Custom imports below
import sys


class ScanStatus(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='scan_status',
                description='Get status of scan',
                input=ScanStatusInput(),
                output=ScanStatusOutput())

    def run(self, params={}):
        scan_id = str(params.get('scan_id'))
        try:
            stat = self.connection.scanner.get_scan_status(scan_id)
        except:
            return {'status': '', 'success': False,
                    'message': ' | '.join([str(sys.exc_info()[0]), str(sys.exc_info()[1])])}
        return {'status': str(stat), 'success': True, 'message': 'Got status successfully'}

    def test(self):
        # TODO: Implement test function
        return {}
