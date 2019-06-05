import komand
from .schema import CertificateInput, CertificateOutput
# Custom imports below
import requests


class Certificate(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='certificate',
                description='Retrieve root certificates',
                input=CertificateInput(),
                output=CertificateOutput())

    def run(self, params={}):
        try:
            url = "https://api.ssllabs.com/api/v2/getRootCertsRaw"
            r = requests.get(url).text
            return {"certificates": r}
        except requests.exceptions.RequestException as e:
            self.logger.error(e)
            raise Exception(e)

    def test(self):
        try:
            url = "https://api.ssllabs.com/api/v2/getRootCertsRaw"
            r = requests.get(url).text
            return {"certificates": r}
        except requests.exceptions.RequestException as e:
            self.logger.error(e)
            raise Exception(e)
