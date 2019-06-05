import komand
import requests
from .schema import ListSshKeysInput, ListSshKeysOutput


class ListSshKeys(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='list_ssh_keys',
            description='Lists all SSH keys from the account',
            input=ListSshKeysInput(),
            output=ListSshKeysOutput())

    def run(self, params={}):
        url = "https://api.digitalocean.com/v2/account/keys"

        try:
            response = requests.get(headers=self.connection.headers, url=url)

            if response.status_code == 200:
                return {"ssh_keys": response.json()["ssh_keys"]}
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
