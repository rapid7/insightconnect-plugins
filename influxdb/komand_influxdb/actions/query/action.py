import komand
import requests
from .schema import QueryInput, QueryOutput


class Query(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='query',
                description='Query data and manage databases, retention policies, and users',
                input=QueryInput(),
                output=QueryOutput())

    def run(self, params={}):
        server = self.connection.server
        database_name = params.get('database_name', '')
        chunked = params.get('chunked', '')
        epoch = params.get('epoch', '')
        username = params.get('username', '')
        password = params.get('password', '')
        query = params.get('query', '')

        endpoint = server + "/query?db=%s" % (database_name)

        if chunked:
            endpoint += "&chunked=%s" % (chunked)
        if epoch:
            endpoint += "&epoch=%s" % (epoch)
        if username:
            endpoint += "&username=%s" % (username)
        if password:
            endpoint += "&password=%s" % (password)

        endpoint += "&q=%s" % (query)

        r = requests.post(endpoint)
        response = r.json()

        for result in response['results']:
            if "series" in result:
                new_points = []
                for point in result['series']:
                    old_values = point['values']
                    new_values = []
                    name = point['name']
                    columns = point['columns']
                    for entry in old_values:
                        temp_list = []
                        for item in entry:
                            temp_list.append(str(item))
                        new_values.append(temp_list)
                    new_point = {
                        "name": point['name'],
                        "columns": point['columns'],
                        "values": new_values
                    }
                    new_points.append(new_point)
                result['series'] = new_points

        return response

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
