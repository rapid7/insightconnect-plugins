import komand
from .schema import GetBlacklistInput, GetBlacklistOutput, Input, Output
# Custom imports below
from komand.exceptions import PluginException
import json
import requests
import logging
from komand_abuseipdb.util import helper
logging.getLogger('requests').setLevel(logging.WARNING)


class GetBlacklist(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_blacklist',
                description='Get list of blacklisted IPs',
                input=GetBlacklistInput(),
                output=GetBlacklistOutput())

    def run(self, params={}):
        base = self.connection.base
        endpoint = 'blacklist'
        url = f'{base}/{endpoint}'

        params = {
            'confidenceMinimum': params.get(Input.CONFIDENCEMINIMUM)
        }

        if params.get(Input.LIMIT):
            params['limit'] = params.get(Input.LIMIT)

        r = requests.get(url, params=params, headers=self.connection.headers)

        try:
            json_ = helper.get_json(r)
            blacklist = json_["data"]
            out = {Output.BLACKLIST: blacklist}
        except json.decoder.JSONDecodeError:
            raise PluginException(cause='Received an unexpected response from AbuseIPDB.',
                                  assistance=f"(non-JSON or no response was received). Response was: {r.text}")

        if len(out) > 0:
            out[Output.SUCCESS] = True
        else:
            out[Output.SUCCESS] = False

        return out
