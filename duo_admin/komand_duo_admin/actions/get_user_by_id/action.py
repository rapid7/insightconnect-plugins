import komand
from .schema import GetUserByIdInput, GetUserByIdOutput, Input, Output, Component
# Custom imports below


class GetUserById(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_user_by_id',
            description=Component.DESCRIPTION,
            input=GetUserByIdInput(),
            output=GetUserByIdOutput())

    def run(self, params={}):
        try:
            user = self.connection.admin_api.get_user_by_id(params.get(Input.USER_ID))
            results = komand.helper.clean({Output.USER: user})
            return results
        except KeyError as e:
            self.logger.error(f'User not found. Error: {str(e)}')
