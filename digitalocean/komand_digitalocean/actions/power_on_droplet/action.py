import komand
import json
import requests
from .schema import PowerOnDropletInput, PowerOnDropletOutput


class PowerOnDroplet(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='power_on_droplet',
            description='Powers on the droplet',
            input=PowerOnDropletInput(),
            output=PowerOnDropletOutput())

    def run(self, params={}):
        url = "https://api.digitalocean.com/v2/droplets/{droplet_id}/actions"
        droplet_id = str(params["droplet_id"])

        payload = {"type": "power_on"}

        try:
            response = requests.post(headers=self.connection.headers,
                                     url=url.format(droplet_id=droplet_id), data=json.dumps(payload))

            if response.status_code == 201:
                return {"success": True}
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
