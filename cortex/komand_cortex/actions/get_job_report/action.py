import komand
from .schema import GetJobReportInput, GetJobReportOutput
# Custom imports below
from cortex4py.api import CortexException


class GetJobReport(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_job_report',
                description='List report of a given job, identified by its ID',
                input=GetJobReportInput(),
                output=GetJobReportOutput())

    def run(self, params={}):
        """TODO: Run action"""
        client = self.connection.client

        try:
            out = client.get_job_report(params.get('job_id'))
        except CortexException:
            self.logger.info('Failed to get job report')
            raise

        return out

    def test(self):
        """TODO: Test action"""
        client = self.connection.client

        try:
            out = client.get_analyzers()
        except CortexException:
            self.logger.info('Failed to test getting analyzers')
            raise

        return { 'report': {} }
