import komand
from .schema import CheckCidrInput, CheckCidrOutput, Input, Output
# Custom imports below
from komand.exceptions import PluginException
import json
import requests
import logging
from komand_abuseipdb.util import helper
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
        eval(params)
        params = {
            'network': params.get(Input.CIDR),
            'maxAgeInDays': params.get(Input.DAYS),
        }

        r = requests.get(url, params=params, headers=self.connection.headers)

        try:
            json_ = helper.get_json(r)
            out = json_["data"]
        except json.decoder.JSONDecodeError:
            raise PluginException(cause='Received an unexpected response from AbuseIPDB.',
                                  assistance=f"(non-JSON or no response was received). Response was: {r.text}")

        if len(out) > 0:
            out[Output.FOUND] = True
        else:
            out[Output.FOUND] = False

        return out
