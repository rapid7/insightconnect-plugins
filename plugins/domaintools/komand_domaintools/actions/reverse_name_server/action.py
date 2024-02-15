import insightconnect_plugin_runtime

from .schema import ReverseNameServerInput, ReverseNameServerOutput
from ...util.util import make_request


class ReverseNameServer(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reverse_name_server",
            description="Provides a list of domain names that share the same primary or secondary name server",
            input=ReverseNameServerInput(),
            output=ReverseNameServerOutput(),
        )

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        params["query"] = params.pop("domain")
        response = make_request(self.connection.api.reverse_name_server, **params)
        return response
