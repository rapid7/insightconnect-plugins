import komand
from .schema import CreateVirtualServiceInput, CreateVirtualServiceOutput


class CreateVirtualService(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_virtual_service',
                description='Creates a virtual service with the given values',
                input=CreateVirtualServiceInput(),
                output=CreateVirtualServiceOutput())

    def run(self, params={}):
        action = "virtual_services"
        self.connection.connector.check_required_params(params, [
            "name",
            "type",
            "port",
            "address",
            "address_version"])

        r = self.connection.connector.post(action, self.connection.connector.get_dict_from_params(params, [
            "name",
            "group",
            "type",
            "port",
            "address",
            "vsite",
            "address_version",
            "certificate",
            "service_hostname"]))

        self.connection.connector.raise_error_when_not_in_status(201)

        return {"id": r["id"]}

    def test(self):
        return {"id": ""}
