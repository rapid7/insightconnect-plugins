import komand
from .schema import CreateTrustedHostGroupInput, CreateTrustedHostGroupOutput


class CreateTrustedHostGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_trusted_host_group',
                description='Creates a trusted host group with the given name',
                input=CreateTrustedHostGroupInput(),
                output=CreateTrustedHostGroupOutput())

    def run(self, params={}):
        action = "trusted_host_groups"
        self.connection.connector.check_required_params(params, ["name"])

        r = self.connection.connector.post(action, self.connection.connector.get_dict_from_params(params, [
            "name"
        ]))

        self.connection.connector.raise_error_when_not_in_status(201)

        return {"id": r["id"]}

    def test(self):
        return {"id": ""}
