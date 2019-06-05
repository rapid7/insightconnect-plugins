import komand
import json
import requests
from .schema import UpdateDomainRecordInput, UpdateDomainRecordOutput


class UpdateDomainRecord(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='update_domain_record',
            description='Updates a domain record on the domain name',
            input=UpdateDomainRecordInput(),
            output=UpdateDomainRecordOutput())

    def run(self, params={}):
        url = "https://api.digitalocean.com/v2/domains/{domain_name}/records/{record_id}"

        domain_name = params["domain_name"]
        record_id = params["record_id"]
        record_property = params["property"]
        value = params["value"]

        payload = {record_property: value}

        try:
            response = requests.put(headers=self.connection.headers,
                                    url=url.format(domain_name=domain_name, record_id=record_id),
                                    data=json.dumps(payload))

            if response.status_code == 200:
                return {"success": True}
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
