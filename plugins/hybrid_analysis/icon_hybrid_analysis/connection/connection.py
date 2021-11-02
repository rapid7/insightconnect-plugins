import komand
from .schema import ConnectionSchema

# Custom imports below
import requests


class Connection(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def get(self, hash_):
        if self.params.get("url"):

            url = self.params.get("url") + "/scan/" + hash_
        else:
            url = "https://www.hybrid-analysis.com/api" + "/scan/" + hash_

        return requests.get(
            url,
            {
                "apikey": self.params.get("api_key").get("secretKey"),
                "secret": self.params.get("api_token").get("secretKey"),
            },
            headers={
                "User-Agent": "Bogus UA",
                "From": "youremail@domain.com",  # This is another valid field
            },
        )

    def connect(self, params={}):
        """ """
        self.logger.info("Connecting")
        self.params = params

    def test(self):
        """Test action"""
        result = self.lookup("040c0111aef474d8b7bfa9a7caa0e06b4f1049c7ae8c66611a53fc2599f0b90f")
        self.logger.info("Got test result: %s", result)
        return result
