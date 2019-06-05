import komand
import time
from .schema import ScrapingInput, ScrapingOutput
# Custom imports below
import json
import re
from queue import Queue
from threading import Thread
from ...util import utils
import requests


class Scraping(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='scraping',
                description='Scrape most recent pastes every interval for a given pattern',
                input=ScrapingInput(),
                output=ScrapingOutput())

    def run(self, params={}):
        """Run the trigger"""
        pattern = re.compile(params.get("pattern"))
        req_params = {
            "api_dev_key": self.connection.dev_key,
            "limit": params.get("limit", "100"),
            }

        if params.get("language") is not "All":
            req_params['lang'] = utils.format_dict.get(params.get("language"))

        queue = Queue()
        old_pastes = []

        # Create 8 worker threads
        for x in range(8):
            worker = ScrapeWorker(self, pattern, queue)
            worker.daemon = True
            worker.start()

        while True:
            new_pastes = []
            resp = requests.post(self.connection.scraping_url, data=req_params)
            pastes_raw = resp.content.decode()
            if pastes_raw.startswith("YOUR IP:"):
                response = pastes_raw.replace("\r\n\r\n", "")
                raise Exception(response)
            else:
                pastes = json.loads(pastes_raw)
            for paste in pastes:
                paste_key = paste.get("key")
                if paste_key not in old_pastes:
                    queue.put(paste)
                new_pastes.append(paste_key)
                old_pastes = new_pastes
            time.sleep(params.get('frequency', 300))

    def test(self):
        if self.connection.user_key:
            return {"success": True}
        else:
            return {"success": False}


class ScrapeWorker(Thread):
    def __init__(self, trigger, pattern, queue):
        Thread.__init__(self)
        self.queue = queue
        self.pattern = pattern
        self.trigger = trigger

    def run(self):
        while True:
            paste = self.queue.get()
            paste_req = requests.get(paste.get("scrape_url"))
            paste_text = paste_req.content.decode()
            if self.pattern.search(paste_text) is not None:
                self.trigger.send(paste)
