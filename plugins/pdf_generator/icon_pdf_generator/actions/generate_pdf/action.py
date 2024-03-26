from base64 import b64encode

import insightconnect_plugin_runtime
from fpdf import FPDF

from .schema import GeneratePdfInput, GeneratePdfOutput


class GeneratePdf(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="generate_pdf",
            description="Generate a PDF from a text input",
            input=GeneratePdfInput(),
            output=GeneratePdfOutput(),
        )

    def run(self, params={}):
        text = params.get("text")

        pdf = FPDF(format="A4")
        pdf.add_page()
        pdf.set_font("helvetica", size=12)
        pdf.multi_cell(0, text=text)
        pdf_bytes = pdf.output()

        b64_content = b64encode(pdf_bytes).decode()
        return {"pdf": b64_content}
