import komand
from komand.exceptions import PluginException
from .schema import AddUserToGroupInput, AddUserToGroupOutput, Input, Output, Component
# Custom imports below


class AddUserToGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_user_to_group',
                description=Component.DESCRIPTION,
                input=AddUserToGroupInput(),
                output=AddUserToGroupOutput())

    def run(self, params={}):
        client = self.connection.box_connection

        group_id = params.get(Input.GROUP_ID)
        user_id = params.get(Input.USER_ID)
        role = params.get(Input.ROLE)

        user = client.user(user_id)
        try:
            membership = client.group(group_id=group_id).add_member(user, role)
        except Exception as e:
            raise PluginException(cause="Add user to group failed.",
                                  assistance=f"Exception returned was {e}")

        membership_object = {
            "user_id": membership.user.object_id,
            "group_id": membership.group.object_id,
            "role": membership.role,
            "type": membership.type
        }

        return {Output.GROUP: membership_object}


