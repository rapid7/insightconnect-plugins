import insightconnect_plugin_runtime
from .schema import ThreatsFetchFileInput, ThreatsFetchFileOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class ThreatsFetchFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="threats_fetch_file",
            description=Component.DESCRIPTION,
            input=ThreatsFetchFileInput(),
            output=ThreatsFetchFileOutput(),
        )

    def run(self, params={}):
        threat_id = params.get(Input.ID, None)
        password = params.get(Input.PASSWORD)

        if len(password) <= 10 or " " in password:
            raise PluginException(
                cause="Wrong password.",
                assistance="Password must have more than 10 characters and cannot contain whitespace.",
            )

        agent_filter = {"ids": [threat_id]}
        self.connection.threats_fetch_file(params.get(Input.PASSWORD), agent_filter)
        if agent_filter["ids"]:
            agent_filter["threatIds"] = agent_filter["ids"]
            del agent_filter["ids"]

        return {Output.FILE: self.connection.download_file(agent_filter, password)}
