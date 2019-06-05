import komand
from .schema import RetrieveAttackActionsInput, RetrieveAttackActionsOutput


class RetrieveAttackActions(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='retrieve_attack_actions',
                description='Lists all attack actions for the given attack group with actionID',
                input=RetrieveAttackActionsInput(),
                output=RetrieveAttackActionsOutput())

    def run(self, params={}):
        action = "security_policies"
        policy_id = params.get("policy_id")
        attack_group_id = params.get("attack_group_id")
        if not policy_id or not attack_group_id:
            self.connection.connector.raise_error("Policy_id and attack_group_id can't be null")

        action = action + "/" + policy_id + "/attack_groups/" + attack_group_id + "/actions"

        action_id = params.get("action_id")
        if action_id:
            action = action + "/" + action_id

        r = self.connection.connector.get(action)
        self.connection.connector.raise_error_when_not_in_status(200)

        if 'data' not in r and action_id:
            data = [r]
        elif 'data' not in r:
            self.connection.connector.raise_error("Empty returned value")
        else:
            data = r['data']

        for k, val in enumerate(data):
            if data[k]["follow_up_action_time"]:
                data[k]["follow_up_action_time"] = int(data[k]["follow_up_action_time"])

        return {"action_policy": data}

    def test(self):
        return {"action_policy": [{"action": "",
                                  "deny_response": "send_response",
                                  "follow_up_action": "none",
                                  "follow_up_action_time": 60,
                                  "redirect_url": "",
                                  "numeric_id": "invalid_soap_envelope",
                                  "id": "invalid-soap-envelope",
                                  "name": "invalid-soap-envelope",
                                  "attack_group": "xmlfw-soap-violations",
                                  "response_page": "default"}]}
