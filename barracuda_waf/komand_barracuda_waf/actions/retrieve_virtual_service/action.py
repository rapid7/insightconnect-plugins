import komand
from .schema import RetrieveVirtualServiceInput, RetrieveVirtualServiceOutput


class RetrieveVirtualService(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='retrieve_virtual_service',
                description='Lists all virtual services',
                input=RetrieveVirtualServiceInput(),
                output=RetrieveVirtualServiceOutput())

    def run(self, params={}):
        action = "virtual_services"

        service_id = params.get("id")
        if service_id:
            action = action + "/" + service_id

        r = self.connection.connector.get(action)
        self.connection.connector.raise_error_when_not_in_status(200)

        if 'data' not in r and service_id:
            data = [r]
        elif 'data' not in r:
            self.connection.connector.raise_error("Empty returned value")
        else:
            data = r['data']

        return data

    def test(self):
        return [{
            "address": "",
            "address_version": "",
            "comments": [],
            "content_rules": [],
            "enable": False,
            "enable_access_log": False,
            "group": "",
            "id": "",
            "load_balance": [],
            "name": "",
            "port": 0,
            "security": [],
            "servers": [],
            "ssl_off_loading": []
        }]
