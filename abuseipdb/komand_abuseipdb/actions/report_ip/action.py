import komand
from .schema import ReportIpInput, ReportIpOutput, Input, Output
# Custom imports below
from komand.exceptions import PluginException
import json
import requests
import logging
from komand_abuseipdb.util import helper
logging.getLogger('requests').setLevel(logging.WARNING)


class ReportIp(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='report_ip',
                description='Report an abusive IP address',
                input=ReportIpInput(),
                output=ReportIpOutput())

    def run(self, params={}):
        base = self.connection.base
        endpoint = 'report'
        url = f'{base}/{endpoint}'

        params = {
            'ip': params.get(Input.IP),
            'categories': params.get(Input.CATEGORIES),
            'comment': params.get(Input.COMMENT)
        }

        r = requests.post(url, params=params, headers=self.connection.headers)

        try:
            json_ = helper.get_json(r)
            out = json_["data"]
        except json.decoder.JSONDecodeError:
            raise PluginException(cause='Received an unexpected response from AbuseIPDB.',
                                  assistance=f"(non-JSON or no response was received). Response was: {r.text}")

        if len(out) > 0:
            out[Output.SUCCESS] = True
        else:
            out[Output.SUCCESS] = False

        return out
