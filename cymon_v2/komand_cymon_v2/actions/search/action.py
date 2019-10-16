import komand
from .schema import SearchInput, SearchOutput
# Custom imports below


class Search(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search',
                description='Search threat reports',
                input=SearchInput(),
                output=SearchOutput())

    def run(self, params={}):
        search_by = params.get('search_by')
        value = params.get('value')
        start_date = params.get('start_date')
        end_date = params.get('end_date')

        # Change user friendly name into actual endpoint
        try:
            search_by = search_by[:search_by.index('_')]
            self.logger.info(
                'Changing "search_by" value to "{}" endpoint'.format(search_by)
            )
        except ValueError:
            self.logger.info(
                '"search_by" value is already a correct endpoint: {}'.format(
                    search_by
                )
            )

        hits = self.connection.api.search(
            search_by, value, start_date, end_date
        )
        return {'hits': hits}

    def test(self):
        return {
            'hits': [{
                'feed': 'senderbase.org',
                'title': 'Spam activity',
                'reported_by': 'cymon',
                'timestamp': '2018-07-14T04:06:08.000Z',
                'tags': ['spam'],
                'feed_id': 'AVsGXxCjVjrVcoBZyoh-',
                'link': 'http://www.senderbase.org/lookup/?search_string=66.220.155.142',
                'location': {
                    'country': 'US',
                    'city': 'New York',
                    'point': {
                        'lat': 40.7143,
                        'lon': -74.006
                    }
                },
                'ioc': {
                    'ip': '66.220.155.142',
                    'domain': 'facebook.com',
                    'hostname': '66-220-155-142.mail-mail.facebook.com'
                },
                'id': '91bd5f515a1e0a93a4f4d689b123409fb214c1990e2735be8fb3f4b2a960e2b5'
            }, {
                'feed': 'hosts-file.net',
                'description': 'Website: facebook.com.179863857.connect.user.19472973904038575.ajslyr36hur85.replymprevivaldi.angelas.cl \nIP: 192.141.168.137 \nClassification: PSH \nAdded: 5/30/2018 3:49:09 PM \nAdded By: TeMerc',
                'title': 'Phishing activity',
                'reported_by': 'cymon',
                'timestamp': '2018-05-30T15:49:00.000Z',
                'tags': ['phishing'],
                'feed_id': 'AVsGZTOOVjrVcoBZyoiQ',
                'link': 'http://hosts-file.net/?s=facebook.com.179863857.connect.user.19472973904038575.ajslyr36hur85.replymprevivaldi.angelas.cl',
                'ioc': {
                    'ip': '192.141.168.137',
                    'domain': 'angelas.cl',
                    'hostname': 'facebook.com.179863857.connect.user.19472973904038575.ajslyr36hur85.replymprevivaldi.angelas.cl'
                },
                'id': '402735dcb98b47e572da48723e53837b2fd067da211b05464322e2da37be9e77'
            }]
        }
