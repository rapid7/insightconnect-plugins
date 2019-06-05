import komand
from .schema import LaunchScanInput, LaunchScanOutput
# Custom imports below
import json
import base64
from tenable_io.exceptions import TenableIOApiException
from komand_tenable_io.util import util

class LaunchScan(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='launch_scan',
                description='Scan external assets',
                input=LaunchScanInput(),
                output=LaunchScanOutput())

    def run(self, params={}):
        try:
            scan_name = params['name']
            scan = self.connection.client.scan_helper.create(
                name=scan_name,
                text_targets=params['targets'],
                template=params['template']
            )
            scan.launch()
            return { "scan_name": scan.name() }

        except TenableIOApiException as e:
            self.logger.error("An API error occurred: " + str(e))
        except Exception as e:
            self.logger.error("Scan could not be launched. Error: " + str(e))

    def test(self):
        conn = self.connection.client
        return { "scan_name": util.folder_verify(conn, self.logger) }
