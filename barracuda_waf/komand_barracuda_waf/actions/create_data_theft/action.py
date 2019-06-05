import komand
from .schema import CreateDataTheftInput, CreateDataTheftOutput



class CreateDataTheft(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_data_theft',
                description='Adds a data theft element with the given values',
                input=CreateDataTheftInput(),
                output=CreateDataTheftOutput())

    def run(self, params={}):
        action = "security_policies"
        self.connection.connector.check_required_params(params, [
            "policy_id",
            "name",
            "identity_theft_type"])

        action = action + "/" + params.get("policy_id") + "/data_theft_protection"

        r = self.connection.connector.post(action, self.connection.connector.get_dict_from_params(params, [
            "action",
            "initial_characters_to_keep",
            "identity_theft_type",
            "enabled",
            "custom_identity_theft_type",
            "name",
            "trailing_characters_to_keep"]))

        self.connection.connector.raise_error_when_not_in_status(201)

        return {"id": r["id"]}

    def test(self):
        return {"id": ""}
