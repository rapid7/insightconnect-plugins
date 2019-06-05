import komand
from .schema import (
    ListAllActivityMonitorMatchesInput, ListAllActivityMonitorMatchesOutput
)
# Custom imports below


class ListAllActivityMonitorMatches(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_all_activity_monitor_matches',
                description='Fetches a list of all activity monitor matches, '
                'sorted by the creation time of the match',
                input=ListAllActivityMonitorMatchesInput(),
                output=ListAllActivityMonitorMatchesOutput())

    def run(self, params={}):
        max_results = params.get('max_results', 100)
        api = self.connection.api

        return {
            'activity_monitor_matches': api.list_all_activity_monitor_matches(
                max_results=max_results
            )
        }
