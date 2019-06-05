import komand
from .schema import GetUserByUsernameInput, GetUserByUsernameOutput, Input, Output, Component
# Custom imports below


class GetUserByUsername(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_user_by_username',
            description=Component.DESCRIPTION,
            input=GetUserByUsernameInput(),
            output=GetUserByUsernameOutput())

    def run(self, params={}):
        user = self.connection.admin_api.get_users_by_name(params.get(Input.USERNAME))
        try:
            out = {Output.USER: user[0]}
            results = komand.helper.clean(out)
            return results

        except (TypeError, IndexError) as e:
            raise Exception(f"User not found. Error: {e}") from e
