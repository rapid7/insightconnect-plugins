import komand
import time
from .schema import NewIncidentsInput, NewIncidentsOutput
# Custom imports below


class NewIncidents(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='new_incidents',
                description='Check for new incidents',
                input=NewIncidentsInput(),
                output=NewIncidentsOutput())

    def run(self, params={}):
        frequency = params.get('frequency', 10)
        cache_file_name = 'cached_incidents_ids'

        with komand.helper.open_cachefile(cache_file_name) as cache_file:
            self.logger.info(
                'Found or created cache file: {}'.format(cache_file_name)
            )
            cached_ids = {l.strip() for l in cache_file.readlines()}
            self.logger.info('Cached IDs: {}'.format(cached_ids))

        while True:
            try:
                incidents = self.connection.api.list_incidents()

                new_ids = set()

                for incident in incidents:
                    incident_id = str(incident['id'])
                    if incident_id not in cached_ids:
                        cached_ids.add(incident_id)
                        new_ids.add(incident_id)
                        self.logger.info(
                            'New incident found: {}'.format(incident_id)
                        )
                        self.send({'incident': incident})

                with komand.helper.open_cachefile(
                    cache_file_name, append=True
                ) as cache_file:
                    for incident_id in new_ids:
                        self.logger.info(
                            'Writing incident {} to cache file'.format(
                                incident_id
                            )
                        )
                        cache_file.write(incident_id)

                time.sleep(frequency)
            except Exception as e:
                raise Exception(
                    'An error occurred while reading incidents: {}'.format(e)
                )

    def test(self):
        self.connection.api.list_incidents()
        return {'incident': {}}
