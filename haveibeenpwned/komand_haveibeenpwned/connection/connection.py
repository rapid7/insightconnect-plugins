import komand
from .schema import ConnectionSchema, Input
import requests
import json
from komand.exceptions import ConnectionTestException
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.api_key = params.get('credentials').get('secretKey')
        self.base = 'https://haveibeenpwned.com/api/v3'

        self.logger.info('Connect: Connecting to %s...' % self.base)

    def test(self):
        url = 'https://haveibeenpwned.com/api/v3/breachedaccount/somebody@gmail.com'
        _HEADERS = {'User-Agent': "Rapid7 InsightConnect", 'Accept': "application/vnd.haveibeenpwned.v2+json", 'hibp-api-key': self.api_key}

        try:
            r = requests.get(url, headers=_HEADERS)
            if r.status_code == 401:
                raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
            if r.status_code == 503:
                raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
            json_ = r.json()
            
        except json.decoder.JSONDecodeError:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.INVALID_JSON, data=r.text)
        except Exception as e:
            self.logger.error(e)
            raise

        return json_
