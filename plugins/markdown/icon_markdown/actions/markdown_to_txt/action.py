import insightconnect_plugin_runtime
from .schema import MarkdownToTxtInput, MarkdownToTxtOutput, Input, Output, Component
from icon_markdown.util import utils
from insightconnect_plugin_runtime.exceptions import PluginException


# Custom imports below
from bs4 import BeautifulSoup
import binascii


class MarkdownToTxt(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="markdown_to_txt",
            description=Component.DESCRIPTION,
            input=MarkdownToTxtInput(),
            output=MarkdownToTxtOutput(),
        )

    def run(self, params={}):
        inbytes = params.get(Input.MARKDOWN)
        instr = params.get(Input.MARKDOWN_STRING)

        if not (((instr is None) ^ (inbytes is None)) or ((instr == "") ^ (inbytes == ""))):
            raise PluginException(
                cause="Input Error",
                assistance=(
                    "Only one of Markdown or Markdown String can be defined"
                    if instr != inbytes
                    else "You must define one of Markdown or Markdown String."
                ),
            )

        if inbytes != "":
            try:
                markdown = utils.from_bytes(inbytes)
            except binascii.Error:
                bytes_len = len(inbytes)
                markdown = utils.from_bytes(inbytes[: bytes_len - (bytes_len % 4)])
        else:
            markdown = instr

        soup = BeautifulSoup(utils.convert(markdown, "md", "html"), features="html.parser")
        for script in soup(["script", "style"]):
            script.extract()
        txt_string = soup.get_text()

        return {Output.TXT_STRING: txt_string, Output.TXT: utils.to_bytes(txt_string)}
