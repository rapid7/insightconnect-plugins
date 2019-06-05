import komand
import requests
from .schema import DeleteDropletInput, DeleteDropletOutput


class DeleteDroplet(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='delete_droplet',
            description='Deletes a droplet from the account',
            input=DeleteDropletInput(),
            output=DeleteDropletOutput())

    def run(self, params={}):
        url = "https://api.digitalocean.com/v2/droplets/{droplet_id}"
        droplet_id = str(params["droplet_id"])

        try:
            response = requests.delete(headers=self.connection.headers, url=url.format(droplet_id=droplet_id))

            if response.status_code == 204:
                return {"success": True}
            else:
                self.logger.error("Status code: %s, message: %s", response.status_code, response.json()["message"])
                Exception('Non-204 status code received')
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
