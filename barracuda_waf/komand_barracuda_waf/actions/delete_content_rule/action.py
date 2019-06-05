import komand
from .schema import DeleteContentRuleInput, DeleteContentRuleOutput


class DeleteContentRule(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_content_rule',
                description='Deletes the given content rule',
                input=DeleteContentRuleInput(),
                output=DeleteContentRuleOutput())

    def run(self, params={}):
        action = "virtual_services/"
        self.connection.connector.check_required_params(params, [
            "virtual_service_id",
            "id"])

        action = action + params.get("virtual_service_id") + "/content_rules/" + params.get("id")
        r = self.connection.connector.delete(action)

        self.connection.connector.raise_error_when_not_in_status(200)
        return {"msg": r["msg"]}

    def test(self):
        return {"msg": ""}
