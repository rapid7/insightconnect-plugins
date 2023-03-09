import insightconnect_plugin_runtime
from .schema import GetZoneAccessRulesInput, GetZoneAccessRulesOutput, Input, Output, Component

# Custom imports below
from icon_cloudflare.util.helpers import clean, convert_dict_keys_to_camel_case
from icon_cloudflare.util.constants import configuration_target, mode, order_by


class GetZoneAccessRules(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="getZoneAccessRules",
            description=Component.DESCRIPTION,
            input=GetZoneAccessRulesInput(),
            output=GetZoneAccessRulesOutput(),
        )

    def run(self, params={}):
        provided_mode = params.get(Input.MODE)
        target = params.get(Input.CONFIGURATIONTARGET)
        parameters = {
            "notes": params.get(Input.NOTES),
            "mode": mode.get(provided_mode) if provided_mode != "all" else None,
            "match": params.get(Input.MATCH),
            "configuration.target": configuration_target.get(target) if target != "all" else None,
            "configuration.value": params.get(Input.CONFIGURATIONVALUE),
            "page": params.get(Input.PAGE),
            "per_page": params.get(Input.PERPAGE),
            "order": order_by.get(params.get(Input.ORDER)),
            "direction": params.get(Input.DIRECTION),
        }
        return {
            Output.ACCESSRULES: convert_dict_keys_to_camel_case(
                self.connection.api_client.get_zone_access_rules(params.get(Input.ZONEID), clean(parameters)).get(
                    "result", []
                )
            )
        }
