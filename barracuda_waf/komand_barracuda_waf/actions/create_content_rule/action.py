import komand
from .schema import CreateContentRuleInput, CreateContentRuleOutput

from komand_barracuda_waf.util.connector import Connector


class CreateContentRule(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_content_rule',
                description='Creates a content rule for the given service',
                input=CreateContentRuleInput(),
                output=CreateContentRuleOutput())

    def run(self, params={}):
        if not params or not params.get("virtual_service_id"):
            Connector.raise_error("Virtual service id can't be null")

        action = "virtual_services/" + params.get("virtual_service_id") + "/content_rules"
        Connector.check_required_params(params, [
            "name",
            "host_match",
            "url_match",
            "extended_match",
            "extended_match_sequence"])
        r = self.connection.connector.post(action, Connector.get_dict_from_params(params, [
            "name",
            "status",
            "web_firewall_policy",
            "host_match",
            "url_match",
            "extended_match",
            "extended_match_sequence"]))

        self.connection.connector.raise_error_when_not_in_status(201)

        return {"id": r["id"]}

    def test(self):
        return {"id": ""}
