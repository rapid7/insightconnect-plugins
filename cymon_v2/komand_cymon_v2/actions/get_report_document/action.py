import komand
from .schema import GetReportDocumentInput, GetReportDocumentOutput
# Custom imports below


class GetReportDocument(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_report_document',
                description='Get threat report from feed',
                input=GetReportDocumentInput(),
                output=GetReportDocumentOutput())

    def run(self, params={}):
        feed_id = params.get('feed_id')
        report_id = params.get('report_id')

        response = self.connection.api.get_report(feed_id, report_id)

        return {
            'feed': response.get('feed'),
            'report': response.get('report')
        }

    def test(self):
        return {
            'feed': {
                'updated': '2017-06-12T14:28:22.519Z',
                'is_owner': False,
                'name': 'zeustracker.abuse.ch',
                'created': '2017-03-25T17:25:57.534Z',
                'is_member': False,
                'privacy': 'public',
                'slug': 'zeustracker.abuse.ch',
                'link': 'https://zeustracker.abuse.ch',
                'logo': 'https://i.imgur.com/rBvuwon.jpg',
                'is_admin': False,
                'is_guest': False,
                'id': 'AVsGgNL4VjrVcoBZyoib',
                'tags': [
                    'malware',
                    'c2',
                    'c&c',
                    'zeus',
                    'tracker'
                ],
                'description': 'This feed is run by @abuse_ch (as well as all other abuse.ch projects) for non-profit. For questions please refer to: https://zeustracker.abuse.ch'
            },
            'report': {
                'feed': 'Test feed for komand',
                'description': 'Very technical text',
                'tags': ['malware'],
                'reported_by': 'komand_test',
                'timestamp': '2017-03-25T17:25:57.534Z',
                'title': 'New test report',
                'feed_id': 'AVsGgNL4VjrVcoBZyoib',
                'ioc': {
                    'url': 'https://google.com',
                    'ip': '8.8.8.8',
                    'domain': 'google.com'
                },
                'id': '0d0f19991d5450a1d34d945971eed08d9d27e183d474d2ee14bca8bf7e569617'
            }
        }
