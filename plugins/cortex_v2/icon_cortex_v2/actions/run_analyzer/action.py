import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import RunAnalyzerInput, RunAnalyzerOutput, Input, Output, Component

# Custom imports below
from icon_cortex_v2.util.util import filter_job, filter_job_artifacts


class RunAnalyzer(insightconnect_plugin_runtime.Action):
    tlp = {"WHITE": 0, "GREEN": 1, "AMBER": 2, "RED": 3}

    def __init__(self):
        super(self.__class__, self).__init__(
            name="run_analyzer",
            description=Component.DESCRIPTION,
            input=RunAnalyzerInput(),
            output=RunAnalyzerOutput(),
        )

    def run(self, params={}):
        api = self.connection.API

        analyzer_name = params.get(Input.ANALYZER_ID)
        observable = params.get(Input.OBSERVABLE)
        data_type = params.get(Input.ATTRIBUTES).get("dataType")
        tlp_num = params.get(Input.ATTRIBUTES).get("tlp")

        analyzer = api.get_analyzer_by_name(analyzer_name)
        analyzer_id = analyzer.get("id")
        if not analyzer_id:
            raise PluginException(f"Analyzer {analyzer_name} not found")
        job = filter_job(api.run_analyzer(analyzer_id, {"data": observable, "dataType": data_type, "tlp": tlp_num}))
        if not job or not isinstance(job, dict) or "id" not in job:
            raise PluginException(f"Failed to receive job from analyzer {analyzer_name}")
        job["artifacts"] = filter_job_artifacts(api.get_job_artifacts(job["id"]))

        return {Output.JOB: job}
