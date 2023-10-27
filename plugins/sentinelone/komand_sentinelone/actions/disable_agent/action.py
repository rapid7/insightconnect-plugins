import insightconnect_plugin_runtime
from .schema import DisableAgentInput, DisableAgentOutput, Input, Output, Component

# Custom imports below
from komand_sentinelone.util.constants import TIMEZONES_MAP


class DisableAgent(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="disable_agent",
            description=Component.DESCRIPTION,
            input=DisableAgentInput(),
            output=DisableAgentOutput(),
        )

    def run(self, params={}):
        expiration_timezone = params.get(Input.EXPIRATIONTIMEZONE)
        expiration_time = params.get(Input.EXPIRATIONTIME)
        agent = params.get(Input.AGENT)
        user_filter = params.get(Input.FILTER, {})
        data = {"shouldReboot": params.get(Input.REBOOT)}

        if expiration_time:
            for timezone, timezone_list in TIMEZONES_MAP.items():
                if expiration_timezone in timezone_list:
                    expiration_timezone = timezone
                    break

            if not expiration_timezone:
                expiration_timezone = "GMT +02:00"

            if "Z" in expiration_time:
                data["expirationTimezone"] = expiration_timezone.replace(" ", "")
                data["expiration"] = expiration_time.replace("Z", "") + expiration_timezone.split()[1]
            else:
                data["expirationTimezone"] = expiration_timezone
                data["expiration"] = expiration_time

        if agent:
            user_filter["uuid"] = self.connection.client.get_agent_uuid(agent)

        return {
            Output.AFFECTED: self.connection.client.disable_agent(data, user_filter).get("data", {}).get("affected", 0)
        }
