import logging
import sys
import os

from unittest import TestCase
from unittest.mock import MagicMock
from botocore.exceptions import ClientError

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_aws_securityhub.actions.batch_update_findings import BatchUpdateFindings

sys.path.append(os.path.abspath("../"))

STUB_FINDING_IDENTIFIER = {
    "Id": "arn:aws:securityhub:us-east-1:123456789012:finding/abc",
    "ProductArn": "arn:aws:securityhub:us-east-1::product/aws/guardduty",
}


class TestBatchUpdateFindings(TestCase):
    def setUp(self):
        self.action = BatchUpdateFindings()

        self.mock_client = MagicMock()

        self.action.connection = MagicMock()
        self.action.connection.aws.client.return_value = self.mock_client

        self.action.logger = logging.getLogger("action logger")

    def test_successful_batch_update(self):
        self.mock_client.batch_update_findings.return_value = {
            "ProcessedFindings": [STUB_FINDING_IDENTIFIER],
            "UnprocessedFindings": [],
        }

        result = self.action.run(
            {
                "finding_identifiers": [STUB_FINDING_IDENTIFIER],
                "note": {
                    "Text": "Closed by Rapid7",
                    "UpdatedBy": "Rapid7",
                },
                "severity": {"Label": "HIGH"},
                "workflow": {"Status": "NEW"},
            }
        )

        self.mock_client.batch_update_findings.assert_called_once()

        self.assertEqual(
            result["ProcessedFindings"],
            [STUB_FINDING_IDENTIFIER],
        )
        self.assertEqual(result["UnprocessedFindings"], [])

    def test_unprocessed_findings_returned(self):
        unprocessed = [
            {
                "FindingIdentifier": STUB_FINDING_IDENTIFIER,
                "ErrorCode": "FindingNotFound",
                "ErrorMessage": "The finding was not found.",
            }
        ]

        self.mock_client.batch_update_findings.return_value = {
            "ProcessedFindings": [],
            "UnprocessedFindings": unprocessed,
        }

        result = self.action.run({"finding_identifiers": [STUB_FINDING_IDENTIFIER]})

        self.assertEqual(result["ProcessedFindings"], [])
        self.assertEqual(
            result["UnprocessedFindings"],
            unprocessed,
        )

    def test_none_optional_params_filtered(self):
        self.mock_client.batch_update_findings.return_value = {
            "ProcessedFindings": [],
            "UnprocessedFindings": [],
        }

        self.action.run(
            {
                "finding_identifiers": [STUB_FINDING_IDENTIFIER],
                "note": None,
                "severity": None,
                "workflow": None,
                "confidence": None,
                "criticality": None,
                "types": None,
                "user_defined_fields": None,
                "verification_state": None,
                "related_findings": None,
            }
        )

        call_kwargs = self.mock_client.batch_update_findings.call_args.kwargs

        self.assertNotIn("Note", call_kwargs)
        self.assertNotIn("Severity", call_kwargs)
        self.assertNotIn("Workflow", call_kwargs)
        self.assertNotIn("Confidence", call_kwargs)
        self.assertNotIn("Criticality", call_kwargs)
        self.assertNotIn("Types", call_kwargs)
        self.assertNotIn("UserDefinedFields", call_kwargs)
        self.assertNotIn("VerificationState", call_kwargs)
        self.assertNotIn("RelatedFindings", call_kwargs)

    def test_zero_value_confidence_not_dropped(self):
        self.mock_client.batch_update_findings.return_value = {
            "ProcessedFindings": [],
            "UnprocessedFindings": [],
        }

        self.action.run(
            {
                "finding_identifiers": [STUB_FINDING_IDENTIFIER],
                "confidence": 0,
            }
        )

        call_kwargs = self.mock_client.batch_update_findings.call_args.kwargs

        self.assertIn("Confidence", call_kwargs)
        self.assertEqual(call_kwargs["Confidence"], 0)

    def test_client_error_raises_plugin_exception(self):
        self.mock_client.batch_update_findings.side_effect = ClientError(
            {
                "Error": {
                    "Code": "InvalidInputException",
                    "Message": "Invalid input.",
                }
            },
            "BatchUpdateFindings",
        )

        with self.assertRaises(PluginException):
            self.action.run({"finding_identifiers": [STUB_FINDING_IDENTIFIER]})
