import insightconnect_plugin_runtime
import pypandoc
import base64
import re
from .schema import MarkdownInput, MarkdownOutput, Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException


class Markdown(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="markdown",
            description="Convert HTML to Markdown",
            input=MarkdownInput(),
            output=MarkdownOutput(),
        )

    def run(self, params={}):
        tag_parser = "(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>"  # noqa: W605
        tags = re.findall(tag_parser, params.get(Input.DOC))

        if not tags:
            raise PluginException(cause="Run: Invalid input.", assistance="Input must be of type HTML.")

        try:
            output = pypandoc.convert_text(params.get(Input.DOC), "md", format="html")
        except RuntimeError as error:
            raise PluginException(cause="Pypandoc Runtime Error: ", assistance="Check stack trace log", data=error)
        f = base64.b64encode(output.encode("ascii")).decode()
        return {Output.MARKDOWN_CONTENTS: output, Output.MARKDOWN_FILE: f}
