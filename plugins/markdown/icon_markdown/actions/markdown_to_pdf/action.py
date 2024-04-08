import insightconnect_plugin_runtime
import pdfkit
import tempfile
import shutil
from icon_markdown.util import utils
from .schema import MarkdownToPdfInput, MarkdownToPdfOutput, Output, Input, Component
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import Tuple


def make_pdf_bytes(html: str, path: str) -> Tuple[bytes, str]:
    infile = path + "str.html"
    outfile = path + "tmp.pdf"
    with open(infile, "w", encoding="utf-8") as file:
        file.write(html)
    pdfkit.from_file(infile, outfile)
    with open(outfile, "rb") as file:
        pdf_string = file.read()

    bytes_pdf = utils.to_bytes_pdf(pdf_string)
    return bytes_pdf, str(pdf_string)


class MarkdownToPdf(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="markdown_to_pdf",
            description=Component.DESCRIPTION,
            input=MarkdownToPdfInput(),
            output=MarkdownToPdfOutput(),
        )

    def run(self, params={}):
        inbytes = params.get(Input.MARKDOWN)
        instr = params.get(Input.MARKDOWN_STRING)

        if not (((instr is None) ^ (inbytes is None)) or ((instr == "") ^ (inbytes == ""))):
            raise PluginException(
                cause="Input error",
                assistance=(
                    "Only one of Markdown or Markdown String can be defined"
                    if instr != inbytes
                    else "You must define one of Markdown or Markdown String."
                ),
            )

        path = tempfile.mkdtemp() + "/"
        if instr:
            html_string = utils.convert(instr, "md", "html")
        else:
            html_string = utils.convert(utils.from_bytes(inbytes), "md", "html")

        pdf_bytes, pdf_string = make_pdf_bytes(html_string, path)

        shutil.rmtree(path)

        return {Output.PDF: pdf_bytes, Output.PDF_STRING: pdf_string}
