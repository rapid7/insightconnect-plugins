import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import (
    BatchUpdateFindingsInput,
    BatchUpdateFindingsOutput,
    Input,
    Output,
    Component,
)
from botocore.exceptions import ClientError

# Custom imports below
import logging

logging.getLogger("botocore")


class BatchUpdateFindings(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="batch_update_findings",
            description=Component.DESCRIPTION,
            input=BatchUpdateFindingsInput(),
            output=BatchUpdateFindingsOutput(),
        )

    def run(self, params={}):
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

        filtered_params = {param: value for param, value in update_params.items() if value is not None}
        client = self.connection.aws.client("securityhub")

        results = client.batch_update_findings(**filtered_params)

        try:
            results = client.batch_update_findings(**filtered_params)
        except ClientError as error:
            raise PluginException(
                cause="AWS Security Hub API call failed.",
                assistance=f"Verify your credentials and finding identifiers. Error: {error.response['Error']['Message']}",
                data=error,
            )

        return {
            Output.PROCESSED_FINDINGS: results.get("ProcessedFindings", []),
            Output.UNPROCESSED_FINDINGS: results.get("UnprocessedFindings", []),
        }
