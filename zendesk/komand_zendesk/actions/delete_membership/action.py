import komand
import zenpy
from .schema import DeleteMembershipInput, DeleteMembershipOutput
# Custom imports below


class DeleteMembership(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_membership',
                description='Delete organization membership',
                input=DeleteMembershipInput(),
                output=DeleteMembershipOutput())

    def run(self, params={}):
        try:
          org_mem = self.connection.client.organization_memberships(id = params.get('membership_id'))
          self.connection.client.organization_memberships.delete(org_mem)
          return {"status": True}
        except zenpy.lib.exception.APIException as e:
          return {"status": False}
          self.logger.debug(e)

    def test(self):
        try:
          test = self.connection.client.users.me().email
          return { 'success': test }
        except:
          raise
