import komand
from .schema import ImportHashReportInput, ImportHashReportOutput, Input, Output
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
        query = params.get(Input.QUERY)
        response = utils.get_query(self.API_URL, query)
        data = utils.extract_json_data(response)

        # https://www.threatminer.org/api.php outlines valid response codes
        expected_range = list(range(200, 299))
        expected_range.append(404)

        utils.check_api_status_code(data, expected_range)
        normalized_data = utils.normalize_data(data)

        return {Output.RESPONSE: normalized_data}

