import komand
from .schema import DeleteSecurityPolicyInput, DeleteSecurityPolicyOutput


class DeleteSecurityPolicy(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_security_policy',
                description='Deletes the given security policy',
                input=DeleteSecurityPolicyInput(),
                output=DeleteSecurityPolicyOutput())

    def run(self, params={}):
        self.connection.connector.check_required_params(params, ["id"])
        action = "security_policies/" + params.get("id")
        r = self.connection.connector.delete(action)
        self.connection.connector.raise_error_when_not_in_status(200)
        return {"msg": r["msg"]}

    def test(self):
        return {"msg": ""}
