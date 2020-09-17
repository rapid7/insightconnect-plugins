import komand
from .schema import LatestDomainsInput, LatestDomainsOutput, Input
# Custom imports below
from komand.exceptions import PluginException
from IPy import IP as IP_Validate


class LatestDomains(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='latest_domains',
            description='Return associated malicious domains for an IP address',
            input=LatestDomainsInput(),
            output=LatestDomainsOutput())

    def run(self, params={}):
        IP = params.get(Input.IP)
        try:
            IP_Validate(IP)
        except Exception as e:
            raise PluginException(
                cause='Invalid IP provided by user.',
                assistance='Please try again by submitting a valid IP address.',
                data=e
            )

        try:
            latest_domains = self.connection.investigate.latest_domains(IP)
        except Exception as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
        return {"domains": latest_domains}

    def test(self):
        return {"domains": []}
