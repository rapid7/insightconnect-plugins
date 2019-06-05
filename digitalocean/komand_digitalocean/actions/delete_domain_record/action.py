import komand
import requests
from .schema import DeleteDomainRecordInput, DeleteDomainRecordOutput


class DeleteDomainRecord(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='delete_domain_record',
            description='Deletes a domain record from the domain name',
            input=DeleteDomainRecordInput(),
            output=DeleteDomainRecordOutput())

    def run(self, params={}):
        url = "https://api.digitalocean.com/v2/domains/{domain_name}/records/{record_id}"
        domain_name = params["domain_name"]
        record_id = params["record_id"]

        try:
            response = requests.delete(headers=self.connection.headers,
                                       url=url.format(domain_name=domain_name, record_id=record_id))

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
