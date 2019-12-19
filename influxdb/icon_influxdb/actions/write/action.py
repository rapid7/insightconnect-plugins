import komand
import requests
from .schema import WriteInput, WriteOutput


class Write(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='write',
                description='Write data to a pre-existing database',
                input=WriteInput(),
                output=WriteOutput())

    def run(self, params={}):
        server = self.connection.server
        database_name = params.get('database_name', '')
        consistency = params.get('consistency', '')
        precision = params.get('precision', '')
        retention_policy = params.get('retention_policy', '')
        username = params.get('username', '')
        password = params.get('password', '')
        data = params.get('data', '')

        endpoint = server + "/write?db=%s" % (database_name)

        if consistency:
            endpoint += "&consistency=%s" % (consistency)
        if precision:
            endpoint += "&precision=%s" % (precision)
        if retention_policy:
            endpoint += "&rp=%s" % (retention_policy)
        if username:
            endpoint += "&username=%s" % (username)
        if password:
            endpoint += "&password=%s" % (password)

        r = requests.post(endpoint, data=data)

        status_code = r.status_code
        if status_code == 204:
            message = "Success!"
        elif status_code in [400, 401, 404, 500]:
            message = r.json()['error']

        return {"status_code": status_code, "message": message}

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
