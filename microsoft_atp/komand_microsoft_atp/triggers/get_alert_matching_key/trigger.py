import komand
import time
from .schema import GetAlertMatchingKeyInput, GetAlertMatchingKeyOutput, Input, Output
# Custom imports below


class GetAlertMatchingKey(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_alert_matching_key',
                description='Get alerts that match a given key to its value',
                input=GetAlertMatchingKeyInput(),
                output=GetAlertMatchingKeyOutput())

    def run(self, params={}):
        alert_key = params.get(Input.KEY)
        alert_value = params.get(Input.VALUE)

        frequency = params.get(Input.FREQUENCY, 10)

        # Set a baseline for the time to start looking for alerts.
        initial_results = self.connection.get_all_alerts(query_parameters="?$orderby=alertCreationTime+desc&$top=1")
        all_results = initial_results.json()

        if len(all_results.get("value", [])):
            most_recent_result = all_results.get("value")[0]
            most_recent_time_string = most_recent_result.get("alertCreationTime")
        else:
            self.logger.info("No current alerts found, setting time to start looking to 2010-10-01.")
            most_recent_time_string = "2010-01-01T00:00:00.000000Z" # We don't have any alerts yet

        # Start looking for new results
        while True:
            query_params = f"?$filter=alertCreationTime+gt+{most_recent_time_string}&$orderby=alertCreationTime+desc"

            self.logger.info("Looking for new alerts.")
            self.logger.info(f"Query params:{query_params}")
            current_results_result = self.connection.get_all_alerts(query_parameters=query_params)
            current_results = current_results_result.json()

            # If new results available, return each of them, update the time we saw the latest result
            current_results_list = current_results.get("value", [])
            if len(current_results_list):
                self.logger.info(f"New results found, examining {len(current_results_list)} results.")
                for alert in current_results_list:
                    current_value = alert.get(alert_key)
                    if current_value == alert_value:
                        self.send({Output.RESULTS: komand.helper.clean(alert)})
                        self.logger.info("\n") # This keeps the logs easier to read, Send doesn't add newlines
                    else:
                        self.logger.info(f"Found new alert, however, value {current_value} did not match {alert_value}."
                                         f" Skipping this alert.")
                self.logger.info(f"Updating time from.\n")
                most_recent_time_string = current_results.get("value")[0].get("alertCreationTime")
            else:
                self.logger.info(f"No new results were found. Sleeping for {frequency} seconds\n")

            time.sleep(frequency)
