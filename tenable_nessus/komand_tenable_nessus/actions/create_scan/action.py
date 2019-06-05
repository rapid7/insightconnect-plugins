import komand
import requests
from copy import deepcopy
from .. import utils
from .schema import CreateScanInput, CreateScanOutput


class CreateScan(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_scan',
                description='Create a new scan',
                input=CreateScanInput(),
                output=CreateScanOutput())

    def run(self, params={}):
        try:
            conn = self.connection.conndict
            post_body = {
                'uuid': utils.get_template_by_name(params['template_name'], deepcopy(conn)),
                'settings': {
                    'name': params['scan_name'],
                    'enabled': 'true',
                    'scanner_id': utils.get_scanner_by_name(params['scanner_name'], deepcopy(conn)),
                    'text_targets': ', '.join(params['targets'])
                }
            }
            post_body['settings'].update({'description': params['description']} if 'description' in params else {})
            conn['url'] += '/scans'
            conn['headers'].update({'content-type': 'application/json'})
            conn.update({'json': post_body})
            r = requests.post(**conn)
            return { 'message': 'Scan successfully created', 'new_scan': r.json()['scan']}
        except Exception as e:
            self.logger.error('Could not create scan. Error: ' + str(e))

    def test(self):
        check = utils.folder_check(self.connection.conndict)
        return {'message': check, 'new_scan': {}}
