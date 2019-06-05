import komand
import requests
from copy import deepcopy
from .. import utils
from .schema import LaunchScanInput, LaunchScanOutput


class LaunchScan(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='launch_scan',
                description='Run a specified scan',
                input=LaunchScanInput(),
                output=LaunchScanOutput())

    def run(self, params={}):
        try:
            conn = self.connection.conndict
            scan_id = utils.get_scan_by_name(params['scan_name'], deepcopy(conn))
            conn['url'] += '/scans/{}/launch'.format(scan_id)
            r = requests.post(**conn)
            if isinstance(r.json()['scan_uuid'], str):
                return { 'message': 'Scan launched successfully', 'scan_name': params['scan_name'] }
        except Exception as e:
            self.logger.error('Could not launch specified scan. Error: ' + str(e))
            raise

    def test(self):
        check = utils.folder_check(self.connection.conndict)
        return {'message': check, 'scan_name': ''}
