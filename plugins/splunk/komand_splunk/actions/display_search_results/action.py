import komand
from .schema import DisplaySearchResultsInput, DisplaySearchResultsOutput, Input, Output, Component

# Custom imports below
import splunklib.results as results
from time import sleep
from komand.exceptions import PluginException


class DisplaySearchResults(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="display_search_results",
            description=Component.DESCRIPTION,
            input=DisplaySearchResultsInput(),
            output=DisplaySearchResultsOutput(),
        )

    def run(self, params={}):
        job_id = params.get(Input.JOB_ID)
        timeout = params.get(Input.TIMEOUT)
        timer_step = 0.2  # What we should increment the timeout counter by

        try:
            search_job = self.connection.client.jobs[job_id]
        except KeyError as error:
            self.logger.error(error)
            raise PluginException(
                cause="Unable to find job.",
                assistance="Ensure the provided job ID input is valid.",
                data=f"Job ID: {job_id}",
            )

        timer = 0  # Keep track of the timeout

        self.logger.info("Streaming results")
        while not search_job.is_done() and timer < timeout:
            sleep(timer_step)
            timer += timer_step
            self.logger.info("Search not complete, sleeping for %s seconds" % timer_step)
        if timer > timeout:
            self.logger.info("Timeout occurred, finalizing and attempting to retrieve results...")
            search_job.finalize()

        rr = results.ResultsReader(search_job.results())

        gathered_results = []

        for result in rr:
            if isinstance(result, dict):
                gathered_results.append(result)

        return {Output.SEARCH_RESULTS: gathered_results}
