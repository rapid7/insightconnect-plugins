import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import RunAnalyzerInput, RunAnalyzerOutput, Input, Output, Component

# Custom imports below


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
        analyzer_name = params.get(Input.ANALYZER_ID)
        observable = params.get(Input.OBSERVABLE)
        data_type = params.get(Input.ATTRIBUTES).get("dataType")
        tlp_num = params.get(Input.ATTRIBUTES).get("tlp")

        return {
            Output.JOB: self.connection.API.run_analyzer_by_name(
                analyzer_name, {"data": observable, "dataType": data_type, "tlp": tlp_num}
            )
        }
