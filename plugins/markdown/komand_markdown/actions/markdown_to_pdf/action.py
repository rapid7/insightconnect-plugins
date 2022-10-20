import insightconnect_plugin_runtime
import pdfkit
import tempfile
import shutil
from komand_markdown.util import utils
from .schema import MarkdownToPdfInput, MarkdownToPdfOutput, Output, Input
from insightconnect_plugin_runtime.exceptions import PluginException


def makePDF(html: str, path: str) -> str:
    infile = path + "str.html"
    outfile = path + "tmp.pdf"
    with open(infile, "w", encoding="utf-8") as file:
        file.write(html)
    pdfkit.from_file(infile, outfile)
    with open(outfile, "rb") as file:
        out_bytes = file.read().decode("UTF-8", errors="replace")
    return out_bytes


class MarkdownToPdf(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="markdown_to_pdf",
            description="Convert Markdown to PDF",
            input=MarkdownToPdfInput(),
            output=MarkdownToPdfOutput(),
        )

    def run(self, params={}):
        inbytes = params.get(Input.MARKDOWN)
        instr = params.get(Input.MARKDOWN_STRING)

        if not (((instr is None) ^ (inbytes is None)) or ((instr == "") ^ (inbytes == ""))):
            raise PluginException(
                cause="Input error",
                assistance="Only one of Markdown or Markdown String can be defined"
                if instr != inbytes
                else "You must define one of Markdown or Markdown String.",
            )

        path = tempfile.mkdtemp() + "/"
        if instr:
            html_string = utils.convert(instr, "md", "html")
        else:
            html_string = utils.convert(utils.from_bytes(inbytes), "md", "html")

        pdf_string = makePDF(html_string, path)
        pdf_b64 = utils.to_bytes(pdf_string)
        shutil.rmtree(path)
        return {Output.PDF_STRING: pdf_string, Output.PDF: pdf_b64}
