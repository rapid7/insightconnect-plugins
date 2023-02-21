import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import ShowMembershipsInput, ShowMembershipsOutput, Input, Output

# Custom imports below
from icon_zendesk.util.objects import Objects
from icon_zendesk.util.exceptions import detect_type_exception


class ShowMemberships(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="show_memberships",
            description="Show all Organization Memberships",
            input=ShowMembershipsInput(),
            output=ShowMembershipsOutput(),
        )

    def run(self, params={}):
        user_id = params.get(Input.USER_ID)

        try:
            organization_memberships = self.connection.client.users.organization_memberships(user=user_id)
        except Exception as error:
            self.logger.debug(error)
            detect_type_exception(error)
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        memberships_array = []
        for organization_membership in organization_memberships:
            membership_object = Objects.create_membership_object(organization_membership)
            memberships_array.append(membership_object)
        return {Output.MEMBERSHIPS: memberships_array}
