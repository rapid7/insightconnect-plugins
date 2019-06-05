import komand
import requests
from copy import deepcopy
from .. import utils
from .schema import GetScansInput, GetScansOutput


class GetScans(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_scans',
                description='Returns a list of scans running on the requested scanner',
                input=GetScansInput(),
                output=GetScansOutput())

    def run(self, params={}):
        try:
            conn = self.connection.conndict
            if 'scanner_name' in params:
                scanner_id = utils.get_scanner_by_name(params['scanner_name'], deepcopy(conn))
                url_suffix = '/scanners/{}/scans'.format(scanner_id)
            else:
                url_suffix = '/scans'

            conn['url'] += url_suffix
            r = requests.get(**conn)
            results = r.json()['scans'] if r.json()['scans'] is not None else []
            return { 'scans': results }
        except Exception as e:
            self.logger.error('Could not retrieve scans. Error: ' + str(e))
            raise

    def test(self):
        check = utils.folder_check(self.connection.conndict)
        return {'scans': [{'message': check}]}
