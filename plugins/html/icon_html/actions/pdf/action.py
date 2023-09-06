import insightconnect_plugin_runtime
import base64

from insightconnect_plugin_runtime.exceptions import PluginException
import pypandoc
import re
from .schema import PdfInput, PdfOutput, Input, Output, Component


class Pdf(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="pdf", description=Component.DESCRIPTION, input=PdfInput(), output=PdfOutput()
        )

    def run(self, params={}):
        temp_file = "temp_html_2_pdf.pdf"
        tag_parser = "(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>"  # noqa: W605
        doc = params.get(Input.DOC)
        tags = re.findall(tag_parser, doc)

        if not tags:
            raise PluginException(cause="Invalid input.", assistance="Input must be of type HTML.")

        try:
            pypandoc.convert(doc, "pdf", outputfile=temp_file, format="html")
        except RuntimeError as error:
            raise PluginException(cause="Error converting doc file. ", assistance="Check stack trace log.", data=error)
        with open(temp_file, "rb") as output:
            # Reading the output and sending it in base64
            return {Output.PDF: base64.b64encode(output.read()).decode("utf-8")}
