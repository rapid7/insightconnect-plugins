import insightconnect_plugin_runtime
from .schema import GetReportInput, GetReportOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.helper import clean


class GetReport(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_report",
            description=Component.DESCRIPTION,
            input=GetReportInput(),
            output=GetReportOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        task = params.get(Input.TASK, False)
        # END INPUT BINDING - DO NOT REMOVE

        # Get report from AnyRun
        report = clean(self.connection.any_run_api.get_report(task).get("data", {}))

        # If tags exists, and are objects, convert to list of tag names
        tags = report.get("analysis", {}).get("tags", [])
        if tags and isinstance(tags[0], dict):
            report["analysis"]["tags"] = [tag["tag"] for tag in tags]

        # If mitre exists, convert its keys and values to strings
        for incident in report.get("incidents", []):
            incident["mitre"] = [
                {str(key): str(value) for key, value in mitre.items()} for mitre in incident.get("mitre", [])
            ]
        return {Output.REPORTS: report}
