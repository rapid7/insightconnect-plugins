import komand
from .schema import DeleteTrustedHostInput, DeleteTrustedHostOutput


class DeleteTrustedHost(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_trusted_host',
                description='Deletes the given trusted host',
                input=DeleteTrustedHostInput(),
                output=DeleteTrustedHostOutput())

    def run(self, params={}):
        action = "trusted_host_groups/"
        self.connection.connector.check_required_params(params, [
            "name",
            "group_name"])

        action = action + params.get("group_name") + "/trusted_hosts/" + params.get("name")
        r = self.connection.connector.delete(action)

        self.connection.connector.raise_error_when_not_in_status(200)
        return {"msg": r["msg"]}

    def test(self):
        return {"msg": ""}
