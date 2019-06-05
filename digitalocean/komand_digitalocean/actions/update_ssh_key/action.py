import komand
import json
import requests
from .schema import UpdateSshKeyInput, UpdateSshKeyOutput


class UpdateSshKey(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='update_ssh_key',
            description='Updates an SSH key from the account',
            input=UpdateSshKeyInput(),
            output=UpdateSshKeyOutput())

    def run(self, params={}):
        url = "https://api.digitalocean.com/v2/account/keys/{key_id}"
        key_id = params["ssh_key_id"]
        new_name = params["name"]

        payload = {'name': new_name}

        try:
            response = requests.put(headers=self.connection.headers,
                                    url=url.format(key_id=key_id), data=json.dumps(payload))

            if response.status_code == 200:
                return response.json()
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
