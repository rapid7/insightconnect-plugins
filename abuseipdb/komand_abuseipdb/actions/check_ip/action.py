import komand
from .schema import CheckIpInput, CheckIpOutput, Input, Output
# Custom imports below
from komand.exceptions import PluginException
import json
import requests
import logging
from komand_abuseipdb.util import helper
logging.getLogger('requests').setLevel(logging.WARNING)


class CheckIp(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_ip',
                description='Look up an IP address in the database',
                input=CheckIpInput(),
                output=CheckIpOutput())

    @staticmethod
    def transform_output(out: dict) -> dict:
        if out[Output.ISPUBLIC] is None:
            out[Output.ISPUBLIC] = False

        out = komand.helper.clean(out)

        return out

    def run(self, params={}):
        base = self.connection.base
        endpoint = 'check'
        url = f'{base}/{endpoint}'
        params = {
            'ipAddress': params.get(Input.ADDRESS),
            'maxAgeInDays': params.get(Input.DAYS),
            'verbose': params.get(Input.VERBOSE)
        }

        r = requests.get(url, params=params, headers=self.connection.headers)

        try:
            json_ = helper.get_json(r)
            out = self.transform_output(json_["data"])

        except json.decoder.JSONDecodeError:
            raise PluginException(cause='Received an unexpected response from AbuseIPDB.',
                                  assistance=f"(non-JSON or no response was received). Response was: {r.text}")

        if len(out) > 0:
            out[Output.FOUND] = True
        else:
            out[Output.FOUND] = False

        return out
