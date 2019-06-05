import komand
from .schema import UpdateContentRuleInput, UpdateContentRuleOutput


class UpdateContentRule(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_content_rule',
                description='Updates the values of given parameters in the given content rule',
                input=UpdateContentRuleInput(),
                output=UpdateContentRuleOutput())

    def run(self, params={}):
        action = "virtual_services"
        self.connection.connector.check_required_params(params, [
            "id",
            "virtual_service_id"])

        action = action + "/" + params.get("virtual_service_id") + "/content_rules/" + params.get("id")

        del params["id"]
        del params["virtual_service_id"]

        r = self.connection.connector.put(action, params)

        self.logger.info(r)

        if "error" in r and "status" in r["error"]:
            self.connection.connector.raise_error("Problem with update")

        return {"id": r["id"]}

    def test(self):
        return {"id": ""}
