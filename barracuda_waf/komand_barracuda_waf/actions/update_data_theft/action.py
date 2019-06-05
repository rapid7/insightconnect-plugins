import komand
from .schema import UpdateDataTheftInput, UpdateDataTheftOutput



class UpdateDataTheft(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_data_theft',
                description='Updates the values of given parameters in the given data theft element',
                input=UpdateDataTheftInput(),
                output=UpdateDataTheftOutput())

    def run(self, params={}):
        action = "security_policies"
        self.connection.connector.check_required_params(params, [
            "policy_id",
            "id"])

        action = action + "/" + params.get("policy_id") + "/data_theft_protection/" + params.get("id")

        r = self.connection.connector.put(action, self.connection.connector.get_dict_from_params(params, [
            "action",
            "initial_characters_to_keep",
            "identity_theft_type",
            "enabled",
            "custom_identity_theft_type",
            "name",
            "trailing_characters_to_keep"]))

        self.connection.connector.raise_error_when_not_in_status(202)

        return {"id": r["id"]}

    def test(self):
        return {"id": ""}
