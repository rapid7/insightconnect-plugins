import insightconnect_plugin_runtime
from .schema import DisableAgentInput, DisableAgentOutput, Input, Output, Component

# Custom imports below


class DisableAgent(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="disable_agent",
            description=Component.DESCRIPTION,
            input=DisableAgentInput(),
            output=DisableAgentOutput(),
        )

    def run(self, params={}):
        agent = params.get(Input.AGENT)
        user_filter = params.get(Input.FILTER, {})
        data = {"shouldReboot": params.get(Input.REBOOT)}
        expiration_time = params.get(Input.EXPIRATION_TIME)
        if expiration_time:
            expiration_timezone = params.get(Input.EXPIRATION_TIMEZONE)
            data["expirationTimezone"] = expiration_timezone
            data["expiration"] = expiration_time

        if agent:
            user_filter["uuid"] = self.connection.client.get_agent_uuid(agent)

        return {Output.AFFECTED: self.connection.disable_agent(data, user_filter).get("data", {}).get("affected", 0)}
