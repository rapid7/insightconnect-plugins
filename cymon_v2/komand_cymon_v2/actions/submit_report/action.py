import komand
from .schema import SubmitReportInput, SubmitReportOutput
# Custom imports below


class SubmitReport(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_report',
                description='Upload a threat report with observables',
                input=SubmitReportInput(),
                output=SubmitReportOutput())

    def run(self, params={}):
        report = params.get('report')
        report = self.connection.api.submit_report(report)
        return {'report': report}

    def test(self):
        return {
            'report': {
                'feed': 'Test feed for komand',
                'description': 'Very technical text',
                'tags': ['malware'],
                'reported_by': 'komand_test',
                'timestamp': 1509396994,
                'title': 'New test report',
                'feed_id': 'AWcd2qUMuPEX_z4v01Q2',
                'ioc': {
                    'url': 'https://google.com',
                    'ip': '8.8.8.8',
                    'domain': 'google.com'
                },
                'id': '0d0f19991d5450a1d34d945971eed08d9d27e183d474d2ee14bca8bf7e569617'
            }
        }
