import komand
from .schema import ListUserFeedsInput, ListUserFeedsOutput
# Custom imports below


class ListUserFeeds(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_user_feeds',
                description='Get list of feeds that user has access to',
                input=ListUserFeedsInput(),
                output=ListUserFeedsOutput())

    def run(self, params={}):
        feeds = self.connection.api.list_user_feeds()
        return {'feeds': feeds}

    def test(self):
        return {
            'feeds': [{
                'updated': '2018-11-16T18:25:46.241Z',
                'is_owner': True,
                'name': 'A test feed',
                'created': '2018-11-16T18:25:46.241Z',
                'is_member': False,
                'privacy': 'public',
                'slug': 'a-test-feed',
                'is_admin': False,
                'is_guest': False,
                'id': 'AWcdxZFyuPEX_z4v01Q1',
                'tags': ['malware']
            }, {
                'updated': '2018-11-16T18:47:35.606Z',
                'is_owner': True,
                'name': 'A test feed for Komand',
                'created': '2018-11-16T18:47:35.606Z',
                'is_member': False,
                'privacy': 'public',
                'slug': 'a-test-feed-for-komand',
                'is_admin': False,
                'is_guest': False,
                'id': 'AWcd2Yw4ZDr3mu5zLPTF',
                'tags': ['malware']
            }]
        }
