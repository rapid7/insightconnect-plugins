import komand
import requests
from .schema import ListSnapshotsOutput, ListSnapshotsInput


class ListSnapshots(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='list_snapshots',
            description='Lists all snapshots belonging to the account',
            input=ListSnapshotsInput(),
            output=ListSnapshotsOutput())

    def run(self, params={}):
        url = "https://api.digitalocean.com/v2/snapshots"

        try:
            response = requests.request("GET", url, headers=self.connection.headers)

            if response.status_code == 200:
                return {"snapshots": response.json()["snapshots"]}
            else:
                self.logger.error("Status code: %s, message: %s", response.status_code, response.json()["message"])
                Exception('Non-200 status code received')
        except requests.exceptions.RequestException:
            self.logger.error("An unexpected error occurred during the API request")
            raise

    def test(self):
        url = "https://api.digitalocean.com/v2/account"

        try:
            response = requests.get(headers=self.connection.headers, url=url)

            if response.status_code == 200:
                return {}
            else:
                self.logger.error("Status code: %s, message: %s", response.status_code, response.json()["message"])
                Exception("Non-200 status code received")
        except requests.exceptions.RequestException:
            self.logger.error("An unexpected error occurred during the API request")
