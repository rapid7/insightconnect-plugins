import insightconnect_plugin_runtime
from .schema import GetBlockedHostsInput, GetBlockedHostsOutput, Output, Component

# Custom imports below


class GetBlockedHosts(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_blocked_hosts",
            description=Component.DESCRIPTION,
            input=GetBlockedHostsInput(),
            output=GetBlockedHostsOutput(),
        )

    def run(self, params={}):  # pylint: disable=unused-argument
        return {Output.HOSTS: self.connection.cisco_asa_api.get_blocked_hosts()}
