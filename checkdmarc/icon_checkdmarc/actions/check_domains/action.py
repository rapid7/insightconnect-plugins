import komand
from .schema import CheckDomainsInput, CheckDomainsOutput, Input, Output, Component
from komand.exceptions import PluginException
# Custom imports below
import json
import checkdmarc
from komand import helper


class CheckDomains(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_domains',
                description=Component.DESCRIPTION,
                input=CheckDomainsInput(),
                output=CheckDomainsOutput())

    def run(self, params={}):
        timeout = params.get(Input.TIMEOUT)
        output = checkdmarc.check_domains([params.get(Input.DOMAIN)], timeout=timeout)
        try:
            clean_output = helper.clean(json.loads(json.dumps(output)))
        except Exception as e:
            raise PluginException(cause="Unexpected response from server",
                                  assistance=e)

        return {Output.REPORT: clean_output}
