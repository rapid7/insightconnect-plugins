import insightconnect_plugin_runtime
import pypandoc
import base64
import re
from .schema import MarkdownInput, MarkdownOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException


class Markdown(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="markdown",
            description=Component.DESCRIPTION,
            input=MarkdownInput(),
            output=MarkdownOutput(),
        )

    def run(self, params={}):
        tag_parser = "(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>"  # noqa: W605
        doc = params.get(Input.DOC)
        tags = re.findall(tag_parser, doc)

        if not tags:
            raise PluginException(cause="Invalid input.", assistance="Input must be of type HTML.")

        try:
            output = pypandoc.convert_text(doc, "md", format="html")
        except RuntimeError as error:
            raise PluginException(cause="Error converting doc file. ", assistance="Check stack trace log.", data=error)
        file_ = base64.b64encode(output.encode("ascii")).decode()
        return {Output.MARKDOWN_CONTENTS: output, Output.MARKDOWN_FILE: file_}
