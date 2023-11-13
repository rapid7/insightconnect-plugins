from base64 import b64encode
from html import escape
from textwrap import wrap

import insightconnect_plugin_runtime
from weasyprint import HTML

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

        html_template = """
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title></title></head>
<body><pre>{}</pre></body>
</html>"""
        # Wrap text preserving existing newlines
        text = "\n".join(
            wrapped
            for line in text.splitlines()
            for wrapped in wrap(line, width=70, expand_tabs=False, replace_whitespace=False, drop_whitespace=False)
        )
        text = escape(text)
        html_content = html_template.format(text)
        pdf_content = HTML(string=html_content).write_pdf()

        b64_content = b64encode(pdf_content).decode()

        return {"pdf": b64_content}
