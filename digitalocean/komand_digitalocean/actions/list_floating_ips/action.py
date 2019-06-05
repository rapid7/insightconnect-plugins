import komand
import requests
from .schema import ListFloatingIpsInput, ListFloatingIpsOutput


class ListFloatingIps(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='list_floating_ips',
            description='List all floating IPs from the account',
            input=ListFloatingIpsInput(),
            output=ListFloatingIpsOutput())

    def run(self, params={}):
        url = "https://api.digitalocean.com/v2/floating_ips"

        try:
            response = requests.get(headers=self.connection.headers, url=url)

            if response.status_code == 200:
                floating_ips = response.json()["floating_ips"]

                for floating_ip in floating_ips:
                    if floating_ip["droplet"] is None:
                        floating_ip.pop("droplet", None)

                return {"floating_ips": floating_ips}
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
