import komand
from .schema import UpdateGlobalAclRuleInput, UpdateGlobalAclRuleOutput



class UpdateGlobalAclRule(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_global_acl_rule',
                description='Updates the values of given parameters in the given global ACL rule',
                input=UpdateGlobalAclRuleInput(),
                output=UpdateGlobalAclRuleOutput())

    def run(self, params={}):
        action = "security_policies"
        self.connection.connector.check_required_params(params, [
            "policy_id",
            "id"])

        action = action + "/" + params.get("policy_id") + "/global_acls/" + params.get("id")

        del params["id"]
        del params["policy_id"]

        r = self.connection.connector.put(action, params)

        self.connection.connector.raise_error_when_not_in_status(202)

        return {"id": r["id"]}

    def test(self):
        return {"id": ""}
