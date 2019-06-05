import komand
import json
import requests
from .schema import CreateSnapshotFromVolumeInput, CreateSnapshotFromVolumeOutput


class CreateSnapshotFromVolume(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='create_snapshot_from_volume',
            description='Creates a snapshot from a volume',
            input=CreateSnapshotFromVolumeInput(),
            output=CreateSnapshotFromVolumeOutput())

    def run(self, params={}):
        url = "https://api.digitalocean.com/v2/volumes/{volume_id}/snapshots"
        volume_id = params["volume_id"]
        url = url.format(volume_id=volume_id)
        payload = {'name': params["snapshot_name"]}

        try:
            response = requests.post(headers=self.connection.headers, url=url, data=json.dumps(payload))

            if response.status_code == 201:
                return response.json()
            else:
                self.logger.error("Status code: %s, message: %s", response.status_code, response.json()["message"])
                Exception('Non-201 status code received')
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
