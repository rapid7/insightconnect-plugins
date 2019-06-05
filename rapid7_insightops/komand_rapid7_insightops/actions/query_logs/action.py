import komand
import requests
from .schema import QueryLogsInput, QueryLogsOutput


class QueryLogs(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='query_logs',
                description='Retrieves logs from InsightOps service',
                input=QueryLogsInput(),
                output=QueryLogsOutput())

    def run(self, params={}):
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
