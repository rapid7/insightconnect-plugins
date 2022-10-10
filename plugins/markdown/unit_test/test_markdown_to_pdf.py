import sys
import os

sys.path.append(os.path.abspath("../"))
from parameterized import parameterized
from unittest import TestCase
from komand_markdown.actions.markdown_to_pdf import MarkdownToPdf
from insightconnect_plugin_runtime.exceptions import PluginException


class TestMarkdownToPdf(TestCase):
    # TODO - Import the expected results from a json file instead
    # expected_result = {'pdf_string': "%PDF-1.4\n", 'pdf': "JVBERi0xLjQKMSAwIG9iago8PAovVGl0bGUgKO+/ve+/vSkKL0NyZWF0b3IgKO+/ve+/vQB3AGsAaAB0AG0AbAB0AG8AcABkAGYAIAAwAC4AMQAyAC4ANikKL1Byb2R1Y2VyICjvv73vv70AUQB0ACAANAAuADgALgA3KQovQ3JlYXRpb25EYXRlIChEOjIwMjIxMDEwMTQ0MzQxKzAxJzAwJykKPj4KZW5kb2JqCjMgMCBvYmoKPDwKL1R5cGUgL0V4dEdTdGF0ZQovU0EgdHJ1ZQovU00gMC4wMgovY2EgMS4wCi9DQSAxLjAKL0FJUyBmYWxzZQovU01hc2sgL05vbmU+PgplbmRvYmoKNCAwIG9iagpbL1BhdHRlcm4gL0RldmljZVJHQl0KZW5kb2JqCjYgMCBvYmoKPDwKL1R5cGUgL0NhdGFsb2cKL1BhZ2VzIDIgMCBSCj4+CmVuZG9iago1IDAgb2JqCjw8Ci9UeXBlIC9QYWdlCi9QYXJlbnQgMiAwIFIKL0NvbnRlbnRzIDcgMCBSCi9SZXNvdXJjZXMgOSAwIFIKL0Fubm90cyAxMCAwIFIKL01lZGlhQm94IFswIDAgNTk1IDg0Ml0KPj4KZW5kb2JqCjkgMCBvYmoKPDwKL0NvbG9yU3BhY2UgPDwKL1BDU3AgNCAwIFIKL0NTcCAvRGV2aWNlUkdCCi9DU3BnIC9EZXZpY2VHcmF5Cj4+Ci9FeHRHU3RhdGUgPDwKL0dTYSAzIDAgUgo+PgovUGF0dGVybiA8PAo+PgovRm9udCA8PAo+PgovWE9iamVjdCA8PAo+Pgo+PgplbmRvYmoKMTAgMCBvYmoKWyBdCmVuZG9iago3IDAgb2JqCjw8Ci9MZW5ndGggOCAwIFIKL0ZpbHRlciAvRmxhdGVEZWNvZGUKPj4Kc3RyZWFtCnjvv73vv713D05USC9W77+9dw4uUEjvv73vv73vv73vv71cBnrvv70GEO+/vQDvv73vv73vv70CRhZ6UO+/ve+/ve+/ve+/vTHvv73vv73vv73vv73vv71V77+9UO+/vRXvv70VCCRhNEhvLu+/ve+/ve+/ve+/vR5I77+977+9Ke+/ve+/ve+/ve+/vTU0MDHvv70z77+9NO+/ve+/vQDvv70b77+9c0Hvv70z77+9wrUU77+9DFYI77+9AgAUDSYOCmVuZHN0cmVhbQplbmRvYmoKOCAwIG9iagoxMDkKZW5kb2JqCjIgMCBvYmoKPDwKL1R5cGUgL1BhZ2VzCi9LaWRzIApbCjUgMCBSCl0KL0NvdW50IDEKL1Byb2NTZXQgWy9QREYgL1RleHQgL0ltYWdlQiAvSW1hZ2VDXQo+PgplbmRvYmoKeHJlZgowIDExCjAwMDAwMDAwMDAgNjU1MzUgZiAKMDAwMDAwMDAwOSAwMDAwMCBuIAowMDAwMDAwODQwIDAwMDAwIG4gCjAwMDAwMDAxNjMgMDAwMDAgbiAKMDAwMDAwMDI1OCAwMDAwMCBuIAowMDAwMDAwMzQ0IDAwMDAwIG4gCjAwMDAwMDAyOTUgMDAwMDAgbiAKMDAwMDAwMDYzOCAwMDAwMCBuIAowMDAwMDAwODIxIDAwMDAwIG4gCjAwMDAwMDA0NjMgMDAwMDAgbiAKMDAwMDAwMDYxOCAwMDAwMCBuIAp0cmFpbGVyCjw8Ci9TaXplIDExCi9JbmZvIDEgMCBSCi9Sb290IDYgMCBSCj4+CnN0YXJ0eHJlZgo5MzgKJSVFT0YK"}
    # expected_results2 = open_results()
    expected_error = "Input error"

    def setUp(self) -> None:
        self.action = MarkdownToPdf()

    # @parameterized.expand(
    #     [
    #         ({"markdown": "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q="}, expected_results2),
    #         ({"markdown_string": "#"}, expected_results2),
    #     ]
    # )
    # def test_markdown_to_pdf_valid(self, input_params, expected):
    #     results = self.action.run(input_params)
    #     self.assertEqual(results, expected)

    @parameterized.expand(
        [
            (
                {"markdown": "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q=", "markdown_string": "# Rapid7 InsightConnect"},
                expected_error,
            ),
            ({"markdown": "", "markdown_string": ""}, expected_error),
        ]
    )
    def test_markdown_to_pdf_invalid(self, input_params, exception):
        with self.assertRaises(PluginException) as context:
            self.action.run(input_params)
        self.assertEqual(context.exception.cause, exception)
