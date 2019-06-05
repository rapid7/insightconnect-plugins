import komand
import json
import requests
from .schema import AddDomainRecordInput, AddDomainRecordOutput


class AddDomainRecord(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='add_domain_record',
            description='Adds a domain record to the specified domain name',
            input=AddDomainRecordInput(),
            output=AddDomainRecordOutput())

    def run(self, params={}):
        domain_name = params['domain_name']
        url = "https://api.digitalocean.com/v2/domains/{domain_name}/records"

        payload = {
          "type": params['record_type'],
          "name": params['name'],
          "data": params['data'],
          "priority": params['priority'],
          "port": params['port'],
          "weight": params['weight']
        }

        try:
            response = requests.post(headers=self.connection.headers,
                                    url=url.format(domain_name=domain_name),
                                    data=json.dumps(payload))

            if response.status_code == 201:
                self.logger.info("Run: Success")
                r = response.json()
                self.logger.info('Response: %s', r)
                if r.get('domain_record').get('priority') is None:
                    del r['domain_record']['priority']
                if r.get('domain_record').get('weight') is None:
                    del r['domain_record']['weight']
                if r.get('domain_record').get('port') is None:
                    del r['domain_record']['port']
                self.logger.info('Cleaned Response: %s', r)
                return r
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
