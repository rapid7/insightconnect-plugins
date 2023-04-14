import insightconnect_plugin_runtime
from .schema import CreateZoneAccessRuleInput, CreateZoneAccessRuleOutput, Input, Output, Component

# Custom imports below
from icon_cloudflare.util.helpers import clean, set_configuration, convert_dict_keys_to_camel_case
from icon_cloudflare.util.constants import mode


class CreateZoneAccessRule(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="createZoneAccessRule",
            description=Component.DESCRIPTION,
            input=CreateZoneAccessRuleInput(),
            output=CreateZoneAccessRuleOutput(),
        )

    def run(self, params={}):
        payload = {
            "mode": mode.get(params.get(Input.MODE)),
            "configuration": set_configuration(params.get(Input.TARGET)),
            "notes": params.get(Input.NOTES),
        }
        return {
            Output.ACCESSRULE: convert_dict_keys_to_camel_case(
                self.connection.api_client.create_zone_access_rule(params.get(Input.ZONEID), clean(payload)).get(
                    "result"
                )
            )
        }
