import insightconnect_plugin_runtime
import time
from .schema import NewExceptionRequestInput, NewExceptionRequestOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightvm.util.endpoints import VulnerabilityException
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests
from typing import List


class NewExceptionRequest(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="new_exception_request",
            description=Component.DESCRIPTION,
            input=NewExceptionRequestInput(),
            output=NewExceptionRequestOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        status_filters = params.get(Input.STATUS_FILTER, ["Under Review"])
        frequency = params.get(Input.FREQUENCY, 5)
        # END INPUT BINDING - DO NOT REMOVE

        # Initialize the trigger
        self.logger.info("Initialising the trigger data")
        resource_helper = ResourceRequests(self.connection.session, self.logger, self.connection.ssl_verify)

        # Get current vulnerability exceptions
        previous_ids = self._get_ids(status_filters, resource_helper)

        while True:
            self.logger.info("Checking for new exceptions")
            current_ids = self._get_ids(status_filters, resource_helper)
            new_ids = list(filter(lambda element: element not in previous_ids, current_ids))

            if new_ids:
                self.logger.info(f"Found new {len(new_ids)} exceptions. Returning results...")
                for id_ in new_ids:
                    try:
                        self.send(
                            {
                                Output.EXCEPTION: resource_helper.resource_request(
                                    endpoint=VulnerabilityException.vulnerability_exception(
                                        self.connection.console_url, id_
                                    )
                                )
                            }
                        )
                    except Exception as error:
                        self.logger.error(
                            f"Unexpected exception during trigger execution occurs. The error is: '{error}'"
                        )
                previous_ids = current_ids
            else:
                self.logger.info(f"No new exceptions found. Sleeping for {frequency} minutes...")

            # Sleep for configured frequency in minutes
            time.sleep(frequency * 60)

    def _get_ids(self, status_filters: List[str], resource_helper: ResourceRequests) -> List[int]:
        """
        Get IDs. This method allows to get a list of vulnerability exception IDs from the API where the
        vulnerability exception matches status filters.

        :param status_filters: List of string that contain statuses the vulnerability exception needs to have.
        :type status_filters: List[str]

        :param resource_helper: The resource helper object to send requests.
        :type resource_helper: ResourceRequests

        :return: List of IDs that matches the criteria.
        :rtype: List[int]
        """

        response = resource_helper.paged_resource_request(
            endpoint=VulnerabilityException.vulnerability_exceptions(self.connection.console_url),
            params={"sort": "id,desc"},
        )
        return [
            element.get("id")
            for element in response
            if element.get("state", "").lower() in map(str.lower, status_filters)
        ]
