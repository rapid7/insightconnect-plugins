import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import ReverseWhoisInput, ReverseWhoisOutput
from ...util.util import make_request


class ReverseWhois(insightconnect_plugin_runtime.Action):

    MODES = ["purchase", "quote"]

    def __init__(self):
        super(self.__class__, self).__init__(
            name="reverse_whois",
            description="Provides a list of domain names that share the same Registrant Information",
            input=ReverseWhoisInput(),
            output=ReverseWhoisOutput(),
        )

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        params["query"] = params.pop("terms")
        mode = params.get("mode")
        if mode and mode not in self.MODES:
            raise PluginException(cause=f"DomainTools: mode must be one of: {', '.join(self.MODES)}")

        response = make_request(self.connection.api.reverse_whois, **params)
        return response
