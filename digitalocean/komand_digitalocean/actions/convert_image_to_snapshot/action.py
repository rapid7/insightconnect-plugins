import komand
import json
import requests
from .schema import ConvertImageToSnapshotInput, ConvertImageToSnapshotOutput


class ConvertImageToSnapshot(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='convert_image_to_snapshot',
            description='Converts an image to a snapshot',
            input=ConvertImageToSnapshotInput(),
            output=ConvertImageToSnapshotOutput())

    def run(self, params={}):
        url = "https://api.digitalocean.com/v2/images/{image_id}/actions"
        payload = {"type": "convert"}

        try:
            response = requests.post(headers=self.connection.headers,
                                     url=url.format(image_id=params['image_id']),
                                     data=json.dumps(payload))

            if response.status_code == 201:
                return {'success': True}
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

