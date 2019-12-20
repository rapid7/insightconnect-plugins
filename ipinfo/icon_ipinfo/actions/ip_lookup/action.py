import komand
from .schema import IpLookupInput, IpLookupOutput, Input
# Custom imports below
import requests


class IpLookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='ip_lookup',
                description='Lookup IP Address Information',
                input=IpLookupInput(),
                output=IpLookupOutput())

    def run(self, params={}):

        # Set variables
        ip = params.get(Input.IP)
        token = self.connection.token
        server = self.connection.domain

        # Check if token is provided and set correct URL
        if token:
            url = f"{server}{ip}/json?token={token}"
            self.logger.info('API token was provided by user')
        else:
            url = f"{server}{ip}/json"

        # Make request
        request = requests.get(url)
        dic = request.json()
        return dic
