import komand
from .schema import DeleteTrustedHostGroupInput, DeleteTrustedHostGroupOutput


class DeleteTrustedHostGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_trusted_host_group',
                description='Deletes the given service group',
                input=DeleteTrustedHostGroupInput(),
                output=DeleteTrustedHostGroupOutput())

    def run(self, params={}):
        action = "trusted_host_groups/"
        self.connection.connector.check_required_params(params, ["name"])

        action = action + params.get("name")
        r = self.connection.connector.delete(action)

        self.connection.connector.raise_error_when_not_in_status(200)
        return {"msg": r["msg"]}

    def test(self):
        return {"msg": ""}
