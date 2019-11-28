import komand
from .schema import AccountRevertPolicyInput, AccountRevertPolicyOutput, Input, Output, Component
# Custom imports below


class AccountRevertPolicy(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='account_revert_policy',
                description=Component.DESCRIPTION,
                input=AccountRevertPolicyInput(),
                output=AccountRevertPolicyOutput())

    def run(self, params={}):
        return {
            Output.SUCCESS: self.connection.account_revert_policy(
                params.get(Input.ACCOUNT_ID, None),
                params.get(Input.ID, None)
            ).get("data", {}).get("success", False)
        }
