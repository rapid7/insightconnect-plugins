import komand
from .schema import SubmitReportsInBulkInput, SubmitReportsInBulkOutput
# Custom imports below


class SubmitReportsInBulk(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_reports_in_bulk',
                description='Upload multiple threat reports in one request',
                input=SubmitReportsInBulkInput(),
                output=SubmitReportsInBulkOutput())

    def run(self, params={}):
        reports = params.get('reports')
        reports = self.connection.api.bulk_submit_reports(reports)
        return {'reports': reports}

    def test(self):
        return {
            'reports': [{
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
            }, {
                'feed': 'Another Test feed for komand',
                'description': 'Different very technical text',
                'tags': ['ransomware'],
                'reported_by': 'komand_test',
                'timestamp': 1509396994,
                'title': 'New test report',
                'feed_id': 'AWcd2qUMuPEX_z4v01Q2',
                'ioc': {
                    'url': 'https://non-google.com',
                    'ip': '8.8.8.8',
                    'domain': 'non-google.com'
                },
                'id': '0def19991d5450a1d34d945971eed08d9d27e183d474d2ee14bca8bf7e569617'

            }]
        }
