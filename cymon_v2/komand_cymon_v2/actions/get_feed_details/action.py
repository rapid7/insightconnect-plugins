import komand
from .schema import GetFeedDetailsInput, GetFeedDetailsOutput
# Custom imports below


class GetFeedDetails(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_feed_details',
                description='Get feed object',
                input=GetFeedDetailsInput(),
                output=GetFeedDetailsOutput())

    def run(self, params={}):
        feed_id = params.get('feed_id')
        feed = self.connection.api.get_feed(feed_id)
        return {'feed': feed}

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
            }
        }
