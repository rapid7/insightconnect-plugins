import insightconnect_plugin_runtime
from .schema import DeleteMembershipInput, DeleteMembershipOutput, Input, Output

# Custom imports below


class DeleteMembership(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_membership",
            description="Delete organization membership",
            input=DeleteMembershipInput(),
            output=DeleteMembershipOutput(),
        )

    def run(self, params={}):
        identifier = params.get(Input.MEMBERSHIP_ID)

        try:
            organization_membership = self.connection.client.organization_memberships(id=identifier)
            self.connection.client.organization_memberships.delete(organization_membership)
            return {Output.STATUS: True}
        except Exception as error:
            # API exception is only raised when incorrect data is input (Membership ID here)
            self.logger.error(error)
            return {Output.STATUS: False}
