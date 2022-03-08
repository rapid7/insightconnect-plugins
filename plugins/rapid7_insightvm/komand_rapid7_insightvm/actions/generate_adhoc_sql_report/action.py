import insightconnect_plugin_runtime
from .schema import (
    GenerateAdhocSqlReportInput,
    GenerateAdhocSqlReportOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
import base64
import json
import uuid
from komand_rapid7_insightvm.util import util
from insightconnect_plugin_runtime.exceptions import PluginException


class GenerateAdhocSqlReport(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="generate_adhoc_sql_report",
            description=Component.DESCRIPTION,
            input=GenerateAdhocSqlReportInput(),
            output=GenerateAdhocSqlReportOutput(),
        )

    def run(self, params={}):
        query = params.get(Input.QUERY)
        # Generate unique identifier for report name
        identifier = uuid.uuid4()

        # Configure payload for SQL report generation
        report_payload = {
            "name": f"Rapid7-InsightConnect-AdhocReport-{identifier}",
            "format": "sql-query",
            "query": query,
            "version": "2.3.0",
            "filters": json.loads(params.get(Input.FILTERS)),
        }
        # Add scope if set in action
        if params.get(Input.SCOPE) != "none" and len(params.get(Input.SCOPE_IDS)) > 0:
            if params.get(Input.SCOPE) == "scan":
                report_payload["scope"] = {params.get(Input.SCOPE): params.get(Input.SCOPE_IDS)[0]}
            else:
                report_payload["scope"] = {params.get(Input.SCOPE): params.get(Input.SCOPE_IDS)}

        report_contents = util.adhoc_sql_report(self.connection, self.logger, report_payload)

        try:
            base_64_report = base64.b64encode(report_contents["raw"].encode("utf-8"))
        except base64.binascii.Error as e:
            raise PluginException(
                cause="Error: Failed to base64 encode report contents due to incorrect padding.",
                assistance=f"Exception returned was {e}",
            )

        return {
            Output.REPORT: {
                "content": base_64_report.decode("utf-8"),
                "filename": "adhoc_sql_report.csv",
            }
        }
