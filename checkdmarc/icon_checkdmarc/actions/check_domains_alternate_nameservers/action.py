import komand
from .schema import CheckDomainsAlternateNameserversInput, CheckDomainsAlternateNameserversOutput, Input, Output, Component
from komand.exceptions import PluginException
# Custom imports below
import json
import checkdmarc
from komand import helper


class CheckDomainsAlternateNameservers(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_domains_alternate_nameservers',
                description=Component.DESCRIPTION,
                input=CheckDomainsAlternateNameserversInput(),
                output=CheckDomainsAlternateNameserversOutput())

    def run(self, params={}):
        timeout = params.get(Input.TIMEOUT)
        nameservers = params.get(Input.NAMESERVERS)
        output = checkdmarc.check_domains([params.get(Input.DOMAIN)], timeout=timeout, nameservers=nameservers)
        try:
            clean_output = helper.clean(json.loads(json.dumps(output)))
        except Exception as e:
            raise PluginException(cause="Unexpected response from server",
                                  assistance=e)

        return {Output.REPORT: clean_output}
