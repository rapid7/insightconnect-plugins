import insightconnect_plugin_runtime
import base64
import pypandoc
import re

from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import EpubInput, EpubOutput, Input, Output


class Epub(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="epub", description="Convert HTML to EPUB", input=EpubInput(), output=EpubOutput()
        )

    def run(self, params={}):
        temp_file = "temp_html_3_epub.epub"
        tag_parser = "(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>"  # noqa: W605
        tags = re.findall(tag_parser, params.get(Input.DOC))

        if not tags:
            raise PluginException(cause="Invalid input.", assistance="Input must be of type HTML.")

        try:
            pypandoc.convert(params.get(Input.DOC), "epub", outputfile=temp_file, format="html")
        except RuntimeError as error:
            raise PluginException(cause="Pypandoc Runtime Error: ", assistance="Check stack trace log", data=error)
        with open(temp_file, "rb") as output:
            # Reading the output and sending it in base64
            return {Output.EPUB: base64.b64encode(output.read()).decode("utf-8")}
