import komand
from .schema import RetrieveContentRulesInput, RetrieveContentRulesOutput


class RetrieveContentRules(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='retrieve_content_rules',
                description='Lists all content rules with rule ID',
                input=RetrieveContentRulesInput(),
                output=RetrieveContentRulesOutput())

    def run(self, params={}):
        action = "virtual_services"
        virtual_service_id = params.get("virtual_service_id")
        if not virtual_service_id:
            self.connection.connector.raise_error("Empty argument virtual_service_id")

        action = action + "/" + virtual_service_id + "/content_rules"

        rule_id = params.get("rule_id")
        if rule_id:
            action = action + "/" + rule_id

        r = self.connection.connector.get(action)
        self.connection.connector.raise_error_when_not_in_status(200)

        if 'data' not in r and rule_id:
            data = [r]
        elif 'data' not in r:
            self.connection.connector.raise_error("Empty returned value")
        else:
            data = r['data']

        for k, val in enumerate(data):
            if "servers" not in data[k] and not data[k]["servers"]:
                data[k]["servers"] = []

        return data

    def test(self):
        return [{
            "comments": "",
            "extended_match": "",
            "extended_match_sequence": 0,
            "host_match": "",
            "id": "",
            "lb_algorithm": "",
            "name": "",
            "persistence_method": "",
            "servers": [],
            "service_name": "",
            "url_match": ""
        }]
