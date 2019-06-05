import komand
from .schema import ConnectionSchema
# Custom imports below
from komand.exceptions import ConnectionTestException
import json
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.api_key = params.get('credentials').get('secretKey')
        self.base = 'https://www.abuseipdb.com'

        self.logger.info('Connect: Connecting to %s...' % self.base)

    def test(self):
        # Use private IP Addresses for testing the API (e.g. 127.0.0.1) from https://www.abuseipdb.com/api
        url = 'https://www.abuseipdb.com/check/127.0.0.1/json'
        try:
            r = requests.get(url)
            json_ = r.json()
        except json.decoder.JSONDecodeError:
            raise ConnectionTestException(cause='Received an unexpected response from AbuseIPDB.',
                                  assistance="(non-JSON or no response was received). Response was: %s" % r.text)
        except Exception as e:
            self.logger.error(e)
            raise

        #return { 'list': out, 'found': True }
        return json_
