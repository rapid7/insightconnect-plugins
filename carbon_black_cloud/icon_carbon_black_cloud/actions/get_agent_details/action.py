import insightconnect_plugin_runtime
from .schema import GetAgentDetailsInput, GetAgentDetailsOutput, Input, Output, Component
# Custom imports below
import icon_carbon_black_cloud.util.agent_typer as agent_typer


class GetAgentDetails(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_agent_details',
                description=Component.DESCRIPTION,
                input=GetAgentDetailsInput(),
                output=GetAgentDetailsOutput())

    def run(self, params={}):
        agent = params[Input.AGENT]
        agent_type = agent_typer.get_agent_type(agent)

        endpoint = "/device"
        if agent_type == agent_typer.HOSTNAME:
            endpoint+=f"?hostNameExact={agent}"
        elif agent_type == agent_typer.IP_ADDRESS:
            endpoint += f"?ipAddress={agent}"
        elif agent_type == agent_typer.DEVICE_ID:
            endpoint += f"/{agent}"

        self.logger.info(f"Searching at {endpoint}")
        result = self.connection.get_from_api(endpoint, {})

        if agent_type == agent_typer.DEVICE_ID:
            device = result.get("deviceInfo", {})
            all_devices = {}
        else:
            devices = result.get("results")
            if len(devices):
                device = devices[0]
            else:
                device = {}
            all_devices = result.get("results")

        return {Output.AGENT: device, Output.ALL_AGENTS_MATCHED: all_devices}
