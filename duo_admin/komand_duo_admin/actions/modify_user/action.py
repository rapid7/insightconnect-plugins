import komand
from .schema import ModifyUserInput, ModifyUserOutput, Input, Output, Component
# Custom imports below


class ModifyUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='modify_user',
            description=Component.DESCRIPTION,
            input=ModifyUserInput(),
            output=ModifyUserOutput())

    def run(self, params={}):
        status = params.get(Input.STATUS)
        user_id = params.get(Input.USER_ID)

        try:
            user = self.connection.admin_api.update_user(user_id=user_id, status=status)
            # Keys whose values are none are not supported in schema, remove them
            results = komand.helper.clean(user)
            return {Output.USER: results}
        except Exception as e:
            raise Exception(f"Error: User not found. {e}")
