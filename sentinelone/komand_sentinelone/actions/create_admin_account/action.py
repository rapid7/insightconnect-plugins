import komand
from .schema import CreateAdminAccountInput, CreateAdminAccountOutput, Input, Output, Component
# Custom imports below


class CreateAdminAccount(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_admin_account',
                description=Component.DESCRIPTION,
                input=CreateAdminAccountInput(),
                output=CreateAdminAccountOutput())

    def run(self, params={}):
        accounts = self.connection.create_admin_account({
            "accountType": params.get(Input.ACCOUNT_TYPE, None),
            "expiration": params.get(Input.EXPIRATION, None),
            "user": params.get(Input.USER, None),
            "skus": params.get(Input.SKUS, None),
            "externalId": params.get(Input.EXTERNAL_ID, None),
            "policy": params.get(Input.POLICY, None),
            "unlimitedExpiration": params.get(Input.UNLIMITED_EXPIRATION, None),
            "name": params.get(Input.NAME, None),
            "inherits": params.get(Input.INHERITS, None)
        })

        return {
            Output.DATA: accounts.get("data")
        }
