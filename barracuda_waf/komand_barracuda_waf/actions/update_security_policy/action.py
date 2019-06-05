import komand
from .schema import UpdateSecurityPolicyInput, UpdateSecurityPolicyOutput



class UpdateSecurityPolicy(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_security_policy',
                description='Updates a security policy with the given values',
                input=UpdateSecurityPolicyInput(),
                output=UpdateSecurityPolicyOutput())

    def run(self, params={}):
        action = "security_policies"
        policy_id = params.get("policy_id")
        if not policy_id:
            self.connection.connector.raise_error("Empty argument policy_id")

        action = action + "/" + policy_id

        r = self.connection.connector.put(action, self.connection.connector.get_dict_from_params(params, [
            "request_limits",
            "cloaking",
            "url_normalization",
            "url_protection",
            "cookie_security",
            "parameter_protection"
        ]))

        if "error" in r and "status" in r["error"] and r["error"]["status"] == 400 :
            self.connection.connector.raise_error("Problem with update")

        return {"msg": r["msg"]}

    def test(self):
        return {"msg": "success"}
