import komand
from .schema import RetrieveAttackGroupsInput, RetrieveAttackGroupsOutput


class RetrieveAttackGroups(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='retrieve_attack_groups',
                description='Lists all attack groups with attack group ID',
                input=RetrieveAttackGroupsInput(),
                output=RetrieveAttackGroupsOutput())

    def run(self, params={}):
        action = "security_policies/"
        policy_id = params.get("policy_id")
        if not policy_id:
            self.connection.connector.raise_error("Empty argument policy_id")

        action = action + "/" + policy_id + "/attack_groups"

        attack_group_id = params.get("attack_group_id")
        if attack_group_id:
            action = action + "/" + attack_group_id

        r = self.connection.connector.get(action)
        self.connection.connector.raise_error_when_not_in_status(200)

        if 'data' not in r and attack_group_id:
            data = [r]
        elif 'data' not in r:
            self.connection.connector.raise_error("Empty returned value")
        else:
            data = r['data']

        return {"action_policy": data}

    def test(self):
        return {"action_policy": [{
            "action": "",
            "denyResponse": "",
            "followUpAction": "",
            "followUpActionTime": 0,
            "redirectUrl": "",
            "responsePage": ""
        }]}
