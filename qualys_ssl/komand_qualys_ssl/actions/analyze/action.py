import komand
from .schema import AnalyzeInput, AnalyzeOutput
# Custom imports below
import requests


class Analyze(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='analyze',
                description='Initialize an SSL assessment',
                input=AnalyzeInput(),
                output=AnalyzeOutput())

    def run(self, params={}):
        try:
            url = 'https://api.ssllabs.com/api/v2/analyze'

            r_params = {'host': params.get('host'),
                        'publish': params.get('ip'),
                        'maxAge': params.get('max_age'),
                        'all': params.get('all').lower(),
                        'fromCache': params.get('from_cache').lower(),
                        'startNew': params.get('start_new').lower()}

            r = requests.get(url, params=r_params).json()
            if "endpoints" not in r:
                self.logger.info('Endpoints not found in response')
                r.update({'endpoints': []})

            if "testTime" not in r:
                self.logger.info('testTime not found in response, marking as 0')
                r.update({'testTime': 0})

            return r

        except requests.exceptions.RequestException as e:
            raise Exception(e)

    def test(self):
        try:
            url = "https://api.ssllabs.com/api/v2/info"
            r = requests.get(url)
            if r.ok:
                return {"testTime": 1,
                        "criteriaVersion": "True",
                        "port": 1,
                        "isPublic": True,
                        "status": "True",
                        "startTime": 1,
                        "engineVersion": "True",
                        "endpoints": [],
                        "host": "True",
                        "protocol": "Truw"}
        except requests.exceptions.RequestException as e:
            raise Exception(e)


