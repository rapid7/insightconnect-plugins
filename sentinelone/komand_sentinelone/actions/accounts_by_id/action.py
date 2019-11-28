import komand
from .schema import AccountsByIdInput, AccountsByIdOutput, Input, Output, Component
# Custom imports below


class AccountsById(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='accounts_by_id',
                description=Component.DESCRIPTION,
                input=AccountsByIdInput(),
                output=AccountsByIdOutput())

    def run(self, params={}):
        return {
            Output.DATA: self.connection.accounts_by_id(params.get(Input.ACCOUNT_ID, None)).get("data", {})
        }
