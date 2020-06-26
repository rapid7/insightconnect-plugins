import insightconnect_plugin_runtime
from .schema import QuarantineInput, QuarantineOutput, Input, Output, Component
# Custom imports below
import icon_carbon_black_cloud.util.whitelist_checker as whitelist_checker


class Quarantine(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='quarantine',
                description=Component.DESCRIPTION,
                input=QuarantineInput(),
                output=QuarantineOutput())

    def run(self, params={}):
        agent = params.get(Input.AGENT)
        whitelist = params.get(Input.WHITELIST)
        quarantine_state = params.get(Input.QUARANTINE_STATE)

        if quarantine_state and whitelist_checker.match_whitelist(agent, whitelist, self.logger):
            self.logger.info(f"Agent {agent} matched item in whitelist, skipping quarantine.")
            return {Output.QUARANTINED: False}

        agent_object = self.connection.get_agent(agent)
        agent_id = agent_object.get("id")

        if quarantine_state:
            toggle = "ON"
        else:
            toggle = "OFF"

        payload = {
            "action_type": "QUARANTINE",
            "device_id": [str(agent_id)],
            "options": {
                "toggle": toggle
            }
        }

        url = f"{self.connection.base_url}/appservices/v6/orgs/{self.connection.org_key}/device_actions"
        self.connection.post_to_api(url, payload)

        # This API returns 204 no content if successful, we have to assume the state was applied on a successful call
        return {Output.QUARANTINED: quarantine_state}
