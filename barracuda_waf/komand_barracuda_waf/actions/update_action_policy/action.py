import komand
from .schema import UpdateActionPolicyInput, UpdateActionPolicyOutput


class UpdateActionPolicy(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_action_policy',
                description='Updates the values of given parameters in the given action policy',
                input=UpdateActionPolicyInput(),
                output=UpdateActionPolicyOutput())

    def run(self, params={}):
        action = "security_policies"
        policy_id = params.get("policy_id")
        attack_group_id = params.get("attack_group_id")
        action_id = params.get("action_id")
        if not policy_id or not attack_group_id or not action_id:
            self.connection.connector.raise_error("Policy ID, attack group ID and attack ID can't be empty")

        action = action + "/" + policy_id + "/attack_groups/" + attack_group_id + "/actions/" + action_id

        r = self.connection.connector.put(action, params.get("action_policy"))

        if "error" in r and "status" in r["error"] and r["error"]["status"] == 400:
            self.connection.connector.raise_error("Problem with update")

        return {"msg": r["msg"]}

    def test(self):
        return {"msg": ""}
