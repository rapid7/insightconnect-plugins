import komand
from .schema import VsitesInput, VsitesOutput


class Vsites(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='vsites',
                description='Lists all vsites',
                input=VsitesInput(),
                output=VsitesOutput())

    def run(self, params={}):
        action = "vsites"
        vsite_id = params.get("id")
        if vsite_id:
            action = action + "/" + vsite_id
        r = self.connection.connector.get(action)

        self.connection.connector.raise_error_when_not_in_status(200)

        if 'data' not in r and vsite_id:
            data = [r]
        elif 'data' not in r:
            self.connection.connector.raise_error("Empty argument attack_group_ID")
        else:
            data = r['data']

        for i, val in enumerate(data):
            if 'comments' not in data[i]:
                data[i]['comments'] = []
            if data[i]['comments'] is None:
                data[i]['comments'] = []

            if data[i]['active_on'] is not None:
                data[i]['active_on'] = int(data[i]['active_on'])
            else:
                data[i]['active_on'] = 0

            if data[i]['service_group'] is None:
                data[i]['service_group'] = []

            if data[i]['service_groups'] is None:
                data[i]['service_groups'] = []

        return {"vsites": data}

    def test(self):
        return {"vsites": [{
            "id": "",
            "service_group": [],
            "name": "",
            "active_on": 0,
            "comments": []
        }]}
