import komand
from .schema import ScrapeInput, ScrapeOutput
# Custom imports below
import time
import json
import urllib
import ssl
import os
import re
#from Queue import Queue
from threading import Thread
import requests

class Scrape(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='scrape',
                description='Scrape the most recent pastes',
                input=ScrapeInput(),
                output=ScrapeOutput())

    def run(self, params={}):
        r = requests.session()
        url = self.connection.scraping_url

        pattern = re.compile(params.get("pattern"))
        req_params = {
            "api_dev_key": self.connection.dev_key,
            "limit": params.get("limit", "100"),
        }
        try:
            resp = r.post(url, data=req_params)  #urllib.urlopen(self.connection.scraping_url, urllib.urlencode(req_params), context=ctx)
        except Exception as e:
            self.logger.error("An error occurred ", e)
            raise
        data = resp.content.decode()
        data = json.loads(data)

        paste_list = []
        #pastes_raw = request.read()
        if resp.text.startswith("YOUR IP:"):
            self.logger.error('Scraping: IP not whitelisted')
        else:
            for item in data:
                scrape_url = item.get("scrape_url")
                resp = requests.get(scrape_url)
                response = resp.content.decode()
            if pattern.search(response) is not None:
                paste_list.append(item)
        results = dict()
        results["paste_list"] = paste_list
        self.logger.info(results)
        return results

    def test(self):
        if self.connection.user_key:
            return {"success": True}
        else:
            return {"success": False}

