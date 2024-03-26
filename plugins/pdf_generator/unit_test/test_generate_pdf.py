import sys
import os

from jsonschema import validate

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_pdf_generator.actions.generate_pdf import GeneratePdf
from icon_pdf_generator.actions.generate_pdf.schema import Input, GeneratePdfOutput


class TestGeneratePdf(TestCase):
    def setUp(self):
        self.action = GeneratePdf()
        self.params = {Input.TEXT: "example"}

    def test_generate_pdf(self):
        result = self.action.run(self.params)

        self.assertIsNotNone(result.get("pdf"))
        validate(result, GeneratePdfOutput.schema)
