import insightconnect_plugin_runtime
from .schema import BatchUpdateFindingsInput, BatchUpdateFindingsOutput, Input, Output, Component

# Custom imports below
import logging

logging.getLogger("botocore").setLevel(logging.CRITICAL)

class BatchUpdateFindings(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="batch_update_findings",
            description=Component.DESCRIPTION,
            input=BatchUpdateFindingsInput(),
            output=BatchUpdateFindingsOutput(),
        )

    def run(self, params={}):
        processed_findings = []
        unprocessed_findings = []

        finding_identifiers = params.get(Input.FINDING_IDENTIFIERS)
        note = params.get(Input.NOTE, None)
        severity = params.get(Input.SEVERITY, None)
        verification_state = params.get(Input.VERIFICATION_STATE, None)
        confidence = params.get(Input.CONFIDENCE, None)
        criticality = params.get(Input.CRITICALITY, None)
        types = params.get(Input.TYPES, None)
        user_defined_fields = params.get(Input.USER_DEFINED_FIELDS, None)
        workflow = params.get(Input.WORKFLOW, None)
        related_findings = params.get(Input.RELATED_FINDINGS, None)

        update_params = {
            "FindingIdentifiers": finding_identifiers,
            "Note": note,
            "Severity": severity,
            "VerificationState": verification_state,
            "Confidence": confidence,
            "Criticality": criticality,
            "Types": types,
            "UserDefinedFields": user_defined_fields,
            "Workflow": workflow,
            "RelatedFindings": related_findings,
        }

        filtered_params = {k: v for k, v in update_params.items() if v}
        client = self.connection.aws.client("securityhub")

        results = client.batch_update_findings(**filtered_params)

        if results.get("UnprocessedFindings"):
            for finding in results["UnprocessedFindings"]:
                unprocessed_findings.append(finding)

        if results.get("ProcessedFindings"):
            for finding in results["ProcessedFindings"]:
                processed_findings.append(finding)

        return {Output.PROCESSED_FINDINGS: processed_findings, Output.UNPROCESSED_FINDINGS: unprocessed_findings}
