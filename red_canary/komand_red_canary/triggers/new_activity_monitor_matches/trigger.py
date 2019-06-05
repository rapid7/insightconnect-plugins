import komand
import time
from .schema import (
    NewActivityMonitorMatchesInput, NewActivityMonitorMatchesOutput
)
# Custom imports below


class NewActivityMonitorMatches(komand.Trigger):
    CACHE_FILE_NAME = 'activity_monitor_matches_cache_'

    def __init__(self):
        super(self.__class__, self).__init__(
                name='new_activity_monitor_matches',
                description='Checks for new matches for a '
                'specific activity monitor',
                input=NewActivityMonitorMatchesInput(),
                output=NewActivityMonitorMatchesOutput())

    def run(self, params={}):
        cache_file_name = self.CACHE_FILE_NAME + self.connection.customer_id
        activity_monitor_id = params.get('activity_monitor_id')

        with komand.helper.open_cachefile(cache_file_name) as cache_file:
            self.logger.info(
                'Found or created cache file: {}'.format(cache_file_name)
            )
            cached_ids = {l.strip() for l in cache_file.readlines()}
            self.logger.info('Cached IDs: {}'.format(cached_ids))

        while True:
            try:
                matches = self.connection.api.list_activity_monitor_matches(
                    activity_monitor_id
                )

                new_ids = set()

                for match in matches:
                    match_id = str(match['id'])
                    if match_id not in cached_ids:
                        cached_ids.add(match_id)
                        new_ids.add(match_id)
                        self.logger.info(
                            'New match found: {}'.format(match_id)
                        )
                        self.send({'activity_monitor_match': match})

                with komand.helper.open_cachefile(
                    cache_file_name, append=True
                ) as cache_file:
                    for match_id in new_ids:
                        self.logger.info(
                            'Writing match {} to cache file'.format(
                                match_id
                            )
                        )
                        cache_file.write(match_id)

                time.sleep(params.get('frequency', 5))
            except Exception as e:
                raise Exception(
                    'An error occurred while reading matches: {}'.format(e)
                )
