import komand
import json
import requests
from .schema import SubmitLogDataInput, SubmitLogDataOutput


class SubmitLogData(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_log_data',
                description='Submits JSON to a specified log within an InsightOps logset',
                input=SubmitLogDataInput(),
                output=SubmitLogDataOutput())

    def run(self, params={}):
        url = self.connection.postdataurl
        url = url + params["logset_container_id"]
        payload = params["data"]
        try:
            resp = requests.post(url, json=payload)
            self.logger.info("Status code: " + str(resp.status_code))
            if resp.status_code == 204:
                return json.loads('{"success": true}')
        except Exception:
            self.logger.info(Exception)
            raise

    def test(self):
        service_url = "/management/logs"
        url = self.connection.insighturl + service_url
        headers = {'x-api-key': self.connection.api_key}
        try:
            resp = requests.get(url, headers=headers)
            cleaned_resp = komand.helper.clean(resp.json())
            return cleaned_resp
        except Exception:
            self.logger.info(Exception)
            raise
