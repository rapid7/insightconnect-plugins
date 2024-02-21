import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import ReverseWhoisInput, ReverseWhoisOutput, Input, Output, Component

# Custom imports below
from komand_domaintools.util import util


class ReverseWhois(insightconnect_plugin_runtime.Action):

    MODES = ["purchase", "quote"]

    def __init__(self):
        super(self.__class__, self).__init__(
            name="reverse_whois",
            description=Component.DESCRIPTION,
            input=ReverseWhoisInput(),
            output=ReverseWhoisOutput(),
        )

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        params["query"] = params.pop(Input.TERMS)
        mode = params.get(Input.MODE)
        if mode and mode not in self.MODES:
            modes = ", ".join(self.MODES)
            raise PluginException(f"DomainTools: mode must be one of: {modes}")

        response = util.make_request(self.connection.api.reverse_whois, **params)
        return response
