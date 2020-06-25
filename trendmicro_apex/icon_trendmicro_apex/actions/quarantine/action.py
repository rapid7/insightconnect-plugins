import komand
from .schema import QuarantineInput, QuarantineOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
import validators


class Quarantine(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='quarantine',
            description=Component.DESCRIPTION,
            input=QuarantineInput(),
            output=QuarantineOutput())

    def run(self, params={}):
        return self.connection.api.execute(
            "post",
            "/WebApp/API/AgentResource/ProductAgents",
            self._get_payload(params)
        )

    def _get_payload(self, params):
        agent = params.get(Input.AGENT)
        if params.get(Input.QUARANTINE_STATE, True):
            action = "cmd_isolate_agent"
        else:
            action = "cmd_restore_isolated_agent"

        if "cmd_isolate_agent" == action and agent in params.get(Input.WHITELIST, []):
            raise PluginException(cause="Unable to block whitelisted entry.",
                                  assistance=f"Please remove the host from the action's whitelist or quarantine a different host.")


        payload = {
            "act": action,
            "allow_multiple_match": True
        }

        validate_dict = {
            "entity_id": validators.uuid,
            "ip_address": lambda address: (validators.ipv4(address) or validators.ipv6(address)),
            "host_name": self.validate_host_name,
        }

        if validators.mac_address(agent.replace("-", ":")):
            payload["mac_address"] = agent
        else:
            for name, validate_fn in validate_dict.items():
                if validate_fn(agent):
                    payload[name] = agent
                    break

        return payload

    @staticmethod
    def validate_host_name(agent):
        return agent is not ""
