import komand
import requests
from .schema import ListDomainRecordsInput, ListDomainRecordsOutput


class ListDomainRecords(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='list_domain_records',
            description='List all domain records belonging to the domain name',
            input=ListDomainRecordsInput(),
            output=ListDomainRecordsOutput())

    def run(self, params={}):
        url = "https://api.digitalocean.com/v2/domains/{domain_name}/records"

        try:
            response = requests.get(headers=self.connection.headers,
                                    url=url.format(domain_name=params["domain_name"]))

            if response.status_code == 200:
                records = response.json()["domain_records"]

                for record in records:
                    if record["port"] is None:
                        record["port"] = 0
                    if record["priority"] is None:
                        record["priority"] = 0
                    if record["weight"] is None:
                        record["weight"] = 0

                return {"domain_records": records}
            else:
                self.logger.error("Status code: %s, message: %s", response.status_code, response.json()["message"])
                Exception('Non-200 status code received')
        except requests.exceptions.RequestException:
            self.logger.error("An unexpected error occurred during the API request")
            raise

        return {}

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
