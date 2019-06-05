import komand
from .schema import DeleteScanInput, DeleteScanOutput
# Custom imports below
from openvas_lib.common import AuditNotFoundError
import sys


class DeleteScan(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_scan',
                description='Delete specified scan ID in the OpenVAS server',
                input=DeleteScanInput(),
                output=DeleteScanOutput())

    def run(self, params={}):
        scan_id = str(params.get('scan_id'))
        try:
            self.connection.scanner.delete_scan(scan_id)
        except AuditNotFoundError:
            return {'success': False, 'message': 'Scan to delete not found using supplied scan ID'}
        except:
            return {'success': False, 'message': ' | '.join([str(sys.exc_info()[0]), str(sys.exc_info()[1])])}
        return {'success': True, 'message': 'Scan successfully deleted'}

    def test(self):
        # TODO: Implement test function
        return {}
