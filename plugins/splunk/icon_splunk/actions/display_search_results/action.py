import insightconnect_plugin_runtime
from .schema import DisplaySearchResultsInput, DisplaySearchResultsOutput, Input, Output, Component

# Custom imports below
from icon_splunk.util.constants import TIMER_STEP
from splunklib import results
from time import sleep
from insightconnect_plugin_runtime.exceptions import PluginException


class DisplaySearchResults(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="display_search_results",
            description=Component.DESCRIPTION,
            input=DisplaySearchResultsInput(),
            output=DisplaySearchResultsOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        job_id = params.get(Input.JOB_ID)
        timeout = params.get(Input.TIMEOUT)
        # END INPUT BINDING - DO NOT REMOVE

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
            sleep(TIMER_STEP)
            timer += TIMER_STEP
            self.logger.info(f"Search not complete, sleeping for {TIMER_STEP} seconds")
        if timer > timeout:
            self.logger.info("Timeout occurred, finalizing and attempting to retrieve results...")
            search_job.finalize()

        gathered_results = []
        results_reader = results.ResultsReader(search_job.results())
        for result in results_reader:
            if isinstance(result, dict):
                gathered_results.append(result)
        return {Output.SEARCH_RESULTS: gathered_results}
