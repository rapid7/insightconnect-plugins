import komand
import requests
import xmltodict
from .. import demo_test
from .schema import DownloadHashRiskListInput, DownloadHashRiskListOutput


class DownloadHashRiskList(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='download_hash_risk_list',
                description='This action is used to return a list of hashes matching a specified risk rule',
                input=DownloadHashRiskListInput(),
                output=DownloadHashRiskListOutput())

    def run(self, params={}):
        try:
            risklist = params.get("list")
            query_headers = {'X-RFToken': self.connection.token}
            query_params = {'format': 'xml/stix/1.2', 'gzip': 'false', 'list': risklist}
            results = requests.get("https://api.recordedfuture.com/v2/hash/risklist",
                                    params=query_params,
                                    headers=query_headers)
            return dict(xmltodict.parse(results.text))
        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        return demo_test.demo_test(self.connection.token, self.logger)
