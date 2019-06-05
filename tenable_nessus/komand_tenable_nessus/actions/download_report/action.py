import komand
import json
import requests
import time
import base64
from copy import deepcopy
from .. import utils
from .schema import DownloadReportInput, DownloadReportOutput


class DownloadReport(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='download_report',
                description='Export and download a specified report',
                input=DownloadReportInput(),
                output=DownloadReportOutput())

    def run(self, params={}):
        try:
            conn = self.connection.conndict
            scan_name = params['scan_name']
            base_url = conn['url']

            scan_status = ''
            while scan_status != 'completed':
                time.sleep(0.5) if scan_status == '' else time.sleep(10)
                scan_status = utils.check_scan_status(scan_name, deepcopy(conn))

            scan_id = utils.get_scan_by_name(scan_name, deepcopy(conn))
            conn['url'] += '/scans/{}/export'.format(scan_id)

            export_request_dict = {'json': {'format': params['report_format']}}
            export_request_dict.update(conn)
            export_request_dict['headers'].update({'content-type': 'application/json'})
            file_id = requests.post(**export_request_dict).json()['file']

            conn['url'] += '/{}/status'.format(file_id)
            export_status = ''
            while export_status != 'ready':
                export_response = requests.get(**conn).json()
                export_status = export_response['status'] if 'status' in export_response else ''
                time.sleep(0.5)

            conn['url'] = base_url + '/scans/{}/export/{}/download'.format(scan_id, file_id)
            download = str(requests.get(**conn)._content, 'utf-8')
            return { 'report': download }
            #file is automatically deleted once downloaded, has to be re-exported to use download call again
            #file id works only once

        except Exception as e:
            self.logger.error("Could not export and/or download report. Error: " + str(e))

    def test(self):
        check = utils.folder_check(self.connection.conndict)
        return { 'report': check }
