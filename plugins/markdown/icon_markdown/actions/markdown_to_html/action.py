import insightconnect_plugin_runtime
from icon_markdown.util import utils
from .schema import MarkdownToHtmlInput, MarkdownToHtmlOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException


class MarkdownToHtml(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="markdown_to_html",
            description=Component.DESCRIPTION,
            input=MarkdownToHtmlInput(),
            output=MarkdownToHtmlOutput(),
        )

    def run(self, params={}):
        inbytes = params.get(Input.MARKDOWN)
        instr = params.get(Input.MARKDOWN_STRING)
        if not (
            ((instr is None) ^ (inbytes is None)) or ((instr == "") ^ (inbytes == ""))
        ):
            raise PluginException(
                cause="Input error",
                assistance=(
                    "Only one of Markdown or Markdown String can be defined"
                    if instr != inbytes
                    else "You must define one of Markdown or Markdown String."
                ),
            )
        if instr:
            html_string = utils.convert(instr, "md", "html")
            html_b64 = utils.to_bytes(html_string)
        else:
            html_string = utils.convert(utils.from_bytes(inbytes), "md", "html")
            html_b64 = utils.to_bytes(html_string)
        return {Output.HTML_STRING: html_string, Output.HTML: html_b64}
