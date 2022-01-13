import insightconnect_plugin_runtime
from .schema import ShowMembershipsInput, ShowMembershipsOutput, Input, Output

# Custom imports below
import json


class ShowMemberships(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="show_memberships",
            description="Show all Organization Memberships",
            input=ShowMembershipsInput(),
            output=ShowMembershipsOutput(),
        )

    def run(self, params={}):
        mem_array = []
        for org_memb in self.connection.client.users.organization_memberships(user=params.get(Input.USER_ID)):
            memb_obj = {
                "id": org_memb.id,
                "user_id": org_memb.user_id,
                "organization_id": org_memb.organization_id,
                "default": org_memb.default,
                "created_at": org_memb.created_at,
                "updated_at": org_memb.updated_at,
            }
            mem_array.append(memb_obj)
        return {Output.MEMBERSHIPS: mem_array}

    def test(self):
        try:
            test = self.connection.client.users.me().email
            return {"success": test}
        except:
            raise
