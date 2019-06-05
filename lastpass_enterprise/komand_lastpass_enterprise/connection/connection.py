import komand
import requests
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        cid = params.get('account')
        provhash = params.get('provhash').get('secretKey')

        self.cid = cid
        self.provhash = provhash

    def test(self):
        cid = self.cid
        provhash = self.provhash

        # Use the "Get Shared Folder Data" command to test authentication
        cmd = "getsfdata"

        # API URL
        url = "https://lastpass.com/enterpriseapi.php"

        # Set headers
        headers = {'content-type': "application/json"}

        # Set POST data
        data = {'provhash': provhash, 'cid': cid, 'cmd': cmd}

        # Generate request
        response = requests.post(url, json=data, headers=headers)

        # Check authentication
        if "Authorization Error" in response.text:
            self.logger.error(f"Connection test failed.\n"
                              f"Response was {response.text}")
            raise Exception("Authorization Error")
