import komand
from .schema import StopScanInput, StopScanOutput
# Custom imports below
import sys
from openvas_lib import AuditNotFoundError


class StopScan(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='stop_scan',
                description='Stops specified scan ID in the OpenVAS server',
                input=StopScanInput(),
                output=StopScanOutput())

    def run(self, params={}):
        scan_id = str(params.get('scan_id', ''))
        try:
            self.connection.scanner.stop_audit(scan_id)
        except AuditNotFoundError:
            return {'success': False, 'message': 'Could not find the specified scan id to stop'}
        except:
            return {'success': False, 'message': ' | '.join([str(sys.exc_info()[0]), str(sys.exc_info()[1])])}
        return {'success': True, 'message': 'Scan successfully stopped'}

    def test(self):
        # TODO: Implement test function
        return {}
