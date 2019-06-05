import komand
from .schema import DeleteVirtualServiceInput, DeleteVirtualServiceOutput


class DeleteVirtualService(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_virtual_service',
                description='Delete virtual service with service ID',
                input=DeleteVirtualServiceInput(),
                output=DeleteVirtualServiceOutput())

    def run(self, params={}):
        action = "virtual_services/"
        self.connection.connector.check_required_params(params, ["id"])

        action = action + params.get("id")
        r = self.connection.connector.delete(action)

        self.connection.connector.raise_error_when_not_in_status(200)
        return {"msg": r["msg"]}

    def test(self):
        return {"msg": ""}
