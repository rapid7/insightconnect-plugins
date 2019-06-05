import komand
from .schema import CreateGlobalAclRuleInput, CreateGlobalAclRuleOutput



class CreateGlobalAclRule(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_global_acl_rule',
                description='Adds a global ACL rule with the given values',
                input=CreateGlobalAclRuleInput(),
                output=CreateGlobalAclRuleOutput())

    def run(self, params={}):
        action = "security_policies"
        self.connection.connector.check_required_params(params, [
            "policy_id",
            "global_acl"])
        self.connection.connector.check_required_params(params.get("global_acl"), [
            "name",
            "extended_match"])
        if "extended_match_sequence" not in params.get("global_acl"):
            self.connection.connector.raise_error("Required param: extended_match_sequence")

        action = action + "/" + params.get("policy_id") + "/global_acls"

        r = self.connection.connector.post(action, self.connection.connector.get_dict_from_params(params.get("global_acl"), [
            "name",
            "extended_match",
            "extended_match_sequence"]))

        self.connection.connector.raise_error_when_not_in_status(201)

        return {"id": r["id"]}

    def test(self):
        return {"id": ""}
