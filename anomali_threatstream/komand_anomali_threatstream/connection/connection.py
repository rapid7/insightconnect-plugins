import komand
from .schema import ConnectionSchema
# Custom imports below
import requests
from requests import Session, Request
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import logging


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.session = Session()
        self.request = Request()

    def connect(self, params):
        # Silence warnings and request logging
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        logging.getLogger('urllib3').setLevel(logging.CRITICAL)

        username, threatstream_url, api_key = params["username"], \
            params["url"], params["api_key"]["secretKey"]
        # Set up the base request
        self.request.url = threatstream_url + "/api/v1"
        self.request.verify = params.get("ssl_verify")
        self.request.params = {
            "username": username,
            "api_key": api_key
        }
