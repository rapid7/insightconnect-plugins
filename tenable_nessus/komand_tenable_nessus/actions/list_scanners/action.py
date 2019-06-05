import komand
import requests
from .. import utils
from .schema import ListScannersInput, ListScannersOutput


class ListScanners(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_scanners',
                description='Return an array of all available scanners',
                input=ListScannersInput(),
                output=ListScannersOutput())

    def run(self, params={}):
        try:
            conn = self.connection.conndict
            conn['url'] += '/scanners'
            r = requests.get(**conn)
            results = r.json()['scanners'] if r.json()['scanners'] is not None else []
            return { 'scanners': results }
        except Exception as e:
            self.logger.error('Could not list scanners. Error: ' + str(e))
            raise

    def test(self):
        check = utils.folder_check(self.connection.conndict)
        return {'scanners': [{'message': check}]}
