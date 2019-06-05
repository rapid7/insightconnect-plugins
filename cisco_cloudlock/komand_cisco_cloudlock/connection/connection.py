import komand
from .schema import ConnectionSchema
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.CLIENT = None

    def connect(self, params={}):
        api_key_prelim = params.get("api_key").get("secretKey")
        api_key = "Bearer %s" % api_key_prelim  # Prefix token with 'Bearer ' to comply with header requirement

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": api_key
        }

        self.CLIENT = requests.Session()
        self.CLIENT.headers.update(headers)
