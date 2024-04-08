import insightconnect_plugin_runtime
from icon_markdown.util import utils
from .schema import HtmlToMarkdownInput, HtmlToMarkdownOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException


class HtmlToMarkdown(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="html_to_markdown",
            description=Component.DESCRIPTION,
            input=HtmlToMarkdownInput(),
            output=HtmlToMarkdownOutput(),
        )

    def run(self, params={}):
        inbytes = params.get(Input.HTML)
        instr = params.get(Input.HTML_STRING)
        if not (((instr is None) ^ (inbytes is None)) or ((instr == "") ^ (inbytes == ""))):
            raise PluginException(
                cause="Input error",
                assistance=(
                    "Only one of HTML or HTML String can be defined"
                    if instr != inbytes
                    else "You must define one of HTML or HTML String."
                ),
            )
        if instr:
            markdown_string = utils.convert(instr, "html", "md")
            markdown_b64 = utils.to_bytes(markdown_string)
        else:
            markdown_string = utils.convert(utils.from_bytes(inbytes), "html", "md")
            markdown_b64 = utils.to_bytes(markdown_string)
        return {Output.MARKDOWN_STRING: markdown_string, Output.MARKDOWN: markdown_b64}
