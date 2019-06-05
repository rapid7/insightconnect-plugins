import komand
from .schema import GetReportInput, GetReportOutput
# Custom imports below
import json
import requests
import base64


class GetReport(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_report',
                description='Returns the report associated with the specified task ID',
                input=GetReportInput(),
                output=GetReportOutput())

    def run(self, params={}):
        server = self.connection.server
        task_id = params.get('task_id', '')
        desired_format = params.get('format', '')

        if desired_format:
            endpoint = server + "/tasks/report/%d/%s" % (task_id, desired_format)
        else:
            endpoint = server + "/tasks/report/%d" % (task_id)
        
        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            ctype = r.headers['Content-Type']
            if ctype.startswith("application/x-tar") or ctype.startswith("application/octet-stream") or ctype.startswith("application/json") or ctype.startswith("text/html"):
                content = r.content
                return {'report': base64.b64encode(content).decode('UTF-8')}
        
        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        out = self.connection.test()
        out['report'] = ''
        return out
