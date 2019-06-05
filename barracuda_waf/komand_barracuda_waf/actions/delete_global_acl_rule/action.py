import komand
from .schema import DeleteGlobalAclRuleInput, DeleteGlobalAclRuleOutput


class DeleteGlobalAclRule(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_global_acl_rule',
                description='Deletes the given global ACL rule',
                input=DeleteGlobalAclRuleInput(),
                output=DeleteGlobalAclRuleOutput())

    def run(self, params={}):
        action = "security_policies/"
        self.connection.connector.check_required_params(params, [
            "policy_id",
            "global_acl_id"])

        action = action + params.get("policy_id") + "/global_acls/" + params.get("global_acl_id")
        r = self.connection.connector.delete(action)

        self.connection.connector.raise_error_when_not_in_status(200)
        return {"msg": r["msg"]}

    def test(self):
        return {"msg": ""}
