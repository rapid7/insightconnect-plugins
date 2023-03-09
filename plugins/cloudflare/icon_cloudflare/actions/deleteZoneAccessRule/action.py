import insightconnect_plugin_runtime
from .schema import DeleteZoneAccessRuleInput, DeleteZoneAccessRuleOutput, Input, Output, Component

# Custom imports below


class DeleteZoneAccessRule(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="deleteZoneAccessRule",
            description=Component.DESCRIPTION,
            input=DeleteZoneAccessRuleInput(),
            output=DeleteZoneAccessRuleOutput(),
        )

    def run(self, params={}):
        return {
            Output.SUCCESS: self.connection.api_client.delete_zone_access_rule(
                params.get(Input.ZONEID), params.get(Input.RULEID)
            )
        }
