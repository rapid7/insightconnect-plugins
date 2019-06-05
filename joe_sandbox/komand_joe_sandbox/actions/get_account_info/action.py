import komand
from .schema import GetAccountInfoInput, GetAccountInfoOutput, Input, Output
# Custom imports below


class GetAccountInfo(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_account_info',
                description='Query information about your account',
                input=GetAccountInfoInput(),
                output=GetAccountInfoOutput())

    def run(self, params={}):
        account_info = self.connection.api.account_info()
        return account_info
