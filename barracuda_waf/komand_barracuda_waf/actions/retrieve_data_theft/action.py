import komand
from .schema import RetrieveDataTheftInput, RetrieveDataTheftOutput


class RetrieveDataTheft(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='retrieve_data_theft',
                description='Lists data theft element',
                input=RetrieveDataTheftInput(),
                output=RetrieveDataTheftOutput())

    def run(self, params={}):
        action = "security_policies"
        policy_id = params.get("policy_id")
        if not policy_id:
            self.connection.connector.raise_error("Empty argument policy_id")

        action = action + "/" + policy_id + "/data_theft_protection"

        data_id = params.get("id")
        if data_id:
            action = action + "/" + data_id

        r = self.connection.connector.get(action)
        self.connection.connector.raise_error_when_not_in_status(200)

        if 'data' not in r and data_id:
            data = [r]
        elif 'data' not in r:
            self.connection.connector.raise_error("Empty returned value")
        else:
            data = r['data']

        return data

    def test(self):
        return [{
            "action": "",
            "custom_identity_theft_type": "",
            "enabled": "",
            "identity_theft_type": "",
            "initial_characters_to_keep": "",
            "trailing_characters_to_keep": ""
        }]
