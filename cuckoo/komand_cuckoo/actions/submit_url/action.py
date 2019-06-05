import komand
from .schema import SubmitUrlInput, SubmitUrlOutput
# Custom imports below
import json
import requests


class SubmitUrl(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_url',
                description='Adds a file (from URL) to the list of pending tasks',
                input=SubmitUrlInput(),
                output=SubmitUrlOutput())

    def run(self, params={}):
        server = self.connection.server
        endpoint = server + "/tasks/create/url"
        url = params.get('url', '')
        data = {"url": url}

        try:
            r = requests.post(endpoint, data=data)
            r.raise_for_status()
            response = r.json()
            return response

        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        out = self.connection.test()
        out['task_id'] = 0
        return out