import insightconnect_plugin_runtime
import time
from .schema import NewExceptionRequestInput, NewExceptionRequestOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class NewExceptionRequest(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="new_exception_request",
            description=Component.DESCRIPTION,
            input=NewExceptionRequestInput(),
            output=NewExceptionRequestOutput(),
        )

    def run(self, params={}):
        """Run the trigger"""

        # get most recent vulnerability exception request - since they're sequential, find highest id
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.VulnerabilityException.vulnerability_exceptions(self.connection.console_url)
        std_params = {"sort": "id,desc"}
        response = resource_helper.paged_resource_request(endpoint=endpoint, method="get", params=std_params)
        last_id = 0
        for r in response:
            if r["id"] > last_id:
                last_id = r["id"]
        params["interval"] = params["frequency"]
        status_filter = []
        for i in params.get("status_filter", []):
            status_filter.append(i.lower())
        while True:
            # process all new exceptions.  The inner loop is to handle grabbing
            # multiple exceptions since last cycle.  It is broken when we run out
            # of new vulnerabity exceptions to process returning us to the outer loop
            # where we sleep for the configured amount of time.
            # We detect that we're out of work to do when we try and grab the
            # next higher exception id and we get an exception back instead of a
            # response containing a vulnerability exception.
            while True:
                endpoint = endpoints.VulnerabilityException.vulnerability_exception(
                    self.connection.console_url, last_id + 1
                )
                # check if there is a new vulnerability exception
                try:
                    response = resource_helper.resource_request(endpoint=endpoint, method="get")
                except Exception:
                    break
                last_id += 1
                # do we send it on it's way?
                if response.get("state").lower() not in status_filter:
                    continue
                # send it on it's way
                self.send({Output.EXCEPTION: response})

            # Sleep for configured frequency in minutes
            time.sleep(params.get(Input.FREQUENCY, 5) * 60)
