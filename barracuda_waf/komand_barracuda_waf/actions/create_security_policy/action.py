import komand
from .schema import CreateSecurityPolicyInput, CreateSecurityPolicyOutput


class CreateSecurityPolicy(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_security_policy',
                description='Creates a security policy with the default values',
                input=CreateSecurityPolicyInput(),
                output=CreateSecurityPolicyOutput())

    def run(self, params={}):
        action = "security_policies"
        r = self.connection.connector.post(action, {"name": params.get("name")})
        self.connection.connector.raise_error_when_not_in_status(201)
        return {"id": r["id"]}

    def test(self):
        return {"id": "id"}
