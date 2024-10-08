import insightconnect_plugin_runtime
from .schema import MarkdownInput, MarkdownOutput, Input, Output, Component
from icon_html.util.api import HTMLConverter
from icon_html.util.strategies import ConvertToMarkdown
from icon_html.util.helpers import encode_to_base64


class Markdown(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="markdown",
            description=Component.DESCRIPTION,
            input=MarkdownInput(),
            output=MarkdownOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        document = params.get(Input.DOC, "")
        # END INPUT BINDING - DO NOT REMOVE

        converted_markdown = HTMLConverter(ConvertToMarkdown()).convert(document)
        return {
            Output.MARKDOWN_CONTENTS: converted_markdown,
            Output.MARKDOWN_FILE: encode_to_base64(converted_markdown),
        }
