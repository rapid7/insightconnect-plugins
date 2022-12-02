import insightconnect_plugin_runtime
from .schema import SwitchOrganizationInput, SwitchOrganizationOutput, Input, Output, Component

# Custom imports below


class SwitchOrganization(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="switch_organization",
            description=Component.DESCRIPTION,
            input=SwitchOrganizationInput(),
            output=SwitchOrganizationOutput(),
        )

    def run(self, params={}):
        return {
            Output.SUCCESS: self.connection.api.switch_organization(
                {"organization_name": params.get(Input.ORGANIZATIONNAME)}
            )
        }
