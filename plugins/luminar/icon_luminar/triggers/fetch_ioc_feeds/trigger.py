import time

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
from icon_luminar.util.utils import (
    get_last_run,
    is_valid_date,
    next_checkpoint,
    pull_feeds,
    save_last_run,
)

from .schema import Component, FetchIocFeedsInput, FetchIocFeedsOutput, Input, Output


class FetchIocFeeds(insightconnect_plugin_runtime.Trigger):
    _CACHE_FILE_NAME = "iocs"

    def __init__(self):
        super(self.__class__, self).__init__(
            name="fetch_ioc_feeds",
            description=Component.DESCRIPTION,
            input=FetchIocFeedsInput(),
            output=FetchIocFeedsOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        frequency = params.get(Input.FREQUENCY)
        initial_fetch_date = params.get(Input.INITIAL_FETCH_DATE)
        # END INPUT BINDING - DO NOT REMOVE

        if not is_valid_date(initial_fetch_date):
            self.logger.error("Invalid initial fetch date. Format should be YYYY-MM-DD")
            return

        # Normalize date once
        initial_fetch_date = f"{initial_fetch_date}T00:00:00.000000Z"

        while True:
            try:
                from_date = (
                    get_last_run(self._CACHE_FILE_NAME, self.logger)
                    or initial_fetch_date
                )
                next_run = next_checkpoint()

                records = pull_feeds(
                    self.connection.client, "iocs", from_date, self.logger
                )
                self.send({Output.RESULTS: records})

                save_last_run(self._CACHE_FILE_NAME, next_run, self.logger)
                self.logger.info(f"Sleeping for {frequency}")
                time.sleep(frequency)
            except Exception as error:
                raise PluginException(
                    cause=f"Plugin exception occurred: {error}",
                    assistance="Please check the input and try again.",
                )
