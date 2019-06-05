import komand
from .schema import DeleteDataTheftInput, DeleteDataTheftOutput


class DeleteDataTheft(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_data_theft',
                description='Deletes the given data theft element',
                input=DeleteDataTheftInput(),
                output=DeleteDataTheftOutput())

    def run(self, params={}):
        action = "security_policies/"
        self.connection.connector.check_required_params(params, [
            "policy_id",
            "id"])

        action = action + params.get("policy_id") + "/data_theft_protection/" + params.get("id")
        r = self.connection.connector.delete(action)

        self.connection.connector.raise_error_when_not_in_status(200)
        return {"msg": r["msg"]}

    def test(self):
        return {"msg": ""}
