import insightconnect_plugin_runtime
from .schema import BulkAnalyzeInput, BulkAnalyzeOutput, Input, Output, Component

# Custom imports below
from icon_cortex_v2.util.convert import job_to_dict


class BulkAnalyze(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="bulk_analyze",
            description=Component.DESCRIPTION,
            input=BulkAnalyzeInput(),
            output=BulkAnalyzeOutput(),
        )

    def run(self, params={}):
        api = self.connection.api
        job_results = []
        cortex_analyzers = set()
        # set vars
        analyzer_ids, observable, analyze_all, attributes = (
            params.get(Input.ANALYZER_IDS),
            params.get(Input.OBSERVABLE),
            params.get(Input.ANALYZE_ALL),
            params.get(Input.ATTRIBUTES),
        )
        data_type = attributes.get("dataType", None)
        tlp_num = attributes.get("tlp", None)
        # get list of analyzers
        all_analyzers = api.analyzers.find_all(query="")
        # get list of cortex analyzers
        for analyzer in all_analyzers:
            cortex_analyzers.add(analyzer.json()["name"])
        # check analyzers in list and available
        if analyze_all == False:
            missing_ids = set(analyzer_ids).difference(cortex_analyzers)
            if len(missing_ids) > 0:
                self.logger.error(f"Error Analyzers: {missing_ids} not found in Cortex")
                # remove missing analyzers
                for analyzer in missing_ids:
                    self.logger.debug(f"Removing {analyzer}")
                    del analyzer_ids[analyzer_ids.index(analyzer)]

            # loop through analyzers and run
            for analyzer in analyzer_ids:
                self.logger.debug(f"Running Analyzer: {analyzer}")
                job = api.analyzers.run_by_name(
                    analyzer, {"data": observable, "dataType": data_type, "tlp": tlp_num}, force=1
                )
                job_results.append(job_to_dict(job, api))
        else:
            # Analyze all
            for analyzer in cortex_analyzers:
                job = api.analyzers.run_by_name(
                    analyzer, {"data": observable, "dataType": data_type, "tlp": tlp_num}, force=1
                )
                job_results.append(job_to_dict(job, api))

        # results
        return {"jobs": job_results}
