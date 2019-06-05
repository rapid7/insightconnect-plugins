import komand
from .schema import GetPhonesByUserIdInput, GetPhonesByUserIdOutput, Input, Output, Component
# Custom imports below


class GetPhonesByUserId(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_phones_by_user_id',
                description=Component.DESCRIPTION,
                input=GetPhonesByUserIdInput(),
                output=GetPhonesByUserIdOutput())

    def run(self, params={}):
        try:
            phone_list = self.connection.admin_api.get_user_phones(params.get(Input.USER_ID))
            results = komand.helper.clean({Output.PHONE_LIST: phone_list})
            return results
        except KeyError as e:
            self.logger.error('User not found. Error: ' + str(e))
        return {Output.PHONE_LIST: []}
