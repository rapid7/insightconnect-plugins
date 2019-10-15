import komand
import time
from .schema import NewEventsInput, NewEventsOutput

# Custom imports below
import maya
from komand.exceptions import PluginException
from komand_red_canary.util.cacher import cache, load_cache


class NewEvents(komand.Trigger):
    CACHE_FILE_NAME = "events_cache_"

    def __init__(self):
        super(self.__class__, self).__init__(
            name="new_events",
            description="Checks for new events",
            input=NewEventsInput(),
            output=NewEventsOutput(),
        )

    def run(self, params={}):
        force_offset = params.get("force_offset")

        date_offset = params.get("date_offset")
        # what happens when its left blank?
        self.logger.info("Date Offset: {} ".format(date_offset))

        # If date is left blank in the UI
        if date_offset == "0001-01-01T00:00:00Z":
            date_offset = None

        # Set date_offset to maya.MayaDT
        if date_offset:
            date_offset = maya.MayaDT.from_rfc3339(date_offset)

        # New cache util. Will return maya DT
        cache_file_name, cache_date = load_cache(
            self.CACHE_FILE_NAME,
            self.connection.customer_id,
            self.logger,
            force_offset,
            date_offset,
        )

        # testing printing out log
        self.logger.info(cache_date)

        last_cache_date = cache_date

        event_date_list = []

        while True:
            try:
                self.logger.info("[*] Pulling events!")
                events = self.connection.api.list_events()

                self.logger.info("[*] Reviewing events")
                for event in events:
                    event_date = maya.MayaDT.from_rfc3339(
                        event["attributes"]["process"]["attributes"]["started_at"]
                    ).datetime()
                    if event_date > cache_date:
                        event_date_list.append(event_date)
                        self.send({"event": event})

                # Set cache date to max its seen
                if event_date_list:
                    max_date = max(event_date_list)
                    if max_date > cache_date:
                        cache_date = max_date

                # reset list
                event_date_list = []

                # Write to cache if it needs updating
                if last_cache_date != cache_date:
                    last_cache_date = cache_date
                    cache(cache_file_name, cache_date, self.logger)

                time.sleep(params.get("frequency", 5))
            except Exception as e:
                raise PluginException(
                    cause='An error occurred while reading events.',
                    assistance=f'{e}')
