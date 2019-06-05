import komand
from .schema import RerunReportInput, RerunReportOutput
# Custom imports below
import json
import requests


class RerunReport(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='rerun_report',
                description='Re-run reporting for task associated with the specified task ID',
                input=RerunReportInput(),
                output=RerunReportOutput())

    def run(self, params={}):
        server = self.connection.server
        task_id = params.get('task_id', '')
        endpoint = server + "/tasks/rereport/%d" % (task_id)

        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            response = r.json()
            return response

        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        out = self.connection.test()
        out['success'] = True
        return out
