import komand
import requests
from .schema import PingInput, PingOutput


class Ping(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='ping',
                description='Check the status of your InfluxDB instance and your version of InfluxDB',
                input=PingInput(),
                output=PingOutput())

    def run(self, params={}):
        server = self.connection.server
        endpoint = server + "/ping"
        result = {}

        r = requests.get(endpoint)

        if r.status_code == 204:
            result['status'] = "Running"

        result['version'] = r.headers['X-Influxdb-Version']

        return result

    def test(self):
        """TODO: Test action"""
        server = self.connection.server
        endpoint = server + "/ping"
        result = {}

        r = requests.get(endpoint)

        if r.status_code == 204:
            result['status'] = "Running"

        result['version'] = r.headers['X-Influxdb-Version']

        return result
