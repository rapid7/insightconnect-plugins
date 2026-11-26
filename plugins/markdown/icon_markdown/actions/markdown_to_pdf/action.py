import insightconnect_plugin_runtime
import subprocess  # nosec B404
import tempfile
import shutil
from icon_markdown.util import utils
from icon_markdown.util.sanitizer import sanitize_html
from .schema import MarkdownToPdfInput, MarkdownToPdfOutput, Output, Input, Component
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import Dict, List

# Defense-in-depth flags for wkhtmltopdf: --disable-javascript blocks script execution,
# --disable-local-file-access blocks file:// SSRF, load-error-handling ignores fetches
# blocked by the sanitizer so a stripped resource does not abort the render.
PDF_OPTIONS = {
    "disable-javascript": None,
    "disable-local-file-access": None,
    "load-error-handling": "ignore",
    "load-media-error-handling": "ignore",
}


WKHTMLTOPDF_TIMEOUT = 120


def build_wkhtmltopdf_command(infile: str, outfile: str) -> List[str]:
    command = ["wkhtmltopdf", "--quiet"]
    for option, value in PDF_OPTIONS.items():
        command.append(f"--{option}")
        if value is not None:
            command.append(value)
    command.extend([infile, outfile])
    return command


def make_pdf_bytes(html: str, path: str) -> Dict[str, str]:
    infile = path + "str.html"
    outfile = path + "tmp.pdf"
    with open(infile, "w", encoding="utf-8") as file:
        file.write(html)
    try:
        result = subprocess.run(  # nosec B603
            build_wkhtmltopdf_command(infile, outfile),
            capture_output=True,
            text=True,
            timeout=WKHTMLTOPDF_TIMEOUT,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        raise PluginException(
            cause="PDF rendering timed out.",
            assistance=f"wkhtmltopdf did not finish within {WKHTMLTOPDF_TIMEOUT} seconds.",
        ) from error
    if result.returncode != 0:
        raise PluginException(
            cause="PDF rendering failed.",
            assistance="Check that the Markdown converts to valid HTML.",
            data=f"wkhtmltopdf exit code {result.returncode}: {result.stderr}",
        )
    with open(outfile, "rb") as file:
        pdf_string = file.read()

    bytes_pdf = utils.to_bytes_pdf(pdf_string)
    return {"pdf": bytes_pdf, "pdf_string": str(pdf_string)}


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

        results = make_pdf_bytes(sanitize_html(html_string), path)

        shutil.rmtree(path)

        return {
            Output.PDF: results.get("pdf"),
            Output.PDF_STRING: results.get("pdf_string"),
        }
