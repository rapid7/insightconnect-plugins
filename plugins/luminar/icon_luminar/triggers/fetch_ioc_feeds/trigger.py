import insightconnect_plugin_runtime
import time
from .schema import FetchIocFeedsInput, FetchIocFeedsOutput, Input, Output, Component
# Custom imports below

from .util.util import get_ioc_from_pattern, filtered_records

class FetchIocFeeds(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="fetch_ioc_feeds",
                description=Component.DESCRIPTION,
                input=FetchIocFeedsInput(),
                output=FetchIocFeedsOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        frequency = params.get(Input.FREQUENCY)
        initial_fetch_date = params.get(Input.INITIAL_FETCH_DATE)
        # END INPUT BINDING - DO NOT REMOVE

        while True:
            initial_fetch_date = initial_fetch_date + "T00:00:00.000000Z"
            params = {"limit": 9999}
            params["added_after"] = initial_fetch_date
            self.logger.info(f"Using initial fetch date: {initial_fetch_date}")
            ioc_collection_id = self.connection.client.get_taxi_collections().get("iocs")
            if ioc_collection_id:
                self.logger.info(f"Fetching IOC feeds from Luminar....")
                ioc_records = self.connection.client.get_collection_objects(ioc_collection_id, params)
                if ioc_records:
                    self.logger.info(f"Fetched IOC records.")
                    #filter ioc records based on created date
                    filter_records = filtered_records(ioc_records, initial_fetch_date)
                    if filter_records:
                        for x in filter_records:
                            if x.get('type') == "indicator" and x.get('pattern'):
                                x['ioc'] = get_ioc_from_pattern(self.logger, x.get('pattern'))

                        self.send({
                            Output.RESULTS: filter_records,
                        })
                    else:
                        self.logger.info("No new IOC records found.")
                else:
                    self.logger.info("No IOC records found.")
            else:
                self.logger.info("No IOC collection found.")
            time.sleep(frequency)
