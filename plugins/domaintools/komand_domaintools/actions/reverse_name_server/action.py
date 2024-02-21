import insightconnect_plugin_runtime
from .schema import ReverseNameServerInput, ReverseNameServerOutput, Input, Output, Component

# Custom imports below
from komand_domaintools.util import util


class ReverseNameServer(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reverse_name_server",
            description=Component.DESCRIPTION,
            input=ReverseNameServerInput(),
            output=ReverseNameServerOutput(),
        )

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        params["query"] = params.pop(Input.DOMAIN)
        response = util.make_request(self.connection.api.reverse_name_server, **params)
        return response
