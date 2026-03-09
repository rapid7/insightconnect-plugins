import os
import sys

from jsonschema import validate

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_pdf_generator.actions.generate_pdf import GeneratePdf
from icon_pdf_generator.actions.generate_pdf.schema import GeneratePdfOutput, Input

STUB_PARAMS = {
    Input.TEXT: "example",
}


class TestGeneratePdf(TestCase):
    def setUp(self) -> None:
        self.action = GeneratePdf()

    def test_generate_pdf(self) -> None:
        result = self.action.run(STUB_PARAMS)
        self.assertIsNotNone(result.get("pdf"))
        validate(result, GeneratePdfOutput.schema)
