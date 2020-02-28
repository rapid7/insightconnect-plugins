import komand
from .schema import ImportHashReportInput, ImportHashReportOutput
from komand_threatminer.util import utils

# Custom imports below
import requests


class ImportHashReport(komand.Action):
    API_URL = 'https://www.threatminer.org/imphash.php?api=True&rt=2'

    def __init__(self):
        super(self.__class__, self).__init__(
            name='import_hash_report',
            description='Fetches information related to a hash',
            input=ImportHashReportInput(),
            output=ImportHashReportOutput())

    def run(self, params={}):
        query = params.get('query')
        response = utils.get_query(self.API_URL, query)
        data = utils.extract_json_data(response)

        # https://www.threatminer.org/api.php outlines valid response codes
        expected_range = list(range(200, 299))
        expected_range.append(404)

        utils.check_api_status_code(data, expected_range)
        data["status_code"] = int(data["status_code"])
        return {'response': data}

    def test(self):
        params = {
            "q": "1f4f257947c1b713ca7f9bc25f914039"
        }
        response = requests.get(self.API_URL, params=params)
        if response.status_code != 200:
            raise Exception(
                '%s (HTTP status: %s)' % (response.text, response.status_code))

        return {'status_code': response.status_code}
