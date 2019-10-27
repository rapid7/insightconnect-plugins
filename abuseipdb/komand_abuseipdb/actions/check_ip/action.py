import komand
from .schema import CheckIpInput, CheckIpOutput, Input
# Custom imports below
from komand.exceptions import PluginException
import json
import requests
import logging
logging.getLogger('requests').setLevel(logging.WARNING)


class CheckIp(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_ip',
                description='Look up an IP address in the database',
                input=CheckIpInput(),
                output=CheckIpOutput())

    def transform_output(self, out: dict) -> dict:
        if out["isPublic"] is None:
            out["isPublic"] = False

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
            json_ = r.json()
            if "errors" in json_:
                raise PluginException(cause='Received an error response from AbuseIPDB.',
                                      assistance=json_['errors'][0]["detail"])

            out = self.transform_output(json_["data"])

        except json.decoder.JSONDecodeError:
            raise PluginException(cause='Received an unexpected response from AbuseIPDB.',
                                  assistance="(non-JSON or no response was received). Response was: %s" % r.text)

        if len(out) > 0:
            out["found"] = True
        else:
            out["found"] = False

        return out
