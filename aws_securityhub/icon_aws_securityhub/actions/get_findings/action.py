import komand
from .schema import GetFindingsInput, GetFindingsOutput, Input, Output, Component

# Custom imports below
import logging

logging.getLogger("botocore").setLevel(logging.CRITICAL)


class GetFindings(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_findings",
            description=Component.DESCRIPTION,
            input=GetFindingsInput(),
            output=GetFindingsOutput(),
        )

    def run(self, params={}):
        findings = []
        filters = params.get(Input.FILTERS, {})
        client = self.connection.aws.client("securityhub")
        results = client.get_findings(Filters=filters)

        while results.get("NextToken"):
            if results.get("Findings"):
                for finding in results["Findings"]:
                    findings.append(finding)
            results = client.get_findings(
                Filters=filters, NextToken=results.get("NextToken")
            )

        return {Output.FINDINGS: findings}
