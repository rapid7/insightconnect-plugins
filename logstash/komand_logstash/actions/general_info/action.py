import komand
from .schema import GeneralInfoInput, GeneralInfoOutput
# Custom imports below
from komand_logstash.util import utils
import requests


class GeneralInfo(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='general_info',
                description='Retrieves general information about the Logstash instance, including the host and version',
                input=GeneralInfoInput(),
                output=GeneralInfoOutput())

    def run(self, params={}):
        r = requests.get(self.connection.url)
        return {'response': utils.serialize(r.json())}

    def test(self):
        r = requests.get(self.connection.url)
        if r.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (r.text, r.status_code))

        return {'status_code': r.status_code}
