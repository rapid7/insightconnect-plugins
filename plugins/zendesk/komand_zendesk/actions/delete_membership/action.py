import insightconnect_plugin_runtime
import zenpy
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
        try:
            org_mem = self.connection.client.organization_memberships(id=params.get(Input.MEMBERSHIP_ID))
            self.connection.client.organization_memberships.delete(org_mem)
            return {Output.STATUS: True}
        except zenpy.lib.exception.APIException as e:
            # API exception is only raised when incorrect data is input (Membership ID here)
            self.logger.error(e)
            return {Output.STATUS: False}

    def test(self):
        try:
            test = self.connection.client.users.me().email
            return {"success": test}
        except:
            raise
