import komand
from .. import demo_test
from .schema import LookupIPAddressInput, LookupIPAddressOutput


class LookupIPAddress(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup_IP_address',
                description='This action is used to query for data related to a specific IP address',
                input=LookupIPAddressInput(),
                output=LookupIPAddressOutput())

    def run(self, params={}):
        try:
            ip_address = params.get("IP_address")
            address_report = self.connection.client.lookup_ip(ip_address)
            return address_report
        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        return demo_test.demo_test(self.connection.token, self.logger)
