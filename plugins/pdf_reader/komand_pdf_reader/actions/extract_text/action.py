import insightconnect_plugin_runtime
from .schema import ExtractTextInput, ExtractTextOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import pdfplumber
from pdfplumber.utils.exceptions import PdfminerException
import base64
import io


class ExtractText(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="extract_text",
            description=Component.DESCRIPTION,
            input=ExtractTextInput(),
            output=ExtractTextOutput(),
        )

    def run(self, params={}):
        pdf_text = ""
        try:
            with io.BytesIO(base64.b64decode(params.get(Input.CONTENTS))) as f:
                pdf_file = pdfplumber.open(f)
                try:
                    pages = pdf_file.pages
                    for page in enumerate(pages):
                        pdf_text += page[1].extract_text().replace("\n", " ")
                finally:
                    pdf_file.close()
        except PdfminerException:
            raise PluginException(
                cause="The provided content is not in PDF file format.",
                assistance="Please check that the input is correct and try again.",
            )
        return {Output.OUTPUT: pdf_text}
