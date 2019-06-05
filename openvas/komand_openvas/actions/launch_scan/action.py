import komand
from .schema import LaunchScanInput, LaunchScanOutput
# Custom imports below
from openvas_lib.common import AuthFailedError
from openvas_lib.common import RemoteVersionError
import sys


class LaunchScan(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='launch_scan',
                description='Launch a new audit in OpenVAS',
                input=LaunchScanInput(),
                output=LaunchScanOutput())

    def run(self, params={}):
        target = str(params.get('target'))
        profile = str(params.get('profile'))
        schedule = params.get('schedule')
        if schedule:
            schedule = str(schedule)
        try:
            scan_id, target_id = self.connection.scanner.launch_scan(target=target, profile=profile, schedule=schedule)
        except RemoteVersionError:
            return {'success': False, 'scan_id': '', 'target_id': '',
                    'message': 'Error while trying to connect to the server: Invalid OpenVAS version on remote server'}
        except AuthFailedError:
            return {'success': False, 'scan_id': '', 'target_id': '',
                    'message': 'Error while trying to connect to the server: Authentication failed'}
        except:
            type_, value_, traceback_ = sys.exc_info()
            return {'success': False, 'scan_id': '', 'target_id': '', 'message': str(type_) + ' | ' + str(value_)}
        return {'success': True, 'scan_id': scan_id, 'target_id': target_id, 'message': 'Target scan initiated'}

    def test(self):
        # TODO: Implement test function
        return {}
