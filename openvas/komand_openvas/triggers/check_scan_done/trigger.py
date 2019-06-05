import komand
import time
from .schema import CheckScanDoneInput, CheckScanDoneOutput
# Custom imports below
import sys


class CheckScanDone(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_scan_done',
                description='Poll scan by scan ID for completion',
                input=CheckScanDoneInput(),
                output=CheckScanDoneOutput())

    def run(self, params={}):
        scan_id = str(params.get('scan_id'))
        poll_timeout = abs(float(params.get('poll')))
        while True:
            try:
                stat = self.connection.scanner.get_scan_status(scan_id)
            except:
                self.logger.error('Error trying to get scan status: ' + ' | '.join([str(sys.exc_info()[0]),str(sys.exc_info()[1])]) )
                return
            if stat == 'Done':
                self.send({'scan_finished': True})
            else:
                self.send({'scan_finished': False})
            time.sleep(60*poll_timeout)

    def test(self):
        # TODO: Implement test function
        return {}
