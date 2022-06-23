import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import BulkAnalyzeInput, BulkAnalyzeOutput, Input, Output, Component

# Custom imports below
from typing import Iterable, List, Dict, Any


class BulkAnalyze(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="bulk_analyze",
            description=Component.DESCRIPTION,
            input=BulkAnalyzeInput(),
            output=BulkAnalyzeOutput(),
        )

    def run(self, params={}):
        api = self.connection.API
        job_results = []
        cortex_analyzers = set()
        # set vars
        analyzer_names, observable, analyze_all, attributes = (
            params.get(Input.ANALYZER_IDS),
            params.get(Input.OBSERVABLE),
            params.get(Input.ANALYZE_ALL),
            params.get(Input.ATTRIBUTES),
        )
        data_type = attributes.get("dataType", None)
        tlp_num = attributes.get("tlp", None)
        data = {"data": observable, "dataType": data_type, "tlp": tlp_num}
        # get list of analyzers
        all_analyzers = api.search("analyzer", "")
        # get list of cortex analyzers
        for analyzer in all_analyzers:
            cortex_analyzers.add(analyzer.get("name"))
        # check analyzers in list and available
        if not analyze_all:
            missing_ids = set(analyzer_names).difference(cortex_analyzers)
            if missing_ids:
                self.logger.error(f"Error Analyzers: {missing_ids} not found in Cortex")
                # remove missing analyzers
                for analyzer in missing_ids:
                    self.logger.debug(f"Removing {analyzer}")
                    del analyzer_names[analyzer_names.index(analyzer)]

            # loop through analyzers and run
            job_results = self.run_analyzers(analyzer_names, data)
        else:
            # Analyze all
            job_results = self.run_analyzers(cortex_analyzers, data)
        # results
        return {Output.JOBS: job_results}

    def run_analyzers(self, analyzer_names: Iterable[str], data: Dict[str, Any]) -> List[Dict[str, Any]]:
        jobs = []
        for analyzer_name in analyzer_names:
            self.logger.debug(f"Running Analyzer: {analyzer_name}")
            jobs.append(self.connection.API.run_analyzer_by_name(analyzer_name, data))
        return jobs
