import komand
from .schema import ConnectionSchema
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.dev_key = None
        self.url = "https://pastebin.com"
        self.scraping_url = "https://scrape.pastebin.com/api_scraping.php"
        self.post_url = self.url + "/api/api_post.php"

    def connect(self, params):
        self.dev_key = params.get("key").get("secretKey")

        payload = {"api_dev_key": self.dev_key,
                   "api_user_name":params.get("credentials").get("username"),
                   "api_user_password":params.get("credentials").get("password")
        }

        req_url = self.url + "/api/api_login.php"
        resp = requests.post(req_url, data=payload)

        response = resp.content.decode()
        if response.startswith("Bad API request"):
            self.logger.info("Connecting: Bad user login, continuing anonymous")
        else:
            self.user_key = response
            self.logger.info("Connecting: Successful user login")
