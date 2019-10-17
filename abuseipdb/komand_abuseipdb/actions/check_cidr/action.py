import komand
from .schema import CheckCidrInput, CheckCidrOutput, Input
# Custom imports below
from komand.exceptions import PluginException
import json
import requests
import logging
logging.getLogger('requests').setLevel(logging.WARNING)


class CheckCidr(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_cidr',
                description='Look up a CIDR address in the database',
                input=CheckCidrInput(),
                output=CheckCidrOutput())

    def run(self, params={}):
        base = self.connection.base
        endpoint = 'check-block'
        url = f'{base}/{endpoint}'

        params = {
            'network': params.get(Input.CIDR),
            'maxAgeInDays': params.get(Input.DAYS),
        }

        r = requests.get(url, params=params, headers=self.connection.headers)

        try:
            json_ = r.json()
            if "errors" in json_:
                raise PluginException(cause='Received an error response from AbuseIPDB.',
                                      assistance=json_['errors'][0]["detail"])
            out = json_["data"]
        except json.decoder.JSONDecodeError:
            raise PluginException(cause='Received an unexpected response from AbuseIPDB.',
                                  assistance="(non-JSON or no response was received). Response was: %s" % r.text)

        if len(out) > 0:
            out["found"] = True
        else:
            out["found"] = False

        return out
