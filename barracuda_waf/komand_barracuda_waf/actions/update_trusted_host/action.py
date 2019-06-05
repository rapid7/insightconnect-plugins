import komand
from .schema import UpdateTrustedHostInput, UpdateTrustedHostOutput


class UpdateTrustedHost(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_trusted_host',
                description='Updates the values of given parameters',
                input=UpdateTrustedHostInput(),
                output=UpdateTrustedHostOutput())

    def run(self, params={}):
        action = "trusted_host_groups"
        name = params.get("name")
        group_name = params.get("group_name")
        if not name or not group_name:
            self.connection.connector.raise_error("Policy ID, attack group ID and attack ID can't be empty")

        action = action + "/" + group_name + "/trusted_hosts/" + name

        del params["name"]
        del params["group_name"]

        if params.get("address"):
            params["ip_address"] = params.get("address")
            del params["address"]

        r = self.connection.connector.put(action, params)

        if "error" in r and "status" in r["error"] and r["error"]["status"] == 400:
            self.connection.connector.raise_error("Problem with update")

        return {"id": r["id"]}

    def test(self):
        return {"id": ""}
