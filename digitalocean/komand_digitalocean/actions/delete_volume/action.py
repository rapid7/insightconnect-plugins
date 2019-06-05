import komand
import requests
from .schema import DeleteVolumeInput, DeleteVolumeOutput


class DeleteVolume(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='delete_volume',
            description='Deletes a volume (volume must be detached)',
            input=DeleteVolumeInput(),
            output=DeleteVolumeOutput())

    def run(self, params={}):
        url = "https://api.digitalocean.com/v2/volumes/{volume_id}"
        volume_id = params["image_id"]

        url = url.format(volume_id=volume_id)

        try:
            response = requests.delete(headers=self.connection.headers, url=url)

            if response.status_code == 409:
                Exception("Volume is attached, can't delete")
            elif response.status_code == 204:
                return {"success": True}
            else:
                self.logger.error("Status code: %s, message: %s", response.status_code, response.json()["message"])
                Exception('Unsuccessful status code received')
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
