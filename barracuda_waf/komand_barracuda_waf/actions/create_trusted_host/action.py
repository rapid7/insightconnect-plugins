import komand
from .schema import CreateTrustedHostInput, CreateTrustedHostOutput


class CreateTrustedHost(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_trusted_host',
                description='Create a trusted host in group',
                input=CreateTrustedHostInput(),
                output=CreateTrustedHostOutput())

    def run(self, params={}):
        action = "trusted_host_groups"
        self.connection.connector.check_required_params(params, [
            "name",
            "address",
            "group_name",
            "mask",
            "address_version"])

        action = action + "/" + params.get("group_name") + "/trusted_hosts"

        r = self.connection.connector.post(action, self.connection.connector.get_dict_from_params(params, [
            "address",
            "mask",
            "comments",
            "name",
            "address_version"]))

        self.connection.connector.raise_error_when_not_in_status(201)

        return {"id": r["id"]}

    def test(self):
        return {"id": ""}
